import streamlit as st
import pandas as pd
st.set_page_config(
    layout="wide"
)

df_poster = pd.read_parquet('/Users/julien/cinema/df_poster.parquet')
df_reco = pd.read_parquet('/Users/julien/cinema/df_reco.parquet')

col1, col2, col3 = st.columns([2, 3, 2])  # Centrer et définir les proportions
with col2:
    option = st.selectbox(
        "",
        options=df_poster["titre"],
        format_func=lambda x: x if st.session_state.get("search_query", "").lower() in x.lower() else None, index=None, placeholder="Choisissez un film"
    )
image_url = "https://image.tmdb.org/t/p/original"

if option:
    resultat = df_reco.loc[df_reco["titre"] == option]
    if not resultat.empty: 
        # Recherche de l'index de la source
        recherche = resultat["source"].iloc[0]
        if df_poster['poster_path'].iloc[recherche] is None:
           poster_url = "file:///Users/julien/cinema/logo_sans_fond.png"
        else:
           poster_url = image_url + df_poster['poster_path'].iloc[recherche]

        # **Affichage du premier film (au-dessus des recommandations)**
        st.markdown(
            f"""
            <div style="text-align: center;">
                <h2>Film sélectionné</h2>
                <p>{df_poster['titre'].iloc[recherche]}</p>
                <img src="{poster_url}" alt="Poster" style="width: 250px;">
                <p>📅 <strong>Année :</strong> {df_poster['année'].iloc[recherche]}</p>
                <p>🎥 <strong>Réalisateur :</strong> {df_poster['Real'].iloc[recherche]}</p>
            </div>
            """,
            unsafe_allow_html=True
        )
        
        # Ajouter un séparateur et plusieurs espaces vides
        st.empty()
        st.divider()
        st.empty()
       
        
        # **Affichage des recommandations**
        st.markdown(
            f"""
            <div style="text-align: center;">
                <h2>Suggestions similaires</h2>
            """,
            unsafe_allow_html=True
        )
        columns = st.columns(5)  # Création des 5 colonnes
        
        # Récupération des recommandations
        recos = list(resultat[["r1", "r2", "r3", "r4", "r5"]].values)[0]
        titres = df_poster["titre"].iloc[recos].tolist()
        annee = df_poster["année"].iloc[recos].tolist()
        real = df_poster["Real"].iloc[recos].tolist()
        poster = df_poster["poster_path"].iloc[recos].tolist()

        # Affichage des recommandations dans les colonnes
        for i, (titre, annee, realisateur, poster_path) in enumerate(zip(titres, annee, real, poster)):
            with columns[i % 5]:  # Répartir les films sur 5 colonnes
                st.text(f"{titre}")
                if poster_path is None :
                 st.image("/Users/julien/cinema/logo_sans_fond.png", width=150)
                else:
                 st.image(f"{image_url}{poster_path}", width=150)
                st.text(f"📅 Année : {annee}")
                st.text(f"🎥 Réalisateur : {realisateur}")
                
    else:
        st.warning("Aucun résultat trouvé pour cette sélection.")

else:
    with col2:
        st.info("Veuillez chercher un film.")
