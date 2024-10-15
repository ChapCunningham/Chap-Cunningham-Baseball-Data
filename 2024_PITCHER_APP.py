import streamlit as st
import pandas as pd
import gdown

# Step 1: Define the Google Drive file ID
file_id = '1iZ5nZ-Vy6uDW8P2xf-bNe-MPoLmL9c-w'  # Replace with your actual file ID

# Step 2: Build the download URL and define the output file name
url = f'https://drive.google.com/uc?id={file_id}'
output = 'pitcherapp_statcast_2024.csv'

# Step 3: Download the CSV file from Google Drive
gdown.download(url, output, quiet=False)

# Step 4: Load the CSV into a DataFrame
df2024 = pd.read_csv(output)

# Step 5: Streamlit App Layout
st.title("Pitch Movement Visualization")

# Player dropdown for selecting
players = df2024['player_name'].unique()
selected_player = st.selectbox('Select a player:', players)

# Filter data for the selected player
player_data = df2024[df2024['player_name'] == selected_player]

# Create the scatter plot using Plotly Express
import plotly.express as px
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
