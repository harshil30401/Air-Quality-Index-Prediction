from dash import Dash
import dash_bootstrap_components as dbc
from dash import html, dcc
from dash.dependencies import Input, Output


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(id = "main-div", children=[
    html.Div(id="headerDiv", children=[
        html.H1(id="homeHeader", children=["Analysis and Prediction of Air Quality in India"])
    ]),

    html.Div(id="cardDiv", children=[
        # dbc.Button("Amritsar", id="amritsar", href="#", style={"color":"white"}),
        # dbc.Button("Chennai", id="chennai", href="#", style={"color":"white"}),
        # dbc.Button("Delhi", id="delhi", href="#", style={"color":"white"})
        dbc.Button("Amritsar", id="amritsar", href="cities/amritsar")
    ])
])

if __name__ == '__main__':
    app.run_server(debug=True)