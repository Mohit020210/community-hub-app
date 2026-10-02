import streamlit as st
import pandas as pd
import google.generativeai as genai

# Page Configuration
st.set_page_config(page_title="Community Hub", page_icon="🌱", layout="wide", initial_sidebar_state="collapsed")

# Custom CSS for Pinterest-style UI and Bottom Navigation
st.markdown("""
    <style>
    /* Main Background & Force Dark Text */
    .stApp { 
        background-color: #fdfbf7; 
    }
    .stApp, .stApp p, .stApp h1, .stApp h2, .stApp h3, .stApp h4, .stApp h5, .stApp h6, .stApp span {
        color: #2b2b2b !important; 
    }
    
    /* Hide top header to look more like an app */
    header {visibility: hidden;}
    
    /* Pinterest Style Cards */
    .pin-card {
        background-color: white;
        border-radius: 16px;
        padding: 15px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        margin-bottom: 20px;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        text-align: center;
        border: 1px solid #eaeaea;
    }
    .pin-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 15px rgba(0,0,0,0.1);
    }
    .pin-image {
        width: 100%;
        border-radius: 12px;
        margin-bottom: 10px;
        object-fit: cover;
        height: 150px;
    }
    
    /* JustDial Style Directory Cards */
    .dir-card {
        background-color: white;
        border-radius: 12px;
        padding: 20px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
        margin-bottom: 15px;
        border-left: 6px solid #ff4b4b;
        display: flex;
        justify-content: space-between;
        align-items: center;
        border: 1px solid #eaeaea;
    }
    
    /* Chatbot Bubble */
    .chat-bubble {
        background-color: #e3f2fd;
        border-radius: 15px 15px 15px 0px;
        padding: 15px;
        margin: 10px 0;
        color: #0d47a1 !important;
        font-weight: 500;
        border: 1px solid #bbdefb;
    }
    </style>
""", unsafe_allow_html=True)
# App Title & Navigation (Using Tabs to simulate app navigation)
st.markdown("<h1 style='text-align: center; color: #ff4b4b;'>🌱 Community Hub</h1>", unsafe_allow_html=True)

# Navigation Tabs
home_tab, search_tab, learn_tab, profile_tab = st.tabs(["🏠 Home (Marketplace)", "🔍 Search (Local Pros)", "💡 Learn (AI)", "👤 Profile"])

