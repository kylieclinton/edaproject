import pandas as pd
import numpy as np
import streamlit as st
import plotly as pt
import plotly.express as px
import plotly.graph_objects as go
import plotly.offline as py
from plotly.offline import init_notebook_mode

# print(sys.executable)
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
st.write("This dashboard provides insights into the popularity of Marvel comics characters over time. Select characters and years to learn about their popularity over time")
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
              title=f'Cumulative Comic Book Appearances for {selected_character}',
              line_shape="linear", width=800, height=500, color_discrete_sequence=colors)

# # Customize the layout
fig.update_layout(xaxis=dict(tickmode='auto'),     annotations=[
        dict(
            x=0,  # Adjust this value to the x-coordinate where you want the note
            y=-2,   # Adjust this value to the y-coordinate where you want the note
            xref="x",
            yref="y",
            text="Note: Year 0 is 1939 and goes to 2023",
            showarrow=False,
            ax=0,
            ay=-40
        )
    ])

tickval = list(years_df.columns)
fig.update_layout(xaxis=dict(tickmode='array', tickvals=tickval, ticktext = ["1939",
"1940","1941","1942","1943","1944","1945","1946","1947","1948","1949",
"1950","1951","1952","1953","1954","1955",'1956',"1957","1958","1959",
"1960","1961","1962","1963","1964","1965","1966","1967","1968","1969",
"1970","1971","1972","1973","1974","1975","1976","1977","1978","1979",
"1980","1981","1982","1983","1984","1985","1986","1987","1988","1989",
"1990","1991","1992","1993","1994","1995","1996","1997","1998","1999",
"2000","2001","2002","2003","2004","2005","2006","2007","2008","2009",
"2010","2011","2012","2013","2014","2015","2016","2017","2018","2019",
"2020","2021","2022","2023"
]))

st.plotly_chart(fig)
# st.dataframe(years_df.index)
st.write(f"Total mentions for {selected_character}: {cumulative_sum.iloc[-1]}")
st.write(f"Year {selected_character} was mentioned the most: {character.idxmax()}")
st.write(f"Number of mentions in {character.idxmax()}: {character.max()}")
#top 5 characters for a selected year and total mentions
st.text(" ")
st.text(" ")
#make a slider for selected year
selected_year = st.select_slider('Select a year', years_df.columns)

selected_year_df = years_df[selected_year].sort_values(ascending=False)[:5]
st.subheader(f"Top 5 characters for {selected_year}:")
st.dataframe(selected_year_df, width=450)
st.caption("Note: Year column shows mentions in that year for the character")
#make the dataframe larger so the whole name shows


#comic mentions barplot for selected character(s)
#use selection checkbox
st.text(" ")
st.text(" ")
selected_characters = st.multiselect('Select characters', marvel_df['name'])

st.subheader('Character Mentions in Comics')
# st.bar_chart(marvel_df[marvel_df['name'].isin(selected_characters)]['comics_available'].astype(int))
selected_data = marvel_df[marvel_df['name'].isin(selected_characters)]
selected_data.set_index('name', inplace=True)

# Plot the bar chart
st.bar_chart(selected_data['stories_available'].astype(int), color='#d0384e')

st.markdown('[Visit My Blog](https://kylieclinton.github.io/blog386/)', unsafe_allow_html=True)
st.markdown('[Visit My GitHub Repository](https://github.com/kylieclinton/edaproject/)', unsafe_allow_html=True)