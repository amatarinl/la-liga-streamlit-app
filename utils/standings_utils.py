import pandas as pd
from utils.match_utils import parse_result


def calculate_standings(df):
    """
    Calculate league standings from the match results dataset.

    The table includes:
    matches played, wins, draws, losses,
    goals scored, goals conceded, goal difference, and points.
    """
    # Build the full list of teams appearing in the dataset
    teams = sorted(set(df["Home Team"]).union(set(df["Away Team"])))

    table = []

    # Compute stats team by team
    for team in teams:
        home_matches = df[df["Home Team"] == team]
        away_matches = df[df["Away Team"] == team]

        matches_played = len(home_matches) + len(away_matches)

        wins = 0
        draws = 0
        losses = 0
        goals_for = 0
        goals_against = 0

        # Process home matches
        for _, match in home_matches.iterrows():
            home_goals, away_goals = parse_result(match["Result"])

            goals_for += home_goals
            goals_against += away_goals

            if home_goals > away_goals:
                wins += 1
            elif home_goals == away_goals:
                draws += 1
            else:
                losses += 1

        # Process away matches
        for _, match in away_matches.iterrows():
            home_goals, away_goals = parse_result(match["Result"])

            goals_for += away_goals
            goals_against += home_goals

            if away_goals > home_goals:
                wins += 1
            elif away_goals == home_goals:
                draws += 1
            else:
                losses += 1

        # Standard football scoring system
        points = wins * 3 + draws

        table.append({
            "Team": team,
            "PJ": matches_played,
            "G": wins,
            "E": draws,
            "P": losses,
            "GF": goals_for,
            "GC": goals_against,
            "DG": goals_for - goals_against,
            "Points": points
        })

    standings_df = pd.DataFrame(table)

    # Sort the table by points, goal difference, and goals scored
    standings_df = standings_df.sort_values(
        by=["Points", "DG", "GF"],
        ascending=False
    ).reset_index(drop=True)

    # Start ranking from 1 instead of 0
    standings_df.index += 1

    return standings_df


def calculate_standings_until_round(df, round_number):
    """
    Calculate standings using only matches played
    up to a specific round number.
    """
    filtered_df = df[df["Round Number"] <= round_number].copy()
    return calculate_standings(filtered_df)