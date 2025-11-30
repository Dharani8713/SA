# 🤖 Support Assistant AI Agent

An intelligent FAQ chatbot that answers company-related queries and escalates unresolved questions to human support via Telegram. Built for the 48-Hour AI Agent Development Challenge.

---

## 🚀 Overview

This agent helps users resolve common support queries using a keyword-matching FAQ system. If no relevant answer is found or the user marks the response as insufficient, the query is escalated to a human via Telegram.

---

## 🧠 Features

- ✅ Keyword-based FAQ matching
- ✅ Interactive user feedback (Yes/No)
- ✅ Telegram escalation for unresolved queries
- ✅ Modular architecture (easy to extend)
- ✅ Streamlit UI for instant deployment

---

## 🛠️ Tech Stack

| Component        | Tool/Library            |
|------------------|-------------------------|
| UI               | Streamlit               |
| Logic            | Python                  |
| Knowledge Base   | JSON (`faqs.json`)      |
| Escalation       | Telegram Bot API        |
| Deployment       | Streamlit Cloud         |

---

## 📂 File Structure

SA/ 
│ 
├── app.py # Main Streamlit app 
├── requirements.txt # Dependencies 
├── README.md # Documentation 
├── architecture.png # Architecture diagram 
├── data/ 
│ └── faqs.json # FAQ knowledge base 
└── utils/ 
└── escalation.py # Telegram escalation helper


---

## 🖼️ Architecture

![Architecture Diagram](architecture.png)

---

## ⚙️ Setup Instructions

1. Clone the repo:
   ```bash
   git clone https://github.com/yourusername/support-assistant.git
   cd support-assistant
2. Install dependencies:
   pip install -r requirements.txt
3. Run the app:
   streamlit run app.py (in local)
4. Configure Telegram:
   Create a bot via BotFather
   Get your bot token and chat ID
   Add them to utils/escalation.py

   
