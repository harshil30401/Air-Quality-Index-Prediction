from tokenize import Triple
import dash
from dash import dcc, html
import dash_bootstrap_components as dbc

testPath = "C:/Users/DELL/Desktop/Air-Quality-Index-Prediction/test.css"
js = "C:/Users/DELL/Desktop/Air-Quality-Index-Prediction/assets/index.js"
foo = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    external_scripts=[testPath, js]
    )

foo.layout = html.Div(className='main',children=[
    html.P("Hello World")
])

if __name__ == "__main__":
    foo.run_server(debug=True, port=1111)