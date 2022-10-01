# Telegram Report Bot
This is a "bot" that connects to your telegram account
fetches some messages from the telegram channel of your choice and generates
an excel report with all the data of the messages.

If there are any incorrectly formatted messages, they are simply ignored, so you
can have users chatting in the same channel and they will be simply ignored
(Doesn't work if the user sends a message that's correctly formatted.)


# Configuration
You need to get API_ID and API_HASH for your account
from telegram.

> You are not allowed by telegram to share these
details with anyone.


You can get CHAT_ID by opening https://web.telegram.org,
selecting the chat you'd like to generate a report for,
and taking the part of the URL after the hashtag.

> In some cases there is a dash (-) at the front, make sure you copy that as well.

MESSAGE_LIMIT refers to the number of messages the
program is allowed to read, even if you set a
specific date range, if you set MESSAGE_LIMIT to 0
no messages are going to be received.

> to disable the limit set MESSAGE_LIMIT to "None" (without the quotes)

FROM_DATE and TO_DATE refer to the start of the date range and the end of the date range respectively.

FROM_DATE, by default, is set to "datetime.today() - timedelta(days=5)"
which means, today's date - 5 days, and the result is the 5 days ago's date.

TO_DATE, by default, is set to "datetime.today()" which means, today's date.


> Each of those have a commented line under them with options to set
year, month and day.
To enable them just uncomment them (remove the hashtag at the front of
the line)


All that's left are the "Output Options"

EXCEL_FILE_NAME is the name for the output excel file, the default is "Report.xlsx"

EXCEL_SHEET_NAME is the name of the sheet inside the excel (You shouldn't need to change it.)

REVERSE_ORDER, when "True" the output is reversed (First line goes last, and last line goes First)

> NOTE: When REVERSE_ORDER is "False" the output most recent message at the start and the oldest message at the end.