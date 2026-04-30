import streamlit as st

# 1. Page Config
st.set_page_config(
    page_title="NIC Honestly Crafted Ice Creams", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

# 2. Initialize Toggle State
if 'show_info' not in st.session_state:
    st.session_state.show_info = True 

# 3. Video Links (Raw GitHub Links)
video_1 = "https://raw.githubusercontent.com/Deslandes1/Nic-Honestly-Crafted-Ice-creams/main/dreamina-2026-04-29-5258-make%20the%20different%20flavor%20ice%20creams%20mov....mp4"
video_2 = "https://raw.githubusercontent.com/Deslandes1/Nic-Honestly-Crafted-Ice-creams/main/dreamina-2026-04-29-3384-his%20writing%20must%20passing%20by%20as%20a%20slidesh....mp4"

# 4. Sidebar Content
with st.sidebar:
    st.title("Menu")
    if st.button('“ Tap to see/hide info ”'):
        st.session_state.show_info = not st.session_state.show_info

    if st.session_state.show_info:
        st.markdown("---")
        st.markdown("### 🍦 Indulge in Perfection")
        st.write("Experience the art of pure indulgence. **NIC Honestly Crafted Ice Creams** is a masterpiece of flavor.")
        st.markdown("👉 [www.nicicecreams.com](https://www.nicicecreams.com/)")
        st.divider()
        st.markdown("### 🚀 Powered by GlobalInternet.py")
        st.write("We promote your online business with custom video content.")
        st.write("📞 **Phone:** (509)-47385663")
        st.write("📧 **Email:** deslandes78@gmail.com")
        st.write("🌐 **Web:** [GlobalInternet.py](https://globalinternetsitepy-abh7v6tnmskxxnuplrdcgk.streamlit.app/)")

# 5. CSS and Javascript for the Slideshow
st.markdown(f"""
    <style>
    footer {{ visibility: hidden; }}
    header {{ visibility: hidden; }}
    .stApp {{ margin: 0; padding: 0; background-color: #4a2c21; }}
    
    [data-testid="stSidebar"] {{ background-color: #4a2c21 !important; }}
    [data-testid="stSidebar"] * {{ color: white !important; }}

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

    .top-overlay {{
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        padding: 50px 0;
        text-align: center;
        z-index: 9999;
        background: linear-gradient(to bottom, rgba(0,0,0,0.6) 0%, rgba(0,0,0,0) 100%);
    }}

    .website-name {{
        color: white !important;
        font-family: 'Arial Black', sans-serif;
        font-size: 3.5rem;
        text-shadow: 4px 4px 15px rgba(0,0,0,1);
    }}
    </style>

    <div class="top-overlay">
        <h1 class="website-name">NIC Honestly Crafted Ice Creams</h1>
    </div>

    <div class="video-container">
        <video id="mainPlayer" autoplay muted playsinline>
            <source src="{video_1}" type="video/mp4">
        </video>
    </div>

    <script>
    var player = document.getElementById('mainPlayer');
    var playlist = ["{video_1}", "{video_2}"];
    var activeVideo = 0;

    player.onended = function() {{
        activeVideo++;
        if (activeVideo >= playlist.length) {{
            activeVideo = 0;
        }}
        
        // Update the source and force a reload
        player.src = playlist[activeVideo];
        player.pause();
        player.load();
        player.play().catch(error => {{
            console.log("Auto-play was prevented. Ensuring muted state.");
            player.muted = true;
            player.play();
        }});
    }};
    </script>
    """, unsafe_allow_html=True)
