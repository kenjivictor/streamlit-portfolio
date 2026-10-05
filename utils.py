import streamlit as st



# CSS global : scroll fluide + style du bouton ancré
# ex : scroll vers le haut de page
def css_scroll_fluide():
    st.markdown(
        """
        <style>
        /* Scroll fluide au niveau du conteneur Streamlit */
        html, body, 
        [data-testid="stAppViewContainer"],
        [data-testid="stMain"],
        .main {
            scroll-behavior: smooth !important;
        }
        
        /* Style pour transformer le lien HTML en bouton identique à Streamlit */
        .btn-scroll-custom {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            padding: 0.5rem 0.9rem;
            border-radius: 8px;
            text-decoration: none !important;
            font-weight: 400;
            font-size: 0.9rem;
            cursor: pointer;
            transition: background-color 0.2s, border-color 0.2s, color 0.2s;
            
            /* Récupération dynamique des couleurs du thème actif */
            background-color: var(--background-color);
            color: var(--text-color) !important;
            border: 1px solid rgba(128, 128, 128, 0.3);
            font-family: var(--font);
        }
        .btn-scroll-custom:hover {
            background-color: rgba(172, 177, 195, 0.15);
        }
        
        </style>
        """,
        unsafe_allow_html=True
    )