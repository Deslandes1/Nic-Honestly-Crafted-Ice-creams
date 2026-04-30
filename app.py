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

# 3. Direct Video Links (Using the RAW format)
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
        st.markdown("👉 [Visit NIC Ice Creams](https://www.nicicecreams.com/)")
        st.divider()
        st.markdown("### 🚀 Powered by GlobalInternet.py")
        st.write("We promote your online business with the best-fit video content.")
        st.write("📞 **Phone:** (509)-47385663")
        st.write("📧 **Email:** deslandes78@gmail.com")
        st.write("🌐 **Web:** [GlobalInternet.py](https://globalinternetsitepy-abh7v6tnmskxxnuplrdcgk.streamlit.app/)")

# 5. Video Player with Persistent Playback (iframe component)
video_html = f"""
<!DOCTYPE html>
<html>
<head>
    <style>
        body {{ margin: 0; padding: 0; overflow: hidden; background-color: black; }}
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
            object-fit: cover;   /* Full screen – fills the entire viewport */
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
            pointer-events: none;
        }}
        .website-name {{
            color: white !important;
            font-family: 'Arial Black', sans-serif;
            font-size: 3.5rem;
            text-shadow: 4px 4px 15px rgba(0,0,0,1);
            margin: 0;
        }}
    </style>
</head>
<body>
    <div class="top-overlay">
        <h1 class="website-name">NIC Honestly Crafted Ice Creams</h1>
    </div>
    <div class="video-container">
        <video id="vidPlayer" autoplay muted playsinline>
            <source id="vidSource" src="{video_1}" type="video/mp4">
        </video>
    </div>
    <script>
        var player = document.getElementById('vidPlayer');
        var source = document.getElementById('vidSource');
        var secondVideo = "{video_2}";
        var playedSecond = false;

        player.onended = function() {{
            if (!playedSecond) {{
                playedSecond = true;
                source.src = secondVideo;
                player.load();
                player.play();
            }}
        }};
    </script>
</body>
</html>
"""

st.components.v1.html(video_html, height=800, scrolling=False)