# ---------------------------------------------------------
# TAB 1: HOME (Fiverr/Pinterest Style Skill-Sharing)
# ---------------------------------------------------------
with home_tab:
    st.markdown("### ✨ Discover Local Talent & Goods")
    
    # Category chips
    st.write("**Trending:** 🎨 Art | 👗 Tailoring | 💻 Tech | 🍰 Baking")
    st.divider()
    
    # Pinterest Grid using Streamlit Columns
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
        <div class="pin-card">
            <img src="https://picsum.photos/400/300?random=1" class="pin-image">
            <h4 style="margin:0;">Hand-woven Baskets</h4>
            <p style="color:gray; font-size:14px; margin:5px 0;">By: Ananya Crafts</p>
            <p style="font-weight:bold; color:#1dbf73; margin:0;">₹450</p>
        </div>
        """, unsafe_allow_html=True)
        st.button("Buy Now", key="buy1", use_container_width=True)

    with col2:
        st.markdown("""
        <div class="pin-card">
            <img src="https://picsum.photos/400/300?random=2" class="pin-image">
            <h4 style="margin:0;">Custom Embroidery</h4>
            <p style="color:gray; font-size:14px; margin:5px 0;">By: Sarah Tailors</p>
            <p style="font-weight:bold; color:#1dbf73; margin:0;">₹800</p>
        </div>
        """, unsafe_allow_html=True)
        st.button("Hire Sarah", key="buy2", use_container_width=True)

    with col3:
        st.markdown("""
        <div class="pin-card">
            <img src="https://picsum.photos/400/300?random=3" class="pin-image">
            <h4 style="margin:0;">Homemade Pickles</h4>
            <p style="color:gray; font-size:14px; margin:5px 0;">By: Raju's Kitchen</p>
            <p style="font-weight:bold; color:#1dbf73; margin:0;">₹200</p>
        </div>
        """, unsafe_allow_html=True)
        st.button("Order Fresh", key="buy3", use_container_width=True)
        
    with col4:
        st.markdown("""
        <div class="pin-card">
            <img src="https://picsum.photos/400/300?random=4" class="pin-image">
            <h4 style="margin:0;">Phone Repair</h4>
            <p style="color:gray; font-size:14px; margin:5px 0;">By: Tech Guru</p>
            <p style="font-weight:bold; color:#1dbf73; margin:0;">Starts at ₹500</p>
        </div>
        """, unsafe_allow_html=True)
        st.button("Book Repair", key="buy4", use_container_width=True)

# ---------------------------------------------------------
# TAB 2: SEARCH (JustDial Style Local Directory)
# ---------------------------------------------------------
with search_tab:
    st.markdown("### 📍 Find Trusted Local Services")
    
    # Search Bar
    search_query = st.text_input("What do you need help with? (e.g., Plumber, Tutor, Electrician)", placeholder="Type a service...")
    
    # Mock Database
    businesses = [
        {"name": "QuickFix Plumbing", "cat": "Plumber", "rating": "⭐⭐⭐⭐", "phone": "📞 +91 98765 43210"},
        {"name": "City Bright Tutors", "cat": "Education", "rating": "⭐⭐⭐⭐⭐", "phone": "📞 +91 98765 43211"},
        {"name": "Spark Electricians", "cat": "Electrician", "rating": "⭐⭐⭐⭐", "phone": "📞 +91 98765 43212"}
    ]
    
    for biz in businesses:
        st.markdown(f"""
        <div class="dir-card">
            <div>
                <h3 style="margin:0; color:#333;">{biz['name']}</h3>
                <p style="margin:0; color:gray;">{biz['cat']} | {biz['rating']}</p>
            </div>
            <div>
                <h4 style="margin:0; color:#ff4b4b;">{biz['phone']}</h4>
            </div>
        </div>
        """, unsafe_allow_html=True)

# ---------------------------------------------------------
# TAB 3: LEARN (AI Financial Literacy)
# ---------------------------------------------------------
with learn_tab:
    st.markdown("### 💡 Financial Helper")
    st.markdown("<p style='color:gray;'>Ask me anything about money, savings, or business. I use simple stories to explain!</p>", unsafe_allow_html=True)
    
    if "GEMINI_API_KEY" in st.secrets:
        genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        user_question = st.text_area("Write your question here:", placeholder="Example: What is an interest rate? Or, how do I save money from my shop?")
        
        if st.button("Ask AI ✨", type="primary"):
            if user_question:
                with st.spinner("Thinking of a simple story for you..."):
                    # Custom prompt to force simple, uneducated-friendly language and emojis
                    prompt = f"""
                    You are a friendly financial helper for people with no formal education. 
                    Explain this concept using very simple, everyday words. 
                    Use a real-life analogy (like farming, cooking, or running a small street stall).
                    Use emojis to make it visual and easy to read.
                    Do not use big financial jargon.
                    
                    User's Question: {user_question}
                    """
                    response = model.generate_content(prompt)
                    
                    st.markdown(f"""
                    <div class="chat-bubble">
                        {response.text}
                    </div>
                    """, unsafe_allow_html=True)
            else:
                st.warning("Please type a question first!")
    else:
        st.error("⚠️ AI is resting! Please add your GEMINI_API_KEY to Streamlit Settings -> Secrets.")
        st.info("Example Answer Preview: Think of an interest rate like planting a seed. If you give the bank your seed (money), they water it for you, and it grows extra leaves (interest) over time!")

# ---------------------------------------------------------
# TAB 4: PROFILE
# ---------------------------------------------------------
with profile_tab:
    st.markdown("### 👤 My Profile")
    st.write("**Name:** Community Member")
    st.write("**Saved Items:** 3 items")
    st.write("**Wallet Balance:** ₹1,200")
    st.button("⚙️ Settings")
    st.button("🚪 Logout")
