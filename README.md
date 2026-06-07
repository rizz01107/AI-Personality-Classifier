# 🧠 AI Powered Behavioral Personality Classifier for Smart Communication

![Python](https://img.shields.io/badge/Python-3.11+-blue?style=flat-square&logo=python)
![Flask](https://img.shields.io/badge/Flask-2.3-black?style=flat-square&logo=flask)
![SQLite](https://img.shields.io/badge/Database-SQLite-lightgrey?style=flat-square&logo=sqlite)
![NLP](https://img.shields.io/badge/AI-NLP%20Engine-purple?style=flat-square)
![Claude AI](https://img.shields.io/badge/Built%20with-Claude%20AI-orange?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)

> Analyze any text and instantly discover your **personality type**, **dominant emotion**, **communication tone** — and get AI-powered recommendations to communicate smarter.

---

## ✨ Features

- 🧠 **9 Personality Types** — Friendly, Professional, Aggressive, Emotional, Reserved, Analytical, Assertive, Extrovert, Introvert
- 💖 **7 Emotion States** — Happy, Sad, Angry, Neutral, Excited, Frustrated, Confused
- 📊 **Visual Analytics** — Radar charts, bar charts, doughnut charts (Chart.js)
- 🤖 **AI Chatbot** — Communication coaching assistant
- 📜 **Analysis History** — Track personality patterns over time
- 🛡️ **Admin Panel** — Full user & system management
- 🔐 **Secure Auth** — Login, signup, password hashing (Werkzeug)
- 🎨 **Premium Dark UI** — Glassmorphism design, fully responsive

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python Flask 2.3 |
| Database | SQLite + SQLAlchemy ORM |
| Auth | Flask-Login + Werkzeug |
| AI Engine | Custom NLP keyword scoring |
| Frontend | HTML5, CSS3, Vanilla JS |
| Charts | Chart.js 4.x |
| Icons | Font Awesome 6.5 |

---

## 🚀 Quick Start

### 1. Clone the repo
```bash
git clone https://github.com/rizz01107/AI-Personality-Classifier.git
cd AI-Personality-Classifier
```

### 2. Install dependencies
```bash
pip install flask Flask-Login Flask-SQLAlchemy Flask-WTF Werkzeug WTForms
```

### 3. Run the app
```bash
python app.py
```

### 4. Open browser
```
http://localhost:5000
```

---

## 🔑 Demo Login

| Field | Value |
|---|---|
| Email | `admin@aipersonality.com` |
| Password | `Admin@1234` |

---

## 📁 Project Structure

```
AI-Personality-Classifier/
├── app.py                  # Flask app entry point
├── config.py               # Configuration
├── models.py               # Database models
├── requirements.txt        # Dependencies
├── routes/
│   ├── auth.py             # Login / Signup / Logout
│   ├── dashboard.py        # All dashboard routes
│   └── main.py             # Landing page
├── utils/
│   └── ai_engine.py        # NLP classification engine
└── templates/
    ├── index.html           # Landing page
    ├── auth/                # Login & Signup
    └── dashboard/           # All dashboard pages
```

---

## 🤖 Built with Claude AI

This project was developed with the assistance of **Claude AI by Anthropic** — used for system architecture, code generation, database design, and documentation.

> *"AI doesn't replace the builder. It amplifies one."*

---

## 👤 Author

**Muhammad Rizwan**
GitHub: [@rizz01107](https://github.com/rizz01107)

---

## 📄 License

This project is licensed under the MIT License.
