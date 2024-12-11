import streamlit as st 
from streamlit_option_menu import option_menu

fichier= open("accueil.html")
contenu = fichier.read()

st.image("logo_sans_fond.png", width = 150)
st.title("The Nearest Movie")
st.subheader("Des recommandations personnalisées pour des films qui vous ressemblent !")
st.image("image.jpg", width = 400)
st.text("Votre cinéma s'invite à la maison.")
st.markdown(contenu, unsafe_allow_html= True)

col1, col2 = st.columns(2)
with col1:
    if st.button("🌎 Analyse", width = 150):
        st.write("🌎 Analyse")

with col2:
    if st.button("🍿 Recommandation"):
        st.write("Recommandation")


