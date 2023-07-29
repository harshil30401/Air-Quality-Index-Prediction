import requests, numpy as np
from app import app
import dash
from dash import html, dcc, Output, Input
import dash_bootstrap_components as dbc
from bs4 import BeautifulSoup

fb = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP, dbc.icons.BOOTSTRAP])

def chooseImage(city):
    # if city == "amritsar":
    #     image = "photos/amritsar.jpg"
    #     return image

    # if city == "delhi":
    #     image = "photos/delhi.jpg"
    #     return image

    # if city == "kanpur":
    #     image = "photos/kanpur.jpg"
    #     return image

    # if city == "mumbai":
    #     image = "photos/mumbai.jpg"
    #     return image

    # if city == "thiruvananthapuram":
    #     image = "photos/thiruvananthapuram.jpg"
    #     return image
    # else:
    return "photos/smog.jpg"

weatherDictionary = {
    "mumbai":204842,
    "amritsar":205593,
    "chennai":206671,
    "delhi":202396,
    "hyderabad":261159,
    "jaipur":205617,
    "kanpur":206679,
    "kolkata":206690,
    "nagpur":204844,
    "patna":202349,
    "thiruvananthapuram":204287,
    "visakhapatnam":202192
}
cities = []

for i in weatherDictionary.keys():
    cities.append(i)

dropdown = html.Div([
    dcc.Dropdown(options=cities, id='input', placeholder="Select a city..."),
], style={'width':'18rem'})


weatherComponent = html.Div([dropdown, 

    html.Div(id='mainRow', children="")

], id='weatherComponent', style={'margin-left':'500px', 'margin-top':'50px'})


fb.layout = html.Div([weatherComponent])

@app.callback(
    Output(component_id='mainRow', component_property='children'),
    [
        Input(component_id='input', component_property='value')
    ]
)
def function(value):
    if value != None:
        city = value
        URL = f"https://www.accuweather.com/en/in/{city.lower()}/{weatherDictionary[city.lower()]}/weather-forecast/{weatherDictionary[city.lower()]}"
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"}
        page = requests.get(URL, headers=headers)
        soup = BeautifulSoup(page.content, 'html.parser')
        AQI = (soup.find(class_ = 'aq-number')).get_text()
        time = soup.find(class_='cur-con-weather-card__subtitle').get_text()
        current_time = time.strip()
        aqi = (AQI.strip())
        temp = soup.find(class_ = 'temp').get_text()
        current_temp = (temp.strip())
        phrase = soup.find(class_ = 'phrase').get_text()
        weather_term = str(phrase.strip())
        asOfCurrentTime = "As of "+current_time+","

        if int(aqi) <= 50:
            aqiBucket = "Good"
        elif int(aqi) <= 100:
            aqiBucket =  "Satisfactory"
        elif int(aqi) <= 200:
            aqiBucket = "Moderate"
        elif int(aqi) <= 300:
            aqiBucket = "Poor" 
        elif int(aqi) <= 400:
            aqiBucket = "Very Poor"
        elif int(aqi) > 400:
            aqiBucket = "Severe"
        else:
            aqiBucket = np.NaN

        multipleOutputs =f"{asOfCurrentTime} it is {weather_term}"
        aqiLine = f"AQI: {aqi}"
        
        card = dbc.Card(
            [
                dbc.CardImg(
                    # imagePath = "photos/smog.jpg",
                    src=app.get_asset_url(chooseImage(city)),
                    top=True,
                    id='weatherTermIMage',
                    style={"opacity": 0.3},
                ),
                dbc.CardImgOverlay(
                    dbc.CardBody(
                        children=[

                            html.H1(current_temp, className="card-title", id='first', style={'text-align':'center'}),
                            html.Hr(),
                            html.H6(multipleOutputs, id='secondThird'),
                            html.H6(aqiLine, id='fourth'),
                            html.H5(aqiBucket, className="card-title", id='fifth')
                        
                        ], id='card-body'
                    ),
                ),
            ],
            id='weatherCard',
            style={"width": "18rem", "border" : "2px solid red"},
        )
        return card 
    else:
        return print("Choose a city...")

fb.run_server(debug=True)