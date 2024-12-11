import streamlit as st
import pandas as pd

df = pd.read_parquet("/Users/julien/cinema/df_film.parquet")


option = st.text_input("Search for a movie title")
filtered_titles = df[df["titre"].str.contains(option, case=False, na=False)]["titre"]
st.selectbox("Movies", filtered_titles)
