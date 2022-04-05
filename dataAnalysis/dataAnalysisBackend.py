import bar_chart_race as bcr
import pandas as pd

# from IPython.display import HTML
import numpy as np
import seaborn as sns
from rootInformation import rootDirectory 
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px

from plotly.offline import init_notebook_mode, plot, iplot
from plotly.subplots import make_subplots
import folium
import folium.plugins as plugins
from folium.plugins import MarkerCluster
from matplotlib.patches import Circle, Wedge, Rectangle
from IPython.lib.display import IFrame
import altair as alt
from app import app

cities = pd.read_excel(
    f"{rootDirectory}/Air-Quality-Index-Prediction/datasets/allCities.xlsx"
)
cities["Date"] = pd.to_datetime(cities["Date"])

cities["PM"] = cities["PM2.5"] + cities["PM10"]

#Box plots & lined graph of every gas (Yearly and monthly trend)
df = cities.copy()

df['year'] = [d.year for d in df.Date]
df['month'] = [d.strftime('%b') for d in df.Date]
df1 = df.groupby("month", sort=False)['PM2.5','PM10','NO2','NOx','NH3','CO','SO2','O3','AQI'].mean().reset_index()

yearly = px.box(df, x='year', y="PM10", color="year")

monthly = px.line(df1, x='month', y="PM10", markers=True)


# Refer to the Top 10 cities graph

gases = ["PM2.5", "PM10", "NO2", "NOx", "CO", "NH3", "O3", "SO2"]


for g in gases:
    x = cities.groupby("City")[g].mean().sort_values(ascending=False).reset_index()
    trace = go.Table(
        domain=dict(x=[0, 0.52], y=[0, 1.0]),
        header=dict(
            values=["City", g],
            fill=dict(color="red"),
            font=dict(color="white", size=14),
            align=["center"],
            height=30,
        ),
        cells=dict(
            values=[x["City"].head(10), x[g].head(10)],
            fill=dict(color=["lightsalmon", "lightsalmon"]),
            align=["center"],
        ),
    )

    trace1 = go.Bar(
        x=x["City"].head(10),
        y=x[g].head(10),
        xaxis="x1",
        yaxis="y1",
        marker=dict(color="red"),
        opacity=0.60,
    )
    layout = dict(
        width=830,
        height=490,
        autosize=False,
        title=f"TOP 10 Cities with Max {g}",
        showlegend=False,
        xaxis1=dict(**dict(domain=[0.58, 1], anchor="y1", showticklabels=True)),
        yaxis1=dict(**dict(domain=[0, 1.0], anchor="x1", hoverformat=".2f")),
    )

    top10 = dict(data=[trace, trace1], layout=layout)
    # iplot(top10), 

    # top10 = iplot(top10)


x2 = (
    cities[["PM2.5", "City"]]
    .groupby(["City"])
    .median()
    .sort_values(by="PM2.5", ascending=False)
    .reset_index()
)
x3 = (
    cities[["PM10", "City"]]
    .groupby(["City"])
    .median()
    .sort_values(by="PM10", ascending=False)
    .reset_index()
)

pm25pm10 = make_subplots(rows=1, cols=2, subplot_titles=("PM2.5", "PM10"))

pm25pm10.add_trace(
    go.Bar(
        y=x2["PM2.5"],
        x=x2["City"],
        marker=dict(color=x2["PM2.5"], coloraxis="coloraxis"),
    ),
    1,
    1,
)

pm25pm10.add_trace(
    go.Bar(
        y=x3["PM10"], x=x2["City"], marker=dict(color=x3["PM10"], coloraxis="coloraxis")
    ),
    1,
    2,
)
pm25pm10.update_layout(
    coloraxis=dict(colorscale="reds"), showlegend=False, plot_bgcolor="white"
)
pm25pm10.update_xaxes(
    ticks="outside",
    tickwidth=2,
    tickangle=45,
    tickcolor="crimson",
    ticklen=10,
    title_text="cities",
)
pm25pm10.update_yaxes(title_text="ug / m3", row=1, col=1)
pm25pm10.update_yaxes(title_text="ug / m3", row=1, col=2)


