from matplotlib.pyplot import title
import dataAnalysisBackend
from plotly.offline import init_notebook_mode, plot, iplot
import plotly.graph_objects as go
import plotly.express as px
import dash
import dash_bootstrap_components as dbc
from dash import dcc, html, Input, Output, State
from rootInformation import rootDirectory
# from app import app

indexPath = rootDirectory + '/assets/index.css'


test = dash.Dash()

def cardLayout(classname, text, figure):
    return  html.Div([ 
        dbc.Card(
            dbc.CardBody([
                html.Div([
                    html.H2(text),
                ], style={
                    'textAlign': 'center',
                    'font-style': 'Calibri',
                    'margin':'10px'
                    }),
                html.Br(),
                figure
            ])
        ),  
    ], className=classname)

test.layout = html.Div(id='dataAnalysisDiv', children=[
    html.H1(id='daTitle', children=["Data Analysis"]),
    dbc.Row(id = '00', children=[
        dcc.RadioItems(dataAnalysisBackend.gases, 'PM2.5', inline=True, id='gasRadioItems'),
        dbc.Col(children=[
            cardLayout(classname='template', text="Yearly Box Plot", figure=
            
            dcc.Graph(id='yearlyBoxPlot', 
            # text='Yearly Box Plot', 
            figure={})
            
            )
        ]),
        dbc.Col(children=[
            cardLayout(classname='template', text="Monthly Lined Graph", figure=
            
            dcc.Graph(id='monthlyLineGraph', 
            # text='Monthly Line Graph', 
            figure={})
            
            )
        ])
    ])
    
])

@test.callback(
    [Output(component_id='yearlyBoxPlot', component_property='figure'),
    Output(component_id='monthlyLineGraph', component_property='figure')],
    Input(component_id='gasRadioItems', component_property='value')
)

def gasSelectorFun(value):
    df = dataAnalysisBackend.cities.copy()

    df['year'] = [d.year for d in df.Date]
    df['month'] = [d.strftime('%b') for d in df.Date]
    df1 = df.groupby("month", sort=False)['PM2.5','PM10','NO2','NOx','NH3','CO','SO2','O3','AQI'].mean().reset_index()

    yearly = px.box(df, x='year', y=value, color="year")

    monthly = px.line(df1, x='month', y=value, markers=True)

    return yearly, monthly


if __name__ == "__main__":
    test.run_server(debug=True)