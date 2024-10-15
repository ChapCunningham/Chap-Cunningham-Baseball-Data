import streamlit as st
import pandas as pd
import plotly.express as px

# Sample data, replace this with your actual DataFrame
# df2024 = pd.read_csv('your_data_file.csv')

df2024 = pd.read_csv('/Users/chap/Documents/pybaseball Projects/pybaseball/pitcherapp_statcast_2024.csv')
# Title of the app
st.title("Pitch Movement Visualization")

# Dropdown to select player
players = df2024['player_name'].unique()
selected_player = st.selectbox('Select a player:', players)

# Filter data for the selected player
player_data = df2024[df2024['player_name'] == selected_player]

# Create the scatter plot using Plotly Express
fig = px.scatter(
    player_data,
    x='pfx_x',
    y='pfx_z',
    color='pitch_type',
    title=f'{selected_player} Pitch Movement',
    labels={'pfx_x': 'Horizontal Movement (pfx_x)', 'pfx_z': 'Vertical Movement (pfx_z)'}
)

# Display the plot in the Streamlit app
st.plotly_chart(fig)
