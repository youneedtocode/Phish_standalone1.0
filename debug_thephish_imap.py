import imaplib
import email
import json
import ssl

# Load ThePhish configuration
with open("configuration.json") as f:
    config = json.load(f)

imap_config = config["imap"]
IMAP_SERVER = imap_config["host"]
IMAP_PORT = int(imap_config["port"])
USERNAME = imap_config["user"]
PASSWORD = imap_config["password"]
FOLDER = imap_config["folder"]

# Connect to Gmail's IMAP server with SSL
context = ssl.create_default_context()
mail = imaplib.IMAP4_SSL(IMAP_SERVER, IMAP_PORT, ssl_context=context)
mail.login(USERNAME, PASSWORD)

print(f"\n✅ Logged in as {USERNAME}")

# Select folder and show status
status, messages = mail.select(FOLDER)
print(f"📁 Selecting folder '{FOLDER}' — status: {status}, count: {messages}")

# Search for unread emails
status, data = mail.search(None, '(UNSEEN)')
print(f"🔍 Searching for UNSEEN — status: {status}")
print(f"📩 UNSEEN message IDs: {data[0].split()}")

# Try printing subjects if there are any
if data[0]:
    for num in data[0].split():
        typ, msg_data = mail.fetch(num, '(RFC822)')
        raw_email = msg_data[0][1]
        msg = email.message_from_bytes(raw_email)
        print("—"*50)
        print("From:", msg["From"])
        print("Subject:", msg["Subject"])
        print("Date:", msg["Date"])
        print("Message-ID:", msg["Message-ID"])
else:
    print("🚫 No unread emails found!")

mail.logout()
