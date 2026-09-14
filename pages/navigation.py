import streamlit as st

def render_top_navbar(current_page="translator"):
    """Renders a consistent top navigation bar across pages."""
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("🏠 Home", use_container_width=True):
            st.switch_page("app.py")
    with col2:
        if st.button("📜 Project Mentors", use_container_width=True):
            st.switch_page("pages/Project_Mentors.py")
    with col3:
        if st.button("🌐 Translator Tool", use_container_width=True):
            st.switch_page("pages/translator.py")
    st.markdown("---")
