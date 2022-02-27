from pydoc import classname
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
import dash
import plotly.graph_objects as go
import plotly.express as px

from dash import dcc, html, Input, Output

city = pd.read_csv("Delhi.csv")

city['Date'] = pd.to_datetime(city['Date'])

app = dash.Dash(
    __name__,
    assets_external_path=r"C:\Users\DELL\Desktop\Text Editors & Softwares\Python\Dash\assets")  

app.scripts.config.serve_locally = True

app.layout = html.Div(id = 'parent', children = [

    html.H1(className = "cityName", children ='DELHI', style = {
        'textAlign':'center',
        'marginTop':40,
        'marginBottom':40,
        'font-family': 'cursive'
        }),

    html.Br(),
    html.Br(),

    html.Div(children=[
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
                style = {
                    'width': "40%",
                    'align-items':'center',
                    'align-items':'center', 
                    'justify-content': 'center'
                    }
                ),
    ], style={'text-align':'center'}),
    html.Div(children=[
        html.Div(dcc.Graph(id = 'gasesLinedGraph', figure = {})),
        html.Div(dcc.Graph(id = 'gasesBoxPlot', figure = {})),
        html.Div(dcc.Graph(id = 'gasesMonthlyPlot', figure = {}))
    ])
], style={
    # 'background':'linear-gradient(#2b1055, #7597de)'
    'background':'beige'
})


@app.callback(
    [Output(component_id='gasesLinedGraph', component_property='figure'),
    Output(component_id='gasesBoxPlot', component_property='figure'),
    Output(component_id='gasesMonthlyPlot', component_property='figure')
    ],
    Input(component_id='slct_gas', component_property='value')
)

def dropdownGraphs(slct_gas):
    fig = px.line(city, x=city.Date, y = slct_gas)
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

    city['year'] = [d.year for d in city.Date]
    city['month'] = [d.strftime('%b') for d in city.Date]
    monthlyData = city.groupby("month", sort=False)['PM2.5','PM10','NO2','NO','NOx','NH3','CO','SO2','O3','AQI'].mean().reset_index()

    fig1 = px.box(city, x='year', y=slct_gas)
    
    fig2 = px.line(monthlyData, x='month', y=slct_gas, markers=True)
    
    return fig, fig1, fig2

if __name__ == '__main__':
    app.run_server(debug=True, port=1000)