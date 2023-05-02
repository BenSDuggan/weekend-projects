# Create a Wordcloud from IOS Text Messages

## Steps

### Get IOS Text Messages

The easiest way to get messages is from a Mac that is running iMessage.

1.  Messages are stored in `~/Library/Messages/chat.db` and is a SQLite database
2. Copy messages to this directory and make sure the file is called `chat.db`


### Convert the database to a CSV file

This uses Python

1. Run the `database-to-csv.py` script and pass the recipient number as an argument: `python database-to-csv.py +18005551234`
2. The messages will be saved in the file `messages.csv`

### Create wordcloud

This uses R script `csv-to-wordcloud.r`. You may want to add additional words to the `remove_words` variable.



## Notes

### Convert the database to a CSV file

* Database is broken up into chats, messages, and other things
* Need to determine chat IDs to collect all the messages from a person
* ***Will not work for group messages***
* Get the `rowids` for all the rows in the `chat` table with `chat_identifier` equal to the phone number formatted like (`+18005551234`).

