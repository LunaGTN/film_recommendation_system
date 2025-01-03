def afficher_reco():
    import streamlit as st
    import pandas as pd
    import re
    import requests

    @st.cache_data
    def getposter():
        return pd.read_parquet('site/poster.parquet')
    @st.cache_data
    def getreco():
        return pd.read_parquet('site/reco.parquet')
    @st.cache_data
    def getgemini():
        return pd.read_csv('site/gemini_id.csv')
    
    df_poster = getposter()
    df_reco = getreco()
    df_gemini = getgemini()

    st.markdown("""
        <style>
        /* Style pour le texte */
        p {
            text-align: center;
            font-size: 20px;
            color: white;
        }
                
        h3 {
            text-align: center; }
        iframe {
                text-align: center;
                }
        </style>""", unsafe_allow_html=True)


    st.markdown("<p>Soirée entre amis, film en solo, en couple ou en famille ?</p>", unsafe_allow_html=True)

    st.markdown("<h3> Moteur de recommandation </h3>", unsafe_allow_html=True)

    st.text("Tapez le début d’un titre qui vous plaît, choisissez parmi les suggestions, et laissez notre système dénicher 5 films qui pourraient vous divertir!" )

    st.text("Un trou de mémoire pour le titre mais vous êtes certain du nom du réalisateur ? La barre de recherche filtrera les titres pour vous.")
    col1, col2 = st.columns([1, 2])  # Centrer et définir les proportions
    with col1:
        option_real = st.selectbox(
            "filtrer par réalisateur",
            options = df_poster["Real"].unique(),
            format_func=lambda x: x if st.session_state.get("search_query", "").lower() in x.lower() else None, index=None, placeholder="Choisissez un réalisateur",
            label_visibility = "hidden"
        )

        if option_real:
            variable_options = df_poster["id"].loc[df_poster["Real"] == option_real]    
        else:
            variable_options = df_poster["id"]

    with col2:
        option = st.selectbox(
            "selection film",
            options = variable_options,
            format_func=lambda x: x if st.session_state.get("search_query", "").lower() in x.lower() else None, index=None, placeholder="Choisissez un film",
            label_visibility = "hidden"
        )
    image_url = "https://image.tmdb.org/t/p/original"

    if option:
        resultat = df_reco.loc[df_reco["id"] == option] # Source + reco
        if not resultat.empty: #S'il y a quelquechose dans la barre
            # Recherche de l'index de la source
            recherche = resultat["source"].iloc[0] #Récupère l'index du film "option"
            titre_str =  df_poster["titre"].iloc[recherche] #Renvoie l'id du film "option"
            if df_poster['poster_path'].iloc[recherche] is None: # Si pas de poster
                poster_url = "https://i.imghippo.com/files/ZOcN3975ToU.png" #Affiche le logo
            else:
                poster_url = image_url + df_poster['poster_path'].iloc[recherche] #Sinon, l'image du film

            # **Affichage du premier film (au-dessus des recommandations)**
            st.markdown(
                f"""
                <div style="text-align: center;">
                    <h2>Film sélectionné</h2>
                    <p><strong>{titre_str}</strong></p>
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
            titres = df_poster["id"].iloc[recos].tolist()
            annee = df_poster["année"].iloc[recos].tolist()
            real = df_poster["Real"].iloc[recos].tolist()
            poster = df_poster["poster_path"].iloc[recos].tolist()

            # Affichage des recommandations dans les colonnes
            for i, (titre, annee, realisateur, poster_path) in enumerate(zip(titres, annee, real, poster)):
                liste_titre_reco = titre.split("-")
                titre_no_date_reco = " ".join(liste_titre_reco[:-1])
                with columns[i % 5]:  # Répartir les films sur 5 colonnes
                    st.markdown(f"{titre_no_date_reco}", unsafe_allow_html=True )
                    if poster_path is None :
                        st.image("site/logo_sans_fond.png", width=150)
                        st.text(f"📅 Année : {annee}")
                        st.text(f"🎥 Réalisateur : {realisateur}")
                    else:
                        st.image(f"{image_url}{poster_path}", width=150)
                        st.text(f"📅 Année : {annee}")
                        st.text(f"🎥 Réalisateur : {realisateur}")
                    
        else:
            st.warning("Aucun résultat trouvé pour cette sélection.")

    else:
        with col2:
            st.info("Veuillez chercher un film.")


    def dataframe_to_context(df):
        # Transformer chaque ligne en une phrase descriptive
        context = "\n".join(
            df.apply(
                lambda row: (
                    f"{row['id']}"
                ),
                axis=1,
            )
        )
        return f"Voici les films disponibles :\n{context}"

    context = dataframe_to_context(df_gemini)

    # Interface utilisateur
    st.markdown("<h3> Demandez à l'IA 🤖 </h3>", unsafe_allow_html=True)
    st.text("Vous ne savez pas précisément quel film vous inspire ? Demandez à l'IA un genre, un thème, un réalisateur ! Essayez donc avec 'film de sorcier', ou 'Tim Burton' par exemple. Le choix de film avec notre Robot est limité, si vous avez un film en tête, tapez le dans la barre de recherche ⬆️")
    user_query = st.text_input("Input gemini", label_visibility="hidden", placeholder="Quel type de film voulez-vous regarder ?")

    if user_query:  # Assurer que user_query n'est pas vide
        url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent"
        api_key = st.secrets["api"]
        payload = {
            "contents": [
                {
                    "parts": [
                        {"text": f"""Je cherche des films qui correspondent à la demande suivante : {user_query}.
                        Pour chaque film de cette liste {context}, assure-toi qu'il correspond bien à la demande en termes de genre, d'intrigue, ou d'autres critères.
                        Affiche les ID des 5 films qui correspondent le mieux tel qui sont exactement écris dans {context}, et rien d'autre, sous forme de liste et n'écris rien d'autres."""}
                    ]
                }
            ]
        }

        headers = {
            "Content-Type": "application/json"
        }

        response = requests.post(url, headers=headers, json=payload, params={"key": api_key})
        
        response_json = response.json()
        films_text = response_json['candidates'][0]['content']['parts'][0]['text']

        cleaned_text = re.sub(r'\*', '', films_text)
        film_titles = cleaned_text.strip().splitlines()

        # Créer une liste pour stocker les titres trouvés dans le DataFrame
        titre_gemini = []
        annee_gemini = []
        real_gemini = []
        poster_gemini = []
    
    # Filtrer le DataFrame pour chaque titre extrait et ajouter les résultats
        for el in film_titles:
            el = el.strip()
            filtered_df = df_poster[df_poster['id'] == el]

            if not filtered_df.empty:  # Vérifier si le DataFrame n'est pas vide
                titre_gemini.append(filtered_df['titre'].values[0])
                annee_gemini.append(filtered_df['année'].values[0])
                real_gemini.append(filtered_df['Real'].values[0])
                poster_gemini.append(filtered_df['poster_path'].values[0])

        # Si aucun film n'a été trouvé, afficher un message d'avertissement
        if not titre_gemini:
            st.warning("Aucun film trouvé correspondant à votre recherche.")
        else:
            columns = st.columns(5)

            # Affichage des recommandations dans les colonnes
            for i, (titre_g, annee_g, realisateur_g, poster_path_g) in enumerate(zip(titre_gemini, annee_gemini, real_gemini, poster_gemini)):
                with columns[i % 5]:  # Répartir les films sur 5 colonnes
                    st.markdown(f"{titre_g}", unsafe_allow_html=True)

                    # Vérification si le poster est disponible
                    if not poster_path_g:
                        st.image("site/logo_sans_fond.png", width=150)  # Afficher une image par défaut si aucun poster n'est trouvé
                    else:
                        st.image(f"{image_url}{poster_path_g}", width=150)  # Afficher l'image du poster

                    # Affichage des autres informations
                    st.text(f"📅 Année : {annee_g}")
                    st.text(f"🎥 Réalisateur : {realisateur_g}")

    else:
        st.warning("Veuillez entrer un type de film pour obtenir des recommandations.")
