import dash_bootstrap_components as dbc
from dash import dcc, html
import numpy as np

def headerComponent(city, startDate, aqi):
    if aqi <= 50:
        aqiBucket = "Good"
    elif aqi <= 100:
       aqiBucket =  "Satisfactory"
    elif aqi <= 200:
        aqiBucket = "Moderate"
    elif aqi <= 300:
        aqiBucket = "Poor"
    elif aqi <= 400:
        aqiBucket = "Very Poor"
    elif aqi > 400:
        aqiBucket = "Severe"
    else:
        aqiBucket = np.NaN

    return dbc.Card(
        dbc.CardBody([
            dbc.Col([
                dbc.Row([

                    html.H1(f"{city} Air Quality Index")
                ]),

                dbc.Row([
                    html.H4(f"From {startDate} to August 2021")
                ]),
                html.Br(),
                dbc.Row([
                    html.H2(aqiBucket)
                ])
            ]),
            dbc.Col([
                html.H1([aqi])
            ], style={'text-align':'right', 'font-size':'25px'})
        ])
    )