import imaplib
import email
from email.header import decode_header

# Gmail credentials
imap_host = "imap.gmail.com"
imap_user = "fishisfrusted@gmail.com"
imap_pass = "atundlrdlgjnksdx"

# Connect to the server
mail = imaplib.IMAP4_SSL(imap_host)
mail.login(imap_user, imap_pass)

# Select inbox
status, messages = mail.select("inbox")
print(f"SELECT status: {status}")
print(f"Total messages in inbox: {messages[0].decode()}")

# Search for all emails
status, data = mail.search(None, "ALL")
print(f"SEARCH status: {status}")
print(f"Email IDs: {data[0].split()}")

mail.logout()
