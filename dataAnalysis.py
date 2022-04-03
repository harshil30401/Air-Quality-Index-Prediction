import bar_chart_race as bcr
import pandas as pd
# from IPython.display import HTML
import numpy as np
import seaborn as sns
from rootInformation import rootDirectory
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px
import folium

cities = pd.read_excel(f"{rootDirectory}/Air-Quality-Index-Prediction/datasets/allCities.xlsx")
cities['Date']=pd.to_datetime(cities['Date'])

cities['PM'] = cities['PM2.5'] + cities['PM10']


# Refer to the Top 10 cities graph