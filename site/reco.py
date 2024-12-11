import streamlit as st
import pandas as pd

df_poster = pd.read_csv('/Users/julien/cinema/df_reco.csv')
df_poster.to_parquet('/Users/julien/cinema/df_poster.parquet')

df_reco = pd.read_csv('/Users/julien/cinema/resultat.csv')
df_reco.to_parquet('/Users/julien/cinema/df_reco.parquet')




option = st.selectbox(
    "Movies",
    options=df_reco["titre"],
    format_func=lambda x: x if st.session_state.get("search_query", "").lower() in x.lower() else None,index=None
)

resultat = df_reco.loc[df_reco["titre"] == option]
st.dataframe(resultat)
recos = list(resultat[["r1","r2","r3","r4","r5"]].values)[0]
st.dataframe(df_poster.iloc[recos])