x4 = (
    cities[["CO", "City"]]
    .groupby(["City"])
    .mean()
    .sort_values(by="CO", ascending=False)
    .reset_index()
)
x5 = (
    cities[["NO2", "City"]]
    .groupby(["City"])
    .mean()
    .sort_values(by="NO2", ascending=False)
    .reset_index()
)
x6 = (
    cities[["SO2", "City"]]
    .groupby(["City"])
    .mean()
    .sort_values(by="SO2", ascending=False)
    .reset_index()
)

cono2so2 = make_subplots(rows=1, cols=3, subplot_titles=("CO", "NO2", "SO2"))

cono2so2.add_trace(
    go.Bar(
        y=x4["CO"], x=x4["City"], marker=dict(color=x4["CO"], coloraxis="coloraxis")
    ),
    1,
    1,
)


cono2so2.add_trace(
    go.Bar(
        y=x5["NO2"], x=x5["City"], marker=dict(color=x5["NO2"], coloraxis="coloraxis")
    ),
    1,
    2,
)

cono2so2.add_trace(
    go.Bar(
        y=x6["SO2"], x=x5["City"], marker=dict(color=x6["SO2"], coloraxis="coloraxis")
    ),
    1,
    3,
)
cono2so2.update_layout(
    coloraxis=dict(colorscale="reds"), showlegend=False, plot_bgcolor="white"
)
cono2so2.update_xaxes(
    ticks="outside",
    tickwidth=2,
    tickangle=45,
    tickcolor="crimson",
    ticklen=10,
    title_text="cities",
)
cono2so2.update_yaxes(title_text="ug / m3", row=1, col=1)
cono2so2.update_yaxes(title_text="ug / m3", row=1, col=2)
cono2so2.update_yaxes(title_text="ug / m3", row=1, col=3)

# Effect of Lockdown on AQI

locations = [
    "Ahmedabad",
    "Amaravati",
    "Amritsar",
    "Bengaluru",
    "Chennai",
    "Delhi",
    "Gandhinagar",
    "Hyderabad",
    "Jaipur",
    "Jodhpur",
    "Kanpur",
    "Kolkata",
    "Lucknow",
    "Mumbai",
    "Nagpur",
    "Patna",
    "Pune",
    "Thiruvananthapuram",
    "Visakhapatnam",
]

filtered_city_day = cities[cities["Date"] >= "2018-10-01"]
AQI = filtered_city_day[filtered_city_day.City.isin(locations)][
    ["Date", "City", "AQI", "AQI_Bucket"]
]

AQI_pivot = AQI.pivot_table(index="Date", columns="City", values="AQI")
AQI_pivot.fillna(method="bfill", inplace=True)
# AQI_pivot = AQI_pivot.drop_duplicates(['Date'])

from plotly.subplots import make_subplots

aqiBeforeAndAfter = make_subplots(
    rows=19,
    cols=1,
    # specs=[[{}, {}],
    #       [{"colspan": 6}, None]],
    subplot_titles=(
        "Ahmedabad",
        "Amaravati",
        "Amritsar",
        "Bengaluru",
        "Chennai",
        "Delhi",
        "Gandhinagar",
        "Hyderabad",
        "Jaipur",
        "Jodhpur",
        "Kanpur",
        "Kolkata",
        "Lucknow",
        "Mumbai",
        "Nagpur",
        "Patna",
        "Pune",
        "Thiruvananthapuram",
        "Visakhapatnam",
    ),
)

aqiBeforeAndAfter.update_annotations(xanchor="left", x=0.8, patch=None)


