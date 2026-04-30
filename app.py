import streamlit as st

# 1. Page Config – remove sidebar, expand to full width
st.set_page_config(
    page_title="NIC Honestly Crafted Ice Creams", 
    layout="wide", 
    initial_sidebar_state="collapsed"
)

# 2. Direct Video Links
video_1 = "https://raw.githubusercontent.com/Deslandes1/Nic-Honestly-Crafted-Ice-creams/main/dreamina-2026-04-29-5258-make%20the%20different%20flavor%20ice%20creams%20mov....mp4"
video_2 = "https://raw.githubusercontent.com/Deslandes1/Nic-Honestly-Crafted-Ice-creams/main/dreamina-2026-04-29-3384-his%20writing%20must%20passing%20by%20as%20a%20slidesh....mp4"

# 3. Full‑screen video player with 'contain' to show entire video (no cropping)
video_html = f"""
<!DOCTYPE html>
<html>
<head>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{ 
            margin: 0; 
            padding: 0; 
            overflow: hidden; 
            background-color: black;
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
            object-fit: contain;   /* Shows the whole video – no cropping, preserves original aspect ratio */
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

# 4. Hide Streamlit’s default chrome (header, footer, sidebar)
hide_streamlit_style = """
    <style>
        header {visibility: hidden;}
        footer {visibility: hidden;}
        .stApp {margin: 0; padding: 0;}
        [data-testid="stSidebar"] {display: none;}
        .main > div {padding: 0;}
        .block-container {padding: 0 !important; max-width: 100% !important;}
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# 5. Embed the video player
st.components.v1.html(video_html, height=800, scrolling=False)
