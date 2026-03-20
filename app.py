import streamlit as st
import requests

st.set_page_config(page_title="AI Voice Clone", page_icon="🎤")
st.title("🎤 AI Voice Converter")

colab_url = st.sidebar.text_input("Colab Link", placeholder="https://xxxx.gradio.live")

uploaded_file = st.file_uploader("Upload Audio (Max 10MB)", type=['mp3', 'wav'])
actor = st.selectbox("Select Voice", ["Babar Azam", "Ronaldo", "Modi"])

if st.button("Start Magic Conversion 🚀"):
    if uploaded_file and colab_url:
        st.info("Uploading & Processing... Please wait.")
        
        try:
            # File ko sahi format mein pack karna
            files = {'data': (uploaded_file.name, uploaded_file.getvalue(), 'audio/mpeg')}
            
            # Colab ko request bhejna
            response = requests.post(f"{colab_url}/api/predict", files=files, data={"data": actor}, timeout=300)
            
            if response.status_code == 200:
                st.success("Conversion Successful!")
                # Resulting audio link
                audio_data = response.json()['data'][0]
                st.audio(f"{colab_url}/file={audio_data['name']}")
            else:
                st.error("Colab busy hai ya file bohot bari hai.")
        except Exception as e:
            st.error(f"Connection Error: {e}")
    else:
        st.warning("Link aur File dono zaroori hain!")
