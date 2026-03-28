import streamlit as st
import plotly.express as px
import pandas as pd

from utils.data_loader import load_matches_data
from utils.match_utils import (
    get_team_matches,
    get_team_home_matches,
    get_team_away_matches,
    parse_result,
)
from utils.translations import get_text


def calculate_team_stats(df, team_name):
    """
    Calculate basic season statistics for a selected team.
    """
    matches = get_team_matches(df, team_name)
    home_matches = get_team_home_matches(df, team_name)
    away_matches = get_team_away_matches(df, team_name)

    wins = draws = losses = 0
    goals_for = goals_against = 0

    for _, row in matches.iterrows():
        home_goals, away_goals = parse_result(row["Result"])

        if row["Home Team"] == team_name:
            goals_for += home_goals
            goals_against += away_goals

            if home_goals > away_goals:
                wins += 1
            elif home_goals == away_goals:
                draws += 1
            else:
                losses += 1
        else:
            goals_for += away_goals
            goals_against += home_goals

            if away_goals > home_goals:
                wins += 1
            elif away_goals == home_goals:
                draws += 1
            else:
                losses += 1

    return {
        "matches_played": len(matches),
        "wins": wins,
        "draws": draws,
        "losses": losses,
        "goals_for": goals_for,
        "goals_against": goals_against,
        "home_matches": len(home_matches),
        "away_matches": len(away_matches),
    }


def update_selected_team_from_dashboard():
    """Sync the dashboard widget value with the global selected team."""
    st.session_state.selected_team = st.session_state.team_dashboard_widget


def show_team_dashboard():
    """
    Render the team performance dashboard view.
    """
    lang = st.session_state.language

    st.title(get_text("team_dashboard_title", lang))

    df = load_matches_data()
    teams = sorted(set(df["Home Team"]).union(set(df["Away Team"])))

    default_team = (
        st.session_state.selected_team
        if st.session_state.selected_team in teams
        else teams[0]
    )

    # Initialize widget state only once
    if "team_dashboard_widget" not in st.session_state:
        st.session_state.team_dashboard_widget = default_team

    # Only repair invalid values, do not overwrite every rerun
    if st.session_state.team_dashboard_widget not in teams:
        st.session_state.team_dashboard_widget = default_team

    st.selectbox(
        get_text("team_dashboard_select", lang),
        teams,
        key="team_dashboard_widget",
        on_change=update_selected_team_from_dashboard,
    )

    selected_team = st.session_state.team_dashboard_widget

    stats = calculate_team_stats(df, selected_team)

    st.subheader(get_text("team_summary", lang, team=selected_team))

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(get_text("matches_played", lang), stats["matches_played"])
    with col2:
        st.metric(get_text("wins", lang), stats["wins"])
    with col3:
        st.metric(get_text("draws", lang), stats["draws"])
    with col4:
        st.metric(get_text("losses", lang), stats["losses"])

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(get_text("goals_for", lang), stats["goals_for"])
    with col2:
        st.metric(get_text("goals_against", lang), stats["goals_against"])
    with col3:
        st.metric(get_text("home_matches", lang), stats["home_matches"])
    with col4:
        st.metric(get_text("away_matches", lang), stats["away_matches"])

    chart_df = pd.DataFrame({
        get_text("metric", lang): [
            get_text("wins_label", lang),
            get_text("draws_label", lang),
            get_text("losses_label", lang),
        ],
        get_text("value", lang): [stats["wins"], stats["draws"], stats["losses"]],
    })

    st.subheader(get_text("results_distribution_chart", lang))

    fig = px.pie(
        chart_df,
        names=get_text("metric", lang),
        values=get_text("value", lang),
        hole=0.4,
    )

    fig.update_layout(
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        height=420,
        margin=dict(t=20, b=20, l=20, r=20),
        font=dict(color="#FFFFFF"),
        legend=dict(font=dict(color="#FFFFFF"))
    )

    st.plotly_chart(fig, use_container_width=True)

    goals_df = pd.DataFrame({
        get_text("metric", lang): [
            get_text("gf_label", lang),
            get_text("ga_label", lang),
        ],
        get_text("value", lang): [stats["goals_for"], stats["goals_against"]],
    })

    st.subheader(get_text("goal_balance_chart", lang))

    fig2 = px.bar(
        goals_df,
        x=get_text("metric", lang),
        y=get_text("value", lang),
        text=get_text("value", lang),
    )

    fig2.update_layout(
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        height=420,
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

    st.plotly_chart(fig2, use_container_width=True)