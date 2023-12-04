import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px

marvel_df= pd.read_csv('marvel_clean.csv')
og_df = pd.read_csv('marvel.csv')
years_df = pd.read_csv('years_df.csv')

st.title('Marvel Comics Dashboard')

selected_character = st.selectbox('Select a character', marvel_df['name'])

name_df = marvel_df[marvel_df['name'] == selected_character]
st.dataframe(name_df)

# st.dataframe(marvel_df)