import streamlit as st
import pandas as pd
import gdown
import plotly.express as px

# Step 1: Download the CSV file from Google Drive
file_id = '1iZ5nZ-Vy6uDW8P2xf-bNe-MPoLmL9c-w'  # Replace with your actual file ID
url = f'https://drive.google.com/uc?id={file_id}'
output = 'pitcherapp_statcast_2024.csv'
gdown.download(url, output, quiet=False)

# Step 2: Load the CSV into a DataFrame
df2024 = pd.read_csv(output)

# Step 3: Streamlit App Layout
st.title("Pitch Movement Visualization and Stats Table")

# Player dropdown for selecting
players = df2024['player_name'].unique()
selected_player = st.selectbox('Select a player:', players)

# Filter data for the selected player
player_data = df2024[df2024['player_name'] == selected_player]

# Step 4: Create the scatter plot using Plotly Express
fig = px.scatter(
    player_data,
    x='pfx_x',
    y='pfx_z',
    color='pitch_type',
    title=f'{selected_player} Pitch Movement',
    labels={'pfx_x': 'Horizontal Movement (pfx_x)', 'pfx_z': 'Vertical Movement (pfx_z)'}
)

# Display the plot
st.plotly_chart(fig)

# Step 5: Create the stats table for each pitch type
pitch_stats = player_data.groupby('pitch_type').agg(
    count=('pitch_type', 'size'),
    avg_release_speed=('release_speed', 'mean'),
    avg_release_pos_x=('release_pos_x', 'mean'),
    avg_release_pos_z=('release_pos_z', 'mean'),
    avg_pfx_x=('pfx_x', 'mean'),
    avg_pfx_z=('pfx_z', 'mean'),
    avg_delta_run_exp=('delta_run_exp', 'mean')
).reset_index()

# Step 6: Display the stats table in Streamlit
st.subheader(f"{selected_player}'s Pitch Statistics")
st.write(pitch_stats)
