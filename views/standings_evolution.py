import streamlit as st
import plotly.express as px

from utils.data_loader import load_matches_data
from utils.standings_utils import calculate_standings_until_round
from utils.translations import get_text


def highlight_rows(row):
    """Highlight relevant rows in the standings table."""
    selected_team = st.session_state.selected_team

    if row["Team"] == selected_team:
        return ["background-color: #FFF3B0; color: black; font-weight: bold"] * len(row)

    if row.name < 4:
        return ["background-color: #D6F5D6; color: black"] * len(row)

    if row.name >= len(st.session_state.evolution_standings) - 3:
        return ["background-color: #FFD6D6; color: black"] * len(row)

    return [""] * len(row)


def show_standings_evolution():
    """Render the standings evolution view for a selected round."""
    lang = st.session_state.language

    st.title(get_text("evolution_title", lang))

    df = load_matches_data()
    rounds = sorted(df["Round Number"].unique())

    selected_round = st.selectbox(
        get_text("select_round", lang),
        rounds,
        index=len(rounds) - 1
    )

    standings = calculate_standings_until_round(df, selected_round)
    st.session_state.evolution_standings = standings

    if st.session_state.selected_team != "ALL_TEAMS":
        st.info(get_text("selected_team_info", lang, team=st.session_state.selected_team))

    styled_table = standings.style.apply(highlight_rows, axis=1)

    st.subheader(get_text("standings_until_selected_round", lang, round=selected_round))
    st.dataframe(styled_table, use_container_width=True)

    st.subheader(get_text("points_until_selected_round", lang))

    fig = px.bar(
        standings,
        x="Team",
        y="Points",
        text="Points"
    )

    fig.update_traces(
        textposition="outside",
        textfont_color="#FFFFFF",
        marker_line_width=0
    )

    fig.update_layout(
        xaxis_title=get_text("team_axis", lang),
        yaxis_title=get_text("points", lang),
        xaxis_tickangle=-45,
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        height=520,
        margin=dict(t=20, b=20, l=20, r=20),
        font=dict(color="#FFFFFF"),
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