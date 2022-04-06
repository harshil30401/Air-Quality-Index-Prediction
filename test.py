from email import header
from cities.frontEndBluePrint import headerComponent
import dash
import dash_bootstrap_components as dbc
from dash import dcc, html

app1 = dash.Dash()
city = "Amritsar", 
startDate = "January 2018",
aqiBucket = "Poor",
aqi = 118

app1.layout = html.Div([
    
    headerComponent("Amritsar", "January 2018", 118),
])


if __name__ == "__main__":
    app1.run_server(debug=True, port=6969)

