import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc 
import pandas as pd
import plotly.graph_objs as go
from dash.dependencies import Input, Output
import dash_table
from app import app
from database import transforms
from datetime import timedelta 

DB = transforms.DB

jtkk = DB.groupby('FECHA').size().reset_index(name = 'nuevo')
jtkk = jtkk.astype('datetime64[ns]')
jtk = jtkk.groupby(pd.Grouper(key='FECHA', axis=0, 
                      freq='1D', sort=True)).sum()
jtk = jtk.reset_index()


ii = DB.groupby('TIPO').size().reset_index(name = 'nuevo')


labels = ii['TIPO'].to_list()
values = ii['nuevo'].to_list()

fig = go.Figure(data=[go.Pie(labels=labels, values=values)])
fig.update_traces(textfont_size=30)

colors = ['aquamarine','indianred','limegreen','mediumvioletred']
tipo=ii['TIPO'].to_list()
fig1 = go.Figure([go.Bar(x=tipo, y=ii['nuevo'].to_list(),marker_color=colors)])



layout =  html.Div([
                  html.Div([dcc.Graph(id='dona',figure=fig)], className='six columns'),            
                  html.Div([dcc.Graph(id='barra',figure=fig1)], className='six columns'),
          ], className='row'),



@app.callback(
    Output("dona", "figure"),
    Output("barra", "figure"),
      [Input("posicion", "value"),
       Input("slider","value")])



def update_figure(selected_position, selected_value):
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
    if selected_position != 'todo':
    
        ce = DT.loc[:, 'POSICION'] == selected_position
        db = DT.loc[ce]
        
        ii = db.groupby('TIPO').size().reset_index(name = 'nuevo')

        labels = ii['TIPO'].to_list()
        values = ii['nuevo'].to_list()

        fig = go.Figure(data=[go.Pie(labels=labels, values=values)])
        fig.update_traces(textfont_size=30)

        tipo=ii['TIPO'].to_list()
        fig1 = go.Figure([go.Bar(x=tipo, y=ii['nuevo'].to_list(),marker_color=colors)])

        fig.update_layout(transition_duration=200)
        fig1.update_layout(transition_duration=200)        
 
    else:
        ii = DT.groupby('TIPO').size().reset_index(name = 'nuevo')

        labels = ii['TIPO'].to_list()
        values = ii['nuevo'].to_list()

        fig = go.Figure(data=[go.Pie(labels=labels, values=values)])
        fig.update_traces(textfont_size=30)


        tipo=ii['TIPO'].to_list()
        fig1 = go.Figure([go.Bar(x=tipo, y=ii['nuevo'].to_list(),marker_color=colors)])

        fig.update_layout(transition_duration=200)
        fig1.update_layout(transition_duration=200)       
    
    return fig, fig1

