import pandas as pd
import altair as alt
import streamlit as st
import geopandas as gpd

data = pd.read_csv("/Users/lukeshuo/Documents/GitHub/Altair/europe_covid.csv")
data = pd.read_csv("/Users/lukeshuo/Documents/GitHub/Altair/europe_covid.csv")
data = data[data.Country != 'Channel Islands']
data = data[data.Country != 'Gibraltar']
data = data[data.Country != 'Isle of Man']
data.replace(['UK'], ['United Kingdom'], inplace=True)
data.replace(['Czechia'], ['Czech Republic'], inplace=True)
data.replace(['Faeroe Islands'], ['Faroe Islands'], inplace=True)
data.replace(['Moldova'], ['Republic of Moldova'], inplace=True)
data.replace(['North Macedonia'], ['The former Yugoslav Republic of Macedonia'], inplace=True)

eu_data = gpd.read_file('/Users/lukeshuo/Documents/GitHub/Altair/materials/europe-economy-visualization-master/data/europe.geojson')

font = 'Ubuntu Mono'
red = '#d53e4f'
blue = '#3288bd'
gray = '#5D646F'

chart = alt.Chart(eu_data, width=1040, height=640).mark_geoshape().encode(
    color=alt.condition('datum["Total Deaths"] >= -1', alt.Color('Total Deaths:Q'), alt.value('Total Deaths:Q')),
    tooltip = ['NAME', 'Total Deaths:Q']
).project(
    'naturalEarth1'
).transform_lookup(
    lookup='NAME',
    from_=alt.LookupData(data, 'Country', ['Total Deaths'])
)


chart.save('chart.html')
st.title('IV Project')

st.altair_chart(chart)