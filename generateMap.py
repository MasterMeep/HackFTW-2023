import numpy as np
import pandas as pd

import json
from urllib.request import urlopen

from ipywidgets import Output, VBox


import plotly.express as px

import plotly.graph_objects as go

import warnings
warnings.filterwarnings("ignore")

df = pd.read_csv('def_area_2004_2019.csv')


stateCodeToState = {"AC": "Acre", "AM": "Amazonas", "AP": "Amapá", "MA": "Maranhão", "MT": "Mato Grosso", "PA": "Pará", "RO": "Rondônia", "RR": "Roraima", "TO": "Tocantins"}

#load brazil geojson from brazil.json
with open("brazil.json") as f:
    Brazil = json.load(f)

for index in df.index[1:]:
    for col in df.columns[1:-2]:
        df[col][index] += df[col][index-1]
        print(index)


def get_graph(year):
    row = df.iloc[year-2004]
    row.drop("Ano/Estados", inplace = True)
    row.drop("AMZ LEGAL", inplace = True)
    row = row.to_frame()
    row.reset_index(inplace = True)
    row.columns = ["state", "deforestation"]
    for index in row.index:
        row["state"][index] = stateCodeToState[row["state"][index]]
    
    fig = px.choropleth(
        row,
        locations = "state",
        color = 'deforestation',
        hover_name = 'state',
        hover_data = ['deforestation'],
        geojson = Brazil,
        title = "Deforestation in " + str(year)
    )
    fig.update_geos(fitbounds = "locations", visible = False)
    return fig