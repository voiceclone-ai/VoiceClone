import streamlit as st
import requests
import base64

st.set_page_config(page_title="AI Voice Clone", layout="centered")
st.title("🎤 AI Voice Converter")

# Sidebar
st.sidebar.header("Setup")
colab_url = st.sidebar.text_input("Colab Link", placeholder="https://xxxx.gradio.live")

# File Upload
uploaded_file = st.file_uploader("Upload Audio", type=['mp3', 'wav'])
actor = st.selectbox("Select Voice", ["Babar Azam", "Ronaldo", "Modi"])

if st.button("Start Magic Conversion 🚀"):
    if not colab_url or not uploaded_file:
        st.error("Pehle link aur file check karein!")
    else:
        st.info("Connecting to AI Engine...")
        try:
            url = colab_url.strip().rstrip('/')
            
            # File conversion
            file_bytes = uploaded_file.getvalue()
            encoded_audio = base64.b64encode(file_bytes).decode()
            
            # Gradio v4+ format
            payload = {
                "data": [
                    {"name": "audio.mp3", "data": f"data:audio/mpeg;base64,{encoded_audio}"}, 
                    actor
                ]
            }
            
            # Endpoint try
            api_url = f"{url}/api/predict"
            response = requests.post(api_url, json=payload, timeout=60)
            
            if response.status_code == 200:
                st.success("✅ Connection Successful! AI is processing.")
                # Agar output audio dikhani ho:
                res_data = response.json()
                if "data" in res_data:
                    st.audio(f"{url}/file={res_data['data'][0]['name']}")
            else:
                st.error(f"❌ Server Error: {response.status_code}. Link check karein.")
        except Exception as e:
            st.error(f"❌ Failed to reach Colab: {e}")
