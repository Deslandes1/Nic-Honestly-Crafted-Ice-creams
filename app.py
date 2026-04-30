import streamlit as st

# 1. Page Config – no sidebar, full width
st.set_page_config(
    page_title="NIC Honestly Crafted Ice Creams", 
    layout="wide", 
    initial_sidebar_state="collapsed"
)

# 2. Direct Video Links
video_1 = "https://raw.githubusercontent.com/Deslandes1/Nic-Honestly-Crafted-Ice-creams/main/dreamina-2026-04-29-5258-make%20the%20different%20flavor%20ice%20creams%20mov....mp4"
video_2 = "https://raw.githubusercontent.com/Deslandes1/Nic-Honestly-Crafted-Ice-creams/main/dreamina-2026-04-29-3384-his%20writing%20must%20passing%20by%20as%20a%20slidesh....mp4"

# 3. Full‑screen video player with moving text and second video cropped to show the table
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
            object-fit: contain;   /* First video shows full frame */
        }}
        /* For second video: cover full screen, show only bottom part (table) */
        .show-table {{
            object-fit: cover !important;
            object-position: 50% 85% !important;  /* Shows bottom 15% where table is */
        }}
        .top-overlay {{
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            padding: 20px 0;
            z-index: 9999;
            background: linear-gradient(to bottom, rgba(0,0,0,0.7) 0%, rgba(0,0,0,0) 100%);
            pointer-events: none;
            white-space: nowrap;
            overflow: hidden;
        }}
        .simple-marquee {{
            font-family: 'Arial', sans-serif;
            font-size: 1.8rem;
            font-weight: bold;
            color: white;
            text-shadow: 2px 2px 8px black;
            white-space: nowrap;
            display: inline-block;
            padding-left: 100%;
            animation: scroll 20s linear infinite;
        }}
        @keyframes scroll {{
            0% {{ transform: translateX(0); }}
            100% {{ transform: translateX(-100%); }}
        }}
    </style>
</head>
<body>
    <div class="top-overlay">
        <div style="overflow: hidden; white-space: nowrap;">
            <div class="simple-marquee">
                Celebrate big with NIC Ice Creams – contact us for special offers for bulk or party orders today! &nbsp;&nbsp;&nbsp;
                Celebrate big with NIC Ice Creams – contact us for special offers for bulk or party orders today! &nbsp;&nbsp;&nbsp;
            </div>
        </div>
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
                player.classList.add('show-table');
                player.load();
                player.play();
            }}
        }};
    </script>
</body>
</html>
"""

# 4. Hide Streamlit’s default UI
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
