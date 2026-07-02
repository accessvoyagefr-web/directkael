import streamlit as st

# Configuration de la page
st.set_page_config(page_title="DirectKael", page_icon="⚡")

# --- DESIGN NOIR & VERT FLUO ---
st.markdown("""
    <style>
    /* Fond global */
    .stApp {
        background-color: #000000;
    }
    
    /* Titre Principal */
    h1 {
        color: #39FF14; 
        font-family: 'Arial Black', sans-serif;
        text-align: center;
        text-transform: uppercase;
        letter-spacing: 2px;
        text-shadow: 0px 0px 15px #39FF14;
    }

    /* Style du chat */
    .stChatMessage {
        background-color: #1a1a1a;
        border-left: 5px solid #39FF14;
    }
    
    /* Couleur du texte */
    div, p {
        color: #e0e0e0;
    }
    
    /* Couleur de la zone de saisie */
    .stTextInput > div > div > input {
        border: 2px solid #39FF14;
        background-color: #000000;
        color: #39FF14;
    }
    </style>
    """, unsafe_allow_html=True)

# Affichage du titre
st.title("DIRECTKAEL")
st.markdown("---") 
st.write("Bienvenue dans ton assistant personnel.")
