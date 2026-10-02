import streamlit as st
import pandas as pd
import google.generativeai as genai

# Page Configuration (Must be the first Streamlit command)
st.set_page_config(page_title="Community Hub", page_icon="🌟", layout="wide")

# Custom CSS to make it look attractive and colorful
st.markdown("""
    <style>
    .fiverr-card {
        background-color: #f8f9fa;
        padding: 15px;
        border-radius: 10px;
        border-left: 5px solid #1dbf73;
        box-shadow: 2px 2px 5px rgba(0,0,0,0.1);
        margin-bottom: 15px;
    }
    .jd-card {
        background-color: #fff4e6;
        padding: 15px;
        border-radius: 10px;
        border-left: 5px solid #ff7b00;
        box-shadow: 2px 2px 5px rgba(0,0,0,0.1);
        margin-bottom: 15px;
    }
    </style>
""", unsafe_allow_html=True)

# Main Title
st.title("🌟 Community Economic Development Hub")
st.write("Empowering local artisans, businesses, and individuals.")

# Create the Navigation Tabs
tab1, tab2, tab3 = st.tabs(["🛒 Marketplace (Fiverr style)", "📍 Local Pros (JustDial style)", "🤖 Financial Advisor (AI)"])

# ---------------------------------------------------------
# TAB 1: FIVERR STYLE MARKETPLACE
# ---------------------------------------------------------
with tab1:
    st.header("Freelance & Artisan Marketplace")
    st.write("Hire local talent for your projects or buy handmade goods.")
    
    # Category Filter
    category = st.radio("Select Category:", ["All", "Graphic Design", "Handicrafts", "Web Development"], horizontal=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="fiverr-card">
            <h4>🎨 Custom Logo Design</h4>
            <p><b>By:</b> Sarah Jen</p>
            <p>⭐ 4.9 (120 reviews)</p>
            <p><i>Starts at ₹500</i> | ⚡ 2 Day Delivery</p>
        </div>
        """, unsafe_allow_html=True)
        st.button("Hire Sarah", key="btn1")

    with col2:
        st.markdown("""
        <div class="fiverr-card">
            <h4>🏺 Hand-Painted Pottery</h4>
            <p><b>By:</b> Rahul Crafts</p>
            <p>⭐ 4.8 (85 reviews)</p>
            <p><i>Starts at ₹800</i> | 📦 Free Local Shipping</p>
        </div>
        """, unsafe_allow_html=True)
        st.button("Buy from Rahul", key="btn2")

    with col3:
        st.markdown("""
        <div class="fiverr-card">
            <h4>💻 Basic Website Setup</h4>
            <p><b>By:</b> Techies Local</p>
            <p>⭐ 5.0 (42 reviews)</p>
            <p><i>Starts at ₹2500</i> | ⚡ 5 Day Delivery</p>
        </div>
        """, unsafe_allow_html=True)
        st.button("Hire Techies", key="btn3")

# ---------------------------------------------------------
# TAB 2: JUSTDIAL STYLE LOCAL PROS
# ---------------------------------------------------------
with tab2:
    st.header("Local Business Directory")
    
    # Search Bar
    search_query = st.text_input("🔍 What service are you looking for? (e.g., Plumber, Electrician, Tutor)")
    
    # Quick Categories
    st.write("**Popular Categories:** 🔧 Repair | 🧹 Cleaning | 📚 Education | 🍎 Groceries")
    st.divider()

    # Mock Database using Pandas for a clean table look
    business_data = pd.DataFrame({
        "Business Name": ["Sharma Electricals", "QuickFix Plumbing", "City Tutors", "Green Grocers"],
        "Category": ["Electrician", "Plumber", "Education", "Groceries"],
        "Rating": ["⭐⭐⭐⭐½", "⭐⭐⭐⭐", "⭐⭐⭐⭐⭐", "⭐⭐⭐⭐"],
        "Contact": ["+91 9876543210", "+91 9876543211", "+91 9876543212", "+91 9876543213"],
        "Location": ["Downtown", "North Side", "West End", "Downtown"]
    })
    
    # Display the directory attractively
    for index, row in business_data.iterrows():
        st.markdown(f"""
        <div class="jd-card">
            <h3 style="margin:0; color:#ff7b00;">{row['Business Name']}</h3>
            <p style="margin:0;"><b>{row['Category']}</b> | {row['Location']}</p>
            <p style="margin:0;">{row['Rating']} | 📞 {row['Contact']}</p>
        </div>
        """, unsafe_allow_html=True)

# ---------------------------------------------------------
# TAB 3: AI FINANCIAL LITERACY BOT
# ---------------------------------------------------------
with tab3:
    st.header("🤖 Simple Financial Advisor")
    st.info("Ask me anything about saving money, starting a small business, or managing debt. I explain things simply!")

    # Check if the API key is in Streamlit Secrets
    if "GEMINI_API_KEY" in st.secrets:
        genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        user_question = st.text_area("What is your financial question?")
        
        if st.button("Ask AI ✨"):
            if user_question:
                with st.spinner("Thinking..."):
                    # We tell the AI to speak simply
                    prompt = f"Explain this financial concept to someone with no financial background using simple words and analogies. Question: {user_question}"
                    response = model.generate_content(prompt)
                    st.success("Here is your answer:")
                    st.write(response.text)
            else:
                st.warning("Please type a question first.")
    else:
        st.error("⚠️ API Key not found! Please add your GEMINI_API_KEY to Streamlit Secrets to use the AI chatbot.")
        st.write("For now, here is a preview of how the chat looks:")
        st.text_area("What is your financial question?", disabled=True)
        st.button("Ask AI ✨", disabled=True)
