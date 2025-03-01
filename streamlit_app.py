import streamlit as st

# Configure page settings
st.set_page_config(
    page_title="Xavi Ch Social Links",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Enhanced CSS with brighter colors and more dynamic elements
st.markdown("""
    <style>
    /* Main background with gradient */
    .stApp {
        background: linear-gradient(135deg, #121212 0%, #2d2d2d 100%);
    }
    
    /* Text styling */
    h1, h2 {
        color: white !important;
    }
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Title styling with glow effect */
    .title {
        color: #FFFFFF;
        text-align: center;
        font-family: 'Arial', sans-serif;
        font-size: 3.5em;
        margin-bottom: 10px;
        font-weight: bold;
        text-shadow: 0 0 10px rgba(255,255,255,0.7);
        letter-spacing: 2px;
    }
    
    .subtitle {
        color: #FFFFFF;
        text-align: center;
        font-family: 'Arial', sans-serif;
        font-size: 1.8em;
        margin-bottom: 10px;
        opacity: 0.9;
        font-weight: 300;
        letter-spacing: 1px;
    }
    
    /* Bio text styling */
    .bio {
        color: #FFFFFF;
        text-align: center;
        font-family: 'Arial', sans-serif;
        font-size: 1.2em;
        margin-bottom: 10px;
        line-height: 1.6;
    }
    
    .contact-info {
        color: #FFFFFF;
        text-align: center;
        font-family: 'Arial', sans-serif;
        font-size: 1.1em;
        margin-bottom: 40px;
        opacity: 0.9;
    }
    
    .highlight {
        color: #29ABE0;
        font-weight: bold;
    }
    
    /* Social links container with animation */
    .social-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        min-height: 100vh;
        gap: 25px;
        padding: 20px;
        animation: fadeIn 1.5s ease-in-out;
    }
    
    @keyframes fadeIn {
        0% { opacity: 0; transform: translateY(20px); }
        100% { opacity: 1; transform: translateY(0); }
    }
    
    /* Social link styling with enhanced hover effects */
    .social-link {
        width: 250px;
        padding: 16px 30px;
        font-size: 20px;
        font-weight: 600;
        text-align: center;
        color: #FFFFFF !important;
        text-decoration: none;
        border: 3px solid #FFFFFF;
        border-radius: 50px;
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        background: rgba(255,255,255,0.08);
        backdrop-filter: blur(8px);
        -webkit-backdrop-filter: blur(8px);
        position: relative;
        overflow: hidden;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    }
    
    .social-link:before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 0;
        height: 100%;
        background: rgba(255,255,255,0.1);
        transition: all 0.4s ease;
        z-index: -1;
    }
    
    .social-link:hover:before {
        width: 100%;
    }
    
    .social-link:hover {
        transform: translateY(-5px) scale(1.03);
        box-shadow: 0 10px 25px rgba(255,255,255,0.2);
        letter-spacing: 1px;
    }
    
    /* YouTube styling with brighter colors */
    .youtube {
        border-color: #FF0000;
        background: linear-gradient(45deg, rgba(255,0,0,0.1), rgba(255,0,0,0.05));
        box-shadow: 0 4px 15px rgba(255,0,0,0.3);
    }
    
    .youtube:hover {
        background: linear-gradient(45deg, rgba(255,0,0,0.3), rgba(255,0,0,0.15));
        box-shadow: 0 10px 25px rgba(255,0,0,0.4);
        text-shadow: 0 0 5px rgba(255,0,0,0.5);
    }
    
    /* Discord styling with brighter colors */
    .discord {
        border-color: #5865F2;
        background: linear-gradient(45deg, rgba(88,101,242,0.1), rgba(88,101,242,0.05));
        box-shadow: 0 4px 15px rgba(88,101,242,0.3);
    }
    
    .discord:hover {
        background: linear-gradient(45deg, rgba(88,101,242,0.3), rgba(88,101,242,0.15));
        box-shadow: 0 10px 25px rgba(88,101,242,0.4);
        text-shadow: 0 0 5px rgba(88,101,242,0.5);
    }
    
    /* Ko-fi styling */
    .kofi {
        border-color: #29ABE0;
        background: linear-gradient(45deg, rgba(41,171,224,0.1), rgba(41,171,224,0.05));
        box-shadow: 0 4px 15px rgba(41,171,224,0.3);
    }
    
    .kofi:hover {
        background: linear-gradient(45deg, rgba(41,171,224,0.3), rgba(41,171,224,0.15));
        box-shadow: 0 10px 25px rgba(41,171,224,0.4);
        text-shadow: 0 0 5px rgba(41,171,224,0.5);
    }
    
    /* Roblox styling */
    .roblox {
        border-color: #FF6B57;
        background: linear-gradient(45deg, rgba(255,107,87,0.1), rgba(255,107,87,0.05));
        box-shadow: 0 4px 15px rgba(255,107,87,0.3);
    }
    
    .roblox:hover {
        background: linear-gradient(45deg, rgba(255,107,87,0.3), rgba(255,107,87,0.15));
        box-shadow: 0 10px 25px rgba(255,107,87,0.4);
        text-shadow: 0 0 5px rgba(255,107,87,0.5);
    }
    
    /* Premium message styling */
    .premium-message {
        margin-top: 30px;
        padding: 15px 20px;
        background: linear-gradient(45deg, rgba(255,215,0,0.1), rgba(255,215,0,0.05));
        border: 2px solid #FFD700;
        border-radius: 10px;
        color: #FFFFFF;
        text-align: center;
        font-size: 16px;
        max-width: 400px;
        backdrop-filter: blur(5px);
        -webkit-backdrop-filter: blur(5px);
        animation: glow 2s infinite alternate;
        box-shadow: 0 5px 15px rgba(255,215,0,0.2);
    }
    
    @keyframes glow {
        0% { box-shadow: 0 0 5px rgba(255,215,0,0.3); }
        100% { box-shadow: 0 0 15px rgba(255,215,0,0.5); }
    }
    
    /* Responsive adjustments */
    @media (max-width: 768px) {
        .title {
            font-size: 2.8em;
        }
        .subtitle {
            font-size: 1.5em;
        }
        .bio {
            font-size: 1.1em;
        }
        .contact-info {
            font-size: 1em;
        }
        .social-link {
            width: 220px;
        }
        .premium-message {
            max-width: 320px;
            font-size: 14px;
        }
    }
    
    /* Adding a subtle animated background pattern */
    .bg-pattern {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: radial-gradient(circle at 15% 50%, rgba(255,255,255,0.03) 0%, transparent 25%),
                   radial-gradient(circle at 85% 30%, rgba(255,255,255,0.03) 0%, transparent 25%);
        z-index: -2;
        animation: patternMove 20s infinite alternate ease-in-out;
    }
    
    @keyframes patternMove {
        0% { background-position: 0% 0%; }
        100% { background-position: 100% 100%; }
    }
    </style>
""", unsafe_allow_html=True)

# Title and Social Media Links with animated background pattern
st.markdown("""
<div class="bg-pattern"></div>
<div class="social-container">
    <h1 class="title">Xavi Ch</h1>
    <div class="bio">God First.</div>
    <div class="contact-info">Media/Sponsorship Inquiries <span class="highlight">✅</span> xavivt.media@gmail.com</div>
    <h2 class="subtitle">Connect With Me</h2>
    <a href="https://www.youtube.com/@i6od" target="_blank" class="social-link youtube">YouTube</a>
    <a href="https://discord.gg/UBpHbWfTcy" target="_blank" class="social-link discord">Discord</a>
    <a href="https://ko-fi.com/xavierr" target="_blank" class="social-link kofi">Support on Ko-fi</a>
    <a href="https://www.roblox.com/users/271617839/profile" target="_blank" class="social-link roblox">Roblox</a>
    <div class="premium-message">
        All premium subscriptions should be able to cross platform and integrate into TikTok and Discord.
    </div>
</div>
""", unsafe_allow_html=True)
