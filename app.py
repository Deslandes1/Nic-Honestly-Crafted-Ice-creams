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

# 3. Video Links (RAW GitHub format is mandatory)
video_1 = "https://raw.githubusercontent.com/Deslandes1/Nic-Honestly-Crafted-Ice-creams/main/dreamina-2026-04-29-5258-make%20the%20different%20flavor%20ice%20creams%20mov....mp4"
video_2 = "https://raw.githubusercontent.com/Deslandes1/Nic-Honestly-Crafted-Ice-creams/main/dreamina-2026-04-29-3384-his%20writing%20must%20passing%20by%20as%20a%20slidesh....mp4"

# 4. Sidebar Content with Your Full Description
with st.sidebar:
    st.title("Menu")
    
    if st.button('“ Tap to see/hide info ”'):
        st.session_state.show_info = not st.session_state.show_info

    if st.session_state.show_info:
        st.markdown("---")
        st.markdown("### 🍦 Indulge in Perfection")
        st.write("""
        Experience the art of pure indulgence. **NIC Honestly Crafted Ice Creams** isn't just a dessert; 
        it’s a masterpiece of flavor and texture. Every scoop is crafted with honesty and quality.
        """)
        st.markdown("👉 **Explore here:** [www.nicicecreams.com](https://www.nicicecreams.com/)")
        
        st.divider()
        
        st.markdown("### 🚀 Powered by GlobalInternet.py")
        st.write("""
        We promote your online business by generating the **best-fit video content** tailored to your brand’s identity.
        """)
        st.write("🌐 **Web:** [GlobalInternet.py](https://globalinternetsitepy-abh7v6tnmskxxnuplrdcgk.streamlit.app/)")
        st.write("📧 **Email:** deslandes78@gmail.com")
        st.write("📞 **Phone:** (509)-47385663")
        
        st.caption("“We craft digital experiences that sell.”")

# 5. CSS & Javascript for Continuous Slideshow
st.markdown(f"""
    <style>
    footer {{ visibility: hidden; }}
    header {{ visibility: hidden; }}
    
    .stApp {{
        margin: 0;
        padding: 0;
        background-color: #4a2c21;
    }}

    [data-testid="stSidebar"] {{
        background-color: #4a2c21 !important;
        border-right: 1px solid rgba(255, 255, 255, 0.1);
    }}
    
    [data-testid="stSidebar"] * {{
        color: white !important;
    }}

    .video-container {{
        position: fixed;
        top: 0;
        left: 0;
        width: 100vw;
        height: 100vh;
        z-index: 1;
        background-color: black;
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
        <video id="slideshowPlayer" autoplay muted playsinline>
            <source src="{video_1}" type="video/mp4">
        </video>
    </div>

    <script>
    var player = document.getElementById('slideshowPlayer');
    var playlist = ["{video_1}", "{video_2}"];
    var current = 0;

    player.onended = function() {{
        current++;
        if (current >= playlist.length) {{
            current = 0;
        }}
        // Force source change and reload
        player.src = playlist[current];
        player.load();
        player.play();
    }};
    </script>
    """, unsafe_allow_html=True)
