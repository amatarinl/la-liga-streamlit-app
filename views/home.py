import streamlit as st
from utils.translations import get_text


def feature_card(icon, title, text):
    st.markdown(
        f"""
        <div class="feature-card">
            <div class="feature-title">{icon} {title}</div>
            <div class="feature-text">{text}</div>
        </div>
        """,
        unsafe_allow_html=True
    )


def section_card(title, text):
    st.markdown(
        f"""
        <div class="section-card">
            <div class="section-title">{title}</div>
            <div class="section-text">{text}</div>
        </div>
        """,
        unsafe_allow_html=True
    )


def show_home():
    lang = st.session_state.language

    st.markdown(
        f"""
        <div class="hero-card">
            <div class="hero-title">⚽ La Liga Streamlit App</div>
            <div class="hero-subtitle">{get_text("home_subtitle", lang)}</div>
            <div>
                <span class="hero-badge">Streamlit</span>
                <span class="hero-badge">Pandas</span>
                <span class="hero-badge">Plotly</span>
                <span class="hero-badge">Session State</span>
                <span class="hero-badge">Bilingual UI</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(f"## {get_text('what_can_you_do', lang)}")

    col1, col2, col3 = st.columns(3)
    with col1:
        feature_card("📅", get_text("matches", lang), get_text("home_matches_desc", lang))
    with col2:
        feature_card("🏆", get_text("standings", lang), get_text("home_standings_desc", lang))
    with col3:
        feature_card("🔍", get_text("compare", lang), get_text("home_compare_desc", lang))

    col4, col5 = st.columns(2)
    with col4:
        feature_card("📈", get_text("evolution", lang), get_text("home_evolution_desc", lang))
    with col5:
        feature_card("📊", get_text("team_dashboard", lang), get_text("home_team_dashboard_desc", lang))

    st.markdown("### Project overview")

    col6, col7 = st.columns(2)

    with col6:
        section_card(get_text("dataset_used", lang), get_text("dataset_description", lang))
        section_card(get_text("navigation", lang), get_text("navigation_description", lang))

    with col7:
        section_card(get_text("language_selector", lang), get_text("language_description", lang))
        section_card("Tech stack", "Streamlit, Pandas and Plotly were used to build a modular interactive dashboard with reusable views and shared session state.")

    st.markdown("### Session status")

    if st.session_state.selected_team != "ALL_TEAMS":
        st.success(get_text("current_selected_team", lang, team=st.session_state.selected_team))
    else:
        st.info(get_text("no_selected_team", lang))