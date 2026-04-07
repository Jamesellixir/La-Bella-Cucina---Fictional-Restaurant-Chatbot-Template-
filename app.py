import os
import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# --- System Prompt (the chatbot's personality and knowledge) ---
SYSTEM_PROMPT = """
You are a friendly and helpful customer service assistant for La Bella Cucina,
an Italian restaurant located at 45 Galle Road, Colombo 03, Sri Lanka.

Your job is to help customers with:
- Menu questions (prices, ingredients, dietary options)
- Making reservations and explaining the booking process
- Providing opening hours, location, and contact information
- Answering general questions about the restaurant

Restaurant details:
- Name: La Bella Cucina
- Cuisine: Italian (wood-fired pizza, fresh pasta, desserts)
- Hours: Monday-Saturday 11am-10pm, Sunday 12pm-9pm
- Location: 45 Galle Road, Colombo 03
- Phone: +94 11 234 5678
- Reservations: Required for groups of 6+, book 24 hrs in advance
- Delivery: Available via PickMe Food and Uber Eats

Menu:
Starters: Bruschetta (Rs. 950), Caprese Salad (Rs. 1,200), Garlic Bread (Rs. 650)
Pasta: Spaghetti Carbonara (Rs. 2,100), Penne Arrabbiata (Rs. 1,850), Fettuccine Alfredo (Rs. 2,000)
Pizza: Margherita (Rs. 2,400), Pepperoni (Rs. 2,800), Quattro Formaggi (Rs. 3,100)
Desserts: Tiramisu (Rs. 1,100), Panna Cotta (Rs. 950), Gelato (Rs. 750)

Always be warm, concise, and helpful. If unsure, direct them to call +94 11 234 5678.
Keep responses under 150 words unless listing the full menu.
"""

# --- Page Configuration ---
st.set_page_config(
    page_title="La Bella Cucina — Chat With Us",
    page_icon="🍽️",
    layout="centered"
)

# --- Sidebar ---
with st.sidebar:
    st.markdown("## 🍽️ La Bella Cucina")
    st.markdown("*Authentic Italian Cuisine*")
    st.divider()
    st.markdown("📍 **Location**")
    st.markdown("45 Galle Road, Colombo 03")
    st.divider()
    st.markdown("🕐 **Opening Hours**")
    st.markdown("Mon–Sat: 11am – 10pm")
    st.markdown("Sun: 12pm – 9pm")
    st.divider()
    st.markdown("📞 **Contact**")
    st.markdown("+94 11 234 5678")
    st.divider()
    st.markdown("🛵 **Delivery**")
    st.markdown("PickMe Food & Uber Eats")
    st.divider()
    # Clear chat button
    if st.button("🗑️ Clear Chat"):
        st.session_state.messages = []
        st.rerun()
    st.divider()
    st.caption("Powered by [StarForge](https://github.com/Jamesellixir) 🌟")

# --- Main Header ---
st.title("🍽️ La Bella Cucina")
st.markdown("**Chat with our virtual assistant — ask about the menu, reservations, or anything else!**")
st.divider()

# --- Initialize Chat History ---
if "messages" not in st.session_state:
    st.session_state.messages = []
    # Add welcome message
    st.session_state.messages.append({
        "role": "assistant",
        "content": "👋 Ciao! Welcome to La Bella Cucina! I'm here to help you with our menu, reservations, and any questions you have. How can I assist you today?"
    })

# --- Display Chat History ---
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# --- Chat Input ---
if prompt := st.chat_input("Ask me anything — menu, reservations, hours..."):
    
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Generate assistant response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            
            # Build messages list for API call
            # We send the full conversation history so GPT has context
            api_messages = [
                {"role": "system", "content": SYSTEM_PROMPT}
            ] + [
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ]
            
            # Call OpenAI API
            response = client.chat.completions.create(
                model="gpt-4o-mini",  # Cheap and fast — perfect for demos
                messages=api_messages,
                max_tokens=300,
                temperature=0.7  # Slightly creative but mostly factual
            )
            
            # Extract response text
            assistant_response = response.choices[0].message.content
            
            # Display the response
            st.markdown(assistant_response)
    
    # Add assistant response to chat history
    st.session_state.messages.append({
        "role": "assistant",
        "content": assistant_response
    })