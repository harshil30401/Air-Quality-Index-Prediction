from distutils.log import debug
import dash
from dash import dcc, html
import dash_bootstrap_components as dbc

path = r'C:\Users\ansuj\OneDrive\Desktop\AQI\Air-Quality-Index-Prediction\assets\dashApp.css'
app = dash.Dash(__name__, external_stylesheets=[path, dbc.themes.BOOTSTRAP])

app.layout = html.Div(id='parent', children=[
    dbc.Card(id = 'mainCard', children=[
        dbc.CardBody(id = 'cardBody', children=[
            html.H1(id='header', children = 'This is a header')
    ])
])
])

if __name__ == '__main__':
    app.run_server(debug=True)