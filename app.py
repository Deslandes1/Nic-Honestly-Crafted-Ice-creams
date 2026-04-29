import streamlit as st

# Set page configuration
st.set_page_config(page_title="Gesner Deslandes - Welcome", page_icon="🍦")

# The Raw GitHub link to your image
# Note: changed 'blob' to 'raw' so Streamlit can read the file directly
image_url = "https://github.com/Deslandes1/Nic-Honestly-Crafted-Ice-creams/raw/main/image1.png"

# Display the Welcome Header
st.title("Welcome to Our App Suite")
st.subheader("Honestly Crafted Innovation by Gesner Deslandes")

# Display the moving ice cream image/GIF
st.image(image_url, caption="Our Signature Flavors in Motion", use_column_width=True)

# Information Section
st.write("---")
st.markdown("""
### 🚀 Start Your Free Trial
We are offering a **two-week free trial**! Explore our suite of applications, learn new skills, and see which tool fits your needs best.

* **No restrictions:** Use any app you want.
* **Duration:** 14 days of full access.
""")

# Call to Action
if st.button("Get in Touch with the CEO"):
    st.write("Contacting **Gesner Deslandes CEO**... Please check our contact page or email support.")

# Footer Link
st.info(f"Visit the full site: [Click Here](https://globalinternetsitepy-abh7v6tnmskxxnuplrdcgk.streamlit.app/)")
