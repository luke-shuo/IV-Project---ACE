import pandas as pd
import altair as alt
import streamlit as st

data = pd.read_csv("/Users/lukeshuo/Documents/GitHub/Altair/europe_covid.csv")
chart = alt.Chart(data)

line = chart.mark_line().encode(
  alt.Y('Total Deaths', scale=alt.Scale(type='log')),
  alt.X('Country/Other')).interactive()

bar = chart.mark_bar().encode(alt.X('Country/Other'), alt.Y('Total Deaths'))

c = line & bar
# c.save('chart.html')
st.title('IV Project')

st.altair_chart(c, use_container_width=True)