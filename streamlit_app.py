import streamlit as st

# Configure page settings
st.set_page_config(
    page_title="Xavi Ch Social Links",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Custom CSS for a clean, aesthetic design
st.markdown("""
    <style>
    /* Main background and text colors */
    .stApp {
        background-color: #000000;
    }
    h1, h2 {
            color: white !important;
        }
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Title styling */
    .title {
        color: #FFFFFF;
        text-align: center;
        font-family: 'Arial', sans-serif;
        font-size: 2.5em;
        margin-bottom: 10px;
        font-weight: bold;
    }
    
    .subtitle {
        color: #FFFFFF;
        text-align: center;
        font-family: 'Arial', sans-serif;
        font-size: 1.5em;
        margin-bottom: 30px;
        opacity: 0.8;
    }
    
    /* Social links styling */
    .social-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        height: 100vh;
        gap: 20px;
    }
    
    .social-link {
        width: 200px;
        padding: 15px 30px;
        font-size: 18px;
        text-align: center;
        color: #FFFFFF !important;
        text-decoration: none;
        border: 2px solid #FFFFFF;
        border-radius: 50px;
        transition: all 0.3s ease;
        background: linear-gradient(45deg, rgba(255,255,255,0.1), rgba(255,255,255,0.05));
        backdrop-filter: blur(5px);
        -webkit-backdrop-filter: blur(5px);
    }
    
    .social-link:hover {
        transform: translateY(-3px);
        box-shadow: 0 7px 20px rgba(255,255,255,0.2);
        background: linear-gradient(45deg, rgba(255,255,255,0.2), rgba(255,255,255,0.1));
    }
    
    .youtube {
        border-color: #FF0000;
    }
    
    .youtube:hover {
        background: linear-gradient(45deg, rgba(255,0,0,0.2), rgba(255,0,0,0.1));
        box-shadow: 0 7px 20px rgba(255,0,0,0.2);
    }
    
    .discord {
        border-color: #5865F2;
    }
    
    .discord:hover {
        background: linear-gradient(45deg, rgba(88,101,242,0.2), rgba(88,101,242,0.1));
        box-shadow: 0 7px 20px rgba(88,101,242,0.2);
    }
    </style>
""", unsafe_allow_html=True)

# Title and Social Media Links
st.markdown("""
<div class="social-container">
    <h1 class="title">Xavi Ch</h1>
    <h2 class="subtitle">Social Media</h2>
    <a href="https://www.youtube.com/@i6od" target="_blank" class="social-link youtube">YouTube</a>
    <a href="https://discord.gg/UBpHbWfTcy" target="_blank" class="social-link discord">Discord</a>
</div>
""", unsafe_allow_html=True)