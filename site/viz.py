import streamlit as st
import pandas as pd

df = pd.read_csv("/Users/julien/cinema/df_film.csv")
df_top_pays = pd.read_csv("/Users/julien/cinema/Top_pays.csv")

st.bar_chart(
    df_top_pays,
    x= "pays",
    y= "score")



