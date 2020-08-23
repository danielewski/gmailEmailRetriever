import imaplib
import email
from collections import Counter
from itertools import count
import re

import user_information

imap_url = 'imap.gmail.com'

connection = imaplib.IMAP4_SSL(imap_url)
connection.login(user_information.user, user_information.password)
connection.select('inbox')

result, data = connection.search(None, "ALL")
mail_ids = data[0]

id_list = mail_ids.split()
first_email_id = int(id_list[0])
latest_email_id = int(id_list[-1])
from_list = []
count = 0

print(f"Email count: {len(id_list)}, starting...")
for i in range(latest_email_id, first_email_id - 1, -1):
    count += 1
    typ, data = connection.fetch(str(i), '(RFC822)')
    for header in data:
        if isinstance(header, tuple):
            msg = email.message_from_string(header[1].decode('utf-8', 'ignore'))
            from_list.append(msg['from'])
            if count % 10 == 0:
                print(f"emails parsed: {count}")

counted_users = Counter(from_list)
count = counted_users.most_common()
for user in count:
    print(f"User: {user[0]}, Emails: {user[1]}")
