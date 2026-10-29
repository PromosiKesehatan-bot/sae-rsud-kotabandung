import io
import os
import time
from google import genai
from gtts import gTTS
import PyPDF2
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="SAE RSUD Kota Bandung", page_icon="🩺", layout="centered"
)

# Kustomisasi Desain: Mengunci teks agar SELALU terbaca jelas di perangkat apa pun
custom_css = """
<style>
/* Background gradien elegan */
.stApp {
    background: linear-gradient(135deg, #0d1b2a 0%, #1b263b 50%, #0f2c42 100%);
    color: #e0e6ed !important;
}

/* Header & sidebar */
header {visibility: hidden;}
section[data-testid="stSidebar"] {
    background-color: rgba(13, 27, 42, 0.95);
    color: #ffffff !important;
}

/* Kotak obrolan dengan latar gelap tegas */
div[data-testid="stChatMessage"] {
    background: rgba(15, 23, 42, 0.85) !important;
    border: 1px solid rgba(255, 255, 255, 0.15) !important;
    border-radius: 14px;
    padding: 12px;
    margin-bottom: 10px;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3);
}

/* Kunci warna teks obrolan agar selalu putih terang */
div[data-testid="stChatMessage"] p, 
div[data-testid="stChatMessage"] div,
div[data-testid="stChatMessage"] span,
div[data-testid="stChatMessage"] li {
    color: #f8fafc !important;
    font-size: 15px;
    line-height: 1.6;
}

/* Input chat di bagian bawah */
div[data-testid="stChatInput"] {
    border-radius: 12px;
}
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])


@st.cache_resource
def load_context_data():
  txt_data = ""
  pdf_data = ""

  # 1. Baca berkas TXT
  for f in os.listdir("."):
    if f.endswith(".txt") and f != "requirements.txt":
      try:
        with open(f, "r", encoding="utf-8") as file:
          txt_data += file.read() + "\n\n"
      except Exception:
        continue

  # 2. Baca berkas PDF
  for f in os.listdir("."):
    if f.
