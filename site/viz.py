def afficher_viz():
    import streamlit as st
    import pandas as pd
    import seaborn as sns
    import matplotlib.pyplot as plt
    import plotly.express as px

    df = pd.read_csv("/Users/julien/cinema/df_film.csv")
    df_top_pays = pd.read_csv("/Users/julien/cinema/Top_pays.csv")
    df_real = pd.read_csv("/Users/julien/cinema/top10_real_note2.csv")
    df_genre = pd.read_csv("/Users/julien/cinema/df_top_genre.csv")
    df_pop_note = pd.read_csv("/Users/julien/cinema/df_pop_note.csv")

        # Disposition des colonnes
    col1, col2 = st.columns([1, 1])

    with col1:
        # Graphique des pays
        pays_chart = px.bar(
            df_top_pays,
            x="pays",
            y="score",
            title="Top Pays",
            labels={"pays": "Pays", "score": "Score"}
        )
        pays_chart.update_traces(marker_color="#9B1B30")
        st.plotly_chart(pays_chart)
        with st.expander("Explications"):
            st.write('''(1) Ce graphique en barres met en avant le top 15 des pays producteurs de films grâce à un score 
                     combinant le nombre moyen de films produits par pays et leur popularité à l’échelle mondiale."
                    ''')
        # Graphique des réalisateurs
        pop_chart = px.bar(
            df_pop_note,
            x="groupes",
            y="popularity",
            title="Popularité des notes",
            labels={"Real": "Réalisateurs", "score": "Score"}
        )
        pop_chart.update_traces(marker_color="#9B1B30")
        st.plotly_chart(pop_chart)
        with st.expander("Explications"):
         st.write("""3) Le graphique en barres montre la relation entre la note des films (sur une échelle de 1 à 10) et leur popularité 
                  (sur une échelle de 0 à 5). On remarque que les films notés 1/10 sont en réalité plus populaires que ceux notés 10/10, 
                  et que les films ayant des notes comprises entre 2/10 et 9/10 affichent des scores de popularité similaires.Par conséquent, 
                  nous avons choisi de ne pas appliquer de filtre basé sur la note ou la popularité, car ces critères ne semblent pas avoir un impact déterminant sur la popularité d'un film. 
                  Ainsi, que vous aimiez les navets où les films d’auteurs 🤓, vous trouverez votre compte !""")

    with col2:
        # Image CNC
        labels = 'Français', 'Americains', 'Européens', 'Autres'
        sizes = [70.6, 74.1, 22.9, 8.8]

        cnc_chart = px.pie(values=sizes, names=labels, color_discrete_sequence=px.colors.sequential.RdBu)
        st.plotly_chart(cnc_chart)
        with st.expander("Explications"):
            st.write("""
            Basé sur le bilan annuel du **CNC de 2023**, ce graphique en secteurs montre la répartition des entrées en salle pour chaque nationalité de film. 
            Un nombre élevé d'entrées reflète généralement l’attractivité d’un film auprès du public français, influencée par sa popularité.

            Afin de concevoir un système de recommandation le plus équilibré possible, nous avons choisi d’intégrer les films produits par les **pays du top 15 (1)** tout en incluant les films européens qui n’y figurent pas. 

            Bien que certains pays européens soient moins représentés au niveau mondial, ils contribuent au marché français, comme en témoigne la part de **13 % des entrées pour des films européens (2)**. 
            Cette approche permet de répondre aux goûts variés du public français tout en valorisant une certaine diversité cinématographique.
            """)