import streamlit as st

st.set_page_config(
    page_title="NIC Honestly Crafted Ice Creams",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ========== RAW MEDIA LINKS ==========
video_1 = "https://raw.githubusercontent.com/Deslandes1/Nic-Honestly-Crafted-Ice-creams/main/dreamina-2026-04-29-5258-make%20the%20different%20flavor%20ice%20creams%20mov....mp4"
video_2 = "https://raw.githubusercontent.com/Deslandes1/Nic-Honestly-Crafted-Ice-creams/main/dreamina-2026-04-29-3384-his%20writing%20must%20passing%20by%20as%20a%20slidesh....mp4"
image_3 = "https://raw.githubusercontent.com/Deslandes1/Nic-Honestly-Crafted-Ice-creams/main/NIC%205.png"
video_4 = "https://raw.githubusercontent.com/Deslandes1/Nic-Honestly-Crafted-Ice-creams/main/NIC6a.mp4"

# ========== HTML/JS PLAYER (no components.html) ==========
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
        .video-container, .image-container {{
            position: fixed;
            top: 0;
            left: 0;
            width: 100vw;
            height: 100vh;
            z-index: 1;
            background: black;
        }}
        video, img {{
            width: 100%;
            height: 100%;
            object-fit: cover;
        }}
        .show-table {{
            object-fit: cover !important;
            object-position: 50% 85% !important;
        }}
        .top-overlay {{
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            padding: 20px 0;
            z-index: 9999;
            background: linear-gradient(to bottom, rgba(0,0,0,0.7), rgba(0,0,0,0));
            pointer-events: none;
            white-space: nowrap;
            overflow: hidden;
        }}
        .simple-marquee {{
            font-family: 'Arial', sans-serif;
            font-size: clamp(1rem, 5vw, 1.8rem);
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

    <!-- Video 1 -->
    <div id="video1Container" class="video-container">
        <video id="player1" autoplay muted playsinline>
            <source src="{video_1}" type="video/mp4">
        </video>
    </div>

    <!-- Video 2 (cropped) -->
    <div id="video2Container" class="video-container" style="display: none;">
        <video id="player2" muted playsinline>
            <source src="{video_2}" type="video/mp4">
        </video>
    </div>

    <!-- Image 3 (static) -->
    <div id="imageContainer" class="image-container" style="display: none;">
        <img id="staticImage" src="{image_3}" alt="NIC Ice Creams">
    </div>

    <!-- Video 4 (final) -->
    <div id="video4Container" class="video-container" style="display: none;">
        <video id="player4" muted playsinline>
            <source src="{video_4}" type="video/mp4">
        </video>
    </div>

    <script>
        var player1 = document.getElementById('player1');
        var player2 = document.getElementById('player2');
        var player4 = document.getElementById('player4');
        var container1 = document.getElementById('video1Container');
        var container2 = document.getElementById('video2Container');
        var imageContainer = document.getElementById('imageContainer');
        var container4 = document.getElementById('video4Container');
        var timeout, imageTimeout;

        function switchToSecond() {{
            clearTimeout(timeout);
            if (container1.style.display !== 'none') {{
                container1.style.display = 'none';
                player1.pause();
                container2.style.display = 'block';
                player2.play();
                player2.classList.add('show-table');
            }}
        }}

        player2.onended = function() {{
            container2.style.display = 'none';
            player2.pause();
            imageContainer.style.display = 'block';
        }};

        function showFinalVideo() {{
            imageContainer.style.display = 'none';
            container4.style.display = 'block';
            player4.play();
            player4.onended = function() {{ }};
        }}

        var observer = new MutationObserver(function(mutations) {{
            mutations.forEach(function(mutation) {{
                if (mutation.type === 'attributes' && mutation.attributeName === 'style') {{
                    if (imageContainer.style.display === 'block') {{
                        if (imageTimeout) clearTimeout(imageTimeout);
                        imageTimeout = setTimeout(showFinalVideo, 5000);
                    }}
                }}
            }});
        }});
        observer.observe(imageContainer, {{ attributes: true }});

        timeout = setTimeout(switchToSecond, 5000);
        player1.onended = switchToSecond;
    </script>
</body>
</html>
"""

# Hide Streamlit UI and inject full‑screen HTML
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

# ✅ Use st.markdown directly – no st.components.v1.html, no deprecation warning
st.markdown(html_code, unsafe_allow_html=True)
