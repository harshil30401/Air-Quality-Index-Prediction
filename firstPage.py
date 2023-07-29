import dash
from dash import dash_table as dt
import pandas as pd
from dash import dcc, html
import dash_bootstrap_components as dbc
from rootInformation import rootDirectory
from weatherDash import weatherComponent
from app import app


# dataset = pd.read_csv(r"C:\Users\DELL\Desktop\Air-Quality-Index-Prediction\datasets\datasetSpecifications.csv")
# breakPointTable = pd.read_csv(r"C:\Users\DELL\Desktop\Air-Quality-Index-Prediction\datasets\breakPointTable.csv")

# theImpactDictionary = {
#     'AQI':'Associated Health Impacts',
#     'Good (0 to 50)':'Minimal impact',
#     'Satisfactory (51 to 100)': 'May cause minor breathing discomfort to sensitive people.',
#     'Moderately polluted (101 to 200)':'May cause breathing discomfort to people with lung disease such as asthma, and discomfort to people with heart disease, children and older adults.',
#     'Poor (201 to 300)':'May cause breathing discomfort to people on prolonged exposure, and discomfort to people with heart disease.',
#     'Very poor (301 to 400)':'May cause respiratory illness to the people on prolonged exposure. Effect may be more pronounced in people with lung and heart diseases.',
#     'Severe (401 to 500)':'May cause respiratory impact even on healthy people, and serious health impacts on people with lung/heart disease. The health impacts may be experienced even during light physical activity.'
# }

theImpactDictionary = pd.read_csv(f"{rootDirectory}/Air-Quality-Index-Prediction/datasets/theImpactDictionary.csv")

