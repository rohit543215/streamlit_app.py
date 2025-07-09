import streamlit as st

# Set page config
st.set_page_config(page_title="Rvivera Consulting", layout="wide")

# --- Top Navbar with Sticky Header and Logo + Navigation Links ---
st.markdown("""
    <style>
    .navbar {
        position: fixed;
        top: 0;
        width: 100%;
        background-color: #ffffff;
        z-index: 999;
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 10px 30px;
        box-shadow: 0 2px 6px rgba(0, 0, 0, 0.1);
    }
    .nav-links a {
        margin: 0 15px;
        text-decoration: none;
        font-weight: 600;
        color: #0B0C10;
        font-size: 1rem;
    }
    .nav-links a:hover {
        color: #00CED1;
    }
    .spacer {
        height: 70px; /* height of fixed navbar */
    }
    </style>
    <div class="navbar">
        <img src="https://raw.githubusercontent.com/rohit543215/streamlit_app.py/main/ChatGPT Image Jul 2, 2025, 08_56_56 PM.png" alt="Rvivera Logo" height="40">
        <div class="nav-links">
            <a href="#About">About</a>
            <a href="#Services">Services</a>
            <a href="#Contact">Contact</a>
        </div>
    </div>
    <div class="spacer"></div>
""", unsafe_allow_html=True)

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
        color: #cccccc;
        text-align: center;
        margin-bottom: 2rem;
    }
    .section-title {
        font-size: 1.8em;
        font-weight: 700;
        margin-top: 2rem;
        color: #00CED1;
        border-bottom: 2px solid #00CED1;
        padding-bottom: 5px;
    }
    .content {
        font-size: 1.15em;
        color: #ffffff;
        line-height: 1.7;
    }
    .contact-box {
        border: 1px solid #00CED1;
        padding: 1em;
        border-radius: 8px;
        margin-top: 1em;
        background-color: #1F2833;
        color: #ffffff;
    }
    footer {
        text-align: center;
        font-size: 0.9em;
        color: #888;
        margin-top: 3rem;
    }
    hr {
        border: 0;
        border-top: 1px solid #2e4a67;
        margin-top: 3rem;
    }
    </style>
""", unsafe_allow_html=True)

# --- Header Text ---
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
st.markdown("<div class='section-title' id='About'>About Us</div>", unsafe_allow_html=True)
st.markdown("""
<div class='content'>
Rvivera Consulting is founded on a passion for financial literacy and market precision. Our vision is to empower everyday investors with the right tools and insights to take charge of their financial future. 

We understand that each individual’s journey is unique — that’s why we tailor our advisory services based on your goals, whether it's short-term momentum trading or building long-term portfolios.
</div>
""", unsafe_allow_html=True)

# --- Services Section ---
st.markdown("<div class='section-title' id='Services'>Our Services</div>", unsafe_allow_html=True)
st.markdown("""
<div class='content'>
At Rvivera Consulting, we offer:
<ul>
    <li><strong>Short-Term Trading:</strong> High-potential intraday and swing trade ideas, daily technical setups, entry/exit alerts</li>
    <li><strong>Long-Term Investments:</strong> Wealth-building strategies with asset allocation, rebalancing, and compounding insights</li>
    <li><strong>1-on-1 Consultations:</strong> Personalized mentoring and guidance for traders, investors, and beginners</li>
    <li><strong>Market Reports:</strong> Weekly market reviews, sector watchlists, and macro commentary</li>
</ul>
</div>
""", unsafe_allow_html=True)

# --- Contact Section ---
st.markdown("<div class='section-title' id='Contact'>Contact</div>", unsafe_allow_html=True)
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
