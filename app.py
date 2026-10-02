import streamlit as st

st.set_page_config(page_title="Community Hub", page_icon="🌱", layout="centered")

st.title("🌱 Community Economic Development")
st.write("Welcome to our local platform! Choose a tab below to explore.")

# Create tabs for your different sections
tab1, tab2, tab3 = st.tabs(["🛒 Marketplace", "💼 Local Pros", "🧠 Learn (AI)"])

with tab1:
    st.header("Local Artisan Marketplace")
    st.success("Support local! Buy handmade crafts and goods.")
    st.button("Browse Artisans")

with tab2:
    st.header("Find Local Entrepreneurs")
    st.info("Search for trusted services in your community.")
    st.text_input("Search for a service (e.g., Plumber, Web Design):")

with tab3:
    st.header("Financial Literacy Bot")
    st.warning("Ask simple questions about money, savings, and business.")
    user_question = st.text_input("What would you like to learn today?")
    if st.button("Ask AI"):
        st.write("*(The AI would answer your question here!)*")
