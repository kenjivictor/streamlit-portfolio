import streamlit as st
from menu import show_menu
from streamlit_extras.scroll_to_element import scroll_to_element


show_menu()

with st.container(key="haut_de_page"):
    st.title('Mes projets Data')
    st.header("Analyse & Insights")


tab1, tab2, tab3 = st.tabs(["🚗 Projet Toys & Models", "🎞️ Projet Film Data Lab", "🌎 Mini-Projet : Séismes"])

# Toys & Models
with tab1:
    st.subheader("🚗 Projet Toys & Models")
    with st.container(border=True):
        col1, col2 = st.columns(2)
        with col1:
            st.write("""
                ***Date de publication :** Octobre 2025*
                
                **Description :** Création d’un tableau de bord interactif de KPIs pour l’analyse et la visualisation 
                des performances d’une entreprise fictive de miniatures automobiles.
                
                **Technologies :**  SQL, Power BI, DAX
                        """)
            
            if st.button("👉 Aperçu en bas de page"):
                scroll_to_element("tableau_de_bord_toysmodels", alignment="start")
                st.rerun()
                
            
            
        with col2:
            st.image("media/projets/toysmodels/Animation_toysmodels.gif", width=400)
    
    
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
    
    
    
    
    st.subheader("Requêtes SQL avancées")
    
    col1, col2 = st.columns(2)
    with col1:
        st.write("")
        st.write("""

            Plonger dans une base de données, c’est un peu comme ouvrir un moteur pour comprendre comment tout s’organise. 
            Les requêtes SQL de sélection sont parfaites pour ça, surtout quand on travaille avec un vrai SGBD (Système de Gestion de Base de Données).

            Au fil de mon expérience, j’ai appris à manier les jointures, les requêtes imbriquées et les fonctions de fenêtrage. 
            Ces outils me permettent d’extraire des infos vraiment utiles et pas simplement des lignes de données. 

            Bref : transformer un tas de tables en vues claires et exploitables.
            """)
    with col2:
        st.write("Voici un exemple classique de requête SQL pour identifier les clients générant le plus de revenus :")
        
        st.image("media/projets/toysmodels/sql.png")
    
    
    
    st.subheader("Conception des tables de faits et des tables de dimensions")
        
    col1, col2 = st.columns(2)
    with col1:
        st.write("Voici un exemple de modélisation en étoile orienté pour l’analyse de données, réalisé avec Power Query (dans Power BI) :")
        
        st.image("media/projets/toysmodels/modelisation.png")
    with col2:
        st.write("")
        st.write("")
        st.write("""
            Les requêtes SQL avancées ne suffisent pas si la base n’est pas pensée pour l’analyse.

            Avant d’alimenter le tableau de bord, il a fallu structurer les données : mesures d’un côté, référentiels de l’autre. 
            Autrement dit, concevoir des tables de faits et des tables de dimensions.

            Cette étape m’a permis de renforcer mes connaissances en terme de conception de bases de données, 
            mais cette fois orientée pour l’analyse de données.
            """)
    
    
    st.subheader("Création de mesures avec DAX (Data Analysis Expressions)")
    
    col1, col2 = st.columns(2)
    with col1:
        st.write("")
        st.write("""
            Une fois la structure en place, il fallait aller plus loin : transformer ces données statiques en indicateurs 
            capables de réagir aux filtres du tableau de bord. C’est là que les mesures DAX entrent en jeu.

            DAX est un ensemble de fonctions, d’opérateurs et de constantes qui permettent de produire des calculs dynamiques 
            en fonction des données du modèle. 

            C’est là que j’ai appris à manipuler et à créer des indicateurs qui s’adaptent aux choix de l’utilisateur.

            Ci-contre, un exemple de mesure DAX qui sert à calculer le taux d’évolution mensuel du chiffre d’affaires afin de suivre 
            les tendances et repérer rapidement une progression ou une chute de performance.
            """)
    with col2:
        st.image("media/projets/toysmodels/dax.png")
        st.write("""
            1. Variable “mois_prec”

            “DATEADD” décale le contexte de filtre d’un mois en arrière, et “CALCULATE” recalcule la mesure “[Tot_ventes]” avec ce nouveau contexte.

            **Résultat :** une valeur représentant le CA du mois N-1

            2. Le calcul du pourcentage d’évolution

            On fait la différence entre le mois courant et le mois précédent, puis on divise par le mois précédent pour obtenir le taux de variation.

            “DIVIDE” évite les erreurs en cas de division par zéro.

            Enfin, on multiplie par 100 pour obtenir un pourcentage
                """)
    
    with st.container(key="tableau_de_bord_toysmodels"):
        st.subheader("Tableau de bord Power BI")
    st.write("""
            Pour finir, voici une courte vidéo qui présente le tableau de bord final. 

            On y voit l’ensemble des KPIs, les filtres interactifs et les mesures dynamiques en action. 
            C’est le rendu complet du travail : un outil clair, réactif et pensé pour aider la dirigeante à prendre des décisions rapides et éclairées.
                    """)
    st.image("media/projets/toysmodels/Animation_toysmodels.gif")
    


