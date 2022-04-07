from tokenize import Triple
import dash
from dash import dcc, html
import dash_bootstrap_components as dbc
from cities.frontEndBluePrint import headerComponent

testPath = "C:/Users/DELL/Desktop/Air-Quality-Index-Prediction/test.css"
js = "C:/Users/DELL/Desktop/Air-Quality-Index-Prediction/assets/index.js"
foo = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    external_scripts=[testPath, js]
    )

foo.layout = html.Div(className='main',children=[
    headerComponent("Mumbai", "January 2018", 45),
    headerComponent("Mumbai", "January 2018", 95),
    headerComponent("Mumbai", "January 2018", 145),
    headerComponent("Mumbai", "January 2018", 245),
    headerComponent("Mumbai", "January 2018", 345),
    headerComponent("Mumbai", "January 2018", 445),
])

if __name__ == "__main__":
    foo.run_server(debug=True, port=1111)