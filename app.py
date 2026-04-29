import streamlit as st

# 1. Page Configuration
st.set_page_config(
    page_title="NIC - Honestly Crafted Ice Creams",
    page_icon="🍦",
    layout="wide"
)

# 2. Custom CSS to make the image cover the screen and fix the background color
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    .stApp {
        background-color: #4a2c21; /* Matching your image's brown background */
        display: flex;
        justify-content: center;
        align-items: center;
    }

    .welcome-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        height: 100vh;
        width: 100vw;
    }

    .welcome-image {
        max-width: 80%;
        height: auto;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. The Raw Image Link
# Using 'raw' instead of 'blob' so the image plays the animation
image_url = "https://github.com/Deslandes1/Nic-Honestly-Crafted-Ice-creams/raw/main/image1.png"

# 4. Displaying the Welcome Content
st.markdown(f"""
    <div class="welcome-container">
        <img src="{image_url}" class="welcome-image">
        <h1 style='color: white; font-family: sans-serif; margin-top: 20px;'>NIC</h1>
        <p style='color: #fce4ec; font-size: 20px;'>Honestly Crafted Ice Creams</p>
    </div>
    """, unsafe_allow_html=True)

# 5. Optional: Use a sidebar or a "Enter App" button to move past the welcome screen
if st.sidebar.button("Enter Experience"):
    st.sidebar.success("Welcome to the flavor lab!")
