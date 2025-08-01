import streamlit as st

# Page config
st.set_page_config(page_title="Rvivera Consulting", page_icon=":chart_with_upwards_trend:", layout="wide")

# --- Header with Logo ---
col1, col2 = st.columns([1, 4])
with col1:
    st.image("ChatGPT Image Jul 2, 2025, 08_56_56 PM.png", use_container_width=True)  # Add your logo file here
with col2:
    st.markdown("<h1 style='color:#0097A7;'>Rvivera Consulting</h1>", unsafe_allow_html=True)
    st.markdown("*Empowering Smart Investments*")

st.markdown("---")

# --- Hero Section ---
st.markdown(
    """
    <div style='text-align:center; font-size: 22px; padding: 10px; background-color:#e3f2fd; border-radius: 10px;'>
        <b>Welcome to Rvivera Consulting!</b>  
        We help businesses and investors make data-driven decisions with expert analysis and strategic insights.  
    </div>
    """,
    unsafe_allow_html=True,
)
st.markdown("<br>", unsafe_allow_html=True)

# Consultation Button
if st.button("📊 Request a Free Consultation"):
    st.info("📧 Email: gj2615059@gmail.com | 📞 Phone: 9322431837")

st.markdown("---")

# --- Our Services ---
st.markdown("## **Our Services**")
st.markdown(
    """
    <ul style="font-size: 18px;">
        <li>📈 <b>Investment Analysis & Reports</b> – Customized stock and market research reports.</li>
        <li>💼 <b>Portfolio Advisory</b> – Build, optimize, and manage profitable portfolios.</li>
        <li>📊 <b>Market Insights</b> – AI-powered analytics and market forecasting.</li>
        <li>🏪 <b>Business Analytics for MSMEs</b> – Helping local businesses grow with smart insights.</li>
        <li>📢 <b>Advertising & Growth Strategy</b> – Data-backed marketing and strategy solutions.</li>
    </ul>
    """,
    unsafe_allow_html=True,
)

# --- Why Choose Us? ---
st.markdown("---")
st.markdown("## **Why Choose Rvivera Consulting?**")
st.write(
    """
    - **Proven Expertise:** Data science and AI-powered strategies tailored for your business.  
    - **Trusted Reports:** We deliver actionable and precise insights that drive results.  
    - **Affordable Packages:** Flexible plans for individuals, traders, and MSMEs.  
    - **Personalized Service:** Every report and advisory plan is custom-built for your needs.
    """
)

# --- Contact Info ---
st.markdown("---")
st.markdown("## **Contact**")
st.markdown("""
**Name:** Girish Joshi  
**Phone:** 9322431837  
**Address:** Uttam Nagar, Shivane, 411023  
**Email:** [gj2615059@gmail.com](mailto:gj2615059@gmail.com)
""")

# --- Footer ---
st.markdown("---")
st.markdown(
    "<div style='text-align:center; font-size:14px;'>© 2025 Rvivera Consulting | <a href='https://www.linkedin.com/in/girish-joshi-539b94262/'>LinkedIn</a> | <a href='https://twitter.com'>Twitter</a></div>",
    unsafe_allow_html=True,
)