layout = html.Div(className='mainLayout',children=[
    html.Header(children=[
        html.H1(className="mainHeader",children=["Analysis and Prediction of Air Quality in India"])
    ]),
    html.Div(className='container', children=[
        html.Div(className='firstComponent', children=[
            # html.H2("How we calculate our Air Quality Index and why we need it", id="firstHeader"),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Img(id='theImage',src=app.get_asset_url("photos/smogg.jpg"), style={
                'width':'500px',

                'height':'500px'
            }),
            html.Br(),html.Br(),
            html.P(className='para',children=[
                html.Em("When it comes to measuring air pollution, raw data is hard to understand. This is why air quality indexes are created. An air quality index (AQI) translates numerical data into a descriptive rating scale and makes it easier for citizens of all ages to understand the level of pollution in the air they breathe.")
            ])
        ]),
        html.Br(),
        html.Div(className='secondComponent', children=[
            html.H1("What is an air quality index?"),
            html.P("An air quality index is a scale used to show how polluted the air is, along with the risks associated with each rating. An AQI is calculated using established standards based on medical research for the acceptable levels of major air pollutants."),
            html.P("Air quality indexes serve two main purposes:"),            
            html.Ul(children=[
                html.Li("To inform the public about air quality in an comprehensible manner so that they may take action to protect their health"),
                html.Li("To help countries develop and assess policies for better air quality")
            ]),
            # dt.DataTable(breakPointTable.to_dict('breakPointTable'), [{"name": i, "id": i} for i in breakPointTable.columns]),
            html.P("There are many different air quality indexes used by various government agencies out there. However, none of the AQIs reviewed by us included all relevant air quality parameters for all relevant timeframes. Hence, we created a system that would process the emissions of all relevant air pollutants in a daily manner.")
        ]),
        html.Br(),
        html.Div(className='thirdComponent', children=[
            html.H1("What sets the project, Analysis and Prediction of Air Quality in India apart from the rest?"),
            # html.P("While performing a research we noticed that in most projects the Time Series Algorithms were used to perform predictions only on the historical data rather than providing the future data forecasts. On the other hand we didn't just use the algorithms to detect the current patten but also used it to predict the future data")
            html.P("While doing the research we noticed that in most projects the Time Series Algorithms were used for predicting only the historical data. Our project takes it one step further by using the Time Series Algorithms to predict the future data as well. Apart from that, we have also performed a Data Analysis."),
            html.P("Our air quality index is based on the official specifications and recommendations of various environmental authorities, including the Central Pollution Control Board (CPCB) as well as the AQIs of several cities. We had several requirements when creating our AQI:"),
            html.H2("The Dataset"),
            html.P("The dataset contains air quality data and AQI (Air Quality Index) at daily level of various stations across 26 major cities in India. Following are the specifications of the dataset:"),
            # dt.DataTable(dataset.to_dict('theDataset'), [{"name": i, "id": i} for i in dataset.columns])
           
            html.H2("Completeness: Integrating as many air pollutants as possible"),
            dbc.Row([
                html.P(
  
                    ["While performing the research it was also noticed that the majority of projects' AQI evaluate only a subset of ",
                    html.A(" Particulate Matter (PM), ", href="https://en.wikipedia.org/wiki/Particulates", target='__blank'),
                    html.A(" Nitric Oxide (NO), ", href="https://en.wikipedia.org/wiki/Nitric_oxide", target='__blank'),
                    html.A(" Nitrogen Dioxide (NO2), ", href="https://en.wikipedia.org/wiki/Nitrogen_dioxide", target='__blank'),
                    html.A(" Any Nitric Oxide (NOx), ", href="https://en.wikipedia.org/wiki/NOx", target='__blank'),
                    html.A(" Ammonia (NH3), ", href="https://en.wikipedia.org/wiki/Ammonia", target='__blank'),
                    html.A(" Carbon Monoxide (CO), ", href="https://en.wikipedia.org/wiki/Carbon_monoxide", target='__blank'),
                    html.A(" Sulfur Dioxide (SO2),", href="https://en.wikipedia.org/wiki/Sulfur_dioxide", target='__blank'),
                    html.A(" ozone (O3)", href="https://en.wikipedia.org/wiki/Ozone", target='__blank')]
                ),
                html.P("our project covers them all, even adding ammonia (NH3) to the list.")
            ]),
            
            html.H2("Applicability: Evaluate air quality on all possible time scales"),
            html.Div([
                html.P(["Other air quality indexes evaluate air pollution concentrations on time scales of either 1 hour, 8 hours, or 24 hours (aggregating measurements and rating the respective averages). We have utilized all three common timeframes (the 8-hour timeframe is currently only used for the evaluation of carbon monoxide concentrations, please refer to the ",
                html.A("dedicated paragraph below.", href="#routeHere")
                ]),  
            ]),
            html.P("While it may be acceptable for individuals to be exposed to a higher concentration of certain pollutants for a short time, this may not be the case in the long run. Because of that pollution thresholds may vary between different time scales; the overall air quality index for a full day may be worse than each individual hourly air quality index. Average measurement benchmarks for 1-hour, 8-hour, and 24-hour intervals provide more accurate air quality data, which in turn allows individuals and governments to make better health and safety decisions."),
            html.P("Our air quality index is calculated based on averages of all pollutant concentrations measured in a full hour, a full 8 hours, or a full day. To calculate an hourly air quality index, we average at least 90 measured data points of pollution concentration from a full hour (e.g. between 09:00 AM and 10:00 AM). At least 18 hourly averages are used to form a daily average."),
            html.P("There are still some limitations: As there is a current lack of scientific and medical data on the effects different levels of concentration have on human health over different amounts of time, differences between 1-hour, 8-hour, and 24-hour evaluation standards do not exist for all pollutants. We are working with scientists and legislators globally towards completing the evaluation standards for all pollutants and timeframes following scientific rigour and good practice. Currently, only pollution thresholds for particulate matter (PM10 and PM2.5) concentrations differ between the 1-hour and the 24-hour time scale. Based on the scientific status quo, threshold limits are the same for ozone, nitrogen dioxide, sulphur dioxide, ammonia, and volatile organic compounds, regardless of whether they are evaluated on a 1-hour or 24-hour time frame."),
            
            html.H2("Transparency: Make the air quality rating understandable", id='routeHere'),
            html.P("It is important to be transparent in which pollution levels result in which air quality index rating. The table below shows an overview over the air quality index"),
            html.Img(src=app.get_asset_url("photos/breakPointTable.jpg"), style={
                'width':'80vw', 
                'height':'50vh',
                'border-radius':'10px'
                }),
            html.Br(),
            html.Br()

            # html.H2("What's the AQI like today?"),
            # html.Div([weatherComponent])
            
            # dt.DataTable(theImpatDictionary.to_dict('records'), 
            #    [{"name": i, "id": i} for i in theImpactDictionary.columns], style_table={'width':'2vw'}),
            # dt.DataTable(
            #    theImpactDictionary.to_dict('records'), 
            #    [{"name": i, "id": i} for i in theImpactDictionary.columns],
            #    style_as_list_view=True,
            #    style_header={
            #         # 'backgroundColor': '#49649a',
            #         # 'color': 'white',
            #         'text-align': 'center'
            #     },
            #     style_data={
            #         # 'backgroundColor': '#95cfe0',
            #         'text-align': 'center'
            #     }
            # )
        ])
    ])
])

