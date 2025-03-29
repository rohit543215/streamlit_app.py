import streamlit as st

# Shop Information
shop_name = "Rohit Farsan"
shop_address = "Niranjan Hira Complex, Beside Kaka Canteen, Uttam Nagar, Near Kaka Canteen, 1, NDA Road Shivane, Pune - 411023, India"
shop_category = "Snacks and Bakery"
owner_name = "Girish Joshi"
owner_email = "gj2615059@gmail.com"
owner_phone = "+91 9322431837"
shop_images = ["Screenshot 2025-03-29 122406.png"]  # Replace with actual image paths

# Streamlit UI Configuration
st.set_page_config(page_title=shop_name, page_icon="🍪", layout="wide")

st.title(f"🛍️ {shop_name}")
st.subheader("Local Shop Information")

# Display Shop Details
st.write(f"**📍 Address:** {shop_address}")
st.write(f"**🏷️ Category:** {shop_category}")
st.write(f"**👨‍💼 Owner:** {owner_name}")
st.write(f"**📧 Email:** {owner_email}")
st.write(f"**📞 Phone:** {owner_phone}")

# Display Shop Images
st.subheader("🏪 Shop Images")
if shop_images:
    for img in shop_images:
        st.image(img, caption="Shop View", width=400)

st.success("Visit us for delicious snacks and bakery items! 🍞🥖")

# Footer Section
st.markdown("---")
st.markdown(
    """
    <style>
        .footer {
            background-color: #00BCD4;
            padding: 20px;
            text-align: center;
            color: white;
            font-size: 16px;
            margin-top: 50px;
        }
        .footer-columns {
            display: flex;
            justify-content: space-around;
            flex-wrap: wrap;
        }
        .footer-section {
            flex: 1;
            min-width: 200px;
            text-align: left;
            padding: 10px;
        }
        .footer h4 {
            margin-bottom: 10px;
            font-weight: bold;
        }
        .footer a {
            color: white;
            text-decoration: none;
            display: block;
            margin-top: 5px;
        }
    </style>
    <div class="footer">
        <div class="footer-columns">
            <div class="footer-section">
                <h4>Help</h4>
                <a href="#">Shipping</a>
                <a href="#">Payments</a>
                <a href="#">Cancellation & Returns</a>
            </div>
            <div class="footer-section">
                <h4>Policies</h4>
                <a href="#">Privacy</a>
                <a href="#">Terms of Use</a>
                <a href="#">Returns</a>
            </div>
            <div class="footer-section">
                <h4>Visit Us</h4>
                📍 Niranjan Hira Complex, Beside Kaka Canteen, Uttam Nagar, Near Kaka Canteen, <br>
                1, NDA Road Shivane, Pune - 411023, India
            </div>
            <div class="footer-section">
                <h4>Contact Us</h4>
                📞 +91 9322431837 <br>
                ✉️ <a href="mailto:gj2615059@gmail.com">gj2615059@gmail.com</a>
            </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

