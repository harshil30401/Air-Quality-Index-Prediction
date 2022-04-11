from dash import dcc, html
import pandas as pd
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from app import app
from rootInformation import rootDirectory
from assets import errorpage
from cities import amritsar
from dataAnalysis import dataAnalysisFrontEnd 
import firstPage
#from cities import amritsar, chennai, delhi,  hyderabad, jaipur,  kanpur, kolkata,  mumbai, nagpur, patna, thiruvananthapuram, visakhapatnam

cities = ["amritsar"]

citiesMean = pd.read_csv(f"{rootDirectory}/Air-Quality-Index-Prediction/datasets/citiesMean.csv")

cityAQI = dict(zip(citiesMean.City, citiesMean.AQI))

navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Home", href="/firstPage")),
        dbc.NavItem(dbc.NavLink("Cities", href="/")),
        dbc.NavItem(dbc.NavLink("Data Analysis", href="/dataAnalysis/dataAnalysisFrontEnd")),

        # dbc.DropdownMenu(
        #     children=[
        #         dbc.DropdownMenuItem("More pages", header=True),
        #         dbc.DropdownMenuItem("Page 2", href="#"),
        #         dbc.DropdownMenuItem("Page 3", href="#"),
        #     ],
        #     nav=True,
        #     in_navbar=True,
        #     label="More",
        # ),
    ],
    brand="",
    brand_href="#",
    color="#1e2e32",
    dark=True,
    style={
        'position': 'sticky',
        'top': '0',
        'box-shadow': '0 2px 2px -2px rgba(0,0,0,.2)',
        'border-radius':'5px',
        'z-index': '1'
    }
)


app.layout = html.Div(id='mainDiv', className='cards', children=[
    dcc.Location(id='url', refresh=True),
    navbar,
    html.Div(id='page-content', children=[])
    ])
 
home_layout =  html.Div(id="home-page", children=[
    # html.Div(id="headerDiv", children=[
    #     html.H1(id="homeHeader", children=["Analysis and Prediction of Air Quality in India"])
    # ]),

    html.Div(className="container", children=[
        html.Div(className="card", children=[
            html.Div(className="content", children=[
                html.H2(id="cardCity", children=[city.capitalize()]),
                html.P(id="cardAQI", children=[f"Average AQI: {cityAQI[city.capitalize()]}"]),
                dbc.Button("Open Analysis", id=city, href=f'/cities/{city}', style={'color':'white'})
            ])
        ], style={'margin':'20px 20px 20px 20px'})for city in cities
    ])
])

@app.callback(Output(component_id='page-content', component_property='children'),
            [Input(component_id='url', component_property='pathname')])
def display_page(pathname):

    if pathname == '/' or pathname == '/index':
        return home_layout
        
    elif pathname == '/cities/amritsar':
        return amritsar.layout

    elif pathname == '/firstPage':
        return firstPage.layout

    elif pathname == '/dataAnalysis/dataAnalysisFrontEnd':
        return dataAnalysisFrontEnd.layout

    # elif pathname == '/cities/chennai':
    #     return chennai.layout

    # elif pathname == '/cities/delhi':
    #     return delhi.layout

    # elif pathname == '/cities/hyderabad':
    #     return hyderabad.layout

    # elif pathname == '/cities/jaipur':
    #     return jaipur.layout

    # elif pathname == '/cities/kanpur':
    #     return kanpur.layout

    # elif pathname == '/cities/kolkata':
    #     return kolkata.layout

    # elif pathname == '/cities/mumbai':
    #     return mumbai.layout
    
    # elif pathname == '/cities/nagpur':
    #     return nagpur.layout

    # elif pathname == '/cities/patna':
    #     return patna.layout
    
    # elif pathname == '/cities/thiruvananthapuram':
    #     return thiruvananthapuram.layout

    # elif pathname == '/cities/visakhapatnam':
    #     return visakhapatnam.layout

    else:
        return errorpage.layout


if __name__ == '__main__':
    app.run_server(debug=True)