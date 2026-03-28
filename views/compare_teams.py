import streamlit as st

from utils.data_loader import load_matches_data
from utils.standings_utils import calculate_standings
from utils.translations import get_text


def show_compare_teams():
    """Render the team comparison view."""
    lang = st.session_state.language

    st.title(get_text("compare_title", lang))

    # Load match data and compute standings to obtain team statistics
    df = load_matches_data()
    standings = calculate_standings(df)

    teams = standings["Team"].tolist()

    # Use the globally selected team as the default first option when possible
    default_team_a = (
        st.session_state.selected_team
        if st.session_state.selected_team in teams
        else teams[0]
    )
    default_team_b = teams[1] if len(teams) > 1 and teams[1] != default_team_a else teams[0]

    col1, col2 = st.columns(2)

    with col1:
        team_a = st.selectbox(
            get_text("team_1", lang),
            teams,
            index=teams.index(default_team_a)
        )

    with col2:
        team_b = st.selectbox(
            get_text("team_2", lang),
            teams,
            index=teams.index(default_team_b)
        )

    # Store both selected teams in session state
    st.session_state.team_a = team_a
    st.session_state.team_b = team_b

    # Prevent comparing the same team against itself
    if team_a == team_b:
        st.warning(get_text("select_different_teams", lang))
        return

    # Extract precomputed stats for both selected teams
    team_a_stats = standings[standings["Team"] == team_a].iloc[0]
    team_b_stats = standings[standings["Team"] == team_b].iloc[0]

    st.subheader(get_text("comparison_summary", lang))

    col1, col2 = st.columns(2)

    with col1:
        st.markdown(f"### {team_a}")
        st.metric(get_text("points", lang), team_a_stats["Points"])
        st.metric(get_text("matches_played", lang), team_a_stats["PJ"])
        st.metric(get_text("wins", lang), team_a_stats["G"])
        st.metric(get_text("draws", lang), team_a_stats["E"])
        st.metric(get_text("losses", lang), team_a_stats["P"])
        st.metric(get_text("goals_for", lang), team_a_stats["GF"])
        st.metric(get_text("goals_against", lang), team_a_stats["GC"])
        st.metric(get_text("goal_difference", lang), team_a_stats["DG"])

    with col2:
        st.markdown(f"### {team_b}")
        st.metric(get_text("points", lang), team_b_stats["Points"])
        st.metric(get_text("matches_played", lang), team_b_stats["PJ"])
        st.metric(get_text("wins", lang), team_b_stats["G"])
        st.metric(get_text("draws", lang), team_b_stats["E"])
        st.metric(get_text("losses", lang), team_b_stats["P"])
        st.metric(get_text("goals_for", lang), team_b_stats["GF"])
        st.metric(get_text("goals_against", lang), team_b_stats["GC"])
        st.metric(get_text("goal_difference", lang), team_b_stats["DG"])

    st.subheader(get_text("compare_better", lang))

    # Compare a small set of key metrics and generate text insights
    comparison_data = [
        (get_text("points", lang), team_a_stats["Points"], team_b_stats["Points"]),
        (get_text("wins", lang), team_a_stats["G"], team_b_stats["G"]),
        (get_text("goals_for", lang), team_a_stats["GF"], team_b_stats["GF"]),
        (get_text("goal_difference", lang), team_a_stats["DG"], team_b_stats["DG"]),
    ]

    for label, value_a, value_b in comparison_data:
        if value_a > value_b:
            st.write(
                get_text(
                    "compare_better_team",
                    lang,
                    label=label,
                    team_a=team_a,
                    team_b=team_b,
                    value_a=value_a,
                    value_b=value_b,
                )
            )
        elif value_b > value_a:
            st.write(
                get_text(
                    "compare_better_team",
                    lang,
                    label=label,
                    team_a=team_b,
                    team_b=team_a,
                    value_a=value_b,
                    value_b=value_a,
                )
            )
        else:
            st.write(get_text("compare_tie", lang, label=label, value=value_a))

    st.subheader(get_text("head_to_head", lang))

    # Filter direct matches between the two selected teams
    h2h = df[
        ((df["Home Team"] == team_a) & (df["Away Team"] == team_b)) |
        ((df["Home Team"] == team_b) & (df["Away Team"] == team_a))
    ].copy()

    if not h2h.empty:
        st.dataframe(h2h, use_container_width=True)
    else:
        st.write(get_text("no_head_to_head", lang))