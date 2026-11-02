import streamlit as st
import utils

utils.css_scroll_fluide()



st.markdown('<div id="haut_de_page" style="scroll-margin-top: 5rem;"></div>', unsafe_allow_html=True)
st.title("🎞️ Film Data Lab")
st.header("Application de recommandation")

with st.container(border=True):
    col1, col2 = st.columns(2)
    with col1:
        st.write("""
            ***Date de publication :** Janvier 2026*

            **Description :** Analyse d'une base de données de plus 6M de lignes et création d’une application basée sur un modèle de recommandation de films.

            **Technologies :** Python, Pandas, DuckDB, Seaborn, Streamlit, ScikitLearn (Machine Learning), API
            
            **Catégorie :** Analyse & Insights
                """)
        st.link_button("Voir le projet sur GitHub", "https://github.com/kenjivictor/projet_recommandation_films", icon="🔗")
        
        st.markdown('<a href="#tableau_de_bord_filmdatalab" class="btn-scroll-custom">👉 Aperçu en bas de page</a>', unsafe_allow_html=True, width="content")
        
    with col2:
        st.image("media/projets/filmdatalab/accueil.png", width=400)
        st.link_button("Live Démo", "https://filmdatalab.streamlit.app/", icon="🔗")
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

st.markdown('<div id="tableau_de_bord_filmdatalab" style="scroll-margin-top: 5.5rem;"></div>', unsafe_allow_html=True)
st.subheader("Aperçu de l'application")
st.image("media/projets/filmdatalab/accueil.png")



st.markdown('<a href="#haut_de_page" class="btn-scroll-custom">⬆️ Haut de page</a>', unsafe_allow_html=True)