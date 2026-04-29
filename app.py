import streamlit as st

# 1. Page Config
st.set_page_config(page_title="GlobalInternet.py", layout="wide", initial_sidebar_state="collapsed")

# 2. RAW GitHub Video Link
video_url = "https://raw.githubusercontent.com/Deslandes1/Nic-Honestly-Crafted-Ice-creams/main/dreamina-2026-04-29-5258-make%20the%20different%20flavor%20ice%20creams%20mov....mp4"

# 3. CSS for Fullscreen Video and Top Text Overlay
st.markdown(f"""
    <style>
    /* Hide all Streamlit UI */
    #MainMenu {{visibility: hidden;}}
    footer {{visibility: hidden;}}
    header {{visibility: hidden;}}
    [data-testid="stSidebar"] {{visibility: hidden;}}
    
    .stApp {{
        margin: 0;
        padding: 0;
        background-color: #4a2c21;
        overflow: hidden;
    }}

    /* Video styling */
    .video-container {{
        position: fixed;
        top: 0;
        left: 0;
        width: 100vw;
        height: 100vh;
        z-index: 1;
    }}

    video {{
        width: 100%;
        height: 100%;
        object-fit: cover;
    }}

    /* Text Overlay styling */
    .top-overlay {{
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        padding: 20px;
        text-align: center;
        z-index: 9999; /* Ensure it stays above the video */
        background: rgba(0, 0, 0, 0.3); /* Subtle dark fade for readability */
    }}

    .website-name {{
        color: white;
        font-family: 'Arial Black', sans-serif;
        font-size: 2.5rem;
        margin: 0;
        letter-spacing: 2px;
        text-shadow: 2px 2px 8px rgba(0,0,0,0.8);
    }}

    .author-name {{
        color: #fce4ec;
        font-family: 'Courier New', monospace;
        font-size: 1.2rem;
        margin: 5px 0 0 0;
        font-weight: bold;
    }}
    </style>

    <div class="top-overlay">
        <h1 class="website-name">GlobalInternet.py</h1>
        <p class="author-name">Built by Gesner Deslandes</p>
    </div>

    <div class="video-container">
        <video autoplay loop muted playsinline>
            <source src="{video_url}" type="video/mp4">
            Your browser does not support the video tag.
        </video>
    </div>
    """, unsafe_allow_html=True)
