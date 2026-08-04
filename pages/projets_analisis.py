import streamlit as st
from menu import show_menu
from menu import set_wide_layout


show_menu()
set_wide_layout()


st.title('Mes projets Data')
st.header("Analyse & Insights")


tab1, tab2, tab3 = st.tabs(["🚗 Projet Toys & Models", "🎞️ Projet Film Data Lab", "🌎 Mini-Projet : Séismes"])

with tab1:
    st.subheader("🚗 Projet Toys & Models")
    with st.container(border=True):
        st.write("""
            ***Date de publication :** Octobre 2025*
            
            **Description :** Création d’un tableau de bord interactif de KPIs pour l’analyse et la visualisation 
            des performances d’une entreprise fictive de miniatures automobiles.
            
            **Technologies :**  SQL, Power BI, DAX
                    """)
    
    st.subheader("Contexte")
    
    st.write("""
            Durant ma formation à la Wild Code School, j’ai travaillé dans une équipe de quatre. 
            En 30h réparties sur un mois, notre objectif était de produire un tableau de bord pour la dirigeante de **TOYS & MODELS**, 
            spécialiste des modèles réduits.

            Notre équipe est intervenue pour définir les indicateurs clés de performance (KPIs) avec la cliente afin de suivre l’activité en temps réel 
            et de l’aider à piloter son entreprise avec une vision plus nette.
            """)
    
    st.subheader("KPIs développés")
    
    st.image("media/projets/toysmodels/kpi.png")
    
    
    

with tab2:
    st.subheader("🎞️ Projet Film Data Lab")
    with st.container(border=True):
        st.write("""
            ***Date de publication :** Décembre 2025*

            **Description :** Création d’une application de recommandation de films.

            **Technologies :** Python, Pandas, DuckDB, Seaborn, Streamlit, ScikitLearn (Machine Learning), API
                    """)
        col1, col2 = st.columns(2)
        with col1:
            st.link_button("Voir le projet sur GitHub", "https://github.com/kenjivictor/projet_recommandation_films", icon="👉")
        with col2:
            st.link_button("Live Démo", "https://filmdatalab.streamlit.app/", icon="👉")
            st.write("**Username :** utilisateur / **Password :** utilisateurMDP")
        
        
with tab3:
    st.subheader("🌎 Mini-Projet : Séismes")
    with st.container(border=True):
        st.write("""
            ***Date de publication :** Janvier 2026*

            **Description :** Création d’un rapport Power BI en 2 jours.

            **Technologies :** Python, Pandas, Power BI, DAX
                    """)