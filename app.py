import streamlit as st
import requests
import base64

st.set_page_config(page_title="AI Voice Clone", layout="centered")
st.title("🎤 AI Voice Converter")

colab_url = st.sidebar.text_input("Colab Link")
uploaded_file = st.file_uploader("Upload Audio", type=['mp3', 'wav'])
actor = st.selectbox("Select Voice", ["Babar Azam", "Ronaldo"])

if st.button("Convert Now 🚀"):
    if not colab_url or not uploaded_file:
        st.error("Link aur File dono provide karein!")
    else:
        st.info("Connecting to AI Engine...")
        try:
            url = colab_url.strip().rstrip('/')
            # Naya aur asaan rasta
            api_url = f"{url}/api/predict"
            
            file_bytes = uploaded_file.getvalue()
            encoded_audio = base64.b64encode(file_bytes).decode()
            
            payload = {
                "data": [
                    {"name": "audio.mp3", "data": f"data:audio/mpeg;base64,{encoded_audio}"},
                    actor
                ]
            }
            
            response = requests.post(api_url, json=payload, timeout=120)
            
            if response.status_code == 200:
                st.success("✅ Connection Successful! AI process shuru ho gaya.")
            else:
                st.error(f"Error {response.status_code}. Link dobara copy karein.")
        except Exception as e:
            st.error(f"Connection Failed: {e}")
