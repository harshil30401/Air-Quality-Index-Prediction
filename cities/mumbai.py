from turtle import position
import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc
from dash import dcc, html, Input, Output, State
from app import app
from rootInformation import rootDirectory
from backend.mumbaiBackend import MumbaiMainElements
from cities.frontEndBluePrint import headerComponent
import math

fontStyle = "Calibri"

cityName = "Mumbai"
file = f"{rootDirectory}/Air-Quality-Index-Prediction/datasets/{cityName}.csv"
city = pd.read_csv(file, parse_dates=True)
city = city[city["Date"] >= "2018-06-18"]


citiesMean = pd.read_csv(
    f"{rootDirectory}/Air-Quality-Index-Prediction/datasets/citiesMean.csv")
cityAQI = dict(zip(citiesMean.City, citiesMean.AQI))

city['Date'] = pd.to_datetime(city['Date'])
path = "../static/dashApp.css"
# app = dash.Dash(
#     __name__,
#     external_stylesheets=[dbc.themes.BOOTSTRAP, path]
#     )


def cardLayout(figure):
    return html.Div([
        dbc.Card(
            dbc.CardBody([
                figure
            ])
        ),
    ])


navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Page 1", href="#")),
        dbc.NavItem(dbc.NavLink("Cities", href="/")),
        dbc.DropdownMenu(
            children=[
                dbc.DropdownMenuItem("More pages", header=True),
                dbc.DropdownMenuItem("Page 2", href="#"),
                dbc.DropdownMenuItem("Page 3", href="#"),
            ],
            nav=True,
            in_navbar=True,
            label="More",
        ),
    ],
    brand=cityName,
    brand_href="#",
    color="#1e2e32",
    dark=True,
    style={
        'position': 'sticky',
        'top': '0',
        'box-shadow': '0 2px 2px -2px rgba(0,0,0,.2)',
        'border-radius':'5px',
        'z-index': '1',
        'margin-bottom': '15px'
    }
)


# app.title = "Analysis and Prediction of Air Quality in India"

# html.Div(id = 'parent', children = [layout])

layout = html.Div(id='mumbaiParent', children=[

    # html.Header(id='header', children=[
    #     html.H1("Mumbai")
    #     # html.Img(id='displayImage',src=app.get_asset_url(f"{rootDirectory}/Air-Quality-Index-Prediction/photos/mumbai.jpg"))
    # ]),
    headerComponent(cityName, "June 2018", math.floor(cityAQI[cityName])),

    html.Div(id='mainBody', children=[

        # navbar,
        html.Div(id="dropdown", children=[
            dcc.Dropdown(id=f"slct_gas{cityName}",
                 options=[
                    {"label": "PM2.5", "value": "PM2.5"},
                    {"label": "PM10", "value": "PM10"},
                    {"label": "NO", "value": "NO"},
                    {"label": "NO2", "value": "NO2"},
                    {"label": "NOx", "value": "NOx"},
                    {"label": "NH3", "value": "NH3"},
                    {"label": "CO", "value": "CO"},
                    {"label": "SO2", "value": "SO2"},
                    {"label": "O3", "value": "O3"},
                    {"label": "AQI", "value": "AQI"}
                 ],
            searchable=False,
             multi=False,
             value="PM2.5",
             style={
                     "width": "55%",
                     "margin": "5px",
                     'text-align': 'center',
                     'margin-left': 'auto',
                     'margin-right': 'auto',
                     'border-color': '#355863',
                     'box-shadow': '5px',
                 }
             # 'backgroundColor': "#ffffff","
                # 'width':'20vH',
                # 'height':'40px'}
             ),
        ]),


        dbc.Card(
            dbc.CardBody(id='card', children=[

                dbc.Row(className='cardBody', children=[
                    cardLayout(html.Div(
                        dcc.Graph(id='mumbaiGasesLinedGraph', className='graphPlot', figure={})))
                ], style={'padding': '5px', 'color': 'blue'}),

                dbc.Row(children=[

                    dbc.Col(className='cardBody', children=[
                        cardLayout(html.Div(
                            dcc.Graph(id='mumbaiGasesBoxPlot', className='graphPlot', figure={})))
                    ], width=7),

                    dbc.Col(className='cardBody', children=[
                        cardLayout(html.Div(
                            dcc.Graph(id='mumbaiGasesMonthlyPlot', className='graphPlot', figure={})))
                    ], width=5)
                ]),
                html.Br(), html.Br(),

                dbc.Row(children=[
                    cardLayout(html.Iframe(srcDoc=MumbaiMainElements.html_arima(), style={
                        'height': '500px',
                        'width': '1450px',
                    })),
                    html.Br(), html.Br(),
                    html.P(
                        'Data of variable pollution concentrations have been taken from the official website of central pollution control board. The filtered format of the data has been used for the AQI calculation. From the above graph it can be observed that the AQI concentration since the year 2017 follows a seasonal format and has a constant trend. The graph is the result of ARIMA timeseries algorithm which has provided the best outcome. It shows that in the year 2022, the AQI of Mumbai would follow the same trend as before with an increase during Diwali and gradual decrease during the rainy season with a slight increase during the summer season.'
                    ),
                    html.Br(), html.Br(),
                ]),


                html.Div(id=f'buttonDiv{cityName}', children=[
                    dbc.Button(
                        ["Comparitive Analysis of Algorithms  ",
                         html.Div(className='rotate', children=[
                            html.I(className="bi bi-chevron-down")
                         ])],
                        id=f"mum-collapse-button{cityName}",
                        className="mb-3",
                        color="primary",
                        n_clicks=0,
                        style={"padding": "15px", "background": "#355863",
                               'text-align': 'center'},
                    )
                ], style={"padding-left": "40%"}),

                dbc.Row(children=[
                    dbc.Collapse(id=f'mum-collapse{cityName}', is_open=False, children=[
                        dcc.Dropdown(id=f"slct_metric{cityName}",
                                     options=[

                                         {"label": "Mean Absolute Error",
                                             "value": "mae"},
                                         {"label": "Mean Absolute Percentage Error",
                                          "value": "mape"},
                                         {"label": "Mean Error", "value": "me"},
                                         {"label": "Mean Percentage Error",
                                             "value": "mpe"},
                                         {"label": "Mean Square Error",
                                             "value": "mse"},
                                         {"label": "Root Mean Square Error",
                                             "value": "rmse"}

                                     ],
                                     searchable=False,
                                     multi=False,
                                     value="rmse",
                                     style={'width': "60%", "margin": "5px", 'text-align': 'center',
                                            'margin-left': 'auto', 'margin-right': 'auto'}
                                     ),

                        cardLayout(
                            html.Iframe(id=f"mum-comp_analysis{cityName}", srcDoc="", style={
                                'height': '500px',
                                'width': '1450px',
                            })
                        ),
                        html.Br(), html.Br(),
                        html.P(
                            'After comparing four timeseries algorithms viz. ARIMA, Facebook Prophet, LSTM RNN, Exponential Smoothing, it can be observed that, ARIMAs Rolling Forecast gives the least amount of error. ETS and FB Probhet give compatible outputs whereas ast LSTM RNN has the least accuracy as Machine Learning algorithms require large series of data.'
                        ),
                        html.Br(), html.Br(),
                    ])
                ]),

                dbc.Row(children=[
                    cardLayout(html.Iframe(srcDoc=MumbaiMainElements.comparingScenarios(), style={
                        'height': '500px',
                        'width': '1450px',
                    })),
                    html.Br(), html.Br(),
                    html.P(
                        'Due to the lockdown, there was a sudden decrease in the industrial and vehicular gas emissions which resulted a decrease in the AQI level In case the lockdown didnt exist, the emission wouldnt had tappered in the year 2020 and 2021. If the emmision of gas was not affected by anything, the AQI concentration would have followed the seasonal trend and there would be a slight increase in the AQI as compared to the current scenario'
                    ),
                    html.Br(), html.Br(),
                ])
            ])
        ),
    ]),

], style={'border': 'none'})


