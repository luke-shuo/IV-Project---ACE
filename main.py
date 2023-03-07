import pandas as pd
import altair as alt
import streamlit as st

data = pd.read_csv("/Users/lukeshuo/Documents/GitHub/Altair/europe_covid.csv")
chart = alt.Chart(data)

point = chart.mark_point().encode(
  y='Country/Other',
  x='Total Cases',
  color='Country/Other',
  tooltip=['Country/Other', 'Total Cases']
)

# c.save('chart.html')
st.title('IV Project')

st.altair_chart(point, use_container_width=True)