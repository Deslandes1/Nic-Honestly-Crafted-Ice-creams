import streamlit as st

# 1. Page Config
st.set_page_config(
    page_title="GlobalInternet.py", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

# 2. Initialize Toggle State
if 'show_info' not in st.session_state:
    st.session_state.show_info = True

def toggle_info():
    st.session_state.show_info = not st.session_state.show_info

# 3. RAW GitHub Video Link
video_url = "https://raw.githubusercontent.com/Deslandes1/Nic-Honestly-Crafted-Ice-creams/main/dreamina-2026-04-29-5258-make%20the%20different%20flavor%20ice%20creams%20mov....mp4"

# 4. Sidebar with Tap-to-Toggle Logic
with st.sidebar:
    st.title("Menu")
    # Tapping this button toggles the visibility
    if st.button("Tap to Toggle Info"):
        toggle_info()

    if st.session_state.show_info:
        st.markdown("---")
        st.markdown("### **Partnership & Promotion**")
        st.write("Visit us at **Nic Honestly Crafted Ice Creams**:")
        st.link_button("Visit Nic Ice Creams", "https://www.nicicecreams.com/")
        
        st.divider()
        
        st.write("**GlobalInternet.py**")
        st.write("The best online company to promote your online business.")

# 5. CSS for Fullscreen, Brown Sidebar, and White Text
st.markdown(f"""
    <style>
    /* Hide top Streamlit UI */
    footer {{ visibility: hidden; }}
    header {{ visibility: hidden; }}
    
    /* Main Background & Text Color */
    .stApp {{
        margin: 0;
        padding: 0;
        background-color: #4a2c21;
        color: white !important;
    }}

    /* Sidebar Styling: Brown Background & White Text */
    section[data-testid="stSidebar"] {{
        background-color: #4a2c21 !important;
        border-right: 1px solid rgba(255, 255, 255, 0.1);
    }}
    
    section[data-testid="stSidebar"] * {{
        color: white !important;
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
        padding: 30px 0;
        text-align: center;
        z-index: 9999;
        background: linear-gradient(to bottom, rgba(0,0,0,0.5) 0%, rgba(0,0,0,0) 100%);
    }}

    .website-name {{
        color: white !important;
        font-family: 'Arial Black', sans-serif;
        font-size: 3rem;
        margin: 0;
        letter-spacing: 3px;
        text-shadow: 3px 3px 10px rgba(0,0,0,0.7);
    }}

    .author-name {{
        color: white !important;
        font-family: 'Arial', sans-serif;
        font-size: 1.1rem;
        margin-top: 5px;
        letter-spacing: 1px;
    }}
    </style>

    <div class="top-overlay">
        <h1 class="website-name">GlobalInternet.py</h1>
        <p class="author-name">built by Gesner Deslandes</p>
    </div>

    <div class="video-container">
        <video autoplay loop muted playsinline>
            <source src="{video_url}" type="video/mp4">
            Your browser does not support the video tag.
        </video>
    </div>
    """, unsafe_allow_html=True)
