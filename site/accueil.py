import streamlit as st
from reco import afficher_reco
from viz import afficher_viz

# Configuration de la page
st.set_page_config(
    page_title="Nearest Movies",
    page_icon="🍿",
    layout="wide",
)

# Initialisation de la variable pour suivre la page active
if "page" not in st.session_state:
    st.session_state.page = "accueil"

# Définir une fonction pour changer la page active
def set_page(page_name):
    st.session_state.page = page_name

# Navigation
col1, col2, col3, col4, col5 = st.columns([2, 1, 1, 1, 2])
with col2:
    if st.button("Accueil", use_container_width=True):
        set_page("accueil")
with col3:
    if st.button("Visualisations", use_container_width=True):
        set_page("viz")
with col4:
    if st.button("Recommandation", use_container_width=True):
        set_page("reco")

# Espacement entre navigation et contenu
st.markdown("<div style='margin-top: 30px;'></div>", unsafe_allow_html=True)

# Pages
if st.session_state.page == "accueil":
    # Page d'accueil
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Henny+Penny&display=swap');

        h1 {
            text-align: center;
            color: white;
            font-family: 'Henny Penny', serif;
            font-size: 80px;
            margin-bottom: 70px;
        }
        p {
            text-align: center;
            font-size: 20px;
            color: white;
        }
        </style>
    """, unsafe_allow_html=True)

    # Titre et description
    st.markdown("<h1>Nearest Movies</h1>", unsafe_allow_html=True)
    st.markdown("<p>Découvrez les films qui correspondent à vos goûts et explorez des visualisations interactives !</p>", unsafe_allow_html=True)

    # Centrer l'image
    col1, col2, col3 = st.columns([3, 2, 3])
    with col2:
        st.image("/Users/julien/cinema/logo_sans_fond.png", use_container_width=True)

elif st.session_state.page == "viz":
    # Page de visualisation
    afficher_viz()

elif st.session_state.page == "reco":
    # Page de recommandations
    afficher_reco()
