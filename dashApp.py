from matplotlib.pyplot import margins
import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc
import dash
import plotly.graph_objects as go
from dash import dcc, html, Input, Output

# from delhiForecast import *

fontStyle = "Calibri"

city = pd.read_csv("Delhi.csv")

city['Date'] = pd.to_datetime(city['Date'])
path = r"C:\Users\ansuj\OneDrive\Desktop\AQI\Air-Quality-Index-Prediction\assets\dashApp.css"
app = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP, path]
    )  

def cardLayout(figure):
    return  html.Div([
        dbc.Card(
            dbc.CardBody([
                # html.Div([
                #     html.H2(text),
                # ], style={
                #     'textAlign': 'center',
                #     'font-style':fontStyle
                #     }),
                # html.Br(),
                figure
            ])
        ),  
    ])



app.layout = html.Div(id = 'parent', children = [

    html.H1(id = 'cityName', children ='DELHI', style = {'textAlign':'center','marginTop':40,'marginBottom':40,}),

    html.Div(id="dropdown", children=[
         dcc.Dropdown(id="slct_gas",
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
                multi = False,
                value = "PM2.5",
                style = {'width': "60%", "margin":"5px", 'text-align':'center', 'margin-left':'auto','margin-right':'auto'}
                # 'backgroundColor': "#ffffff","
                # 'width':'20vH',
                # 'height':'40px'}   
                ),
    ]),

    html.Div(children=[

        dbc.Card(
            dbc.CardBody([
                dbc.Row([
                    cardLayout(html.Div(dcc.Graph(id = 'gasesLinedGraph', figure = {})))
                ], style={'padding':'5px', 'color':'blue'}),
                dbc.Row([
                    dbc.Col([
                        cardLayout(html.Div(dcc.Graph(id = 'gasesBoxPlot', figure = {})))
                    ], width=7),
                    dbc.Col([
                        cardLayout(html.Div(dcc.Graph(id = 'gasesMonthlyPlot', figure = {})))
                    ], width=5)
                ])
            ])
        ),
    ]),
    
    html.Br()

], style={'border':'none'})


@app.callback(
    [Output(component_id='gasesLinedGraph', component_property='figure'),
    Output(component_id='gasesBoxPlot', component_property='figure'),
    Output(component_id='gasesMonthlyPlot', component_property='figure')
    ],
    Input(component_id='slct_gas', component_property='value')
)

def dropdownGraphs(slct_gas):
    fig = px.line(city, x=city.Date, y = slct_gas, title="Emission of "+ slct_gas )
    fig.update_xaxes(
        rangeslider_visible= True,
        rangeselector=dict(
                            buttons = list([
                            dict(count = 17, label = 'The Lockdown Period',step='month',stepmode = "backward"),
                            dict(step = 'all', label = slct_gas)
                                ])        
                            )
                    )
    fig.update_layout(
        xaxis_title="Date",
    )
    fig.layout.template = 'ggplot2'

    city['year'] = [d.year for d in city.Date]
    city['month'] = [d.strftime('%b') for d in city.Date]
    monthlyData = city.groupby("month", sort=False)['PM2.5','PM10','NO2','NO','NOx','NH3','CO','SO2','O3','AQI'].mean().reset_index()

    fig1 = px.box(city, x='year', y=slct_gas, title= "Yearly Box Plot")
    fig1.layout.template = 'ggplot2'

    fig2 = px.line(monthlyData, x='month', y=slct_gas, markers=True, title="Monthly "+slct_gas+" Trend")
    fig2.layout.template = 'ggplot2'

    return fig, fig1, fig2

if __name__ == '__main__':
    app.run_server(debug=True)