import streamlit as st
import utils

utils.css_scroll_fluide()

st.markdown('<div id="haut_de_page" style="scroll-margin-top: 5rem;"></div>', unsafe_allow_html=True)

st.title("🚗 Toys & Models")
st.header("Analyse de performances commerciales")

with st.container(border=True):
    col1, col2 = st.columns(2)
    with col1:
        st.write("""
            ***Date de publication :** Octobre 2025*
            
            **Description :** Création d’un tableau de bord interactif de KPIs pour l’analyse et la visualisation 
            des performances d’une entreprise fictive de miniatures automobiles.
            
            **Technologies :**  SQL, Power BI, DAX
            
            **Catégorie :** Analyse & Insights
                    """)
        
        st.markdown('<a href="#tableau_de_bord_toysmodels" class="btn-scroll-custom">👉 Aperçu en bas de page</a>', unsafe_allow_html=True)
        
        
        
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
        **1. Variable ``mois_prec``**

        ``DATEADD`` décale le contexte de filtre d’un mois en arrière,
        et ``CALCULATE`` recalcule la mesure ``[Tot_ventes]`` avec ce nouveau contexte
        -> _Résultat : une valeur représentant le CA du mois N-1_

        **2. Le calcul du pourcentage d’évolution**

        On fait la différence entre le mois courant et le mois précédent, puis on divise par le mois précédent 
        pour obtenir le taux de variation.
        -> ``DIVIDE`` évite les erreurs en cas de division par zéro.

        Enfin, on multiplie par 100 pour obtenir un pourcentage
            """)

st.divider()
st.markdown('<div id="tableau_de_bord_toysmodels" style="scroll-margin-top: 5.5rem;"></div>', unsafe_allow_html=True)
st.subheader("Tableau de bord Power BI")
st.write("""
        Pour finir, voici une courte vidéo qui présente le tableau de bord final. 

        On y voit l’ensemble des KPIs, les filtres interactifs et les mesures dynamiques en action. 
        C’est le rendu complet du travail : un outil clair, réactif et pensé pour aider la dirigeante à prendre des décisions rapides et éclairées.
                """)
st.image("media/projets/toysmodels/Animation_toysmodels.gif")


st.markdown('<a href="#haut_de_page" class="btn-scroll-custom">⬆️ Haut de page</a>', unsafe_allow_html=True)