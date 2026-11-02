import streamlit as st

st.set_page_config(page_title="Kenji VICTOR - Experte Data analisis", page_icon="📊", initial_sidebar_state="expanded", layout="wide")


# --- Pages pour la sidebar personnalisée ---
pages = {
    "" : [
        ("pages/presentation.py", "Présentation", "🙋‍♀️"),
        ("pages/competences.py", "Compétences", "🛠️"),
    ],
    "Projets Analyse & Insights": [
        ("pages/projets/analisis/seismes.py", "Séismes", "🌎"),
        ("pages/projets/analisis/film_data_lab.py", "Film Data Lab", "🎞️"),
        ("pages/projets/analisis/toys_models.py", "Toys & Models", "🚗"),
    ],
    "Projets Ingénierie & Architecture": [
        ("pages/projets/engineering/fraude.py", "Fraude bancaire", "💵"),
    ],
}

# --- Structure pour st.navigation (n'accepte que des st.Page) ---
nav_pages = {
    group: [
        st.Page(path, title=label, icon=icon)
        for (path, label, icon) in items
    ]
    for group, items in pages.items()
}


# --- NAVIGATION (cachée) ---
pg = st.navigation(nav_pages, position="hidden")
pg.run()   # <<< IMPORTANT : charge la page courante AVANT la sidebar

# --- Sidebar ---
with st.sidebar:
    st.markdown("### Kenji VICTOR")
    st.write("Data Analyste certifiée")
    st.divider()

    for group, items in pages.items():
        if group:
            st.markdown(f"#### {group}")

        for path, label, icon in items:
            st.page_link(path, label=label, icon=icon)

    st.divider()
    st.link_button("🔗 :red[Retrouvez-moi sur LinkedIn !]", "https://www.linkedin.com/in/kenji-victor/", type="tertiary")
    st.link_button("🔗 :red[Mes projets sur GitHub !]", "https://github.com/kenjivictor", type="tertiary")
