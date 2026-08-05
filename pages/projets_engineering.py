import streamlit as st
from menu import show_menu

show_menu()


st.title('Mes projets Data')
st.subheader("Ingénierie & Architecture")


tab1, = st.tabs(["💵 Détection de fraude bancaire"])

with tab1:
    st.header("💵 Détection de fraude bancaire")
    with st.container(border=True):
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
                ***Date de publication :** Février 2026*

                **Description** : Système de simulation de détection de fraude en temps réel avec amélioration continue et monitoring du système

                **Technologies** : Python, Pandas, Docker, Streamlit, XGBoost (Machine Learning), FastAPI, Grafana, Prometheus, Redis, Prefect, BigQuery (Google Cloud Platform)
                        """)
            st.link_button("Voir le projet sur GitHub", "https://github.com/kenjivictor/projet_fraude_cb", icon="👉")
            if st.button("👉 Aperçu en bas de page"):
                st.html("""
                    <script>
                        document.getElementById('apercu-fraud').scrollIntoView({behavior: 'smooth'});
                    </script>
                """, unsafe_allow_javascript=True)
        with col2:
            st.image('media/projets/fraud/resume_stack.png')
    
    col1, col2 = st.columns(2)
    with col1:
            
        st.subheader("Contexte")
    
        st.write("""
                
            Dans le cadre de ma formation en data, nous avons conçu en groupe un **système complet de détection de fraude en temps réel**, 
            allant du stockage des données jusqu’au monitoring des services en production, le tout s’améliorant automatiquement.

            L’idée n’était pas seulement d’entraîner un modèle de machine learning, mais de reproduire un environnement proche d’une application réelle : 
            flux continu, stockage, monitoring et réentrainement automatique.
                
                """)
    
    with col2:
    
        st.subheader("Données")
    
        st.write("""
                    
            Nous avons utilisé un dataset fictif de transactions financières provenant de **Kaggle** ([PaySim, plus de 6 millions de lignes](https://www.kaggle.com/datasets/ealaxi/paysim1/data)).

            Afin de simuler un contexte réel, nous avons divisé le jeu de données :

            - **90% des données** → *entraînement initial du modèle*
            - **10% des données** → *simulation d’un flux continu de transactions*

            Cela nous a permis d’imiter un système recevant des opérations en continu.
                
                """)
    
    st.divider()
    
    st.subheader("Fonctionnement du système")
    
    st.write("Le projet repose sur une architecture orientée données et temps réel.")
    
    col1, col2 = st.columns(2)
    with col1:
        st.write("""
            #### 🔹 Simulation temps réel

            Nous avons mis en place :

            - un service de prédiction basé sur XGBoost interrogeant le modèle et retournant un score de fraude (le cerveau)
            - un simulateur qui envoi les transactions avec **FastAPI** (script “émetteur”)
            - une interface **Streamlit** permettant de visualiser les transactions frauduleuses et leur niveau de risque en direct

            #### 🔹Stockage et buffer

            Les transactions sont temporairement stockées dans **Redis**, puis envoyées par lots vers **BigQuery** sur **Google Cloud Platform**.

            Ce mécanisme permet de lisser le flux et préparer l’apprentissage futur.

            #### 🔹 Apprentissage continu

            Après un certain volume de nouvelles données, un workflow déclenché par **Prefect** :

            1. récupère les nouvelles transactions
            2. réentraîne le modèle
            3. remplace automatiquement le modèle en production si les scores sont meilleurs que le modèle précédent

            Le système s’adapte ainsi aux nouvelles techniques de fraude.
                
                """)
    
    with col2:
        st.write("""
                        
            #### 🔹Conteneurisation

            Chaque composant est isolé avec **Docker** :

            - service de prédiction / simulateur / dashboard
            - buffer Redis / envoi vers BigQuery / réentraînement
            - monitoring

            Cette approche rend l’architecture reproductible et proche d’un déploiement réel :
                
                """)
        st.image('media/projets/fraud/pipeline.png')
    
    st.divider()
    
    st.subheader("Monitoring et observabilité")
    
    st.write("""
        
        
        Un modèle performant c'est bien. Un modèle performant soutenu par une surveillance continue de l’infrastructure , c'est mieux ! 
        Cette couche de monitoring recrée un environnement quasi réel d’entreprise, indispensable pour anticiper les risques et assurer une exploitation fluide.
            """)
    
    col1, col2 = st.columns(2)
    with col1:
        st.write("""
                
            #### Technos de monitoring
            
            Nous avons intégré :
            
            - **cAdvisor** pour le monitoring des conteneurs
            - **node_exporter** pour le monitoring hôte
            - **Prefect** pour le suivi des workflows de Machine Learning
            - **Prometheus** pour la collecte des métriques
            - **Grafana** pour la visualisation des métriques
                """)
    with col2:
        st.write("""
                
            #### Métriques surveillées
            
            **Fraudes :**
    
            - transactions par seconde / latence des prédictions
            - taux de fraude détectée / erreurs du modèle
            
            **Infrastructure :**
            
            - CPU / mémoire / réseau / utilisation disque
            - santé des conteneurs
    
    
            **Machine Learning :**
    
            - déclenchements de réentraînements
            - durée d’entrainement
            - évolution des performances
                """)

    st.divider()
    
    st.subheader("Aperçus de l'application", anchor="apercu-fraud")
    col1, col2 = st.columns(2)
    with col1:
        st.image('media/projets/fraud/streamlit_fraude.gif', caption="L'interface Streamlit : tableau de suivi des fraudes détectées")
    with col2:
        st.image('media/projets/fraud/performances_modele.gif', caption="L'interface Streamlit : performances du modèle")
        
    col1, col2 = st.columns(2)
    with col1:
        st.image('media/projets/fraud/grafana.gif', caption="Le monitoring d'infrastructure avec Grafana")
    with col2:
        st.image('media/projets/fraud/prefect.gif', caption="Le monitoring d'entraînement continu du modèle avec Prefect")
