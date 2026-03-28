import streamlit as st
import plotly.express as px

from utils.data_loader import load_matches_data
from utils.standings_utils import calculate_standings
from utils.translations import get_text


def highlight_rows(row):
    """Highlight the selected team, top 4 teams, and relegation zone."""
    selected_team = st.session_state.selected_team

    if row["Team"] == selected_team:
        return ["background-color: #FFF3B0; color: black; font-weight: bold"] * len(row)

    if row.name < 4:
        return ["background-color: #D6F5D6; color: black"] * len(row)

    if row.name >= len(st.session_state.standings) - 3:
        return ["background-color: #FFD6D6; color: black"] * len(row)

    return [""] * len(row)


def show_standings():
    """Render the main league standings view."""
    lang = st.session_state.language

    st.title(get_text("standings_title", lang))

    # Load match data and compute full-season standings
    df = load_matches_data()
    standings = calculate_standings(df)

    st.session_state.standings = standings

    if st.session_state.selected_team != "ALL_TEAMS":
        st.info(get_text("selected_team_info", lang, team=st.session_state.selected_team))

    styled_table = standings.style.apply(highlight_rows, axis=1)
    st.dataframe(styled_table, use_container_width=True)

    st.subheader(get_text("points_by_team", lang))

    fig = px.bar(
        standings,
        x="Team",
        y="Points",
        text="Points"
    )

    #
    fig.update_traces(
        textposition="outside",
        marker_line_width=0
    )

    fig.update_layout(
        xaxis_title=get_text("team_axis", lang),
        yaxis_title=get_text("points", lang),
        xaxis_tickangle=-45,
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        height=520,
        font=dict(color="white"),
        xaxis=dict(
            title_font=dict(color="#FFFFFF"),
            tickfont=dict(color="#FFFFFF")
        ),
        yaxis=dict(
            title_font=dict(color="#FFFFFF"),
            tickfont=dict(color="#FFFFFF")
        )
        
    )

    st.plotly_chart(fig, use_container_width=True)
