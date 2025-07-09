import streamlit as st

# Set page config
st.set_page_config(page_title="Rvivera Consulting", layout="centered")

# --- Show Logo ---
st.image("ChatGPT Image Jul 2, 2025, 08_56_56 PM.png", width=150)

# --- Custom Styling ---
st.markdown("""
    <style>
    .main {
        background-color: #000;
        color: #ffffff;
        font-family: 'Segoe UI', sans-serif;
        padding: 2rem;
    }
    .title {
        font-size: 3.2em;
        font-weight: 700;
        color: #00ffcc;
        text-align: center;
        margin-bottom: 0.5em;
    }
    .subtitle {
        font-size: 1.5em;
        text-align: center;
        color: #ffffff;
        margin-bottom: 2em;
    }
    .section-title {
        font-size: 1.8em;
        font-weight: bold;
        margin-top: 2em;
        color: #00ffcc;
    }
    .content {
        font-size: 1.1em;
        line-height: 1.6;
        color: #e0e0e0;
    }
    .contact-box {
        border: 1px solid #00ffcc;
        padding: 1em;
        border-radius: 10px;
        margin-top: 1em;
        background-color: #111;
    }
    </style>
""", unsafe_allow_html=True)

# --- Header ---
st.markdown("<div class='title'>Rvivera Consulting</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Empowering Your Financial Future</div>", unsafe_allow_html=True)

# --- Introduction ---
st.markdown("""
<div class='content'>
Welcome to <b>Rvivera Consulting</b>, your trusted partner for personalized investment solutions. We specialize in:
<ul>
    <li>📈 <b>Short-term Investments</b> in the Share Market</li>
    <li>🏦 <b>Long-term Wealth Building</b> through smart stock strategies</li>
</ul>
</div>
""", unsafe_allow_html=True)

# --- About Us Section ---
st.markdown("<div class='section-title'>About Us</div>", unsafe_allow_html=True)
st.markdown("""
<div class='content'>
At Rvivera Consulting, we believe every investor deserves a clear, confident, and profitable journey.
Founded by <b>Girish Joshi</b>, our mission is to simplify investment decisions through expert-backed consulting and actionable insights.
</div>
""", unsafe_allow_html=True)

# --- Services Section ---
st.markdown("<div class='section-title'>Our Services</div>", unsafe_allow_html=True)
st.markdown("""
<div class='content'>
<ul>
    <li>✅ <b>Short-Term Investment Consulting</b><br>
        Timely stock insights, trade setups, and daily market updates.</li>
    <li>🔒 <b>Long-Term Investment Planning</b><br>
        Portfolio structuring, risk management, and compounding strategies.</li>
</ul>
</div>
""", unsafe_allow_html=True)

# --- Contact Section ---
st.markdown("<div class='section-title'>Contact</div>", unsafe_allow_html=True)
st.markdown("""
<div class='contact-box'>
<b>Name:</b> Girish Joshi<br>
<b>Phone:</b> 9322431827<br>
<b>Address:</b> Uttam Nagar, Shivane, 411023
</div>
""", unsafe_allow_html=True)

# --- Footer ---
st.markdown("""
<hr style='margin-top: 3em; border: 0.5px solid #444;'>
<div style='text-align: center; color: #888;'>
Made with ❤️ using Streamlit
</div>
""", unsafe_allow_html=True)
