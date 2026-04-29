import streamlit as st

# 1. Page Config to hide all UI
st.set_page_config(page_title="NIC Welcome", layout="wide", initial_sidebar_state="collapsed")

# 2. RAW GitHub Video Link (Corrected format)
# We replace 'github.com' with 'raw.githubusercontent.com' and remove '/blob/'
video_url = "https://raw.githubusercontent.com/Deslandes1/Nic-Honestly-Crafted-Ice-creams/main/dreamina-2026-04-29-5258-make%20the%20different%20flavor%20ice%20creams%20mov....mp4"

# 3. CSS to force the video to fill the screen
st.markdown(f"""
    <style>
    /* Hide Streamlit elements */
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

    /* Video Container */
    .video-container {{
        position: fixed;
        top: 0;
        left: 0;
        width: 100vw;
        height: 100vh;
        z-index: 9999;
    }}

    video {{
        width: 100%;
        height: 100%;
        object-fit: cover; /* Ensures the video covers the screen without stretching */
    }}
    </style>

    <div class="video-container">
        <video autoplay loop muted playsinline>
            <source src="{video_url}" type="video/mp4">
            Your browser does not support the video tag.
        </video>
    </div>
    """, unsafe_allow_html=True)
