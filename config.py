from datetime import datetime, timedelta

'''
To get this info go to: https://my.telegram.org/auth?to=apps
and enter your mobile number and fill the code they'll send you
to telegram.

Then, go to "API development tools"
and create a new app.

after that, it should have a page with "App api_id"
and "App api_hash", copy those values to the below
fields.
'''
API_ID:str                              = "<API-ID>"
API_HASH:str                            = "<API-HASH>"



# This is a session name, it doesn't really need to be modified.
SESSION_NAME:str                        = "reporter"

'''
You can get this ID by accessing the chat through
the web portal of telegram, and looking at the URL.
'''
CHAT_ID:int                             = -111111111 # That's a fake ID for demonstration.



# How many messages to get (number), to disable it set to "None" without the quotes.
MESSAGE_LIMIT:int                       = 20 # get 20 messages and stop.


'''
FROM_DATE and TO_DATE are here to help you select dates
The date ranges INCLUDE the specified dates.

message_date >= FROM_DATE and message_date <= TO_DATE

to disable, set to "None" without the quotes.

NOTE: To completely disable pick-by-date set BOTH to "None" as
        they can be used separately.
'''
FROM_DATE:datetime                      = datetime.today() - timedelta(days = 5)  # today - 5days
# FROM_DATE:datetime                      = datetime(year=2022, month=12, day=0)    # 2022-12-0


TO_DATE:datetime                        = datetime.today()                        # today
# TO_DATE:datetime                        = datetime(year=2022, month=12, day=3)    # 2022-12-3





# Output Options
EXCEL_FILE_NAME                         = "Report.xlsx"
EXCEL_SHEET_NAME                        = "Data"
REVERSE_ORDER                           = True