aqiBeforeAndAfter.add_trace(
    go.Bar(
        x=AQI_pivot.index,
        y=AQI_pivot["Ahmedabad"],
        marker=dict(color=AQI_pivot["Ahmedabad"], coloraxis="coloraxis"),
    ),
    1,
    1,
)
aqiBeforeAndAfter.add_trace(
    go.Bar(
        x=AQI_pivot.index,
        y=AQI_pivot["Amaravati"],
        marker=dict(color=AQI_pivot["Amaravati"], coloraxis="coloraxis"),
    ),
    2,
    1,
)
aqiBeforeAndAfter.add_trace(
    go.Bar(
        x=AQI_pivot.index,
        y=AQI_pivot["Amritsar"],
        marker=dict(color=AQI_pivot["Amritsar"], coloraxis="coloraxis"),
    ),
    3,
    1,
)
aqiBeforeAndAfter.add_trace(
    go.Bar(
        x=AQI_pivot.index,
        y=AQI_pivot["Bengaluru"],
        marker=dict(color=AQI_pivot["Bengaluru"], coloraxis="coloraxis"),
    ),
    4,
    1,
)
aqiBeforeAndAfter.add_trace(
    go.Bar(
        x=AQI_pivot.index,
        y=AQI_pivot["Chennai"],
        marker=dict(color=AQI_pivot["Chennai"], coloraxis="coloraxis"),
    ),
    5,
    1,
)
aqiBeforeAndAfter.add_trace(
    go.Bar(
        x=AQI_pivot.index,
        y=AQI_pivot["Delhi"],
        marker=dict(color=AQI_pivot["Delhi"], coloraxis="coloraxis"),
    ),
    6,
    1,
)
aqiBeforeAndAfter.add_trace(
    go.Bar(
        x=AQI_pivot.index,
        y=AQI_pivot["Gandhinagar"],
        marker=dict(color=AQI_pivot["Gandhinagar"], coloraxis="coloraxis"),
    ),
    7,
    1,
)
aqiBeforeAndAfter.add_trace(
    go.Bar(
        x=AQI_pivot.index,
        y=AQI_pivot["Hyderabad"],
        marker=dict(color=AQI_pivot["Hyderabad"], coloraxis="coloraxis"),
    ),
    8,
    1,
)
aqiBeforeAndAfter.add_trace(
    go.Bar(
        x=AQI_pivot.index,
        y=AQI_pivot["Jaipur"],
        marker=dict(color=AQI_pivot["Jaipur"], coloraxis="coloraxis"),
    ),
    9,
    1,
)
aqiBeforeAndAfter.add_trace(
    go.Bar(
        x=AQI_pivot.index,
        y=AQI_pivot["Jodhpur"],
        marker=dict(color=AQI_pivot["Jodhpur"], coloraxis="coloraxis"),
    ),
    10,
    1,
)
aqiBeforeAndAfter.add_trace(
    go.Bar(
        x=AQI_pivot.index,
        y=AQI_pivot["Kanpur"],
        marker=dict(color=AQI_pivot["Kanpur"], coloraxis="coloraxis"),
    ),
    11,
    1,
)
aqiBeforeAndAfter.add_trace(
    go.Bar(
        x=AQI_pivot.index,
        y=AQI_pivot["Kolkata"],
        marker=dict(color=AQI_pivot["Kolkata"], coloraxis="coloraxis"),
    ),
    12,
    1,
)
aqiBeforeAndAfter.add_trace(
    go.Bar(
        x=AQI_pivot.index,
        y=AQI_pivot["Lucknow"],
        marker=dict(color=AQI_pivot["Lucknow"], coloraxis="coloraxis"),
    ),
    13,
    1,
)
aqiBeforeAndAfter.add_trace(
    go.Bar(
        x=AQI_pivot.index,
        y=AQI_pivot["Mumbai"],
        marker=dict(color=AQI_pivot["Mumbai"], coloraxis="coloraxis"),
    ),
    14,
    1,
)
aqiBeforeAndAfter.add_trace(
    go.Bar(
        x=AQI_pivot.index,
        y=AQI_pivot["Nagpur"],
        marker=dict(color=AQI_pivot["Nagpur"], coloraxis="coloraxis"),
    ),
    15,
    1,
)
aqiBeforeAndAfter.add_trace(
    go.Bar(
        x=AQI_pivot.index,
        y=AQI_pivot["Patna"],
        marker=dict(color=AQI_pivot["Patna"], coloraxis="coloraxis"),
    ),
    16,
    1,
)
aqiBeforeAndAfter.add_trace(
    go.Bar(
        x=AQI_pivot.index,
        y=AQI_pivot["Pune"],
        marker=dict(color=AQI_pivot["Pune"], coloraxis="coloraxis"),
    ),
    17,
    1,
)
aqiBeforeAndAfter.add_trace(
    go.Bar(
        x=AQI_pivot.index,
        y=AQI_pivot["Thiruvananthapuram"],
        marker=dict(color=AQI_pivot["Thiruvananthapuram"], coloraxis="coloraxis"),
    ),
    18,
    1,
)
aqiBeforeAndAfter.add_trace(
    go.Bar(
        x=AQI_pivot.index,
        y=AQI_pivot["Visakhapatnam"],
        marker=dict(color=AQI_pivot["Visakhapatnam"], coloraxis="coloraxis"),
    ),
    19,
    1,
)


