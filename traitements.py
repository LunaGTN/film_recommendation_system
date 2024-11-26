import pandas as pd
import numpy as np

"""
Pour ajouter des données telles que la popularité,
 les pays de production, les affiches de films, 
nous avons du nou sservir du tmdb.csv
"""
# Lire le csv
df_tmbd = pd.read_csv("tmdb_full.csv")
#Drop les colonnes inutiles
df_tmbd = df_tmbd.drop(columns = [
    "adult",
    "backdrop_path",
    "budget",
    "genres",
    "homepage",
    "id",
    "original_language",
    "original_title",
    "overview",
    "release_date",
    "revenue",
    "runtime",
    "spoken_languages",
    "tagline",
    "title",
    "video",
    "vote_average",
    "vote_count",
    "production_companies_name",
    "production_companies_country"])

#Merge avec les colonnes de notre df_film
df_film = pd.read_csv("df_film.csv")
df_merge = df_film.merge(df_tmbd, left_on = "id_film", right_on = "imdb_id", how = "left")
df_merge = df_merge.drop(columns = ["Unnamed: 0.2","Unnamed: 0.1", "Unnamed: 0", "tconst"])

#Transformer toutes les valeurs nulles notée \\N en np.Nan (reconnu par pandas/numPy)
df_film = df_film.replace('\\N', np.nan)


"""Notre df film a toutes les colonnes dont nous avons besoin, passons à la visualisation.
Pour les graphiques, nous aurons besoins de faire certaines manipulations: """

# Créer une colonne décénie
df_film["decenie"] = ((df_film['année'] // 10) * 10).astype(str) # conversion en str pour l'analyse

#Gérer les valeurs manquantes pour les colonnes: 
""" temps_minutes -> on veut remplacer les durées manquantes par la moyenne par décénie
ex: film sorti en 1900, durée moyenne = 63 -> tout les films des années 1900 dont la durée n'est pas mentionnée
vaudra 63 minutes """

#Converti en int en ignorant les valeurs nulles
df_film['temps_minutes'] = df_film['temps_minutes'].astype('Int64')
# moyenne par décénie
moy_decenie = df_film.groupby("decenie")["temps_minutes"].mean() 
#Fonction qui remplace la valeur manquante par la moyenne/décénie du film
def replacena_mean(row):  
    if str(row["temps_minutes"]) == "<NA>": # <NA> -> valeur manquante
        row["temps_minutes"] = moy_decenie.loc[row["decenie"]]
    return row

#Appliquer la fonction au df_film
df_film = df_film.apply(replacena_mean, axis=1)

