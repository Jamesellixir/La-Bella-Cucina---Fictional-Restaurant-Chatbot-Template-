# StarForge – La Bella Cucina AI Assistant

> *Turning AI complexity into business simplicity.*

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=flat-square&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red?style=flat-square&logo=streamlit)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4o--mini-green?style=flat-square&logo=openai)
![License](https://img.shields.io/badge/License-Proprietary-lightgrey?style=flat-square)

---

## Overview

**La Bella Cucina AI Assistant** is an intelligent customer service chatbot built by StarForge for La Bella Cucina — an authentic Italian restaurant in Colombo, Sri Lanka.

The assistant handles the questions that flood every restaurant's inbox: menu enquiries, pricing, opening hours, reservations, delivery options, and location — 24/7, without any staff intervention. Customers get instant, accurate answers in a warm, on-brand voice, while the restaurant team stays focused on delivering great dining experiences.

Built on OpenAI's GPT-4o mini and delivered through a clean Streamlit web interface, this solution is lightweight to deploy, easy to maintain, and immediately ready for customer-facing use.

---

## ✨ Features

- **Always-on customer support** — answers menu, reservation, and location questions around the clock without staff effort
- **Full menu knowledge** — knows every dish, price, and category, and never fabricates items that don't exist
- **Reservation guidance** — explains booking requirements (groups of 6+, 24-hour advance notice) clearly and consistently
- **Delivery awareness** — informs customers about PickMe Food and Uber Eats availability on demand
- **Persistent conversation memory** — maintains context across the full session so customers never have to repeat themselves
- **On-brand personality** — warm, concise, and Italian-accented ("Ciao!") to match the restaurant's identity
- **Clear escalation path** — gracefully directs customers to call or email when a query falls outside the bot's knowledge
- **One-click chat reset** — sidebar "Clear Chat" button for a fresh conversation at any time

---

## 🚀 Demo
<img width="1056" height="830" alt="image" src="https://github.com/user-attachments/assets/e3bf790d-261f-44e8-a21d-bfa840d7270e" />
<img width="1015" height="812" alt="image" src="https://github.com/user-attachments/assets/72479919-0b7f-447b-902f-fd199b7110d9" />
<img width="1007" height="478" alt="image" src="https://github.com/user-attachments/assets/1d704966-f810-4dc5-8033-d21fcc2ee7e6" />



---

## 🛠 Tech Stack

| Layer | Tools |
|---|---|
| Language | Python 3.10+ |
| Frontend | Streamlit |
| AI Model | OpenAI GPT-4o mini |
| API Client | OpenAI Python SDK (`openai>=1.0.0`) |
| Config | python-dotenv |
| Deployment | Streamlit Community Cloud / Any Python host |

---

## Getting Started

### Prerequisites

- Python 3.10+
- An [OpenAI API key](https://platform.openai.com/api-keys)

### Installation

```bash
git clone https://github.com/YOUR_GITHUB_USERNAME/la-bella-cucina-chatbot.git
cd la-bella-cucina-chatbot
pip install -r requirements.txt
```

### Configuration

Create a `.env` file in the project root:

```bash
cp .env.example .env
```

Then fill in your values:

| Variable | Description | Required |
|---|---|---|
| `OPENAI_API_KEY` | Your OpenAI API key | ✅ |

> ⚠️ **Never commit your `.env` file.** It is already included in `.gitignore`.

### Running Locally

```bash
# Development
streamlit run app.py
```

The app will open at `http://localhost:8501`.

---

## Usage

Once running, customers can:

- Ask about **menu items** — "What pastas do you have?" / "How much is the Margherita?"
- Check **opening hours** — "Are you open on Sundays?"
- Get **reservation info** — "How do I book a table for 8?"
- Find **location & contact** details — "Where are you located?"
- Ask about **delivery** — "Do you deliver?"

The assistant responds in under 150 words for most queries, keeping the conversation fast and easy to read on mobile.

---

## Architecture

```
User (Browser)
     │
     ▼
Streamlit UI  ──►  Session State (chat history)
     │
     ▼
OpenAI API (GPT-4o mini)
     │   system_prompt.txt  ──►  restaurant knowledge + personality
     │   full conversation history  ──►  context-aware responses
     ▼
Assistant Response  ──►  rendered in chat UI
```

The system prompt is loaded from `system_prompt.txt` at startup, keeping restaurant knowledge cleanly separated from application logic. This means updating the menu, hours, or any other details requires no code changes — just edit the text file.

---

## Contributing

This is a client project delivered by StarForge. If you are the client and want to request changes or new features, please get in touch via the contact details below.

---

## License

Proprietary — delivered exclusively to La Bella Cucina by StarForge. Not for redistribution.

---

## Credits & Contact

**Built by StarForge** — AI automation for businesses that want results, not complexity.

- 🌐 Website: [Under construstion]
- 📧 Email: starforge.lk@gmail.com
- 🐙 GitHub: [github.com/YOUR_GITHUB_USERNAME](https://github.com/jamesellixir)

> *"Turning AI complexity into business simplicity."*
