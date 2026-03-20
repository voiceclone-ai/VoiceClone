import streamlit as st
import requests
import base64

# Page Config
st.set_page_config(page_title="AI Voice Clone", layout="centered")
st.title("🎤 AI Voice Converter")

# Sidebar for Link
st.sidebar.header("Settings")
colab_url = st.sidebar.text_input("Colab Link", placeholder="https://xxxx.gradio.live")

# Main Interface
uploaded_file = st.file_uploader("Upload Audio (MP3/WAV)", type=['mp3', 'wav'])
actor = st.selectbox("Select Voice", ["Babar Azam", "Ronaldo", "Narendra Modi"])

if st.button("Convert Now 🚀"):
    if not colab_url or not uploaded_file:
        st.error("Pehle Colab ka link aur audio file provide karein!")
    else:
        st.info("AI Processing... Please wait.")
        try:
            # Step 1: Link ko saaf karna
            url = colab_url.strip().rstrip('/')
            
            # Step 2: Naya API path (Auto-Fix for 404)
            api_url = f"{url}/api/predict/"
            
            # Step 3: File ko Base64 mein convert karna
            file_bytes = uploaded_file.getvalue()
            encoded_audio = base64.b64encode(file_bytes).decode()
            
            # Step 4: Data pack karna
            payload = {
                "data": [
                    {"name": "audio.mp3", "data": f"data:audio/mpeg;base64,{encoded_audio}"},
                    actor
                ]
            }
            
            # Step 5: Colab ko request bhejna
            response = requests.post(api_url, json=payload, timeout=120)
            
            if response.status_code == 200:
                st.success("✅ Connected! AI Engine is working.")
                st.balloons()
                # Yahan hum result display kar sakte hain jab model ready ho jaye
            else:
                st.error(f"❌ Error {response.status_code}: Link refresh karein ya check karein.")
                
        except Exception as e:
            st.error(f"❌ Connection Failed: {e}")

st.markdown("---")
st.caption("Mobile Optimized v3.0 | 404 Fix Included")
