def afficher_viz():
    # Importation des bibliothèques nécessaires
    import streamlit as st
    import pandas as pd
    import plotly.express as px
   
    # Chargement des données depuis des fichiers CSV
    df_top_pays = pd.read_csv("site/Top_pays.csv")
    df_time = pd.read_csv("site/df_time.csv")
    df_pop_note = pd.read_csv("site/df_pop_note.csv")
    df_real = pd.read_csv("site/df_film_filtre.csv")

    # Disposition des colonnes pour l'affichage avec Streamlit
    col1, col2 = st.columns([1, 1])

    # Début de la colonne 1
    with col1:
        # Graphique des pays : Top 15 des pays producteurs de films
        pays_chart = px.bar(
            df_top_pays,
            x="pays",
            y="score",
            labels={"pays": "Pays", "score": "Score"}
        )
        pays_chart.update_layout(title_text='Top 15 des pays producteurs de films', title_x=0.4)
        pays_chart.update_traces(marker_color="#9B1B30")
        st.plotly_chart(pays_chart)

        # Explication du graphique des pays
        with st.expander("Explications"):
            st.write("""
                    **(1)**  

                    Ce graphique en barres met en avant le **top 15 des pays producteurs de films**, grâce à un score combinant :  
                    - Le **nombre moyen de films produits par pays**.  
                    - Leur **popularité à l’échelle mondiale**.  
                    """)

        # Graphique Popularité vs Note : Relation entre la note des films et leur popularité
        pop_chart = px.bar(
            df_pop_note,
            x="groupes",
            y="popularity",
            labels={"popularity": "Popularité", "groupes": "Note"}
        )
        pop_chart.update_layout(title_text='Popularité en fonction de la note', title_x=0.4)
        pop_chart.update_traces(marker_color="#9B1B30")
        st.plotly_chart(pop_chart)

        # Explication du graphique Popularité vs Note
        with st.expander("Explications"):
            st.write("""
                    **(3)**  

                    Le graphique en barres montre la relation entre la note des films (sur une échelle de 1 à 10) et leur popularité (sur une échelle de 0 à 5).  

                    On remarque que :  
                    - Les films notés **1/10** sont en réalité plus populaires que ceux notés **10/10**.  
                    - Les films ayant des notes comprises entre **2/10 et 9/10** affichent des scores de popularité similaires.  

                    Par conséquent, nous avons choisi de **ne pas appliquer de filtre** basé sur la note ou la popularité, car ces critères ne semblent pas avoir un impact déterminant sur la popularité d'un film.  
                    """)

        # Graphique des réalisateurs : Nombre de films réalisés par les cinéastes
        nb_films = df_real["Real"].value_counts()
        nb_real = nb_films.value_counts().sort_index()
        x = nb_real.index
        y = nb_real.values  
        real_chart = px.bar(x=x, 
                            y=y, 
                            labels={'x': 'Nombre de films réalisés', 'y': 'Nombre de réalisateurs'}
                            )
        real_chart.update_layout(title_text='Nombre de films réalisés par les cinéastes', title_x=0.3)
        real_chart.update_xaxes(range=[0, 10])
        real_chart.update_traces(marker_color="#9B1B30")
        st.plotly_chart(real_chart)

        # Explication du graphique des réalisateurs
        with st.expander("Explications"):
            st.write("""
                    **(5)**  

                    Le graphique en barres montre la distribution du **nombre de films réalisés par les cinéastes** :  
                    - Environ **25 000 réalisateurs** n’ont réalisé qu’un seul film.  
                    - **6 000 réalisateurs** en ont réalisé deux.  
                    - Moins de **2 500 réalisateurs** en ont réalisé trois ou plus.  

                    Nous n’avons appliqué **aucun filtre concernant les réalisateurs**.  
                    Cependant, malgré le nombre important de réalisateurs avec une filmographie limitée, nous avons choisi d’accorder un **poids significatif à ce critère dans notre algorithme**.  
                    """)

    # Début de la colonne 2
    with col2:
        # Graphique du Bilan annuel CNC : Répartition des entrées par nationalité de film
        labels = 'Français', 'Américains', 'Européens', 'Autres'
        sizes = [70.6, 74.1, 22.9, 8.8]

        cnc_chart = px.pie(
                           values=sizes,
                           names=labels, 
                           color_discrete_sequence=px.colors.sequential.RdBu)
        cnc_chart.update_layout(title_text='Bilan annuel CNC', title_x=0.4)
        st.plotly_chart(cnc_chart)

        # Explication du graphique CNC
        with st.expander("Explications"):
            st.write("""
                    **(2)** 

                    Basé sur le bilan annuel du **CNC de 2023**, ce graphique en secteurs montre la répartition des **entrées en salle** pour chaque nationalité de film.  
                    Un nombre élevé d'entrées reflète généralement l’attractivité d’un film auprès du public français, influencée par sa popularité.  

                    Afin de concevoir un système de recommandation le plus équilibré possible, nous avons choisi :  
                    - **D’intégrer les films produits par les pays du top 15 (1)**.  
                    - Tout en incluant également les **films européens qui n’y figurent pas**.  
                    """)

        # Graphique de l'évolution de la durée des films au fil du temps
        time_chart = px.line(df_time, 
                             x="année", 
                             y="temps_minutes",
                             labels={"année": "Année", "temps_minutes": "Durée en minutes"}
                             )
        time_chart.update_traces(line_color="#922E44",
                                 line=dict(width=4))
        time_chart.update_layout(
        xaxis=dict(range=[1900, 2029]),
        yaxis=dict(range=[0, 125]),
        )
        time_chart.update_layout(title_text='Évolution de la durée des films au cours des années', title_x=0.3)
        st.plotly_chart(time_chart)

        # Explication du graphique de la durée des films
        with st.expander("Explications"):
            st.write("""
                    **(4)**  

                    Ce graphique met en évidence que la **durée des films** n’a pas connu de changements majeurs au fil du temps.  
                    En conséquence, nous avons choisi de **ne pas appliquer de filtre** sur la durée des films dans notre système de recommandation.  
                    """)
    # Ajout de style personnalisé à la page via Markdown
    st.markdown("""
        <style>
        /* Ajuste les balises Markdown générées si elles ne sont pas automatiquement dans des balises <p> */
        body div[role="document"] {
            font-size: 18px;
            line-height: 1.5;
        }
        </style>
        """, unsafe_allow_html=True)

    # Disposition des colonnes pour l'affichage de la conclusion et des critères de pondération
    col3, col4, col5 = st.columns([1, 2, 1])

    # Colonne 3 : vide
    with col3:
        st.write("")

    # Colonne 4 : Contenu de la conclusion
    with col4:
        st.markdown("""
        ### <h3 style="text-align:center;">Conclusion</h3>
        Nous avons décidé de filtrer les films uniquement en fonction de **leur pays de production**, préférant affiner notre algorithme de recommandation.  
        Nous nous assurons ainsi de recommander des films ayant une **forte visibilité** et en lien avec les attentes culturelles des utilisateurs, tout en maintenant de la **diversité** grâce à l’inclusion des films européens qui n’apparaissent pas dans le top 15 mondial.  

        Nous avons ajusté soigneusement notre **pondération** en fonction de l’importance de chaque critère.
        """, unsafe_allow_html=True)

    # Colonne 5 : vide
    with col5:
        st.write("")

    # Disposition des colonnes pour l'affichage des critères spécifiques
    col6, col7, col8 = st.columns([1, 2, 1])

    # Colonne 6 : Genre et année de parution
    with col6:
        # Affichage du poids du genre
        st.markdown("""
        #### <h4 style="text-align:center;">**Genre**</h4>  
        Le genre a reçu un poids élevé basé sur le rapport du CNC, où nous avons constaté que les Français consommaient beaucoup de comédies, drames, films d’aventure et d’animation.  
        """, unsafe_allow_html=True)
        st.write("")  # Espace vide pour aérer
        st.write("")  # Espace vide pour aérer

        # Affichage de la pondération de l'année de parution
        st.markdown("""
        #### <h4 style="text-align:center;">**Poids de l’année de parution**</h4>  
        L’année de parution n’a été ni minorée ni majorée.
        """, unsafe_allow_html=True)

    # Colonne 7 : Réalisateur et note
    with col7:
        # Affichage du poids du réalisateur
        st.markdown("""
        #### <h4 style="text-align:center;">**Réalisateur**</h4>  
        Le réalisateur a bénéficié d’un poids élevé, bien que la plupart n’aient réalisé qu’un seul film (5). Nous avons équilibré cette pondération en tenant compte d’autres critères (année de parution, genre, popularité…) pour garantir une recommandation diverse et pertinente.  
        Cela met en lumière des réalisateurs ayant une vision artistique particulière tout en offrant une expérience adaptée aux goûts des utilisateurs.  
        """, unsafe_allow_html=True)

        # Affichage du poids de la note
        st.markdown("""
        #### <h4 style="text-align:center;">**Note**</h4>  
        La note a obtenu un poids légèrement inférieur. Bien que la popularité et la note ne soient pas toujours corrélées, nous avons préservé cet indicateur pour inclure des films d’art et d’essai moins populaires tout en maintenant la diversité des propositions (3). 
        """, unsafe_allow_html=True)

    # Colonne 8 : Nombre de votes et durée
    with col8:
        # Affichage du poids du nombre de votes
        st.markdown("""
        #### <h4 style="text-align:center;">**Nombre de votes**</h4>  
        Le nombre de votes a été légèrement minoré, car il peut être influencé par des facteurs externes tels que la visibilité ou des campagnes de promotion, ce qui ne reflète pas toujours la qualité globale.  
        """, unsafe_allow_html=True)
        st.write("")  # Espace vide pour aérer
        st.write("")  # Espace vide pour aérer

        # Affichage de la pondération de la durée
        st.markdown("""
        #### <h4 style="text-align:center;">**Durée**</h4>  
        La durée a reçu une pondération négative faible, car elle présente peu de variation au fil du temps et semble peu significative sur les préférences des utilisateurs (4).  
        """, unsafe_allow_html=True)
        st.write("")  # Espace vide pour aérer
        st.write("")  # Espace vide pour aérer
        st.write("")  # Espace vide pour aérer
        st.write("")  # Espace vide pour aérer

    # Disposition des colonnes pour le résumé
    col9, col10, col11 = st.columns([1, 2, 1])

    # Colonne 10 : Résumé de la recommandation
    with col10:
        st.markdown("""
        **En résumé** : Nous avons pris en compte ces différents critères pour offrir une recommandation équilibrée et diversifiée, répondant aux goûts des utilisateurs tout en valorisant la richesse cinématographique mondiale et européenne.
        """, unsafe_allow_html=True)
