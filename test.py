
from bs4 import BeautifulSoup
import requests, dash
import dash_bootstrap_components as dbc
from dash import Input, Output, html

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

city = "visakhapatnam" 

URL = f"https://www.accuweather.com/en/in/{city.lower()}/{weatherDictionary[city.lower()]}/weather-forecast/{weatherDictionary[city.lower()]}" #throws keyerror
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"}
page = requests.get(URL, headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')
AQI = (soup.find(class_ = 'aq-number')).get_text()
time = soup.find(class_='cur-con-weather-card__subtitle').get_text()
current_time = time.strip()
aqi = (AQI.strip())
aqi_today =  str("Today's AQI is "+aqi)
aqi_bucket = soup.find(class_ = 'category-text').get_text()
temp = soup.find(class_ = 'temp').get_text()
current_temp = (temp.strip())
current_temperature = str("Temperature is "+current_temp)
phrase = soup.find(class_ = 'phrase').get_text()
weather_term = str(phrase.strip())
asOfCurrentTime = ("As of "+current_time+",")
weatherTerm = (weather_term)
temperature = (current_temperature)


app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

text_input = html.Div(
    [
        dbc.Input(id="input", placeholder="Search for a city...", type="text", value=""),
        html.Br(),
        html.P(id="output"),
    ]
)

app.layout = text_input

@app.callback(Output("output", "children"), 
[Input("input", "value")])
def output_text(value):
    return value

# app.run_server(debug=True)

cities = []

for i in weatherDictionary.keys():
    cities.append(i)

print(cities)
