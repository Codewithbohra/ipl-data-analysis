import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("🏏 IPL Data Analysis Dashboard")

# Load data
matches = pd.read_csv('data/matches.csv')
deliveries = pd.read_csv('data/deliveries.csv')

# Sidebar filter
season = st.sidebar.selectbox("Select Season", sorted(matches['season'].unique()))
filtered_matches = matches[matches['season'] == season]

# Top Teams
st.subheader("Top Teams by Wins")
top_teams = filtered_matches['winner'].value_counts().head(5)
st.bar_chart(top_teams)

# Top Batsmen
st.subheader("Top Batsmen")
top_players = deliveries.groupby('batter')['batsman_runs'].sum().sort_values(ascending=False).head(5)
st.bar_chart(top_players)

# Toss Impact
st.subheader("Toss Impact")
toss_win = matches[matches['toss_winner'] == matches['winner']]
percentage = (len(toss_win) / len(matches)) * 100
st.write(f"Toss win match win %: {percentage:.2f}%")

# Matches per Season
st.subheader("Matches per Season")
matches_per_season = matches['season'].value_counts().sort_index()
st.line_chart(matches_per_season)