aqiBeforeAndAfter.update_layout(
    coloraxis=dict(colorscale="Temps"),
    showlegend=False,
    title_text="AQI Before and After Lockdown",
)

aqiBeforeAndAfter.update_layout(plot_bgcolor="white")

aqiBeforeAndAfter.update_layout(
    width=1000,
    height=4000,
    shapes=[
        dict(
            type="line",
            yref="paper",
            y0=0,
            y1=1,
            xref="x",
            x0="2020-03-25",
            x1="2020-03-25",
        )
    ],
)

aqiBeforeAndAfter.update_xaxes(title_text="Date")

aqiBeforeAndAfter.update_yaxes(title_text="AQI")

# Treemap

df = (
    cities.drop(columns=["Date", "AQI_Bucket", "AQI"])
    .groupby("City")
    .mean()
    .reset_index()
)
treemap = px.treemap(
    pd.melt(df, id_vars="City"),
    path=[px.Constant("India"), "City", "variable"],
    values=pd.melt(df, id_vars="City")["value"],
    title="Cities and the proportion of pollution in each",
)
treemap.update_traces(root_color="aliceblue")

#Openstreetmap

before_lockdown = cities[ (cities['Date'] >= '2018-10-01') & ('2020-02-29' >= cities['Date'])]
after_lockdown = cities[ (cities['Date'] >= '2020-03-01') & ('2021-08-15' >= cities['Date'])]
before_lockdown_aqi = before_lockdown.groupby('City')['AQI'].mean().to_frame().reset_index()
after_lockdown_aqi = after_lockdown.groupby('City')['AQI'].mean().to_frame().reset_index()

cities_db = pd.read_csv(f"{rootDirectory}/Air-Quality-Index-Prediction/datasets/IndianCitiesDatabase.csv")
before_lockdown_aqi = pd.merge(before_lockdown_aqi, cities_db, on = 'City')
before_lockdown_aqi['AQI'] = before_lockdown_aqi['AQI'].round(0)
after_lockdown_aqi = pd.merge(after_lockdown_aqi, cities_db, on = 'City')
after_lockdown_aqi['AQI'] = after_lockdown_aqi['AQI'].round(0)


m = plugins.DualMap(location=(21.9734, 79.6569), tiles=None, zoom_start=5)

folium.TileLayer('Stamen Toner').add_to(m)
folium.TileLayer('openstreetmap').add_to(m)


fg_1 = folium.FeatureGroup(name='2018-19').add_to(m.m1)
fg_2 = folium.FeatureGroup(name='2020-21').add_to(m.m2)



for lat, lon, value, name in zip(before_lockdown_aqi['Lat'], before_lockdown_aqi['Long'], before_lockdown_aqi['AQI'], before_lockdown_aqi['City']):
    folium.CircleMarker([lat, lon],
                        radius=10,
                        icon=folium.Icon(color='red'),
                        popup = ('<strong>City</strong>: ' + str(name).capitalize() + '<br>'
                                '<strong>AQI(Average)</strong>: ' + str(value) + '<br>'),
                        fill_color='red',
                        fill_opacity=0.7 ).add_to(fg_1)





for lat, lon, value, name in zip(after_lockdown_aqi['Lat'], after_lockdown_aqi['Long'], after_lockdown_aqi['AQI'], after_lockdown_aqi['City']):
    folium.CircleMarker([lat, lon],
                        radius=10,
                        icon=folium.Icon(color='blue'),
                        popup = ('<strong>City</strong>: ' + str(name).capitalize() + '<br>'
                                '<strong>AQI(Average)</strong>: ' + str(value) + '<br>'),
                        fill_color='blue',
                        fill_opacity=0.7 ).add_to(fg_2)


folium.LayerControl(collapsed=False).add_to(m)

