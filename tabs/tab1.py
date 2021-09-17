import dash
import plotly
import dash_core_components as dcc
import dash_html_components as html 
import dash_bootstrap_components as dbc 
import dash_table
import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff
from dash.dependencies import Input, Output
from datetime import timedelta 

from app import app 
from database import transforms

DB = transforms.DB

jtkk = DB.groupby('FECHA').size().reset_index(name = 'nuevo')
jtkk = jtkk.astype('datetime64[ns]')
jtk = jtkk.groupby(pd.Grouper(key='FECHA', axis=0, 
                      freq='1D', sort=True)).sum()
jtk = jtk.reset_index()




DB["FECHA"] = DB["FECHA"].astype("datetime64")
f = DB.groupby(DB["FECHA"].dt.minute).count()
fig2 = px.bar(f['FECHA'], x=f['FECHA'].index, y=f['FECHA'])

fig3 =  ff.create_table(DB)


layout =  html.Div([
                  dcc.Graph(id='grafica_vehiculos',figure=fig2),
                  dcc.Graph(id='tabla_vehiculos',figure=fig3),
          ], className="five columns")

@app.callback(
    Output(component_id='grafica_vehiculos', component_property='figure'),
    Output(component_id='tabla_vehiculos', component_property='figure'),
    [Input(component_id='tipos', component_property='value'),
     Input(component_id='posicion', component_property='value'),
     Input(component_id='slider', component_property='value')])

def update_figure(selected_vehicle,selected_position,selected_value):

    all_books = ["/home/nabucodonosor/Escritorio/ANTARES/placas_vehiculos/APP/database/data_base_artificial.csv"]
    li = []

    for f in all_books:
           tmp = pd.read_csv(f, delimiter=',')
           li.append(tmp)

    DB = pd.concat(li, axis=0, ignore_index=True)
    
    jtkk = DB.groupby('FECHA').size().reset_index(name = 'nuevo')
    jtkk = jtkk.astype('datetime64[ns]')
    jtk = jtkk.groupby(pd.Grouper(key='FECHA', axis=0, 
                      freq='1D', sort=True)).sum()
    jtk = jtk.reset_index()
    
    DB["FECHA"] = DB["FECHA"].astype("datetime64")
    start_date = jtk['FECHA'][selected_value[0]]
    end_date   = jtk['FECHA'][selected_value[1]] + timedelta(days=1)
    mask = (DB['FECHA'] > start_date) & (DB['FECHA'] <= end_date)   
    DT = DB.loc[mask]  
   


    if selected_vehicle != 'todo' and selected_position != 'todo':
    
        ce = DT.loc[:, 'TIPO'] == selected_vehicle
        dbt = DT.loc[ce]

        ce = dbt.loc[:, 'POSICION'] == selected_position
        db = dbt.loc[ce]
        
        db["FECHA"] = db["FECHA"].astype("datetime64")
        f = db.groupby(db["FECHA"].dt.minute).count()
        fig2 = px.bar(f['FECHA'], x=f['FECHA'].index, y=f['FECHA'])
        fig2.update_layout(transition_duration=200)
                
        fig3 =  ff.create_table(db)
        fig3.update_layout(transition_duration=200)

    if selected_vehicle == 'todo' and selected_position != 'todo':
    
        ce = DT.loc[:, 'POSICION'] == selected_position
        db = DT.loc[ce]
        
        db["FECHA"] = db["FECHA"].astype("datetime64")
        f = db.groupby(db["FECHA"].dt.minute).count()
        fig2 = px.bar(f['FECHA'], x=f['FECHA'].index, y=f['FECHA'])
        fig2.update_layout(transition_duration=200)
                
        fig3 =  ff.create_table(db)
        fig3.update_layout(transition_duration=200)

    if selected_vehicle != 'todo' and selected_position == 'todo':
    
        ce = DT.loc[:, 'TIPO'] == selected_vehicle
        db = DT.loc[ce]
        
        db["FECHA"] = db["FECHA"].astype("datetime64")
        f = db.groupby(db["FECHA"].dt.minute).count()
        fig2 = px.bar(f['FECHA'], x=f['FECHA'].index, y=f['FECHA'])
        fig2.update_layout(transition_duration=200)
                
        fig3 =  ff.create_table(db)
        fig3.update_layout(transition_duration=200)


    if selected_vehicle == 'todo' and selected_position == 'todo':
        DT["FECHA"] = DB["FECHA"].astype("datetime64")
        f = DT.groupby(DB["FECHA"].dt.minute).count()
        fig2 = px.bar(f['FECHA'], x=f['FECHA'].index, y=f['FECHA'])
        fig2.update_layout(transition_duration=200)
                
        fig3 =  ff.create_table(DB)
        fig3.update_layout(transition_duration=200)
        
    
    return fig2, fig3
