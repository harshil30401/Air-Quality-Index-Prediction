import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
import dash
import plotly.graph_objects as go
import plotly.express as px

from dash import dcc, html, Input, Output

city = pd.read_csv("Delhi.csv")

city['Date'] = pd.to_datetime(city['Date'])
city.set_index('Date', inplace=True)
city = city.resample(rule='MS').mean()

app = dash.Dash()  

app.layout = html.Div(id = 'parent', children = [

    html.H1(id = 'cityName', children ='DELHI', style = {'textAlign':'center','marginTop':40,'marginBottom':40}),

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
                style = {'width': "40%"}
                ),

    html.Div(children=[
        html.Div(dcc.Graph(id = 'gasesLinedGraph', figure = {})),
        html.Div(dcc.Graph(id = 'gasesMonthlyPlot', figure = {}))
        # html.P(id = 'test', children = 'The second container would be placed here'),
    ], style={'display': 'inline-block', 'vertical-align': 'top', 'margin-left': '3vw', 'margin-top': '3vw'})


    ]
)

@app.callback(
    [Output(component_id='gasesLinedGraph', component_property='figure'),
    Output(component_id='gasesMonthlyPlot', component_property='figure')],
    Input(component_id='slct_gas', component_property='value')
)

def output_gas(slct_gas):
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
    return fig

def trend_plot(city, slct_gas):
    
    city['year'] = [d.year for d in city.Date]
    city['month'] = [d.strftime('%b') for d in city.Date]
    years = city['year'].unique()

    fig, axes = plt.subplots(1, 2, figsize=(14,6), dpi= 80)
    sns.boxplot(x='year', y = slct_gas, data=city, ax=axes[0])
    sns.pointplot(x='month', y = slct_gas, data=city.loc[~city.year.isin([2015, 2020]), :])

    axes[0].set_title('Year-wise Box Plot \n(The Trend)', fontsize=18); 
    axes[1].set_title('Month-wise Plot \n(The Seasonality)', fontsize=18)
    fig = plt.show()
    return fig


if __name__ == '__main__':
    app.run_server(debug=True)