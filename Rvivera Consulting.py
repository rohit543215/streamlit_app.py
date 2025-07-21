import streamlit as st

# Set page configuration
st.set_page_config(page_title="Rvivera Consulting", page_icon=":chart_with_upwards_trend:", layout="wide")

# Add logo and title
col1, col2 = st.columns([1, 4])
with col1:
    st.image("ChatGPT Image Jul 2, 2025, 08_56_56 PM.png", use_container_width=True)  # Replace 'logo.png' with your logo file
with col2:
    st.markdown(
        """
        # **Rvivera Consulting**
        *Empowering Smart Investments*
        """,
        unsafe_allow_html=True,
    )

st.markdown("---")

# Our Services Section
st.markdown("## **Our Services**")
st.write("""
- **Investment Analysis & Reports**: Customized stock and market research reports for better decision-making.
- **Portfolio Advisory**: Expert guidance to build, optimize, and balance your portfolio.
- **Market Insights**: Data-driven analytics and strategies for stock market trends.
- **Business Analytics Solutions**: Helping MSMEs grow by providing deep data analysis and forecasting.
""")

st.markdown("---")

# Contact Section
st.markdown("## **Contact**")

st.markdown("""
**Name:** Girish Joshi  
**Phone:** 9322431827  
**Address:** Uttam Nagar, Shivane, 411023  
**Email:** [contact@rviveraconsulting.com](mailto:contact@rviveraconsulting.com)
""")

# Footer
st.markdown("---")
st.write("© 2025 **Rvivera Consulting** | All Rights Reserved.")
