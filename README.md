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

[Live Demo](YOUR_DEMO_URL_HERE) · [Screenshots / GIFs — add yours here]

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

## Deployment

**Streamlit Community Cloud (free tier recommended for demos)**

1. Push the repo to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io) and connect your repo
3. Set `OPENAI_API_KEY` as a secret in the Streamlit dashboard
4. Deploy — done

The app will be live at a public URL within minutes.

---

## Roadmap

- [ ] Swap system prompt to live database for real-time menu updates
- [ ] Add an online reservation form with email confirmation
- [ ] Multi-language support (Sinhala / Tamil)
- [ ] Analytics dashboard to track common customer queries
- [ ] WhatsApp / Messenger integration

---

## Contributing

This is a client project delivered by StarForge. If you are the client and want to request changes or new features, please get in touch via the contact details below.

---

## License

Proprietary — delivered exclusively to La Bella Cucina by StarForge. Not for redistribution.

---

## Credits & Contact

**Built by StarForge** — AI automation for businesses that want results, not complexity.

- 🌐 Website: [YOUR_WEBSITE_HERE]
- 📧 Email: [YOUR_EMAIL_HERE]
- 🐙 GitHub: [github.com/YOUR_GITHUB_USERNAME](https://github.com/YOUR_GITHUB_USERNAME)

> *"Turning AI complexity into business simplicity."*
