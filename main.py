import config
from telethon import TelegramClient
from telethon.tl.patched import Message
from datetime import datetime, timedelta
import pandas as pd
from typing import Generator

#####################
# Prepare Functions #
#####################
def getMessages(client:TelegramClient, chat_id:int, msg_limit:float, from_date:datetime, to_date:datetime) -> Generator[Message, None, None]:
    msg:Message = None
    for msg in client.iter_messages(chat_id, limit=msg_limit, offset_date=to_date.date()):
        if (not from_date) or (msg.date.date() > from_date.date()):
            yield msg




def getMessageData(msg:str) -> dict[str, str]:
    # Extracts data from a message
    # with the following format.
    """
    Coin: ETHDOWN
    Position: Buy ETF
    Signal Shared: 21-9-2022 21:12
    TP/SL: TP1
    Peak Profit: 7.20%
    Correction: -.54%
    Time: 1 jam
    """
    # Strip message to get only the data
    msg = msg.strip()
    allParts = {}

    for parts in map(lambda line: line.strip().split(': '), msg.split('\n')):
        if len(parts) == 2:
            allParts[parts[0]] = parts[1]
    return allParts



def saveExcel(fname:str, df:pd.DataFrame, sheet_name:str) -> None:
    writer = pd.ExcelWriter(fname)
    df.to_excel(writer, sheet_name, index=False)
    writer.save()



def generateDataFrame(client:TelegramClient, chat_id:int, message_limit:float, from_date:datetime, to_date:datetime) -> pd.DataFrame:
    ################
    # Get Messages #
    ################
    allData:dict[str, list] = {}
    with client:
        messages = getMessages(client, chat_id, message_limit, from_date, to_date)

        ##################
        # Generate Excel #
        ##################
        msg_i = 0
        for message in messages:
            if message.text is not None:
                data = getMessageData(message.text)
                if data:
                    # Add missing entries to the data
                    # so it's easier to fill in the entries
                    # later.
                    for k in allData.keys():
                        if k not in data:
                            data[k] = ''


                    for k, v in data.items():

                        # If this is the first occurence of the key
                        # add a padding so there are not alternations
                        # to the data.
                        if k not in allData:
                            allData[k] = [''] * msg_i


                        # Store the data in a shared holder for
                        # generating the excel file later.
                        if config.REVERSE_ORDER:
                            allData[k].insert(0, v)
                        else:
                            allData[k].append(v)
                    msg_i += 1
        return pd.DataFrame(allData)




if __name__ == "__main__":

    ##########################
    # Parameter Sanitization #
    ##########################
    if config.FROM_DATE: config.FROM_DATE -= timedelta(days=1)
    if config.TO_DATE: config.TO_DATE += timedelta(days=1)



    ###################
    # Start a session #
    ###################
    client = TelegramClient(config.SESSION_NAME, config.API_ID, config.API_HASH)

    ####################
    # Get & Save Excel #
    ####################
    df = generateDataFrame(client, config.CHAT_ID, config.MESSAGE_LIMIT, config.FROM_DATE, config.TO_DATE)
    saveExcel(config.EXCEL_FILE_NAME, df, config.EXCEL_SHEET_NAME)