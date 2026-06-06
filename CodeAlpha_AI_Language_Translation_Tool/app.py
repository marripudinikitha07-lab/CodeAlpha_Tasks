import streamlit as st
from deep_translator import GoogleTranslator
from gtts import gTTS
import base64

# Page Settings
st.set_page_config(
    page_title="AI Language Translation Tool",
    layout="centered"
)

# Custom CSS
st.markdown("""
<style>

/* Full Background */
.stApp {
    background: linear-gradient(to right, #e8d5ff, #ffd6e7);
}

/* Remove extra top spacing */
.block-container {
    padding-top: 0rem;
}

/* Top Header Bar */
.top-header {
    background: linear-gradient(to right, #c084fc, #f9a8d4);
    padding: 18px;
    border-radius: 0px 0px 18px 18px;
    text-align: center;
    margin-bottom: 30px;
    box-shadow: 0px 3px 10px rgba(0,0,0,0.1);
}

/* Header Title */
.top-header h1 {
    color: white;
    margin: 0;
    font-size: 38px;
    font-weight: bold;
}

/* Main Box */
.main-box {
    background-color: rgba(255,255,255,0.75);
    padding: 30px;
    border-radius: 20px;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.1);
}

/* Buttons */
.stButton>button {
    background-color: #c084fc;
    color: white;
    border: none;
    border-radius: 10px;
    padding: 10px 18px;
    font-size: 16px;
}

.stButton>button:hover {
    background-color: #a855f7;
    color: white;
}

</style>
""", unsafe_allow_html=True)

# Languages
languages = {
    "English": "en",
    "Hindi": "hi",
    "Telugu": "te",
    "Tamil": "ta",
    "French": "fr",
    "German": "de",
    "Spanish": "es",
    "Japanese": "ja",
    "Korean": "ko",
    "Chinese": "zh-CN"
}

# Main Container
st.markdown('<div class="main-box">', unsafe_allow_html=True)

# Title
st.markdown("""
<div class="top-header">
    <h1>AI Language Translation Tool</h1>
</div>
""", unsafe_allow_html=True)

# Input Text
input_text = st.text_area(
    "Enter Text",
    placeholder="Type text here..."
)

# Language Selection
col1, col2 = st.columns(2)

with col1:
    source_lang = st.selectbox(
        "Source Language",
        list(languages.keys())
    )

with col2:
    target_lang = st.selectbox(
        "Target Language",
        list(languages.keys()),
        index=1
    )

# Translate Button
if st.button("Translate"):

    if input_text.strip() == "":
        st.warning("Please enter some text.")
    else:
        try:
            translated = GoogleTranslator(
                source=languages[source_lang],
                target=languages[target_lang]
            ).translate(input_text)

            # Display Translation
            st.subheader("Translated Text")
            st.success(translated)

            # COPY BUTTON FIX
            st.code(translated, language=None)

            # Text To Speech
            tts = gTTS(
                text=translated,
                lang=languages[target_lang]
            )

            audio_file = "translated_audio.mp3"
            tts.save(audio_file)

            audio_bytes = open(audio_file, "rb").read()

            st.subheader("Audio")
            st.audio(audio_bytes, format="audio/mp3")

        except Exception as e:
            st.error(f"Error: {e}")

st.markdown('</div>', unsafe_allow_html=True)