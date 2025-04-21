# ThePhish Standalone 1.0 🐟

> 📅 Last updated: April 21, 2025

A modified standalone version of [ThePhish](https://github.com/emalderson/ThePhish) tailored to:
- ❌ Work without TheHive, Cortex, or MISP
- ✅ Perform phishing analysis using local heuristics
- 🧠 Store verdicts in MongoDB
- 🌐 Display results via a custom Flask web dashboard

---

## 🧰 Prerequisites

| Component     | Version       |
|---------------|---------------|
| Python        | 3.10.17       |
| MongoDB       | 4.4 (systemd) |
| OS            | Ubuntu 20.04  |

---

## 📦 Installation Steps

### 1. Clone this Repository

```bash
git clone https://github.com/youneedtocode/Phish_standalone1.0.git
cd Phish_standalone1.0
```

### 2. Set Up Python Virtual Environment for Main App

```bash
cd app
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3. Configure Email in `configuration.json`

Edit the file `app/configuration.json`:
```json
"email": {
  "server": "imap.gmail.com",
  "port": 993,
  "username": "your_email@gmail.com",
  "password": "your_app_password"
}
```

---

## 🚀 Running ThePhish App

```bash
cd ~/ThePhish/app
source venv/bin/activate
python thephish_app.py
```

Open your browser at: [http://127.0.0.1:8080](http://127.0.0.1:8080)

---

## 💾 MongoDB Setup

MongoDB should be running as a local service:

```bash
sudo systemctl start mongod
```

Check its status:

```bash
sudo systemctl status mongod
```

Verdicts are saved in the following collection:
- Database: `thephish`
- Collection: `verdicts`

---

## 📊 Running the Custom Web Dashboard

### 1. Set up environment

```bash
cd ~/ThePhish/web_dashboard
python3 -m venv venv
source venv/bin/activate
```

### 2. Run the dashboard

```bash
python3 dashboard.py
```

Open in browser: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 🛠️ File Structure

```
ThePhish/
├── app/                    # Core app files
│   ├── thephish_app.py
│   ├── run_analysis.py
│   └── configuration.json
├── web_dashboard/          # Custom dashboard
│   ├── dashboard.py
│   └── templates/
├── README.md               # This file
```

---

## ✅ Features Summary

- Email analysis via IMAP (EML attachments)
- Phishing detection using local rules
- Verdicts saved in MongoDB
- Dashboard for viewing analysis results
- Entirely self-contained (no external integrations required)

---

## 👨‍💻 Maintainer

Made by **[@youneedtocode](https://github.com/youneedtocode)** — customized for standalone use.

