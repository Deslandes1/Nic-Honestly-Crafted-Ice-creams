import streamlit as st

st.set_page_config(
    page_title="NIC Honestly Crafted Ice Creams",
    layout="wide",
    initial_sidebar_state="collapsed"
)

video_1 = "https://raw.githubusercontent.com/Deslandes1/Nic-Honestly-Crafted-Ice-creams/main/dreamina-2026-04-29-5258-make%20the%20different%20flavor%20ice%20creams%20mov....mp4"
video_2 = "https://raw.githubusercontent.com/Deslandes1/Nic-Honestly-Crafted-Ice-creams/main/dreamina-2026-04-29-3384-his%20writing%20must%20passing%20by%20as%20a%20slidesh....mp4"

# Full HTML/CSS/JS page that fits any screen
html_code = f"""
<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no, viewport-fit=cover">
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{
            margin: 0;
            padding: 0;
            width: 100vw;
            height: 100vh;
            overflow: hidden;
            background: black;
        }}
        .video-container {{
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: black;
        }}
        video {{
            width: 100%;
            height: 100%;
            object-fit: cover;   /* first video fills screen */
        }}
        .second-video-style {{
            object-fit: cover !important;
            object-position: 50% 85% !important;   /* crop to show table */
        }}
        .marquee {{
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            padding: 15px 0;
            background: linear-gradient(to bottom, rgba(0,0,0,0.7) 0%, rgba(0,0,0,0) 100%);
            color: white;
            font-family: 'Arial', sans-serif;
            font-size: clamp(1rem, 4vw, 1.6rem);
            font-weight: bold;
            white-space: nowrap;
            overflow: hidden;
            z-index: 9999;
            pointer-events: none;
        }}
        .marquee span {{
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
    <div class="marquee">
        <span>Celebrate big with NIC Ice Creams – contact us for special offers for bulk or party orders today! &nbsp;&nbsp;&nbsp; Celebrate big with NIC Ice Creams – contact us for special offers for bulk or party orders today! &nbsp;&nbsp;&nbsp;</span>
    </div>
    <div class="video-container">
        <video id="player" autoplay muted playsinline>
            <source src="{video_1}" type="video/mp4">
        </video>
    </div>
    <script>
        var player = document.getElementById('player');
        var secondVideo = "{video_2}";
        var playedSecond = false;
        var timeout;

        function switchToSecond() {{
            if (!playedSecond) {{
                playedSecond = true;
                clearTimeout(timeout);
                player.src = secondVideo;
                player.classList.add('second-video-style');
                player.load();
                player.play();
                // Stop after second video ends
                player.onended = function() {{ }};
            }}
        }}

        // Switch after 5 seconds
        timeout = setTimeout(switchToSecond, 5000);

        // If first video ends before 5 seconds, switch anyway
        player.onended = function() {{
            if (!playedSecond) {{
                switchToSecond();
            }}
        }};
    </script>
</body>
</html>
"""

# Kill Streamlit's default UI and force fullscreen
st.markdown(
    """
    <style>
        header, footer, .stApp, .main, .block-container {
            visibility: hidden;
            margin: 0 !important;
            padding: 0 !important;
            height: 100%;
        }
        .stApp {
            background: black;
            margin: 0;
            padding: 0;
        }
        [data-testid="stSidebar"] { display: none; }
        .main > div {
            padding: 0 !important;
            max-width: 100% !important;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Inject the HTML directly (no iframe)
st.markdown(html_code, unsafe_allow_html=True)
