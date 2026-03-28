import streamlit as st
from utils.data_loader import load_matches_data
from utils.translations import get_text


def highlight_team(row):
    """Highlight the selected team only in the corresponding table cell."""
    team = st.session_state.selected_team
    styles = [""] * len(row)

    if team == "ALL_TEAMS":
        return styles

    home_team_label = get_text("home_team", st.session_state.language)
    away_team_label = get_text("away_team", st.session_state.language)

    if row[home_team_label] == team:
        col_index = row.index.get_loc(home_team_label)
        styles[col_index] = "background-color: #FFF3B0; color: black; font-weight: bold"

    if row[away_team_label] == team:
        col_index = row.index.get_loc(away_team_label)
        styles[col_index] = "background-color: #FFF3B0; color: black; font-weight: bold"

    return styles


def update_matches_filters():
    """Sync match filter widgets with global session state."""
    team_value = st.session_state.matches_team_widget
    round_value = st.session_state.matches_round_widget

    all_teams_label = get_text("all_teams", st.session_state.language)
    all_rounds_label = get_text("all_rounds", st.session_state.language)

    st.session_state.selected_team = "ALL_TEAMS" if team_value == all_teams_label else team_value
    st.session_state.selected_round = "ALL_ROUNDS" if round_value == all_rounds_label else round_value


def show_matches():
    """Render the matches view with team and round filters."""
    lang = st.session_state.language

    st.title(get_text("matches_title", lang))

    df = load_matches_data()

    teams = sorted(set(df["Home Team"]).union(set(df["Away Team"])))
    rounds = sorted(df["Round Number"].unique())

    all_teams_label = get_text("all_teams", lang)
    all_rounds_label = get_text("all_rounds", lang)

    team_options = [all_teams_label] + teams
    round_options = [all_rounds_label] + list(rounds)

    default_team = (
        all_teams_label
        if st.session_state.selected_team == "ALL_TEAMS"
        else st.session_state.selected_team
    )
    default_round = (
        all_rounds_label
        if st.session_state.selected_round == "ALL_ROUNDS"
        else st.session_state.selected_round
    )

    if "matches_team_widget" not in st.session_state:
        st.session_state.matches_team_widget = default_team

    if "matches_round_widget" not in st.session_state:
        st.session_state.matches_round_widget = default_round

    if st.session_state.matches_team_widget not in team_options:
        st.session_state.matches_team_widget = default_team

    if st.session_state.matches_round_widget not in round_options:
        st.session_state.matches_round_widget = default_round

    filter_col1, filter_col2 = st.columns(2)

    with filter_col1:
        st.selectbox(
            get_text("select_team", lang),
            team_options,
            key="matches_team_widget",
            on_change=update_matches_filters,
        )

    with filter_col2:
        st.selectbox(
            get_text("select_round", lang),
            round_options,
            key="matches_round_widget",
            on_change=update_matches_filters,
        )

    selected_team = st.session_state.selected_team
    selected_round = st.session_state.selected_round

    filtered_df = df.copy()

    if selected_team != "ALL_TEAMS":
        filtered_df = filtered_df[
            (filtered_df["Home Team"] == selected_team) |
            (filtered_df["Away Team"] == selected_team)
        ]

    if selected_round != "ALL_ROUNDS":
        filtered_df = filtered_df[
            filtered_df["Round Number"] == selected_round
        ]

    filtered_df = filtered_df.sort_values(by=["Round Number", "Date"]).reset_index(drop=True)

    info_col1, info_col2, info_col3 = st.columns(3)

    with info_col1:
        st.metric(
            get_text("results_summary", lang),
            len(filtered_df)
        )

    with info_col2:
        if selected_team != "ALL_TEAMS":
            st.metric(get_text("selected_team", lang), selected_team)
        else:
            st.metric(get_text("selected_team", lang), all_teams_label)

    with info_col3:
        if selected_round != "ALL_ROUNDS":
            st.metric(get_text("selected_round", lang), selected_round)
        else:
            st.metric(get_text("selected_round", lang), all_rounds_label)

    status_col1, status_col2 = st.columns(2)

    with status_col1:
        if selected_team != "ALL_TEAMS":
            st.info(f"{get_text('selected_team', lang)}: {selected_team}")
        else:
            st.info(get_text("showing_all_teams", lang))

    with status_col2:
        if selected_round != "ALL_ROUNDS":
            st.info(f"{get_text('selected_round', lang)}: {selected_round}")
        else:
            st.info(get_text("showing_all_rounds", lang))

    st.subheader(get_text("filtered_matches", lang))
    st.write(get_text("matches_count", lang, count=len(filtered_df)))

    display_df = filtered_df[
        ["Round Number", "Date", "Home Team", "Away Team", "Result", "Location"]
    ].copy()

    display_df.columns = [
        get_text("round", lang),
        get_text("date", lang),
        get_text("home_team", lang),
        get_text("away_team", lang),
        get_text("result", lang),
        get_text("stadium", lang),
    ]

    styled_matches = display_df.style.apply(highlight_team, axis=1)

    st.dataframe(styled_matches, width="stretch")