import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

df = pd.read_csv("/Users/julien/cinema/df_film.csv")
df_top_pays = pd.read_csv("/Users/julien/cinema/Top_pays.csv")
df_real = pd.read_csv("/Users/julien/cinema/top10_real_note2.csv")
df_genre = pd.read_csv("/Users/julien/cinema/df_top_genre.csv")

st.set_page_config(
    layout="wide"
)
col1, col2 = st.columns([1, 1])

with col1:
    pays_chart = px.bar(df_top_pays, 
                     x="pays", 
                     y="score",
                     title="Top Pays")
    pays_chart.update_traces(marker_color='#9B1B30')
    st.plotly_chart(pays_chart)
    st.text("bla bla")

    real_chart = px.bar(df_real, 
                     x="Real", 
                     y="score",
                     title="Top Real")
    real_chart.update_traces(marker_color='#9B1B30')
    st.plotly_chart(real_chart)
    st.text("bla bla")

with col2:
    heatmap = px.imshow([[1, 20, 30],
                [20, 1, 60],
                [30, 60, 1]])
    st.plotly_chart(heatmap)
    st.text("bla bla")