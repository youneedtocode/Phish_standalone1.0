# 🐟 ThePhish - Standalone Edition

This is a **standalone version** of [ThePhish](https://github.com/emalderson/ThePhish) that works without TheHive, Cortex, MISP, or Cassandra. It fetches emails, performs phishing analysis using heuristics and stores verdicts in MongoDB, and displays results on a built-in dashboard.

---

## ✅ Key Features

- Connects to your Gmail inbox using IMAP
- Parses `.eml` attachments or full emails directly
- Performs local phishing detection
- Displays analysis logs live in the browser via WebSockets
- Saves verdicts to MongoDB
- Simple `/verdicts` dashboard to view all verdicts
- No need for external integrations (TheHive, Cortex, MISP)

---

## ⚙️ Requirements

- Python 3.10
- MongoDB 4.4
- A Gmail account (IMAP enabled + App Password)
- The following Python packages (already included in `requirements.txt`):

```
flask
eventlet
flask_socketio
pymongo
email
ioc-fanger==3.3.0
ioc-finder==6.0.1
```

---

## 📁 Project Structure

```
ThePhish/
│
├── app/
│   ├── thephish_app.py          # Main web app
│   ├── run_analysis.py          # Phishing logic + MongoDB logging
│   ├── list_emails.py           # Fetches emails from Gmail
│   ├── case_from_email.py       # Extracts .eml + metadata
│   ├── requirements.txt
│   └── templates/
│       ├── index.html           # Main dashboard UI
│       └── verdicts.html        # Verdicts table
│
├── static/assets/js/thephish.js # JavaScript to handle UI interaction
├── README.md
└── ...
```

---

## 🚀 Setup Instructions

### 1. Clone this repository

```bash
git clone https://github.com/youneedtocode/Phish_standalone1.0.git
cd Phish_standalone1.0
```

### 2. Create and activate a virtual environment

```bash
python3.10 -m venv venv
source venv/bin/activate
```

### 3. Install Python dependencies

```bash
pip install -r app/requirements.txt
```

### 4. Configure `configuration.json`

In `app/`, edit `configuration.json` and set:

- Your Gmail IMAP server and port
- Your Gmail address and app password

### 5. Start MongoDB

Make sure MongoDB is running:

```bash
sudo systemctl start mongod
```

---

## 🖥️ Web Dashboard

Once the app is running, open:

```
http://localhost:8080
```

From there:

- Click **"List Emails"** to fetch new emails
- Click **"Analyze"** to analyze an email
- You will be **automatically redirected to `/verdicts`**, showing verdicts stored in MongoDB.

### Verdict Dashboard

Accessible at:

```
http://localhost:8080/verdicts
```

It displays verdicts sorted by timestamp from MongoDB.

---

## ❌ Removed Components

The following are **NOT used** in this version:

- `web_dashboard/` (custom dashboard – now removed)
- TheHive / Cortex / MISP integrations
- Docker / Cassandra setup

---

## 📦 Git Commands to Push Changes

```bash
git add .
git commit -m "Updated README and removed web_dashboard references"
git push origin main
```

---

## 🧠 Author & Acknowledgments

Forked and modified by **youneedtocode** based on [emalderson's ThePhish](https://github.com/emalderson/ThePhish)

Maintained and improved for educational phishing detection analysis purposes.

---