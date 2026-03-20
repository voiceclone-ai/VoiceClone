import streamlit as st
import requests

st.title("🎤 AI Voice Clone")
colab_url = st.sidebar.text_input("Colab Link")
uploaded_file = st.file_uploader("Upload Audio", type=['mp3', 'wav'])
actor = st.selectbox("Select Voice", ["Babar Azam", "Ronaldo"])

if st.button("Convert Now"):
    if uploaded_file and colab_url:
        st.info("Converting...")
        try:
            # Gradio API call using the official 'predict' endpoint
            # Gradio ke naye version ke liye direct URL
             url = f"{colab_url.strip('/')}/"
            
            # File ko byte stream mein bhejte hain
            files = {'data': uploaded_file.getvalue()}
            # Gradio expects data in a specific list format
            payload = {"data": [None, actor]} 
            
            # Simple direct connection test
            response = requests.post(url, json={"data": ["test", actor]}, timeout=30)
            
            if response.status_code == 200:
                st.success("Connection Live! AI logic incoming.")
            else:
                st.error(f"Status Code: {response.status_code}. Colab link verify karein.")
                
        except Exception as e:
            st.error(f"Error: {e}")
