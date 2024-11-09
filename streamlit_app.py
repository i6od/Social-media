import streamlit as st
from datetime import datetime, time

# Configure page settings
st.set_page_config(
    page_title="Stream Schedule",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Custom CSS for compact black and white modern UI
st.markdown("""
    <style>
    /* Main background and text colors */
    .stApp {
        background-color: #000000;
        color: #FFFFFF;
    }
    
    /* Headings */
    h1 {
        color: #FFFFFF !important;
        font-family: 'Arial', sans-serif;
        font-size: 24px !important;
        margin-bottom: 10px !important;
    }
    
    h2, h3 {
        color: #FFFFFF !important;
        font-family: 'Arial', sans-serif;
        font-size: 18px !important;
        margin-bottom: 8px !important;
    }
    
    /* Regular text */
    p, .stMarkdown {
        font-size: 14px !important;
        line-height: 1.4 !important;
        margin: 5px 0 !important;
    }
    
    /* Links */
    a {
        color: #FFFFFF !important;
        text-decoration: none;
        background-color: #333333;
        padding: 6px 12px;
        border-radius: 4px;
        transition: background-color 0.3s;
        display: inline-block;
        margin: 3px;
        font-size: 12px;
    }
    
    a:hover {
        background-color: #444444;
    }
    
    /* Schedule container */
    .container {
        background-color: #1A1A1A;
        padding: 12px;
        border-radius: 6px;
        margin: 10px 0;
    }
    
    /* Custom container for social links */
    .social-links {
        display: flex;
        flex-wrap: wrap;
        gap: 6px;
        padding: 12px;
        background-color: #1A1A1A;
        border-radius: 6px;
        margin: 10px 0;
    }

    /* Make containers narrower */
    .block-container {
        max-width: 600px;
        padding: 1rem 1rem 1rem !important;
    }

    /* Reduce padding in all sections */
    .stMarkdown, div.row-widget {
        padding-top: 0.5rem !important;
        padding-bottom: 0.5rem !important;
    }
    </style>
""", unsafe_allow_html=True)

# Header


# Schedule section
st.markdown("""
<div class="container">
    <h2>📅 Stream Schedule</h2>
    <p>Live stream times:</p>
    <p>Sunday 7:00 PM - Thursday 7:00 PM</p>
""", unsafe_allow_html=True)

# Current status
current_time = datetime.now().time()
current_day = datetime.now().strftime('%A')
stream_start = time(19, 0)  # 7 PM
stream_end = time(19, 0)    # 7 PM

status_text = ""
if current_day in ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday']:
    if current_day == 'Thursday' and current_time > stream_end:
        status_text = "📴 Offline"
    elif current_day == 'Sunday' and current_time < stream_start:
        status_text = "📴 Offline"
    else:
        status_text = "🔴 Live!"
else:
    status_text = "📴 Offline"

st.markdown(f"""
    <p>{status_text}</p>
</div>
""", unsafe_allow_html=True)

# Moderator Application
st.header("🎯 Mod Application")
st.markdown("""
<div class="container">
    <p>Want to be a moderator?</p>
    <a href="https://forms.gle/ZrjDjRPJRB5uyYAC6" target="_blank">Apply Now</a>
</div>
""", unsafe_allow_html=True)

# Social Media Links
st.header("🌐 Social Media")
st.markdown("""
<div class="social-links">
    <a href="https://www.youtube.com/@i6od" target="_blank">YouTube</a>
    <a href="https://www.instagram.com/i6od/" target="_blank">Instagram</a>
    <a href="https://www.tiktok.com/@xuhsy" target="_blank">TikTok</a>
</div>
""", unsafe_allow_html=True)

# Footer
st.markdown("""
<div style="text-align: center; margin-top: 20px; padding: 10px;">
    <p>Thanks for visiting! 👋</p>
</div>
""", unsafe_allow_html=True)
