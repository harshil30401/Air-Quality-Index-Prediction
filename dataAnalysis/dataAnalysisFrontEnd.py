import imp
import pandas as pd
from turtle import st
from click import style
from matplotlib.pyplot import title
from numpy import mean
from dataAnalysis import dataAnalysisBackend as da
from dataAnalysis import dataAnalysisBackend
from plotly.offline import init_notebook_mode, plot, iplot
import plotly.graph_objects as go
import plotly.express as px
import dash
import dash_daq as daq
import dash_bootstrap_components as dbc
from dash import dcc, html, Input, Output, State, dash_table
from rootInformation import rootDirectory
from app import app
indexPath = rootDirectory + '/static/index.css'

meanData = pd.read_csv(f'{rootDirectory}/Air-Quality-Index-Prediction/datasets/citiesMean.csv')
meanData = meanData[['City','AQI','AQI_Bucket']]
# .drop(columns=['Unnamed: 0', 'Lat', 'Lon', 'PM2.5', 'PM10', 'NO2', 'NOx', 'NH3', 'CO', 'SO2', 'O3',], axis=0, inplace=True)





def cardLayout(classname, text, figure):
    return  dbc.Card(
                dbc.CardBody([
                    html.Div([
                        html.H2(text),
                    ], style={
                        'textAlign': 'center',
                        'font-style': 'Calibri',
                        'margin': '10px'
                    }),
                    html.Br(),
                    figure
                ]),
                className=classname
            )



layout = html.Div(id='dataAnalysisDiv', children=[
    html.H1(id='daTitle', children=["Data Analysis"]),
    html.Br(),
    dbc.Row(id='00', children=[
        dbc.Col([
            dbc.Card([
                html.Br(),
                html.H3(children=["Gases"]),
                html.Br(),
                html.Br(),
                dcc.RadioItems(dataAnalysisBackend.gases, 'PM2.5',
                    id='gasRadioItems', 
                    labelStyle={'display': 'block', 'margin-bottom': '30px'}
                ),
                html.Br()
            ])
        ], width=2, style={ 'text-align': 'center'}),
        dbc.Col(children=[
            cardLayout(classname='template', text="Yearly Box Plot", 
                figure=dcc.Graph(id='yearlyBoxPlot', figure={})
                       )
        ], width=5),
        dbc.Col(children=[
            cardLayout(classname='template', text="Monthly Lined Graph",
                figure=dcc.Graph(id='monthlyLineGraph', figure={})
                       )
        ], width=5, style={'margin-bottom': '10px'}),
    ]),
    dbc.Row(children=[
        dbc.Card([
            daq.ToggleSwitch(
                id='toporbottom',
                label=['Top 10 cities', 'Bottom 10 cities'],
                value='True',
                style={'width': '55%', 'margin': '10px', 'postion':'right'}),
            dcc.Graph(id='ten', figure={},
                style={'height': '62vh',
                        'width': '88vw',
                        'margin-bottom': '10px'
                        })
        ])
    ], style={'margin': '40px 5px'}),
    dbc.Row(children=[
        dbc.Col([
           dash_table.DataTable(
               meanData.to_dict('records'), 
               [{"name": i, "id": i} for i in meanData.columns],
               style_as_list_view=True,
               style_header={
                    # 'backgroundColor': '#49649a',
                    # 'color': 'white',
                    'text-align': 'center'
                },
                style_data={
                    # 'backgroundColor': '#95cfe0',
                    'text-align': 'center'
                }
            )
        ], width=4),
        dbc.Col([
           cardLayout(
           classname='template',text='Air Quality Index',
           figure=html.Iframe(srcDoc=da.aqiLevel, style={
                'height': '66vh',
                'width': '60vw',
                'overflow-x': 'hidden',
                'overflow-y': 'hidden'
            })
            ) 
        ], width=8)
    ]),
    html.Br(),
    dbc.Row([
        cardLayout(
           classname='template',text='Effects of Lockdown on AQI',
           figure=html.Iframe(srcDoc=da.aqiBeforeAndAfter, style={
                'width': '90vw',
                'height': '60vh',
            })
        ) 
    ],style={'margin': '2px'}),
    dbc.Row([
        cardLayout(classname='template',text='Situation Before and After the Lockdown',
            figure=html.Iframe(srcDoc=da.m.get_root().render(), style={'width':'90vw', 'height':'65Vh'})
        )
    ],style={'margin': ' 10px 2px'}),
    dbc.Row([
        cardLayout(classname='template',text='AQI Breakdown of India',
            figure=html.Iframe(srcDoc=da.map.get_root().render(), style={'width':'90vw', 'height':'85vh'})
        )
    ],style={'margin': ' 10px 2px'})

], style={'overflow-x': 'hidden', 'padding': '40px'})

