import streamlit as st

# Set page config
st.set_page_config(page_title="Rvivera Consulting", layout="centered")

# Show logo
st.image("rvivera_logo.png", width=200)

# --- Styling ---
st.markdown("""
    <style>
    body { background-color: #000000; color: white; font-family: 'Segoe UI', sans-serif; }
    .title { font-size: 3em; font-weight: bold; margin-bottom: 0.5em; }
    .section-title { font-size: 1.8em; font-weight: bold; margin-top: 1em; color: #00ffcc; }
    .contact-box { border: 1px solid #00ffcc; padding: 1em; border-radius: 8px; margin-top: 1em; }
    </style>
""", unsafe_allow_html=True)

# --- Content ---
st.markdown("<div class='title'>Rvivera Consulting</div>", unsafe_allow_html=True)

st.markdown("""
**Empowering Your Financial Future**

Welcome to **Rvivera Consulting**, your trusted partner for personalized investment solutions. We specialize in:

- 📈 **Short-term Investments** in the Share Market  
- 🏦 **Long-term Wealth Building** through smart stock strategies
""")

# About Us Section
st.markdown("<div class='section-title'>About Us</div>", unsafe_allow_html=True)
st.markdown("""
At Rvivera Consulting, we believe every investor deserves a clear, confident, and profitable journey. Founded by **Girish Joshi**, our mission is to simplify investment decisions through expert-backed consulting.
""")

# Services Section
st.markdown("<div class='section-title'>Our Services</div>", unsafe_allow_html=True)
st.markdown("""
- ✅ **Short-Term Investment Consulting**  
  Timely stock insights, trade setups, and daily market updates.

- 🔒 **Long-Term Investment Planning**  
  Portfolio structuring, risk management, and compounding strategies.
""")

# Contact Section
st.markdown("<div class='section-title'>Contact</div>", unsafe_allow_html=True)
st.markdown("""
<div class='contact-box'>
<b>Name:</b> Girish Joshi  
<b>Phone:</b> 9322431827  
<b>Address:</b> Uttam Nagar, Shivane, 411023  
</div>
""", unsafe_allow_html=True)

# Footer
st.markdown("""
---
Made with ❤️ using Streamlit
""")