@app.callback(
    Output(component_id=f'mum-comp_analysis{cityName}', component_property='srcDoc'),
    Input(component_id=f'slct_metric{cityName}', component_property='value')
)
def comparitiveAnalysis(value):
    if value == "rmse":
        srcDoc = MumbaiMainElements.comparativeAnalysisRMSE()
    elif value == "mape":
        srcDoc = MumbaiMainElements.comparativeAnalysisMAPE()
    elif value == "mae":
        srcDoc = MumbaiMainElements.comparativeAnalysisMAE()
    elif value == "me":
        srcDoc = MumbaiMainElements.comparativeAnalysisME()
    elif value == "mse":
        srcDoc = MumbaiMainElements.comparativeAnalysisMSE()
    elif value == "mpe":
        srcDoc = MumbaiMainElements.comparativeAnalysisMPE()
    else:
        srcDoc = None

    return srcDoc


@app.callback(
    [Output(component_id='mumbaiGasesLinedGraph', component_property='figure'),
     Output(component_id='mumbaiGasesBoxPlot', component_property='figure'),
     Output(component_id='mumbaiGasesMonthlyPlot',
            component_property='figure')
     ],
    Input(component_id=f'slct_gas{cityName}', component_property='value')
)
def dropdownGraphs(slct_gas):
    fig = px.line(city, x=city.Date, y=slct_gas,
                  title="Emission of " + slct_gas)
    fig.update_xaxes(
        rangeslider_visible=True,
        rangeselector=dict(
            buttons=list([
                dict(count=17, label='The Lockdown Period',
                     step='month', stepmode="backward"),
                dict(step='all', label=slct_gas)
            ])
        )
    )
    fig.update_layout(
        xaxis_title="Date",
        # paper_bgcolor='aqua',
        # plot_bgcolor='aqua'
    )
    fig.layout.template = 'seaborn'

    city['year'] = [d.year for d in city.Date]
    city['month'] = [d.strftime('%b') for d in city.Date]
    monthlyData = city.groupby("month", sort=False)[
        'PM2.5', 'PM10', 'NO2', 'NO', 'NOx', 'NH3', 'CO', 'SO2', 'O3', 'AQI'].mean().reset_index()

    fig1 = px.box(city, x='year', y=slct_gas, title="Yearly Box Plot")
    fig1.layout.template = 'seaborn'

    fig2 = px.line(monthlyData, x='month', y=slct_gas,
                   markers=True, title="Monthly "+slct_gas+" Trend")
    fig2.layout.template = 'seaborn'

    return fig, fig1, fig2


@app.callback(
    Output(f"mum-collapse{cityName}", "is_open"),
    [Input(f"mum-collapse-button{cityName}", "n_clicks")],
    [State(f"mum-collapse{cityName}", "is_open")],
)
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open
