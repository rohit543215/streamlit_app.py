import streamlit as st

# Shop Information
shop_name = "Rohit Farsan"
shop_address = "Uttam Nagar, near Kaka Canteen, Pune - 411023"
shop_category = "Snacks and Bakery"
owner_name = "Girish Joshi"
owner_email = "gj2615059@gmail.com"
owner_phone = "9322431837"
shop_images = ["C:\Users\gj261\Pictures\Screenshots\Screenshot 2025-03-29 122406"]  # Replace with actual image paths

# Streamlit UI
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

# Footer
st.markdown("---")
st.write("📌 Powered by Streamlit | Contact us for collaborations!")

