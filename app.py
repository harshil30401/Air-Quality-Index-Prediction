import dash 
import dash_bootstrap_components as dbc
from rootInformation import rootDirectory

fontAwesome = {
    'href': 'https://use.fontawesome.com/releases/v5.8.1/css/all.css',
    'rel': 'stylesheet',
    'integrity': 'sha384-50oBUHEmvpQ+1lW4y57PTFmhCaXp0ML5d60M1M7uH2+nqUivzIebhndOJK28anvf',
    'crossorigin': 'anonymous'
}

class cssPaths:
    def indexPage():
        return r"C:\Users\DELL\Desktop\Text Editors & Softwares\Python\Dash\Air-Quality-Index-Prediction\static\index.css"
    
    def cityPage():
        return r"C:\Users\DELL\Desktop\Text Editors & Softwares\Python\Dash\Air-Quality-Index-Prediction\static\city.css"

rootDirectory = rootDirectory + '/Air-Quality-Index-Prediction'

indexPath = rootDirectory + '/static/index.css'
jsPath = rootDirectory + '/static/index.js'

app = dash.Dash(
    __name__,
    suppress_callback_exceptions=True,
    external_stylesheets=[dbc.themes.BOOTSTRAP, dbc.icons.BOOTSTRAP, fontAwesome],
    external_scripts=[indexPath, jsPath]
    # favicon_link= rootDirectory+'/static/photos/logo.png',
    )

# app._favicon = f"{rootDirectory}/static/photos/logo.png"

app.index(favicon=f"{rootDirectory}/static/photos/logo.png")

app.title = "Analysis and Prediction of AQI in India"

server = app.server