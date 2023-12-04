import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px
import seaborn as sns
# import matplotlib.pyplot as plt

marvel_df= pd.read_csv('marvel_clean.csv')
og_df = pd.read_csv('marvel.csv')
years_df = pd.read_csv('years_df.csv')

colors = ['#d0384e',
 '#ee6445',
 '#fa9b58',
 '#fece7c',
 '#fff1a8',
 '#f4faad',
 '#d1ed9c',
 '#97d5a4',
 '#5cb7aa']

years_df.set_index('name', inplace=True)

st.title('Marvel Comics Dashboard')

selected_character = st.selectbox('Select a character', years_df.index)

st.header(selected_character)
character = years_df.loc[selected_character]
cumulative_sum = character.cumsum()
cumulative_sum.reset_index(drop = True, inplace=True)
tidy_df = pd.DataFrame({
    'Year': cumulative_sum.index,
    'Mentions': cumulative_sum.values
})

fig = px.line(tidy_df, x='Year', y='Mentions',
              labels={"Mentions": "Mentions", "Year": "Year"},
              title=f'{selected_character} Mentions Over Time in Comics',
              line_shape="linear", width=800, height=500, color_discrete_sequence=colors)

# # Customize the layout
fig.update_layout(xaxis=dict(tickangle=45, tickmode='linear', tick0=min(tidy_df['Year']), dtick=5, tickvals=list(range(1939, 2024, 5))))
# Show the plot in Streamlit

st.plotly_chart(fig)
# st.dataframe(years_df.index)
st.write(f"Total mentions for {selected_character}: {cumulative_sum.iloc[-1]}")
st.write(f"Year of highest mentions: {character.idxmax()}")
st.write(f"Highest number of mentions in {character.idxmax()}: {character.max()}")
#top 5 characters for a selected year and total mentions
selected_year = st.selectbox('Select a year', years_df.columns)

st.header(selected_year)
selected_year_df = years_df[selected_year].sort_values(ascending=False)[:5]
st.write(f"Top 5 characters for {selected_year}:")
st.dataframe(selected_year_df, width=450)
#make the dataframe larger so the whole name shows


#comic mentions barplot for selected character(s)
#use selection checkbox
selected_characters = st.multiselect('Select characters', marvel_df['name'])

st.header('Character Mentions in Comics')
# st.bar_chart(marvel_df[marvel_df['name'].isin(selected_characters)]['comics_available'].astype(int))
selected_data = marvel_df[marvel_df['name'].isin(selected_characters)]
selected_data.set_index('name', inplace=True)

# Plot the bar chart
st.bar_chart(selected_data['comics_available'].astype(int), color='#d0384e')