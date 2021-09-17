import dash
import plotly
import dash_core_components as dcc
import dash_html_components as html 
import dash_table
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import sqlite3
import pandas as pd
from app import app
from tabs import sidepanel, tab1, tab2, tab3, navbar
from database import transforms
app.layout = html.Div([navbar.Navbar()
                        , sidepanel.layout
            ])
@app.callback(Output('tabs-content', 'children'),
              [Input('tabs', 'value')])
def render_content(tab):
    if tab == 'tab-1':
        return tab1.layout
    elif tab == 'tab-2':
       return tab2.layout
    elif tab == 'tab-3':
       return tab3.layout

if __name__ == '__main__':
    app.run_server(debug = True)
