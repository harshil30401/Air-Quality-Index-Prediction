from tokenize import Triple
import dash
from dash import dcc, html
import dash_bootstrap_components as dbc



testPath = "C:/Users/DELL/Desktop/Air-Quality-Index-Prediction/assets/test.css"
js = "C:/Users/DELL/Desktop/Air-Quality-Index-Prediction/assets/index.js"

var = "test"
navbar = html.Nav(id=f'nav{var}', children=[
    html.A('Home', className='box'),
    html.A('About', className='box'),
    html.A('Contact', className='box'),
    html.A('Map', className='box')
])

foo = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    external_scripts=[testPath, js]
    )

foo.layout = html.Div(className='main',children=[
    navbar

])

if __name__ == "__main__":
    foo.run_server(debug=True, port=1111)