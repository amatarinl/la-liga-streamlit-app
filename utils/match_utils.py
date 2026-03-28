def get_team_matches(df, team_name):
    """
    Return all matches played by a given team,
    either as home team or away team.
    """
    return df[(df["Home Team"] == team_name) | (df["Away Team"] == team_name)]


def get_team_home_matches(df, team_name):
    """
    Return all matches where the selected team played at home.
    """
    return df[df["Home Team"] == team_name]


def get_team_away_matches(df, team_name):
    """
    Return all matches where the selected team played away.
    """
    return df[df["Away Team"] == team_name]

def parse_result(result):
    """
    Split a match result string such as '2-1'
    into home goals and away goals.
    """
    home_goals, away_goals = map(int, result.split("-"))
    return home_goals, away_goals