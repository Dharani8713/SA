import streamlit as st
import json
import re
from utils.escalation import escalate_to_telegram

# --- Load FAQs ---
with open("data/faqs.json", "r") as f:
    faq_data = json.load(f)

st.set_page_config(page_title="Support Assistant", page_icon="🤖")
st.title("Support Assistant 🤖")
st.write("Ask me a question about company policies, support, or FAQs.")

user_query = st.text_input("Your question:")

if user_query:
    # --- Keyword-based matching ---
    best_match = None
    for q, a in faq_data.items():
        # Split into keywords
        faq_keywords = set(re.findall(r"\w+", q.lower()))
        query_keywords = set(re.findall(r"\w+", user_query.lower()))
        overlap = faq_keywords.intersection(query_keywords)

        if overlap:
            best_match = (q, a)
            break

    if best_match:
        st.info(f"Closest FAQ: **{best_match[0]}**")
        st.success(best_match[1])

        # Ask user if answer was sufficient
        st.write("Was this answer sufficient?")
        if st.button("Yes ✅"):
            st.success("Glad I could help!")
        if st.button("No ❌"):
            st.warning("Escalating to human support...")
            escalate_to_telegram(user_query)

    else:
        st.warning("I couldn’t find a relevant answer. Escalating to human support...")
        escalate_to_telegram(user_query)
