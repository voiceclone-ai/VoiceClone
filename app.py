import streamlit as st
import requests
import base64

st.title("🎤 AI Voice Clone")

colab_url = st.sidebar.text_input("Colab Link")
uploaded_file = st.file_uploader("Upload Audio", type=['mp3', 'wav'])
actor = st.selectbox("Select Voice", ["Babar Azam", "Ronaldo"])

if st.button("Convert Now"):
    if uploaded_file and colab_url:
        st.info("Processing...")
        try:
            # Link ko bilkul saaf karna
            url = colab_url.strip().rstrip('/')
            
            # Agar 404 aaye toh ye doosra rasta try karega
            api_url = f"{url}/run/predict" # Naye Gradio versions ke liye
            
            file_bytes = uploaded_file.getvalue()
            encoded = base64.b64encode(file_bytes).decode()
            
            payload = {
                "data": [
                    f"data:audio/mpeg;base64,{encoded}",
                    actor
                ]
            }
            
            # Request bhej rahe hain
            response = requests.post(api_url, json=payload, timeout=60)
            
            # Agar /run/predict fail ho toh purana /api/predict try karein
            if response.status_code != 200:
                api_url = f"{url}/api/predict"
                response = requests.post(api_url, json=payload, timeout=60)

            if response.status_code == 200:
                st.success("✅ Connected! AI Engine is responding.")
            else:
                st.error(f"Error {response.status_code}: Link refresh karein.")
                
        except Exception as e:
            st.error(f"Connection Error: {e}")
