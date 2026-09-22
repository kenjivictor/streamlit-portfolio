import streamlit as st
from menu import show_menu

show_menu()

st.write('# Mes compétences')

tab1, tab2 = st.tabs([" Compétences techniques", " Soft skills"])

with tab1:

    st.write("## Compétences techniques")
    st.write("### Data Engineering")
    
    st.write( """
            - **Python :** préparation des données, scripts, modèles
            - **Bases de données** : SQL, NoSQL, Data Warehouses
            - **Pipelines & ETL** : Airflow, Docker
            - **Cloud** : GCP, AWS
            - **Machine Learning** : Scikit-Learn (NLP, régression, classification, clustering)
            - **Automatisation & Data engineering :** web scraping, API, regex
            """ )
    
    st.write("### Data Analisis")
    
    st.write( """
            - **Outils BI :** Power BI & DAX, Matplotlib, Seaborn, Plotly Express
            - **SQL avancé :** requêtage, jointures, agrégations, fenêtrage, CTE
                """ )
    
    st.write("### Compétences transverses")
    
    st.write( """
            - **Gestion de projet :** méthode Agile, Git/GitHub
            - **Bureautique** : Office 365 (Excel, Word, PowerPoint, SharePoint…)
            - **Applications** : Notion, Streamlit, Power Apps, Power Automate
                    """ )
    
with tab2:
    st.write("## Soft skills")
    
    st.write("""
        
        - **Avoir l’esprit d’équipe**  
        Capacité à collaborer efficacement, à partager l’information et à contribuer à une dynamique collective positive.

        - **Avoir le sens du service**  
        Volonté constante de comprendre les besoins des utilisateurs et d’apporter des solutions fiables, utiles et adaptées.

        - **Faire preuve d’autonomie**  
        Aptitude à prendre en charge un sujet, à avancer de manière structurée et à atteindre les objectifs sans supervision constante.

        - **Faire preuve de créativité, d’inventivité**  
        Faculté à proposer des idées nouvelles, à imaginer des solutions originales et à sortir des schémas habituels pour améliorer les résultats.

        - **Faire preuve de rigueur et de précision**  
        Attention portée aux détails, respect des bonnes pratiques et production de livrables fiables, maîtrisés et exempts d’erreurs.

        - **Capacité à travailler en mode projet**  
        Maîtrise des méthodes de gestion de projet, avec une organisation claire, un suivi des étapes et une coordination efficace des acteurs.
        
        """)