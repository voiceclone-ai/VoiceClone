import streamlit as st
import requests

# 1. Website ki Look aur Theme (Parrot Green & White)
st.set_page_config(page_title="Free Voice Clone", page_icon="🦜", layout="centered")

st.markdown("""
    <style>
    /* Background and Text Colors */
    .stApp { background-color: #FFFFFF; }
    h1 { color: #52D017 !important; text-align: center; font-family: 'Arial'; font-weight: 800; }
    p { color: #2C3E50; text-align: center; font-size: 18px; }
    
    /* Input Box Styling */
    .stFileUploader section { border: 2px dashed #7CFC00 !important; border-radius: 20px; }
    
    /* Button Styling */
    div.stButton > button {
        background-color: #7CFC00;
        color: black;
        border: 2px solid #52D017;
        border-radius: 25px;
        height: 3.5em;
        width: 100%;
        font-weight: bold;
        font-size: 20px;
        transition: 0.3s;
    }
    div.stButton > button:hover {
        background-color: #52D017;
        color: white;
        border: 2px solid #7CFC00;
        transform: scale(1.02);
    }
    </style>
    """, unsafe_allow_html=True)

# 2. Header Section
st.markdown("<h1>🦜 Free Voice Clone</h1>", unsafe_allow_html=True)
st.markdown("<p>Clone any song into your favorite actor's voice instantly!</p>", unsafe_allow_html=True)

# 3. API Connection (Google Colab Link)
st.sidebar.header("⚙️ Settings")
colab_url = st.sidebar.text_input("Enter Google Colab API Link", placeholder="https://xxxx.gradio.live")
st.sidebar.info("Pehle Google Colab on karein, phir uska link yahan paste karein.")

# 4. Main Features Area
st.subheader("Step 1: Upload your Song")
uploaded_file = st.file_uploader("Choose an MP3 or WAV file", type=['mp3', 'wav'])

st.subheader("Step 2: Select Actor Voice")
actors = ["Babar Azam", "Narendra Modi", "Cristiano Ronaldo", "Upload My Own Model"]
selected_actor = st.selectbox("Choose who should sing:", actors)

if selected_actor == "Upload My Own Model":
    custom_model = st.file_uploader("Upload .pth file", type=['pth'])

# 5. Conversion Logic
if st.button("Start Magic Conversion 🚀"):
    if not uploaded_file:
        st.error("❌ Please upload a song first!")
    elif not colab_url:
        st.error("❌ Please provide the Google Colab Link from the sidebar!")
    else:
        with st.spinner("⏳ Processing... (Vocal Separation + Voice Cloning)"):
            try:
                # Sending file to your Google Colab Backend
                files = {"file": uploaded_file.getvalue()}
                data = {"actor": selected_actor}
                
                # Note: Colab must be running a FastAPI or Gradio server to receive this
                response = requests.post(f"{colab_url}/process", files=files, data=data, timeout=300)
                
                if response.status_code == 200:
                    st.success("✅ Conversion Complete!")
                    st.audio(response.content)
                    st.download_button("Download Song", data=response.content, file_name="cloned_song.mp3")
                else:
                    st.error("⚠️ Colab is not responding correctly. Check your Colab script.")
            except Exception as e:
                st.error(f"❌ Connection Error: Make sure your Colab link is active.")

# 6. Footer
st.markdown("---")
st.caption("Developed for Mobile | 100% Free | No Login Required")
