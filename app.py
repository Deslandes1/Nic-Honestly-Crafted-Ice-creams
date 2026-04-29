import streamlit as st

# 1. Page Config to hide the sidebar by default
st.set_page_config(page_title="NIC Ice Creams", layout="wide", initial_sidebar_state="collapsed")

# 2. Raw GitHub Link (Changed 'blob' to 'raw' so the player can stream it)
video_url = "https://github.com/Deslandes1/Nic-Honestly-Crafted-Ice-creams/raw/main/dreamina-2026-04-29-5258-make%20the%20different%20flavor%20ice%20creams%20mov....mp4"

# 3. CSS to make the video cover the entire screen
st.markdown(f"""
    <style>
    /* Hide Streamlit UI elements */
    #MainMenu {{visibility: hidden;}}
    footer {{visibility: hidden;}}
    header {{visibility: hidden;}}
    .stApp {{
        margin: 0;
        padding: 0;
        background-color: #4a2c21; /* Matches your background color */
        overflow: hidden;
    }}

    /* Video styling to fill the whole screen */
    .fullscreen-bg {{
        position: fixed;
        top: 0;
        left: 0;
        width: 100vw;
        height: 100vh;
        overflow: hidden;
        z-index: -1;
        display: flex;
        justify-content: center;
        align-items: center;
    }}

    video {{
        min-width: 100%;
        min-height: 100%;
        width: auto;
        height: auto;
        object-fit: cover;
    }}
    </style>

    <div class="fullscreen-bg">
        <video autoplay loop muted playsinline>
            <source src="{video_url}" type="video/mp4">
            Your browser does not support the video tag.
        </video>
    </div>
    """, unsafe_allow_html=True)
