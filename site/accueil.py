import streamlit as st
from reco import afficher_reco  
from viz import afficher_viz    

# Configuration de la page Streamlit
st.set_page_config(
    page_title="Nearest Movies",  
    page_icon="🍿",               
    layout="wide",                # Disposition de la page sur toute la largeur
)

# Initialisation de la variable pour suivre la page active 
if "page" not in st.session_state:
    st.session_state.page = "accueil"  # Par défaut, la page d'accueil est affichée

    # Définition d'une fonction pour changer la page active
def set_page(page_name):
    st.session_state.page = page_name  # Modification de la variable de session pour changer de page

# Configuration de la barre de navigation avec plusieurs colonnes
col1, col2, col3, col4, col5 = st.columns([1, 1, 1, 1, 1])  # Distribution des colonnes
with col2:
    if st.button("Accueil", use_container_width=True):  # Bouton Accueil
        set_page("accueil")  # Change la page en 'accueil' lorsque ce bouton est pressé
with col3:
    if st.button("Visualisations", use_container_width=True):  # Bouton Visualisations
        set_page("viz")  # Change la page en 'viz' lorsque ce bouton est pressé
with col4:
    if st.button("Recommandation", use_container_width=True):  # Bouton Recommandation
        set_page("reco")  # Change la page en 'reco' lorsque ce bouton est pressé

# Ajout d'un espacement entre la navigation et le contenu de la page
st.markdown("<div style='margin-top: 30px;'></div>", unsafe_allow_html=True)

# Affichage de différentes pages en fonction de la variable `st.session_state.page`
if st.session_state.page == "accueil":
    # Page d'accueil : Introduction et explication du site
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Henny+Penny&display=swap');
        
        /* Style pour le titre */
        h1 {
            text-align: center;
            color: white;
            font-family: 'Henny Penny', serif;
            font-size: 80px;
            margin-bottom: 70px;
        }
        
        /* Style pour le texte */
        p {
            text-align: center;
            font-size: 20px;
            color: white;
        }
            
        /* Style pour les paragraphes plus détaillés */
        div {
            font-size: 18px;
            color: white;
            text-align: justify;
        }
        </style>
    """, unsafe_allow_html=True)

    # Titre principal de la page d'accueil
    st.markdown(f"""<h1>Nearest Movies</h1>""", unsafe_allow_html=True)  # Affiche le titre "Nearest Movies" avec une taille de police personnalisée

    # Disposition de l'image du logo (centrée sur la page)
    col1, col2, col3 = st.columns([3, 2, 3])  # Création de trois colonnes de largeur relative (col2 sera au centre)
    with col2:  # Affichage de l'image dans la colonne du centre
        st.image("site/logo_sans_fond.png", width=150)  # L'image est redimensionnée à 10% de sa largeur d'origine

    # Texte d'accueil
    st.markdown("<p> Bienvenue sur Nearest Movie, le site qui vous recommandera des films selon vos envies !</p>", unsafe_allow_html=True)

    # Description détaillée de la plateforme et de ses fonctionnalités
    st.markdown("""
        <div style="margin-bottom: 20px;"> Découvrez une plateforme conçue pour vous inspirer et vous guider dans vos choix cinématographiques ! </div>
        <div style="margin-bottom: 15px;">Grâce à une analyse approfondie des données des films du monde entier et d’un algorithme puissant, notre site vous proposera des films similaires à vos coups de cœur 💓</div>
        <div style="margin-bottom: 15px;">Nous misons sur la transparence de nos choix et de notre algorithme. Vous pourrez donc retrouver tous nos critères ainsi que des graphiques interactifs illustrant les données cinématographiques du monde entier sur l’onglet <span style="text-decoration: underline;"> visualisations </span> </div>
        <div style="margin-bottom: 15px;">Vous comprendrez alors à quels films vous pourrez avoir accès et comment les recommandations sont faites ! </div>
        <div style="margin-bottom: 20px;">Sur la page de <span style="text-decoration: underline;"> recommandations </span>, il vous suffit de commencer à écrire le début du titre d’un film, puis de cliquer sur la suggestion qui correspond. Le système de recommandation vous proposera alors 5 films susceptibles de vous plaire.</div>
        <p style="margin-top: 20px;">Que vous soyez amateur de blockbusters, nostalgique des films des années 90, ou fan de cinéma d'auteur, notre outil est là pour enrichir votre univers cinématographique ! </p>
    """, unsafe_allow_html=True)  # Affichage du texte explicatif détaillant les fonctionnalités du site avec des marges personnalisées

elif st.session_state.page == "viz":
# Page de visualisation : Appel de la fonction pour afficher les visualisations
    afficher_viz()

elif st.session_state.page == "reco":
# Page de recommandations : Appel de la fonction pour afficher les recommandations
    afficher_reco()