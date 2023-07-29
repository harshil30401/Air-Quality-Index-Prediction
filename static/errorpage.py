from turtle import width
from dash import dcc, html
import dash_bootstrap_components as dbc
from app import app


layout = html.Div(id='mainDiv', children=[
    html.H1(id='errorHeader', children=["Oops! The page you requested wasn't found"]),
    html.Div(id='helperDiv',children=[
        dbc.Row(id='theRow', children=[
            html.H2(id='helperText', children=["Let's get you back"]),
            dbc.Button(className="me-1", children=[
                dcc.Link("Go Back", href='/', style={'color':'white'}),
            ])
        ])
    ])
])