import streamlit as st
import google.generativeai as genai

# --- CONFIGURATION ---
st.set_page_config(page_title="DirectKael", page_icon="🔗")

# --- DESIGN ---
st.markdown("""
    <style>
    .stApp { background-color: #000000; }
    h1 { color: #39FF14; text-align: center; text-shadow: 0px 0px 15px #39FF14; }
    div, p, label { color: #e0e0e0; }
    .stTextArea textarea { background-color: #111111; color: #39FF14; border: 1px solid #39FF14; }
    .stButton > button { background-color: #39FF14; color: #000000; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

st.title("DIRECTKAEL")

# --- CONFIGURATION IA ---
try:
    api_key = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-pro')
except:
    st.error("Clé API non trouvée. Vérifie ton fichier secrets.toml")
    st.stop()

# --- ZONE DE RECHERCHE ---
description = st.text_area("Décris en détail ce que tu cherches :", height=150)

if st.button("Générer les liens"):
    if description:
        with st.spinner("Analyse en cours..."):
            reponse = model.generate_content(f"Trouve 3 sites web pertinents pour cette demande : {description}. Donne le nom et l'URL.")
            st.write(reponse.text)
    else:
        st.warning("Écris une description d'abord.")
