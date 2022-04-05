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
    dcc.RadioItems(dataAnalysisBackend.gases, 'PM2.5', inline=True, id='gasRadioItems'),
    dbc.Row(id = '00', children=[
        dbc.Col(children=[
            cardLayout(classname='template', text="Yearly Box Plot", figure=
            
            dcc.Graph(id='yearlyBoxPlot', 
            figure={})
            
            )
        ], width=7),
        dbc.Col(children=[
            cardLayout(classname='template', text="Monthly Lined Graph", figure=
            
            dcc.Graph(id='monthlyLineGraph', 
            figure={})
            
            )
        ], width=5),
    ]),
    dbc.Row(children=[
        cardLayout(classname='template', text='' ,figure=
        
        dcc.Graph(id='top10', 
        figure={})
        
        )
    ])
    
])

@test.callback(
    [Output(component_id='yearlyBoxPlot', component_property='figure'),
    Output(component_id='monthlyLineGraph', component_property='figure'),
    Output(component_id='top10', component_property='figure')],
    Input(component_id='gasRadioItems', component_property='value')
)

def gasSelectorFun(value):
    df = dataAnalysisBackend.cities.copy()

    df['year'] = [d.year for d in df.Date]
    df['month'] = [d.strftime('%b') for d in df.Date]
    df1 = df.groupby("month", sort=False)['PM2.5','PM10','NO2','NOx','NH3','CO','SO2','O3','AQI'].mean().reset_index()

    yearly = px.box(df, x='year', y=value, color="year")

    monthly = px.line(df1, x='month', y=value, markers=True)


    x = dataAnalysisBackend.cities.groupby("City")[value].mean().sort_values(ascending=False).reset_index()
    trace = go.Table(
        domain=dict(x=[0, 0.52], y=[0, 1.0]),
        header=dict(
            values=["City", value],
            fill=dict(color="red"),
            font=dict(color="white", size=14),
            align=["center"],
            height=30,
        ),
        cells=dict(
            values=[x["City"].head(10), x[value].head(10)],
            fill=dict(color=["lightsalmon", "lightsalmon"]),
            align=["center"],
        ),
    )

    trace1 = go.Bar(
        x=x["City"].head(10),
        y=x[value].head(10),
        xaxis="x1",
        yaxis="y1",
        marker=dict(color="red"),
        opacity=0.60,
    )
    layout = dict(
        width=1450,
        height=500,
        autosize=False,
        title=f"TOP 10 Cities with Max {value}",
        showlegend=False,
        xaxis1=dict(**dict(domain=[0.58, 1], anchor="y1", showticklabels=True)),
        yaxis1=dict(**dict(domain=[0, 1.0], anchor="x1", hoverformat=".2f")),
    )

    top10 = dict(data=[trace, trace1], layout=layout)

    return yearly, monthly, top10


if __name__ == "__main__":
    test.run_server(debug=True)