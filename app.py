import dash 
import dash_bootstrap_components as dbc
from rootInformation import rootDirectory

class cssPaths:
    def indexPage():
        return f"{rootDirectory}/Air-Quality-Index-Prediction/assets/index.css"
    
    def cityPage():
        return f"{rootDirectory}/Air-Quality-Index-Prediction/assets/city.css"

indexPath = f"{rootDirectory}/Air-Quality-Index-Prediction/assets/index.css"

app = dash.Dash(
    __name__,
    suppress_callback_exceptions=True,
    external_stylesheets=[dbc.themes.BOOTSTRAP, indexPath]
    )

app.title = "Analysis and Prediction of Air Quality in India"

server = app.server