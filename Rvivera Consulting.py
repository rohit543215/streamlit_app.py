import streamlit as st

# Set page config
st.set_page_config(page_title="Rvivera Consulting", layout="wide")

# Show logo
st.image("rvivera_logo.png", width=140)

# --- Custom Styling ---
st.markdown("""
    <style>
    body {
        background-color: #0c1a32;
        color: #ffffff;
        font-family: 'Segoe UI', sans-serif;
    }
    .title {
        font-size: 3em;
        font-weight: 800;
        color: #ffffff;
        text-align: center;
        margin-top: 1rem;
    }
    .subtitle {
        font-size: 1.5em;
        color: #a3d2ff;
        text-align: center;
        margin-bottom: 2rem;
    }
    .section-title {
        font-size: 1.6em;
        font-weight: 700;
        margin-top: 2rem;
        color: #00d1ff;
    }
    .content {
        font-size: 1.1em;
        color: #e0f7ff;
        line-height: 1.6;
    }
    .contact-box {
        border: 1px solid #00d1ff;
        padding: 1em;
        border-radius: 8px;
        margin-top: 1em;
        background-color: #132b44;
    }
    footer {
        text-align: center;
        font-size: 0.9em;
        color: #aaa;
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
st.markdown("<div class='subtitle'>Advisory-First Stock Market Consulting Platform</div>", unsafe_allow_html=True)

# --- Intro ---
st.markdown("""
<div class='content'>
Welcome to <strong>Rvivera Consulting</strong>, your trusted partner for personalized investment strategies. We provide actionable, timely, and research-backed guidance for:
<ul>
    <li><strong>Short-term Investments</strong> – swing & intraday opportunities</li>
    <li><strong>Long-term Wealth Planning</strong> – growth-oriented portfolios</li>
</ul>
</div>
""", unsafe_allow_html=True)

# --- About Us Section ---
st.markdown("<div class='section-title'>About Us</div>", unsafe_allow_html=True)
st.markdown("""
<div class='content'>
Founded by <strong>Girish Joshi</strong>, Rvivera Consulting is built on the principles of discipline, transparency, and performance. We help new and experienced investors grow confidently in the Indian stock market.
</div>
""", unsafe_allow_html=True)

# --- Services Section ---
st.markdown("<div class='section-title'>Our Services</div>", unsafe_allow_html=True)
st.markdown("""
<div class='content'>
<ul>
    <li><strong>Short-Term Advisory:</strong> Daily trade ideas, setups, and exits based on technicals and sentiment analysis.</li>
    <li><strong>Long-Term Investment Planning:</strong> Asset allocation, portfolio design, and compounding strategies for wealth creation.</li>
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
</div>
""", unsafe_allow_html=True)

# --- Footer ---
st.markdown("""
<hr>
<footer>
Copyright © 2025 Rvivera Consulting. All rights reserved. | Designed with ❤️ in India
</footer>
""", unsafe_allow_html=True)
