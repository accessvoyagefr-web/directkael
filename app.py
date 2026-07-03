import streamlit as st
import google.generativeai as genai

# 1. Configuration de la page
st.set_page_config(page_title="LINKA", page_icon="🔗", layout="centered")

# 2. En-tête avec ton logo dans le dossier 'linka'
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    # Le chemin indique bien qu'on cherche le logo DANS le dossier 'linka'
    st.image("linka/watermarked_img_4695770333962630375.png", use_column_width=True)

# 3. Message de bienvenue
st.markdown("<h2 style='text-align: center;'>Bienvenue sur LINKA</h2>", unsafe_allow_html=True)
st.write("Je suis là pour te trouver le lien direct vers le site web que tu recherches.")

# 4. Input utilisateur
user_input = st.text_input("Quel site cherches-tu aujourd'hui ?")

if user_input:
    # Rappel de la règle métier : uniquement des sites web
    st.write(f"Recherche en cours pour : {user_input}...")
    # Ici viendra ton intégration Gemini