# Film Data Lab
with tab2:
    st.subheader("🎞️ Projet Film Data Lab")
    with st.container(border=True):
        col1, col2 = st.columns(2)
        with col1:
            st.write("""
                ***Date de publication :** Janvier 2026*

                **Description :** Création d’une application de recommandation de films.

                **Technologies :** Python, Pandas, DuckDB, Seaborn, Streamlit, ScikitLearn (Machine Learning), API
                    """)
            st.link_button("Voir le projet sur GitHub", "https://github.com/kenjivictor/projet_recommandation_films", icon="👉")
            if st.button("👉 Aperçu en bas de page", key="btn_apercu_filmdatalab"):
                scroll_to_element("tableau_de_bord_filmdatalab", alignment="start")
                st.rerun()
        with col2:
            st.image("media/projets/filmdatalab/accueil.png", width=400)
            st.link_button("Live Démo", "https://filmdatalab.streamlit.app/", icon="👉")
            st.write("**Username :** utilisateur / **Password :** utilisateurMDP")
    
    st.subheader("Contexte")

    st.write("""
        Durant ma formation de Data Analyst chez la WILD CODE SCHOOL, j’ai été amenée à travailler dans une équipe de 4 étudiants. 
        Nous avions pour mission de doter Nantes Cinéma (un établissement fictif situé sur le Territoire de la Loire-Atlantique) d'un outil technologique
        capable de rivaliser avec les standards des plateformes de streaming.

        L'objectif final était de fidéliser le public nantais via FilmDataLab, un service en ligne innovant qui prolonge l'expérience de la salle obscure
        grâce à la puissance de la Data.
        """)

    st.subheader("Le Défi Stratégique & Technique")
    
    st.write("""
        Pour garantir la pertinence de nos recommandations, notre démarche s’est articulée plusieurs  étapes clés :

        #### **1️⃣ Étude de Marché & Ciblage**

        Nous avons d'abord réalisé une étude de marché sur les données démographiques locales (Loire-Atlantique) pour affiner notre base de données :

        - **Cible prioritaire :** Les 15-30 ans (un tiers de la population).
        - **Préférences identifiées :** Forte appétence pour la **Comédie** et l'**Animation**.
        - **Format :** Priorité aux contenus en **Version Française (VF)**.

        #### **2️⃣ Préparation de la Donnée (Data Engineering)**

        Notre stratégie a consisté à combiner la performance de DuckDB, pour les jointures massives, et la flexibilité de Pandas, 
        pour les transformations et enrichissements.

        Nous avons exploité une base de données cinéma de plus de 7M+ de titres (IMDb et TMDB), puis l'avons nettoyée pour en extraire la valeur.

        - **Volume :** 5 644 films, 31 000+ acteurs, 3 500+ réalisateurs.
        - **Traitement :** Nettoyage des valeurs manquantes, formatage des genres et filtrage des films pertinents.

        #### **3️⃣ Le Moteur de Recommandation (Machine Learning)**

        L'intelligence de l'application repose sur un système de filtrage qui croise :

        - **Le contenu :** Similitude entre les films (genres, mots-clés, réalisateurs).
        - **La popularité :** Pondération par la note moyenne et le nombre de votes.
        
        #### **4️⃣ L'application streamlit**
        
        La dernière étape a consisté à créer l'application Streamlit basée sur ce modèle de recommandation.
        
        - **Le modèle :** Intégration du modèle de recommandation avec joblib pour plus de rapidité dans la recherche de films similaires
        - **Les fonctionnalités :** 
            - Connexion à l'application
            - Page d'accueil qui présente les dernières nouveautés et des films au hasard
            - Recherche de films par filtres (genre, auteur, acteur, mots clefs, pays d'origine, décénie)
            - Page du film, détails et films les plus proches (recommandation)
            - Présentation et analyse globale de la base de données
        
        
        """)
    
    with st.container(key="tableau_de_bord_filmdatalab"):
        st.subheader("Aperçu de l'application")
        st.image("media/projets/filmdatalab/accueil.png")
    

