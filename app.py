import streamlit as st

# Configuration de la page
st.set_page_config(page_title="DirectKael", page_icon="⚡")

# --- DESIGN NOIR & VERT FLUO ---
st.markdown("""
    <style>
    .stApp { background-color: #000000; }
    h1 { color: #39FF14; text-align: center; text-shadow: 0px 0px 15px #39FF14; }
    div, p { color: #e0e0e0; }
    </style>
    """, unsafe_allow_html=True)

st.title("DIRECTKAEL")
st.markdown("---")

# --- ZONE DE TEXTE ---
user_input = st.text_input("Pose ta question ici :", placeholder="Comment puis-je t'aider ?")

if user_input:
    st.write(f"Tu as écrit : {user_input}")
