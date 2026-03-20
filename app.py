import streamlit as st
import requests
import base64

# Page Settings
st.set_page_config(page_title="AI Voice Converter", layout="centered")
st.title("🎤 AI Voice Converter")

# Sidebar
st.sidebar.header("Settings")
colab_url = st.sidebar.text_input("Colab Link", placeholder="https://xxxx.gradio.live")

# Main Interface
uploaded_file = st.file_uploader("Upload Audio (MP3/WAV)", type=['mp3', 'wav'])
actor = st.selectbox("Select Voice", ["Babar Azam", "Ronaldo", "Narendra Modi"])

if st.button("Start Magic Conversion 🚀"):
    if not colab_url or not uploaded_file:
        st.error("Pehle link aur file provide karein!")
    else:
        st.info("Connecting to AI Engine... Please wait.")
        try:
            # Step 1: Link Cleanup
            url = colab_url.strip().rstrip('/')
            
            # Step 2: Audio to Base64
            file_bytes = uploaded_file.getvalue()
            encoded_audio = base64.b64encode(file_bytes).decode()
            
            # Step 3: Try both Gradio Endpoints (404 Fix)
            endpoints = [f"{url}/run/predict", f"{url}/api/predict/"]
            success = False
            
            for api_url in endpoints:
                payload = {"data": [f"data:audio/mpeg;base64,{encoded_audio}", actor]}
                try:
                    response = requests.post(api_url, json=payload, timeout=60)
                    if response.status_code == 200:
                        st.success("✅ Connection Successful!")
                        st.balloons()
                        success = True
                        break
                except:
                    continue
            
            if not success:
                st.error("❌ Connection Failed. Check if Colab is running and link is correct.")
                
        except Exception as e:
            st.error(f"❌ Error: {e}")

st.markdown("---")
st.caption("Version 4.0 | Auto-Endpoint Finder Active")
