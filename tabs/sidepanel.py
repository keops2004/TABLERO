import dash
import plotly
import dash_core_components as dcc
import dash_html_components as html 
import dash_bootstrap_components as dbc 
import dash_table
import pandas as pd
from dash.dependencies import Input, Output
from app import app
from tabs import tab1, tab2, tab3
from database import transforms
DB = transforms.DB

placa = DB['PLACA'][len(DB)-1]
vehiculo = DB['TIPO'][len(DB)-1]
posicion = DB['POSICION'][len(DB)-1]


jtkk = DB.groupby('FECHA').size().reset_index(name = 'nuevo')
jtkk = jtkk.astype('datetime64[ns]')

jtk = jtkk.groupby(pd.Grouper(key='FECHA', axis=0, 
                      freq='1D', sort=True)).sum()
jtk = jtk.reset_index()


numdate= [x for x in range(len(jtk['FECHA'].unique()))]


layout = html.Div([
    html.H1('SISTEMA DETECCION PLACAS VEHICULARES')
    ,dbc.Row([dbc.Col(
        html.Div([
               
        html.Div([html.P()
                ,html.H5('SELECTOR DE FECHAS')
                ,dcc.RangeSlider(id='slider',min=numdate[0], max=numdate[-1],
        marks = {numd:{"label": str(date.strftime('%d/%m/%Y')), "style": {"transform": "rotate(45deg)"}} for numd,date in zip(numdate, jtk['FECHA'].dt.date.unique())},
            ),
                        
                            ])
        ,html.Div([html.P()
            ,html.H5('Posicion')
            , dcc.Dropdown(id='posicion',options=[
            {'label': 'P1C1D1', 'value': 'P1C1D1'},
            {'label': 'P1C1D2', 'value': 'P1C1D2'},
            {'label': 'P1C2D1', 'value': 'P1C2D1'},
            {'label': 'P1C2D2', 'value': 'P1C2D2'},
            {'label': 'Todos', 'value': 'todo'}
                                    ],value='todo')  
        ])
,html.Div([html.P()
            ,html.H5('Tipo de vehiculo')
            , dcc.Dropdown(id='tipos',options=[
            {'label': 'Automoviles', 'value': 'automovil'},
            {'label': 'Buses', 'value': 'bus'},
            {'label': 'Camiones', 'value': 'camion'},
            {'label': 'Motos', 'value': 'moto'},
            {'label': 'Todos', 'value': 'todo'}
                               ],value='todo')]),html.H1('ULTIMO REGISTRO:'),html.H2('Placa:'),html.Div(placa,id='placa-rojo', style={'color': 'red', 'fontSize': 52}),
                                             html.H2('Tipo:'),html.Div(vehiculo,id = 'vehiculo-rojo', style={'color': 'red', 'fontSize': 52}),
                                             html.H2('Posicion:'),html.Div(posicion,id = 'posicion-rojo', style={'color': 'red', 'fontSize': 52}),
                                             html.Button('Actualizar base de datos', id='submit-val', n_clicks=0),
                                             html.Div(id='container-button-timestamp')

], style={'marginBottom': 50, 'marginTop': 25, 'marginLeft':15, 'marginRight':15}
        )#end div
    , width=3) # End col
,dbc.Col(html.Div([
            dcc.Tabs(id="tabs", value='tab-1', children=[
                    dcc.Tab(label='HISTORICO', value='tab-1'),
                    dcc.Tab(label='CONSOLIDADO', value='tab-2'),
                    dcc.Tab(label='ALERTAS', value='tab-3'),
                ])
            , html.Div(id='tabs-content')
        ]), width=9)
        ]) #end row
    
    ])#end div

@app.callback([Output('container-button-timestamp', 'children'),
              Output('placa-rojo', 'children'),
              Output('vehiculo-rojo', 'children'),
              Output('posicion-rojo', 'children'),
              Output('slider','min'),
              Output('slider','max'),
              Output('slider','marks')],
              Input('submit-val', 'n_clicks'))

def displayClick(btn1):
    changed_id = [p['prop_id'] for p in dash.callback_context.triggered][0]
    if 'submit-val' in changed_id:
        msg = 'Base de datos actualizada'

        all_books = ["/home/nabucodonosor/Escritorio/ANTARES/placas_vehiculos/APP/database/data_base_artificial.csv"]
        li = []

        for f in all_books:
           tmp = pd.read_csv(f, delimiter=',')
           li.append(tmp)

        DB = pd.concat(li, axis=0, ignore_index=True)
       
        placa = DB['PLACA'][len(DB)-1]
        vehiculo = DB['TIPO'][len(DB)-1]
        posicion = DB['POSICION'][len(DB)-1]


        jtkk = DB.groupby('FECHA').size().reset_index(name = 'nuevo')
        jtkk = jtkk.astype('datetime64[ns]')

        jtk = jtkk.groupby(pd.Grouper(key='FECHA', axis=0, 
                      freq='1D', sort=True)).sum()
        jtk = jtk.reset_index()
        numdate= [x for x in range(len(jtk['FECHA'].unique()))]
        minimo=numdate[0]
        maximo=numdate[-1]
        marks = {numd:{"label": str(date.strftime('%d/%m/%Y')), "style": {"transform": "rotate(45deg)"}} for numd,date in zip(numdate, jtk['FECHA'].dt.date.unique())}


        
    else:
        msg = 'Pulse para actualizar'
    return html.Div(msg),html.Div(placa),html.Div(vehiculo),html.Div(posicion),minimo,maximo,marks











