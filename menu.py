import streamlit as st

def show_menu():
    
    with st.sidebar:
        st.title("Kenji VICTOR")
        st.write("Data Analyste certifiée,")
        st.write("Aspirante Data Engineer")

        st.divider()

        st.page_link("main.py", label="Présentation", icon="🙋‍♀️")
        st.page_link("pages/projets_engineering.py", label="Projets Data Engineering", icon="📊")
        st.page_link("pages/projets_analisis.py", label="Projets Data Analisis", icon="📊")
        st.page_link("pages/competences.py", label="Compétences", icon="🛠️")
        
        st.divider()
        
        st.link_button("🔗 Retrouvez-moi sur LinkedIn !", "https://www.linkedin.com/in/kenji-victor/", type="tertiary")

