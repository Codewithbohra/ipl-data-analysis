import streamlit as st
import pandas as pd

# Page config
st.set_page_config(page_title="IPL Dashboard", layout="wide")

# Title
st.markdown("<h1 style='text-align: center; color: #00ADB5;'>🏏 IPL Data Analysis Dashboard</h1>", unsafe_allow_html=True)

# Load data
matches = pd.read_csv('data/matches.csv')
deliveries = pd.read_csv('data/deliveries.csv')

# Sidebar
st.sidebar.header("Filters")
season = st.sidebar.selectbox("Select Season", sorted(matches['season'].unique()))
team = st.sidebar.selectbox("Select Team", sorted(matches['team1'].unique()))

filtered_matches = matches[(matches['season'] == season) & 
                           ((matches['team1'] == team) | (matches['team2'] == team))]

# KPIs
col1, col2, col3 = st.columns(3)

col1.metric("Total Matches", len(filtered_matches))
col2.metric("Total Teams", matches['team1'].nunique())
col3.metric("Selected Season", season)

st.markdown("---")

# Top Teams
st.subheader("🏆 Top Teams by Wins")
top_teams = matches['winner'].value_counts().head(5)
st.bar_chart(top_teams)

# Top Batsmen
st.subheader("🔥 Top Batsmen")
top_players = deliveries.groupby('batter')['batsman_runs'].sum().sort_values(ascending=False).head(5)
st.bar_chart(top_players)

# Top Bowlers
st.subheader("🎯 Top Bowlers")
wickets = deliveries[deliveries['dismissal_kind'].notna()]
top_bowlers = wickets['bowler'].value_counts().head(5)
st.bar_chart(top_bowlers)

# Toss Impact
st.subheader("🪙 Toss Impact")
toss_win = matches[matches['toss_winner'] == matches['winner']]
percentage = (len(toss_win) / len(matches)) * 100
st.metric("Toss Win → Match Win %", f"{percentage:.2f}%")

# Matches per Season
st.subheader("📈 Matches per Season")
matches_per_season = matches['season'].value_counts().sort_index()
st.line_chart(matches_per_season) 

# Team vs Team
st.subheader("⚔️ Team vs Team")

team1 = st.selectbox("Team 1", matches['team1'].unique())
team2 = st.selectbox("Team 2", matches['team1'].unique())

vs_matches = matches[((matches['team1'] == team1) & (matches['team2'] == team2)) |
                     ((matches['team1'] == team2) & (matches['team2'] == team1))]

st.write(f"Total Matches: {len(vs_matches)}")
st.write(vs_matches['winner'].value_counts())