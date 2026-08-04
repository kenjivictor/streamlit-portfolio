import streamlit as st
from menu import show_menu

show_menu()

st.title('Mes compétences')

tab1, tab2 = st.tabs([" Compétences techniques", " Soft skills"])

with tab1:

    st.subheader("Data Engineering")
    
    st.write( """
            - **Python :** préparation des données, scripts, modèles
            - **Bases de données** : SQL, NoSQL, Data Warehouses
            - **Pipelines & ETL** : Airflow, Docker
            - **Cloud** : GCP, AWS
            - **Machine Learning** : Scikit-Learn (NLP, régression, classification, clustering)
            - **Automatisation & Data engineering :** web scraping, API, regex
            """ )
    
    st.subheader("Data Analisis")
    
    st.write( """
            - **Outils BI :** Power BI & DAX, Matplotlib, Seaborn, Plotly Express
            - **SQL avancé :** requêtage, jointures, agrégations, fenêtrage, CTE
                """ )
    
    st.subheader("Compétences transverses")
    
    st.write( """
            - **Gestion de projet :** méthode Agile, Git/GitHub
            - **Bureautique** : Office 365 (Excel, Word, PowerPoint, SharePoint…)
            - **Applications** : Notion, Streamlit, Power Apps, Power Automate
                    """ )
    
with tab2:
    st.subheader("Soft skills")