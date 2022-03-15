import dash 
import dash_bootstrap_components as dbc

class cssPaths:
    def indexPage():
        return r"C:\Users\DELL\Desktop\Text Editors & Softwares\Python\Dash\Air-Quality-Index-Prediction\assets\index.css"
    
    def cityPage():
        return r"C:\Users\DELL\Desktop\Text Editors & Softwares\Python\Dash\Air-Quality-Index-Prediction\assets\city.css"

indexPath = cssPaths.indexPage()

app = dash.Dash(
    __name__,
    suppress_callback_exceptions=True,
    external_stylesheets=[dbc.themes.BOOTSTRAP]
    )

app.title = "Analysis and Prediction of Air Quality in India"

server = app.server