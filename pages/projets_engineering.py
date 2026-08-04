import streamlit as st
from menu import show_menu

show_menu()

def set_wide():
    st.markdown(
        """
        <style>
            .main {
                max-width: 100% !important;
                padding-left: 2rem;
                padding-right: 2rem;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

set_wide()

st.title('Mes projets Data')
st.subheader("Ingénierie & Architecture")


tab1, = st.tabs(["💵 Détection de fraude bancaire"])

with tab1:
    st.header("💵 Détection de fraude bancaire")
    with st.container(border=True):
        st.markdown("""
                    ***Date de publication :** Février 2026*

**Description** : Système de simulation de détection de fraude en temps réel avec amélioration continue et monitoring du système

**Technologies** : Python, Pandas, Docker, Streamlit, XGBoost (Machine Learning), FastAPI, Grafana, Redis, Prefect, BigQuery (Google Cloud Platform)
                    """)
        st.link_button("Voir le projet sur GitHub", "https://github.com/kenjivictor/projet_fraude_cb", icon="👉")
    
