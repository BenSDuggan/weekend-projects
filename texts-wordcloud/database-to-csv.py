# Convert the IOS iMessage text SQLite DB to a CSV file for the given conversation
# Pass the formatted phone number as the first argument


import csv
import sqlite3
import sys
import time

print(sys.argv[1])


dbfile = 'chat.db'
save_name = 'messages.csv'


con = sqlite3.connect(dbfile)
cur = con.cursor()

# Get the chat IDs
chat_rows = [a for a in cur.execute('SELECT "_rowid_",* FROM "main"."chat" WHERE "chat_identifier" LIKE \'%'+sys.argv[1]+'%\' ESCAPE \'\\\' ORDER BY "chat_identifier" DESC;')]

print("Chat IDs, Number")
for r in chat_rows:
    print(r[0], ", ", r[2])

chat_ids = list(map(lambda x: x[1], chat_rows))
print("Chat IDs: " + str(chat_ids))

# Get the message IDs that correspond to each chat_id
chat_messages = {}
for cid in chat_ids:
    chat_messages_rows = [a for a in cur.execute('SELECT "_rowid_",* FROM "main"."chat_message_join" WHERE "chat_id" LIKE \'%' + str(cid) + '%\' ESCAPE \'\\\' ORDER BY "message_date" DESC;')]

    chat_messages[cid] = chat_messages_rows
    print(chat_messages_rows[0])


# Get the messages corresponding to the given message IDS
# Will save text, date, date, is_from_me
messages = []
count = 0
print("Collecting messages")
# Save messages to csv
with open(save_name, 'w') as f:
    write = csv.writer(f, quoting=csv.QUOTE_ALL)
    
    write.writerow(["cid", "mid", "text", "datetime", "is_from_me"])
    
    for cid in chat_messages:
        for mid in chat_messages[cid]:
            messages_rows = [a for a in cur.execute('SELECT "_rowid_",* FROM "main"."message" WHERE "ROWID" LIKE \'%' + str(mid[2]) + '%\' ESCAPE \'\\\';')]

            for m in messages_rows:
                if m[3] is None:
                    continue
                
                new_message = [cid, mid, m[3], m[16], m[23]]
                write.writerow(new_message)
                
                count = count + 1
                if count % 1000 == 0:
                    print(str(time.time()) + ": " + str(count))

# Be sure to close the connection
con.close()




