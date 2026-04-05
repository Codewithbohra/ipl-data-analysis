import pandas as pd
import matplotlib.pyplot as plt

# Load data (FIXED PATH)
matches = pd.read_csv('data/matches.csv')
deliveries = pd.read_csv('data/deliveries.csv')

# Top teams
top_teams = matches['winner'].value_counts().head(5)
print("Top Teams:\n", top_teams)

top_teams.plot(kind='bar', title="Top 5 Teams by Wins")
plt.show()

# Top players
top_players = deliveries.groupby('batter')['batsman_runs'].sum().sort_values(ascending=False).head(5)
print("\nTop Players:\n", top_players)

top_players.plot(kind='bar', title="Top 5 Batsmen by Runs")
plt.show()

# Toss impact
toss_win_match_win = matches[matches['toss_winner'] == matches['winner']]
percentage = (len(toss_win_match_win) / len(matches)) * 100

print("\nToss win match win %:", percentage)

# Matches per season
matches_per_season = matches['season'].value_counts().sort_index()
matches_per_season.plot(title="Matches per Season")
plt.show()

# Top teams
top_teams = matches['winner'].value_counts().head(5)
top_teams.plot(kind='bar')
plt.show()


# ===== NEW ADVANCED CODE (YAHAN PASTE KAR) =====

# 1. Team Performance
team_season_wins = matches.groupby(['season', 'winner']).size().unstack().fillna(0)
team_season_wins.plot(figsize=(12,6))
plt.title("Team Performance Over Seasons")
plt.show()


# 2. Strike Rate
batsman_stats = deliveries.groupby('batter').agg({
    'batsman_runs': 'sum',
    'ball': 'count'
})

batsman_stats['strike_rate'] = (batsman_stats['batsman_runs'] / batsman_stats['ball']) * 100

top_sr = batsman_stats[batsman_stats['ball'] > 500].sort_values(by='strike_rate', ascending=False).head(5)
top_sr['strike_rate'].plot(kind='bar')
plt.show()


# 3. Bowlers
wickets = deliveries[deliveries['dismissal_kind'].notna()]
top_bowlers = wickets['bowler'].value_counts().head(5)
top_bowlers.plot(kind='bar')
plt.show()


# 4. Toss Decision
matches['toss_decision'].value_counts().plot(kind='pie', autopct='%1.1f%%')
plt.show()


# 5. Venue
matches['venue'].value_counts().head(10).plot(kind='bar')
plt.show()