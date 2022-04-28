import requests
from bs4 import BeautifulSoup
import time

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

def show_forecast():

    city = "Mumbai"

    URL = f"https://www.accuweather.com/en/in/{city.lower()}/{weatherDictionary[city.lower()]}/weather-forecast/{weatherDictionary[city.lower()]}"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"
    }

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


    # print("-"*79+"Weather"+"-"*75)
    asOfCurrentTime = ("As of "+current_time+",")
    weatherTerm = (weather_term)
    temperature = (current_temperature)
    aqiAqiBucket = (aqi_today+", "+aqi_bucket)
    # print("-"*161)

city = "Mumbai"

URL = f"https://www.accuweather.com/en/in/{city.lower()}/{weatherDictionary[city.lower()]}/weather-forecast/{weatherDictionary[city.lower()]}"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"
}

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
aqiAqiBucket = (aqi_today+", "+aqi_bucket)
