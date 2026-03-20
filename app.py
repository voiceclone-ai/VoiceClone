import streamlit as st
import requests

st.set_page_config(page_title="AI Voice Clone", layout="centered")
st.title("🎤 AI Voice Converter")

# Sidebar
st.sidebar.header("Settings")
colab_url = st.sidebar.text_input("Colab Link", placeholder="https://xxxx.gradio.live")

# Main Interface
uploaded_file = st.file_uploader("Upload Audio", type=['mp3', 'wav'])
actor = st.selectbox("Select Voice", ["Babar Azam", "Ronaldo", "Narendra Modi"])

if st.button("Start Magic Conversion 🚀"):
    if not colab_url or not uploaded_file:
        st.error("Pehle link aur file dono provide karein!")
    else:
        st.info("Connecting to Colab...")
        try:
            # URL aur API setup
            base_url = colab_url.strip().strip('/')
            api_url = f"{base_url}/api/predict"
            
            # File sending logic
            file_content = uploaded_file.getvalue()
            
            # Request sending to Colab
            response = requests.post(
                api_url, 
                json={
                    "data": [
                        {"name": "audio.mp3", "data": "data:audio/mpeg;base64,"}, 
                        actor
                    ]
                },
                timeout=120
            )

            if response.status_code == 200:
                st.success("✅ Connected! AI Engine is working.")
                st.balloons()
            else:
                st.error(f"❌ Error: {response.status_code}. Link check karein.")
        except Exception as e:
            st.error(f"❌ Connection Failed: {e}")

st.markdown("---")
st.caption("Mobile Friendly Version 2.0")
