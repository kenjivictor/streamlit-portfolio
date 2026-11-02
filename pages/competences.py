import streamlit as st


st.write('# Mes compétences')

col1, col2 = st.columns(2)

with col1:
    
    st.write("## Compétences techniques")
    
    
    st.write("### Data Analisis")
    
    st.write( """
            - **Python :** préparation des données, scripts
            - **Outils BI :** Power BI & DAX, Matplotlib, Seaborn, Plotly Express
            - **SQL avancé :** requêtage, jointures, agrégations, fenêtrage, CTE
            - **Automatisation :** web scraping, API, regex
                """ )

    st.write("### Data Engineering")
    
    st.write( """
            - **Bases de données** : SQL, NoSQL, Data Warehouses
            - **Pipelines & ETL** : Airflow, Docker
            - **Cloud** : GCP, AWS
            - **Machine Learning** : Scikit-Learn (NLP, régression, classification, clustering)
            """ )
    
    st.write("### Compétences transverses")
    
    st.write( """
            - **Gestion de projet :** méthode Agile, Git/GitHub
            - **Bureautique** : Office 365 (Excel, Word, PowerPoint, SharePoint…)
            - **Applications** : Notion, Streamlit, Power Apps, Power Automate
                    """ )
    
with col2:
    st.write("## Soft skills")
    
    st.write("""
        
        - **Esprit d’équipe**  
        Capacité à collaborer efficacement, à partager l’information et à contribuer à une dynamique collective positive.

        - **Sens du service**  
        Volonté constante de comprendre les besoins des utilisateurs et d’apporter des solutions fiables, utiles et adaptées.

        - **Autonomie**  
        Aptitude à prendre en charge un sujet, à avancer de manière structurée et à atteindre les objectifs sans supervision constante.

        - **Créativité**  
        Faculté à proposer des idées nouvelles, à imaginer des solutions originales et à sortir des schémas habituels pour améliorer les résultats.

        - **Rigueur**  
        Attention portée aux détails, respect des bonnes pratiques et production de livrables fiables, maîtrisés et exempts d’erreurs.

        - **Travail en mode projet**  
        Maîtrise des méthodes de gestion de projet, avec une organisation claire, un suivi des étapes et une coordination efficace des acteurs.
        
        """)