#Top10 cities with Highest AQI Before and After Lockdown 

b_AQI=before_lockdown_aqi.groupby('City')['AQI'].max().sort_values(ascending=False).reset_index()
a_AQI=after_lockdown_aqi.groupby('City')['AQI'].max().sort_values(ascending=False).reset_index()


trace = go.Table(
    domain=dict(x=[0, 0.52],
                y=[0, 1.0]),
    header=dict(values=["City","AQI"],
                fill = dict(color = 'red'),
                font = dict(color = 'white', size = 14),
                align = ['center'],
               height = 30),
    cells=dict(values=[b_AQI['City'].head(10),b_AQI['AQI'].head(10)],
               fill = dict(color = ['lightsalmon', 'white']),
               align = ['center']))

trace1 = go.Bar(x=b_AQI['City'].head(10),
                y=b_AQI['AQI'].head(10),
                xaxis='x1',
                yaxis='y1',
                marker=dict(color='fuchsia'),opacity=0.60)
layout = dict(
    width=830,
    height=490,
    autosize=False,
    title='TOP 10 Cities with Max AQI',
    showlegend=False,   
    xaxis1=dict(**dict(domain=[0.58, 1], anchor='y1', showticklabels=True)),
    yaxis1=dict(**dict(domain=[0, 1.0], anchor='x1', hoverformat='.2f')),  
)

aqiBefore = dict(data=[trace, trace1], layout=layout)


trace = go.Table(
    domain=dict(x=[0, 0.52],
                y=[0, 1.0]),
    header=dict(values=["City","AQI"],
                fill = dict(color = 'red'),
                font = dict(color = 'white', size = 14),
                align = ['center'],
               height = 30),
    cells=dict(values=[a_AQI['City'].head(10),a_AQI['AQI'].head(10)],
               fill = dict(color = ['lightsalmon', 'white']),
               align = ['center']))

trace1 = go.Bar(x=a_AQI['City'].head(10),
                y=a_AQI['AQI'].head(10),
                xaxis='x1',
                yaxis='y1',
                marker=dict(color='fuchsia'),opacity=0.60)
layout = dict(
    width=830,
    height=490,
    autosize=False,
    title='TOP 10 Cities with Max AQI',
    showlegend=False,   
    xaxis1=dict(**dict(domain=[0.58, 1], anchor='y1', showticklabels=True)),
    yaxis1=dict(**dict(domain=[0, 1.0], anchor='x1', hoverformat='.2f')),  
)

aqiAfter = dict(data=[trace, trace1], layout=layout)

#Choropleth Maps

data = pd.read_csv(f'{rootDirectory}/Air-Quality-Index-Prediction/datasets/citiesMean.csv')
data.rename(columns={"PM2.5":"PM25"}, inplace=True)
data['PM10'].fillna("-", inplace=True)
data['NH3'].fillna("-", inplace=True)

district = cities[(cities['Date'] >= '2018-10-01')]
ahm = district[district.City == 'Ahmedabad']
amra = district[district.City == 'Amaravati']
amri = district[district.City == 'Amritsar']
ben = district[district.City == 'Bengaluru']
chen = district[district.City == 'Chennai']
de = district[district.City == 'Delhi']
ga = district[district.City == 'Gandhinagar']
hy = district[district.City == 'Hyderabad']
ja = district[district.City == 'Jaipur']
jo = district[district.City == 'Jodhpur']
ka = district[district.City == 'Kanpur']
ko = district[district.City == 'Kolkata']
lu = district[district.City == 'Lucknow']
mu = district[district.City == 'Mumbai']
na = district[district.City == 'Nagpur']
pa = district[district.City == 'Patna']
pu = district[district.City == 'Pune']
th = district[district.City == 'Thiruvananthapuram']
vi = district[district.City == 'Visakhapatnam']

districts = [ahm, amra, amri, ben, chen, de, ga, hy, ja, jo, ka, ko, lu, mu, na, pa, pu, th, vi]

city = list(data['City'])
lat = list(data['Lat'])
lon = list(data['Lon'])
aqi = list(data['AQI'])
pm25 = list(data['PM25'])
pm10 = list(data['PM10'])
no = list(data['NO'])
no2 = list(data['NO2'])
nox = list(data['NOx'])
nh3 = list(data['NH3'])
co = list(data['CO'])
so2 = list(data['SO2'])
o3 = list(data['O3'])

