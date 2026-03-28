import streamlit as st

from views.home import show_home
from views.matches import show_matches
from views.standings import show_standings
from views.compare_teams import show_compare_teams
from views.standings_evolution import show_standings_evolution
from views.team_dashboard import show_team_dashboard
from utils.translations import get_text
from utils.styles import inject_global_styles


st.set_page_config(
    page_title="La Liga Streamlit App",
    page_icon="⚽",
    layout="wide",
    initial_sidebar_state="expanded"
)


def initialize_session_state():
    st.session_state.setdefault("selected_team", "ALL_TEAMS")
    st.session_state.setdefault("selected_round", "ALL_ROUNDS")
    st.session_state.setdefault("team_a", None)
    st.session_state.setdefault("team_b", None)
    st.session_state.setdefault("language", "es")
    st.session_state.setdefault("current_page", "home")
    st.session_state.setdefault("_language_widget", st.session_state.language)


def sync_language():
    st.session_state.language = st.session_state._language_widget


def main():
    initialize_session_state()
    inject_global_styles()

    language_options = {
        "es": "🇪🇸 Español",
        "en": "🇬🇧 English",
    }

    lang = st.session_state.language

    st.sidebar.markdown("## ⚽ La Liga App")
    st.sidebar.caption("Streamlit project portfolio")

    st.sidebar.selectbox(
        get_text("language_selector", lang),
        options=list(language_options.keys()),
        format_func=lambda key: language_options[key],
        key="_language_widget",
        on_change=sync_language,
    )

    lang = st.session_state.language

    st.sidebar.markdown("---")
    st.sidebar.subheader(get_text("menu_title", lang))

    page_definitions = {
        "home": {
            "label": get_text("home", lang),
            "view": show_home
        },
        "matches": {
            "label": get_text("matches", lang),
            "view": show_matches
        },
        "standings": {
            "label": get_text("standings", lang),
            "view": show_standings
        },
        "compare": {
            "label": get_text("compare", lang),
            "view": show_compare_teams
        },
        "evolution": {
            "label": get_text("evolution", lang),
            "view": show_standings_evolution
        },
        "team_dashboard": {
            "label": get_text("team_dashboard", lang),
            "view": show_team_dashboard
        },
    }

    page_keys = list(page_definitions.keys())

    selected_page = st.sidebar.radio(
        get_text("page_selector", lang),
        page_keys,
        index=page_keys.index(st.session_state.current_page),
        format_func=lambda key: page_definitions[key]["label"],
    )

    st.session_state.current_page = selected_page

    page_definitions[st.session_state.current_page]["view"]()


if __name__ == "__main__":
    main()