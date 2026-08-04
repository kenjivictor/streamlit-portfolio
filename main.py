import streamlit as st
from menu import show_menu

st.set_page_config(page_title="Kenji VICTOR - Experte Data analisis", page_icon="🎯", initial_sidebar_state="expanded", layout="wide")

show_menu()

left, center, right = st.columns([1, 2, 1])

with center:
    st.title('Kenji VICTOR')
    st.subheader("Data Analyste certifiée & Aspirante Data Engineer")


    col1, col2 = st.columns(2)
    with col1:
        st.image("media/profil.png")
        st.link_button("🔗 N'hésitez pas à me contacter sur LinkedIn !", "https://www.linkedin.com/in/kenji-victor/", type="tertiary")
    with col2:
        st.subheader("A propos de moi")
        st.write("""
                Passionnée par le domaine de l’informatique et les nouvelles technologies, 
                je suis en reconversion vers les métiers de la data après avoir passé 10ans dans le développement web.
                """)
        st.write("""
                Mon objectif est de contribuer à la valorisation des données afin de faire de la data un véritable outil d’aide à la décision.
                """)
    