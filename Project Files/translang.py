from dotenv import load_dotenv
import streamlit as st
import os
try:
    import google.generativeai as genai
except Exception:
    genai = None
    st.error("Missing 'google-generative-ai' package. Install it with: pip install google-generative-ai")
    st.stop()

# Load environment variables
load_dotenv()

# Configure API key
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    st.error("Missing Google API key. Set the environment variable GOOGLE_API_KEY or add it to a .env file.")
    st.stop()
genai.configure(api_key=api_key)

# Initialize model
model = genai.GenerativeModel("gemini-2.5-flash")

# Translation function
def translate_text(text, source_language, target_language):
    prompt = f"Translate the following text from {source_language} to {target_language}: {text}"
    response = model.generate_content(prompt)
    return response.text

# Streamlit UI
st.set_page_config(page_title="AI-Powered Language Translator", page_icon="🌍")
st.header("🌍 AI-Powered Language Translator")

text = st.text_area("📝 Enter text to translate:")
source_language = st.selectbox(
    "🌐 Select source language:",
    ["English", "Telugu", "Hindi", "Spanish", "French", "German", "Chinese"]
)

target_language = st.selectbox(
    "🎯 Select target language:",
    ["English", "Telugu", "Hindi", "Spanish", "French", "German", "Chinese"]
)

if st.button("🔁 Translate"):
    if text:
        translated_text = translate_text(text, source_language, target_language)
        st.subheader("📘 Translated Text:")
        st.write(translated_text)
    else:
        st.warning("⚠️ Please enter text to translate")