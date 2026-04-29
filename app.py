import streamlit as st

# 1. Page Config
st.set_page_config(
    page_title="GlobalInternet.py Promotion", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

# 2. Initialize Toggle State
if 'show_info' not in st.session_state:
    st.session_state.show_info = True # Set to True so it's visible by default

# 3. RAW GitHub Video Link
video_url = "https://raw.githubusercontent.com/Deslandes1/Nic-Honestly-Crafted-Ice-creams/main/dreamina-2026-04-29-5258-make%20the%20different%20flavor%20ice%20creams%20mov....mp4"

# 4. Sidebar with Toggle Logic
with st.sidebar:
    st.title("Navigation")
    
    # Toggle Button with Quotes
    if st.button('“ Tap to see/hide info ”'):
        st.session_state.show_info = not st.session_state.show_info

    # Information Display Logic
    if st.session_state.show_info:
        st.markdown("---")
        st.markdown("### **Partnership & Promotion**")
        st.write("Visit us at **Nic Honestly Crafted Ice Creams**:")
        st.markdown("[Visit Nic Ice Creams Official Site](https://www.nicicecreams.com/)")
        
        st.divider()
        
        st.markdown("#### **GlobalInternet.py**")
        st.write("The best online company to promote your online business.")

# 5. CSS for Fullscreen Video, Name Update, and White Text
# Note: Double curly braces {{ }} are used to avoid the SyntaxError
st.markdown(f"""
    <style>
    /* Hide top Streamlit UI */
    footer {{ visibility: hidden; }}
    header {{ visibility: hidden; }}
    
    .stApp {{
        margin: 0;
        padding: 0;
        background-color: #4a2c21;
    }}

    /* Sidebar Styling: Brown Background & White Text */
    [data-testid="stSidebar"] {{
        background-color: #4a2c21 !important;
        border-right: 1px solid rgba(255, 255, 255, 0.1);
    }}
    
    [data-testid="stSidebar"] * {{
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

    /* Text Overlay styling (Top Video) */
    .top-overlay {{
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        padding: 40px 0;
        text-align: center;
        z-index: 9999;
        background: linear-gradient(to bottom, rgba(0,0,0,0.6) 0%, rgba(0,0,0,0) 100%);
    }}

    .website-name {{
        color: white !important;
        font-family: 'Arial Black', sans-serif;
        font-size: 3.5rem;
        margin: 0;
        letter-spacing: 4px;
        text-shadow: 4px 4px 15px rgba(0,0,0,1);
    }}
    </style>

    <div class="top-overlay">
        <h1 class="website-name">GlobalInternet.py Promotion</h1>
    </div>

    <div class="video-container">
        <video autoplay loop muted playsinline>
            <source src="{video_url}" type="video/mp4">
            Your browser does not support the video tag.
        </video>
    </div>
    """, unsafe_allow_html=True)