fg = folium.FeatureGroup('my map')

count=0

for cty, lt, ln, aq, p25, p10, noxi, ndoxi, nou, nh, cbn, sdo, oz in zip(city, lat, lon, aqi, pm25, pm10, no, no2, nox, nh3, co, so2, o3):

  
  # htmlFile = f"https:/{data['html_files'][count]}".replace(" ", "%20")
  # htmlFile = "/content/figAhmedabad.html"

  # html = """<iframe src=\"""" + htmlFile + """"\" width="850" height="400"  frameborder="0">""" 



  # test = folium.Html(htmlFile, script=True)
  # iframe = branca.element.IFrame(html=test)

  

  # html="""<iframe src="" www.google.com "" width="850" height="400">"""

  # html = """<a href = "www.google.com">Hello this is harshil</a> """

  popuptext = "<b>City : </b>"+str(cty)+", <b> AQI: </b>"+str(aq)+"<br><b>Mean emission of various gases:</b>"+"<br><b>PM2.5: </b>"+str(p25)+"<br><b>PM10: </b>"+str(p10)+"<br><b> NO: </b>"+str(noxi)+"<br><b> NO2: </b>"+str(ndoxi)+"<br><b> NOx: </b>"+str(nou)+"<br><b>NH3: </b>"+str(nh)+"<br><b>CO: </b>"+str(cbn)+"<br><b>SO2: </b>"+str(sdo)+"<br><b>O3: </b>"+str(oz)

    
  if(aq<50):
    fg.add_child(folium.Marker(
      location = [lt, ln],
        icon = folium.Icon(
            color='darkgreen',
            icon = 'dot-circle-o'
        ),
      tooltip = folium.Tooltip(
          text=cty),
      popup = folium.Popup(popuptext, max_width=300)    

      ))
  elif (aq>=51) & (aq<=100):
    fg.add_child(folium.Marker(
      location = [lt, ln],
        icon = folium.Icon(
            color='lightgreen',
            icon = 'dot-circle-o'
        ),

      tooltip = folium.Tooltip(
          text=cty),
       popup = folium.Popup(popuptext, max_width=300)    
 
      ))
  elif(aq>=101) & (aq<=200):
    fg.add_child(folium.Marker(
      location = [lt, ln],
        icon = folium.Icon(
            color='beige',  
            icon = 'dot-circle-o'
        ),
      tooltip = folium.Tooltip(
          text=cty),
      popup = folium.Popup(popuptext, max_width=300)    
 
       ))
  elif(aq>=201) & (aq<=300):
    fg.add_child(folium.Marker(
      location = [lt, ln],
        icon = folium.Icon(
            color='lightred',
            icon = 'dot-circle-o'
        ),
      tooltip = folium.Tooltip(
          text=cty),
      popup = folium.Popup(popuptext, max_width=300)    

      ))
  elif(aq>=301) & (aq<=400):
    fg.add_child(folium.Marker(
      location = [lt, ln],
        icon = folium.Icon(
            color='red',
            icon = 'dot-circle-o'
        ),
          tooltip = folium.Tooltip(
          text=cty),
      popup = folium.Popup(popuptext, max_width=300)    

      ))
  else:
    fg.add_child(folium.Marker(
      location = [lt, ln],
        icon = folium.Icon(
            color='darkred',
            icon = ""
        ),

      tooltip = folium.Tooltip(
          text=cty),
      popup = folium.Popup(popuptext, max_width=300)    

      ))
  
map = folium.Map(
    location = [ 21.7679, 78.8718],
    zoom_start=5,
    max_zoom=5,
    min_zoom=5
)

folium.TileLayer(tiles='Stamen Terrain', min_zoom=0, max_zoom=18, show=True, opacity=1, attr="toner-bcg").add_to(map)

fg.add_child(folium.Choropleth(geo_data=(open(f'{rootDirectory}/Air-Quality-Index-Prediction/india_states.json', 'r', encoding='utf-8-sig').read()), line_color='#665C67', fill_color='#9D7DA2'))
map.add_child(fg)




