# INGRES-Chatbot
# 🌊 AI-Powered Groundwater Chatbot

## 📌 Overview

This project is an *AI-powered multilingual chatbot* designed to simplify access to groundwater data.
Users can ask questions in *English or Hindi, and the chatbot responds with **text, charts, and maps* generated from groundwater datasets.

The prototype was built as part of *Smart India Hackathon 2025*.

## 🚀 Features

* *Multilingual Support*: English & Hindi (powered by SarvamAI for translation).
* *AI-Powered Queries: Uses **Gemini LLM* to convert natural language into SQL queries.
* *User-Friendly*: Simple web-based frontend (HTML, CSS, JavaScript).
* *Scalable: Currently uses mock data but can integrate with **INGRES groundwater datasets*.

## 🛠 Tech Stack

* *Frontend*: HTML, CSS, JavaScript
* *Backend*: Python (Flask)
* *Translation*: SarvamAI (English ↔ Hindi)
* *LLM*: Gemini (via API)
* *Database*: Mock SQL (MySQL)

## ⚙ Workflow

1. User enters query in English or Hindi (Frontend).
2. Flask backend receives the request.
3. If input is Hindi → SarvamAI translates it into English.
4. Gemini LLM interprets the query → generates SQL query.
5. SQL query runs on mock groundwater database.
6. Backend formats the response and sends it back.
7. Frontend displays results as *text*.
8. If needed, output is translated back to Hindi.

## 📂 Project Structure

project/
│── backend/
│   │── app.py            # Flask app entry point
│   │── routes/           # API routes
│   │── services/         # LLM + translation + DB logic
│   │── db/               # Database models + mock data
│
│── frontend/
│   │── index.html        # Chat UI
│   │── style.css
│   │── script.js
│
│── README.md             # Documentation


## 🔧 Installation & Setup

### 1. Clone Repo

bash
git clone https://github.com/your-repo/groundwater-chatbot.git
cd groundwater-chatbot


### 2. Backend Setup

bash
cd backend
pip install -r requirements.txt
python -m flask run
```

### 3. Frontend Setup

Open frontend/index.html in your browser (or serve via VSCode Live Server).

## 🖼 Demo Screenshot

(Add screenshot of your chatbot + chart here)

## 🌍 Future Scope

* Support for *20+ Indian languages* (IndicTrans2).
* Integration with *real INGRES APIs*.
* *Voice queries* (speech-to-text).
* *Mobile & WhatsApp chatbot* version.
* AI-powered *trend prediction & forecasting*.

* This is a project made exclusively for SIH 2025
* Team Debug Squad – SIH 2025
