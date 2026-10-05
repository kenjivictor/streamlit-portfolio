import streamlit as st
from menu import show_menu

st.set_page_config(page_title="Kenji VICTOR - Experte Data analisis", page_icon="📊", initial_sidebar_state="expanded", layout="wide")

show_menu()


st.write("# Kenji VICTOR - Data Analyste certifiée")


col1, col2 = st.columns([1,2])
with col1:
    st.image("media/profil.png", width=450)
    
    st.write("""
            
            ## En résumé
            Je suis une Data Analyst avec une forte culture produit et un passé de développeuse.  
            J’aime créer des outils utiles, élégants, documentés, qui rendent les équipes plus autonomes et les données plus fiables.
            """)
    
    colA, colB = st.columns(2)
    with colA:
        st.link_button("🔗 :red[Retrouvez-moi sur LinkedIn !]", "https://www.linkedin.com/in/kenji-victor/", type="tertiary")
    with colB:
        st.link_button("🔗 :red[Mes projets sur GitHub !]", "https://github.com/kenjivictor", type="tertiary")
    
    
with col2:
    st.write("""
            
            ## Présentation
            Je suis **Kenji Victor**, Data Analyst avec un parcours hybride qui fait ma force : **développement**, **IT**, **gestion de projets**, et **analyse de données**.
            Depuis plus de dix ans, je transforme des irritants métiers en **solutions concrètes** : apps, dashboards, pipelines, automatisations.

            ## Mon parcours en bref
            **🛠️ Développement & IT (2013-2025)**  
            Développeuse web et Android, puis Cheffe de projets IT, j’ai conçu et piloté des outils internes, documenté des flux complexes, géré des anomalies data et accompagné les équipes métiers au quotidien.  
            Cette expérience m’a donné une vraie vision produit et une capacité à traduire un besoin en solution technique robuste.

            **📊 Data Analyst (2025-2026)**  
            Formée à la Wild Code School, j’ai renforcé mon expertise data : SQL, Python, Power BI, Streamlit, Docker.  
            J’ai mené des projets concrets : détection de fraude, dashboards décisionnels, apps data, pipelines automatisés.

            ## Ce que je fais aujourd’hui
            Je crée des **outils data utiles, élégants et documentés** :
            - Dashboards qui éclairent les décisions
            - Pipelines qui tournent sans friction
            - Apps Streamlit qui simplifient la vie des équipes
            - KPIs fiables, traçables, actionnables


            """)
st.divider()

st.write("## Mes projets Data")
st.write("Vous pouvez parcourir mes derniers projets ici :")
st.page_link("pages/projets_analisis.py", label="**Analyse & Insights** : Projets Data Analisis", icon="👉", )
st.page_link("pages/projets_engineering.py", label="**Ingénierie & Architecture** : Projets Data Engineering", icon="👉")