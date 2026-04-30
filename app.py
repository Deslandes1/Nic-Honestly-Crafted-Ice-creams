import streamlit as st

st.set_page_config(
    page_title="NIC Honestly Crafted Ice Creams",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Direct raw video URLs (use the correct raw format)
video_1 = "https://raw.githubusercontent.com/Deslandes1/Nic-Honestly-Crafted-Ice-creams/main/dreamina-2026-04-29-5258-make%20the%20different%20flavor%20ice%20creams%20mov....mp4"
video_2 = "https://raw.githubusercontent.com/Deslandes1/Nic-Honestly-Crafted-Ice-creams/refs/heads/main/dreamina-2026-04-29-3384-his%20writing%20must%20passing%20by%20as%20a%20slidesh....mp4"

html_code = f"""
<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no, viewport-fit=cover">
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body, html {{
            width: 100%;
            height: 100%;
            overflow: hidden;
            background: black;
        }}
        .video-wrapper {{
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
            object-fit: cover;
        }}
        .second-crop {{
            object-fit: cover !important;
            object-position: 50% 85% !important;
        }}
        .marquee {{
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            padding: 12px 0;
            background: linear-gradient(to bottom, rgba(0,0,0,0.7), rgba(0,0,0,0));
            color: white;
            font-family: 'Arial', sans-serif;
            font-size: clamp(0.9rem, 4vw, 1.5rem);
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
    <div class="video-wrapper">
        <video id="myVideo" autoplay muted playsinline>
            <source src="{video_1}" type="video/mp4">
        </video>
    </div>
    <script>
        var video = document.getElementById('myVideo');
        var secondVideoSrc = "{video_2}";
        var secondPlayed = false;

        video.onended = function() {{
            if (!secondPlayed) {{
                secondPlayed = true;
                video.src = secondVideoSrc;
                video.classList.add('second-crop');
                video.load();
                video.play();
                // stop after second video ends
                video.onended = function() {{ }};
            }}
        }};
    </script>
</body>
</html>
"""

# Hide Streamlit's default UI and enforce fullscreen
st.markdown(
    """
    <style>
        header, footer, .stApp, .main, .block-container {
            visibility: hidden !important;
            margin: 0 !important;
            padding: 0 !important;
            height: 100% !important;
        }
        .stApp {
            background: black !important;
        }
        [data-testid="stSidebar"] { display: none !important; }
        .main > div {
            padding: 0 !important;
            max-width: 100% !important;
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(html_code, unsafe_allow_html=True)
