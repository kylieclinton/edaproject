import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px
# import seaborn as sns
# import matplotlib.pyplot as plt

marvel_df= pd.read_csv('marvel_clean.csv')
og_df = pd.read_csv('marvel.csv')
years_df = pd.read_csv('years_df.csv')

years_df.set_index('name', inplace=True)

st.title('Marvel Comics Dashboard')

selected_character = st.selectbox('Select a character', years_df.index)

st.header(selected_character)
character = years_df.loc[selected_character].cumsum()
character.reset_index(drop = True, inplace=True)

# cumulative_sum = character.cumsum()
tidy_df = pd.DataFrame({
    'Year': character.index,
    'Mentions': character.values
})

fig = px.line(tidy_df, x='Year', y='Mentions',
              labels={"Mentions": "Mentions", "Year": "Year"},
              title=f'{selected_character} Mentions Over Time in Comics',
              line_shape="linear", width=800, height=500)

# # Customize the layout
fig.update_layout(xaxis=dict(tickangle=45, tickmode='linear', tick0=min(tidy_df['Year']), dtick=5, tickvals=list(range(1939, 2024, 5))))
# Show the plot in Streamlit

st.plotly_chart(fig)
st.dataframe(years_df.index)