import streamlit as st
import utils

utils.css_scroll_fluide()



st.markdown('<div id="haut_de_page" style="scroll-margin-top: 5rem;"></div>', unsafe_allow_html=True)

st.title("🌎 Séismes")
st.header("Analyse mondiale sur 200ans")


with st.container(border=True):
    col1, col2 = st.columns(2)
    with col1:
        st.write("""
                ***Date de publication :** Février 2026*

                **Description :** Réalisation d'un tableau de bord pour analyser 200ans de séismes à l'échelle mondiale, en seulement deux jours

                **Technologies :** Python, Pandas, Power BI, DAX
            
                **Catégorie :** Analyse & Insights
                        """)
        st.markdown('<a href="#tableau_de_bord_seismes" class="btn-scroll-custom">👉 Aperçu en bas de page</a>', unsafe_allow_html=True, width="content")

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

st.markdown('<div id="tableau_de_bord_seismes" style="scroll-margin-top: 5.5rem;"></div>', unsafe_allow_html=True)

st.subheader("Tableau de bord Power BI")
st.write("Ci-dessous les captures d’écrans du tableau de bord interactif : ")
col1, col2 = st.columns(2)
with col1:
    st.image('media/projets/seismes/capture1.png')
with col2:
    st.image('media/projets/seismes/capture2.png')



st.markdown('<a href="#haut_de_page" class="btn-scroll-custom">⬆️ Haut de page</a>', unsafe_allow_html=True)