import dash 
import dash_bootstrap_components as dbc
from rootInformation import rootDirectory

class cssPaths:
    def indexPage():
        return r"C:\Users\DELL\Desktop\Text Editors & Softwares\Python\Dash\Air-Quality-Index-Prediction\assets\index.css"
    
    def cityPage():
        return r"C:\Users\DELL\Desktop\Text Editors & Softwares\Python\Dash\Air-Quality-Index-Prediction\assets\city.css"

rootDirectory = rootDirectory + '/Air-Quality-Index-Prediction'

indexPath = rootDirectory + '/assets/index.css'
jsPath = rootDirectory + '/assets/index.js'

app = dash.Dash(
    __name__,
    suppress_callback_exceptions=True,
    external_stylesheets=[dbc.themes.BOOTSTRAP, dbc.icons.BOOTSTRAP],
    external_scripts=[indexPath, jsPath]
    )

app.title = "Analysis and Prediction of Air Quality in India"

server = app.server