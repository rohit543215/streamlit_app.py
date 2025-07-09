import streamlit as st

# Set page config
st.set_page_config(page_title="Rvivera Consulting", layout="wide")

# Show logo
st.image("ChatGPT Image Jul 2, 2025, 08_56_56 PM.png", width=140)

# --- Custom Styling ---
st.markdown("""
    <style>
    body {
        background-color: #0B0C10;
        color: #ffffff;
        font-family: 'Segoe UI', sans-serif;
    }
    .title {
        font-size: 3.2em;
        font-weight: bold;
        color: #ffffff;
        text-align: center;
        margin-top: 1rem;
    }
    .subtitle {
        font-size: 1.4em;
        color: #AAAAAA;
        text-align: center;
        margin-bottom: 2rem;
    }
    .section-title {
        font-size: 1.8em;
        font-weight: 700;
        margin-top: 2rem;
        color: #01DFD7;
        border-bottom: 2px solid #01DFD7;
        padding-bottom: 5px;
    }
    .content {
        font-size: 1.1em;
        color: #DDDDDD;
        line-height: 1.7;
    }
    .contact-box {
        border: 1px solid #01DFD7;
        padding: 1em;
        border-radius: 8px;
        margin-top: 1em;
        background-color: #1F2833;
    }
    footer {
        text-align: center;
        font-size: 0.9em;
        color: #666;
        margin-top: 3rem;
    }
    hr {
        border: 0;
        border-top: 1px solid #2e4a67;
        margin-top: 3rem;
    }
    </style>
""", unsafe_allow_html=True)

# --- Header ---
st.markdown("<div class='title'>Rvivera Consulting</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Expert-Driven Stock Market Guidance | Invest Smarter. Grow Faster.</div>", unsafe_allow_html=True)

# --- Intro ---
st.markdown("""
<div class='content'>
Welcome to <strong>Rvivera Consulting</strong>, where insights meet performance. We help you navigate the market with confidence by offering reliable and actionable investment strategies tailored for:
<ul>
    <li><strong>Short-Term Trading</strong> – quick-turnaround opportunities using technical and market sentiment analysis</li>
    <li><strong>Long-Term Wealth Creation</strong> – portfolio planning, compounding, and capital growth strategies</li>
</ul>
</div>
""", unsafe_allow_html=True)

# --- About Us Section ---
st.markdown("<div class='section-title'>About Us</div>", unsafe_allow_html=True)
st.markdown("""
<div class='content'>
Founded by <strong>Girish Joshi</strong>, Rvivera Consulting is a modern advisory firm helping individuals and small businesses make informed financial decisions in the stock market. With a blend of research, risk control, and strategy, we aim to simplify investing for all.
</div>
""", unsafe_allow_html=True)

# --- Services Section ---
st.markdown("<div class='section-title'>Our Services</div>", unsafe_allow_html=True)
st.markdown("""
<div class='content'>
<ul>
    <li><strong>Daily Trade Setups</strong> – curated entries, stop-losses, and targets</li>
    <li><strong>Long-Term Investment Plans</strong> – tax-efficient and diversified portfolio design</li>
    <li><strong>One-on-One Consultations</strong> – personalized strategy discussions</li>
</ul>
</div>
""", unsafe_allow_html=True)

# --- Contact Section ---
st.markdown("<div class='section-title'>Contact</div>", unsafe_allow_html=True)
st.markdown("""
<div class='contact-box'>
<b>Name:</b> Girish Joshi<br>
<b>Phone:</b> 9322431827<br>
<b>Address:</b> Uttam Nagar, Shivane, 411023<br>
<b>Email:</b> contact@rviveraconsulting.com
</div>
""", unsafe_allow_html=True)

# --- Footer ---
st.markdown("""
<hr>
<footer>
Copyright © 2025 Rvivera Consulting. All rights reserved. | Designed with ❤️ in India
</footer>
""", unsafe_allow_html=True)
