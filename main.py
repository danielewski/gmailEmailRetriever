import imaplib
import email
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

for i in range(latest_email_id, first_email_id - 1, -1):
    typ, data = connection.fetch(str(i), '(RFC822)')
    for header in data:
        if isinstance(header, tuple):
            msg = email.message_from_string(header[1].decode())
            subject = msg['subject']
            from_user = msg['from']
            print(f'subject: {subject}, from: {from_user}')
