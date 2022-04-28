import dash_bootstrap_components as dbc
from dash import dcc, html
import numpy as np

def navbar(color):
    return dbc.NavbarSimple(
        children=[
            dbc.NavItem(dbc.NavLink("Page 1", href="#")),
            dbc.DropdownMenu(
                children=[
                    dbc.DropdownMenuItem("More pages", header=True),
                    dbc.DropdownMenuItem("Page 2", href="#"),
                    dbc.DropdownMenuItem("Page 3", href="#"),
                ],
                nav=True,
                in_navbar=True,
                label="More",
            ),
        ],
        brand="NavbarSimple",
        brand_href="#",
        color=color,
        dark=True,
        style={
            'position':'sticky',
            'top':'0',
            'z-index':'1'
        }
    )

def headerComponent(city, startDate, aqi):
    if aqi <= 50:
        aqiBucket = "Good"
        color = '#71e274'
        # color = "#74c990"
    elif aqi <= 100:
       aqiBucket =  "Satisfactory"
       color = "#99f39c"
    elif aqi <= 200:
        aqiBucket = "Moderate"
        color = "#c2e462"
    elif aqi <= 300:
        aqiBucket = "Poor"
        color = "#e4e474"
    elif aqi <= 400:
        aqiBucket = "Very Poor"
        color = "#e0b153"
    elif aqi > 400:
        aqiBucket = "Severe"
        color='#c55151'
        # color = "#e46464"
    else:
        aqiBucket = np.NaN

    return  html.Div([
        html.Div(children=[
                dbc.Col([
                    dbc.Row([

                        html.H1(f"{city} Air Quality Index")
                    ], style={'font-size':'25px'}),

                    dbc.Row([
                        html.H4(f"From {startDate} to August 2021")
                    ], style={'font-size':'15px'}),
                    html.Br(),
                    dbc.Row([
                        html.H2(aqiBucket)
                    ], style={'font-size':'20px'})
                ]),
                dbc.Col([
                    html.H1([aqi])
                ], style={'text-align':'right', 'font-size':'30px', 'font-weight':'bold'})
            ], style={
                'background-color':color, 
                'padding':"20px 50px 15px 50px", 
                'font-weight':'bold',
                'border-radius':'10px'
                })

            # navbar("black")
    
    ])