# Séismes
with tab3:
    st.subheader("🌎 Mini-Projet : Séismes")
    with st.container(border=True):
        col1, col2 = st.columns(2)
        with col1:
            st.write("""
                ***Date de publication :** Février 2026*

                **Description :** Réalisation d'un tableau de bord pour analyser 200ans de séismes à l'échelle mondiale, en seulement deux jours

                **Technologies :** Python, Pandas, Power BI, DAX
                        """)
            if st.button("👉 Aperçu en bas de page", key="btn_apercu_seismes"):
                scroll_to_element("tableau_de_bord_seismes", alignment="start")
                st.rerun()
        with col2:
            st.image("media/projets/seismes/Geo_Vigie.jpg", width=400, caption="Organisme fictif (pour l'exemple)", )
            
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Contexte")
        
        st.write("""
            Le projet consistait à concevoir un rapport Power BI à partir de données réelles ou fictives, sur un thème libre, en un temps limité. 

            J’ai choisi d’explorer les données historiques de séismes enregistrés entre 1826 et 2026, pour un organisme international fictif chargé la 
            surveillance des risques naturels.
            
            L'objectif : mieux comprendre la répartition, l’évolution et les caractéristiques des séismes afin d’améliorer la prévention 
            et l’information du public.
            """)
        
    with col2:
        st.subheader("Le projet")
        st.write("""
            **Geo-Vigie**, organisme international de surveillance des risques naturels, souhaite disposer d'une vision claire et
            synthétique de l'activité sismique mondiale.
            
            La mission confiée : analyser une ensemble de données couvrant 200 ans d'évènements sismiques, identifier les tendances majeures,
            et mettre en avant les informations essentielles pour la prise de décision.
            """)
    
    
    st.divider()
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Objectifs du tableau de bord")
        st.write("""
            Avant de concevoir les visuels, il était essentiel de définir clairement ce que le tableau de bord devait permettre 
            de comprendre.
            
            L’objectif était de proposer une vue à la fois globale et précise de l’activité sismique mondiale, 
            en combinant des indicateurs descriptifs et une analyse spatio-temporelle.
            
            Ces objectifs ont guidé la structure du rapport et le choix des visualisations.

            1. **Analyse descriptive**
                - Fréquence des séismes
                - Distribution des magnitudes
                - Zones géographiques les plus actives
                - Profondeur des séismes
            2. **Analyse spatio-temporelle**
                - Clusters géographiques
                - Activité sismique par région
                - Identification de périodes atypiques

            """)
    with col2:
        st.subheader("Etapes de réalisation")
        st.write("""
            Avant de créer un tableau de bord, il est essentiel de comprendre et préparer les données. Ceci apporte une fiabilité des données et ..
            
            1. **Vérification de la qualité des données**
                - Nettoyage et traitement des dates
                - Filtrage des types de séismes pertinants
                - Harmonisation et simplification des noms de lieux  

            2. **Création de variables calculées**
                - Classification des magnitudes (Mineur, Léger, Modéré, Majeur, Destructeur...)
                - Classification des profondeurs (Superficiel, intermédiaire, profond)  
                
            3. **Construction du rapport Power BI**
                - Création de mesures DAX (nombre de séismes, magnitude moyenne...)
                - Conception des visuels et mise en forme du tableau de bord
        
            """)
    
    
    st.divider()
    
    with st.container(key="tableau_de_bord_seismes"):
        st.subheader("Tableau de bord Power BI")
        st.write("Ci-dessous les captures d’écrans du tableau de bord interactif : ")
        col1, col2 = st.columns(2)
        with col1:
            st.image('media/projets/seismes/capture1.png')
        with col2:
            st.image('media/projets/seismes/capture2.png')


if st.button("⬆️ Haut de page"):
    scroll_to_element("haut_de_page")
    st.rerun()
