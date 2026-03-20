import streamlit as st
import requests
import base64

# Website Title & Style
st.set_page_config(page_title="Free Voice Clone", page_icon="🦜")
st.markdown("<h1 style='text-align: center; color: #52D017;'>🦜 Free Voice Clone</h1>", unsafe_allow_html=True)

# Sidebar for Colab Link
colab_url = st.sidebar.text_input("Enter Google Colab API Link", placeholder="https://xxxx.gradio.live")
st.sidebar.info("Colab on karein aur uska link yahan dalein.")

# Main UI
uploaded_file = st.file_uploader("Upload Song (MP3/WAV)", type=['mp3', 'wav'])
actor = st.selectbox("Select Actor", ["Babar Azam", "Narendra Modi", "Cristiano Ronaldo"])

if st.button("Start Magic Conversion 🚀"):
    if uploaded_file and colab_url:
        st.info("AI Processing... Please wait 1-2 minutes.")
        
        # Audio ko base64 mein convert karna taake error na aaye
        file_bytes = uploaded_file.read()
        encoded_audio = base64.b64encode(file_bytes).decode()
        
        # Gradio API Payload
        payload = {
            "data": [
                {"name": "audio.mp3", "data": f"data:audio/mpeg;base64,{encoded_audio}"},
                actor
            ]
        }
        
        try:
            # Colab se raabta
            response = requests.post(f"{colab_url}/api/predict", json=payload, timeout=600)
            if response.status_code == 200:
                # Output file ka link nikalna
                result = response.json()['data'][0]
                audio_url = f"{colab_url}/file={result['name']}"
                st.audio(audio_url)
                st.success("✅ Conversion Done!")
            else:
                st.error("⚠️ Colab side error. Check your Colab script.")
        except Exception as e:
            st.error(f"❌ Connection Failed: {e}")
    else:
        st.error("Please upload file and enter Colab link!")