@app.callback(
    [Output(component_id='yearlyBoxPlot', component_property='figure'),
     Output(component_id='monthlyLineGraph', component_property='figure'),
     Output(component_id='ten', component_property='figure')],
    [Input(component_id='gasRadioItems', component_property='value'),
    Input(component_id='toporbottom', component_property='value')]

)
def gasSelectorFun(value1, value2):
    df = dataAnalysisBackend.cities.copy()

    df['year'] = [d.year for d in df.Date]
    df['month'] = [d.strftime('%b') for d in df.Date]
    df1 = df.groupby("month", sort=False)[
        'PM2.5', 'PM10', 'NO2', 'NOx', 'NH3', 'CO', 'SO2', 'O3', 'AQI'].mean().reset_index()

    yearly = px.box(df, x='year', y=value1, color="year")

    monthly = px.line(df1, x='month', y=value1, markers=True)
    

    if (value2):
        x = dataAnalysisBackend.cities.groupby(
            "City")[value1].mean().sort_values(ascending=False).reset_index()
        trace = go.Table(
            domain=dict(x=[0, 0.52], y=[0, 1.0]),
            header=dict(
                values=["City", value1],
                fill=dict(color="green"),
                font=dict(color="white", size=14),
                align=["center"],
                height=30,
            ),
            cells=dict(
                values=[x["City"].tail(10), x[value1].tail(10)],
                fill=dict(color=["lightgreen", "lightgreen"]),
                align=["center"],
            ),
        )

        trace1 = go.Bar(
            x=x["City"].tail(10),
            y=x[value1].tail(10),
            xaxis="x1",
            yaxis="y1",
            marker=dict(color="green"),
            opacity=0.60,
        )
        layout = dict(
            autosize=False,
            title=f"Bottom 10 Cities with Max {value1}",
            showlegend=False,
            xaxis1=dict(**dict(domain=[0.58, 1],
                        anchor="y1", showticklabels=True)),
            yaxis1=dict(**dict(domain=[0, 1.0], anchor="x1", hoverformat=".2f")),
        )

        ten = dict(data=[trace, trace1], layout=layout)
    else:
        x = dataAnalysisBackend.cities.groupby(
            "City")[value1].mean().sort_values(ascending=False).reset_index()
        trace = go.Table(
            domain=dict(x=[0, 0.52], y=[0, 1.0]),
            header=dict(
                values=["City", value1],
                fill=dict(color="red"),
                font=dict(color="white", size=14),
                align=["center"],
                height=30,
            ),
            cells=dict(
                values=[x["City"].head(10), x[value1].head(10)],
                fill=dict(color=["lightsalmon", "lightsalmon"]),
                align=["center"],
            ),
        )

        trace1 = go.Bar(
            x=x["City"].head(10),
            y=x[value1].head(10),
            xaxis="x1",
            yaxis="y1",
            marker=dict(color="red"),
            opacity=0.60,
        )
        layout = dict(
            autosize=False,
            title=f"Top 10 Cities with Max {value1}",
            showlegend=False,
            xaxis1=dict(**dict(domain=[0.58, 1],
                        anchor="y1", showticklabels=True)),
            yaxis1=dict(**dict(domain=[0, 1.0], anchor="x1", hoverformat=".2f")),
        )

        ten = dict(data=[trace, trace1], layout=layout)


    return yearly, monthly, ten



