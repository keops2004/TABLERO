import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import folium
import pandas as pd
import geopandas as gpd
from app import app 
from database import transforms
DB = transforms.DB


mymap = folium.Map(location=[9.908853744235852, -67.35551207544937],tiles="openstreetmap",   zoom_start=13)

folium.Marker(
    location=[9.938001173860329, -67.36094086632879],
    popup="<i>PEAJE 1</i>",
    icon=folium.Icon(color="green"),
).add_to(mymap)

folium.Marker(
    location=[9.924643137666754, -67.32763855888918],
    popup="<i>PEAJE 2</i>",
    icon=folium.Icon(color="red"),
).add_to(mymap)

folium.Marker(
    location=[9.887948009505264, -67.39510148059182],
    popup="<i>PEAJE 3</i>",
    icon=folium.Icon(color="blue"),
).add_to(mymap)

folium.Marker(
    location=[9.875940879156952, -67.37330048553778],
    popup="<i>PEAJE 4</i>",
    icon=folium.Icon(color="purple"),
).add_to(mymap)

mymap.save('/home/nabucodonosor/Escritorio/ANTARES/placas_vehiculos/APP/database/mapa_peajes.html')


layout = html.Div([
                   html.Div([dcc.Dropdown(id="selected-feature", options=[{"label": i, "value": i} for i in ['Alerta','Sin placa','Solicitado','De interes']],
                       value='Alerta'
                       , style={"display": "block", "width": "80%"})
                ])
     , html.Div(html.Iframe(id = 'map',srcDoc = open('/home/nabucodonosor/Escritorio/ANTARES/placas_vehiculos/APP/database/mapa_peajes.html','r').read(),width = '100%',height = '600'   )
        )])


