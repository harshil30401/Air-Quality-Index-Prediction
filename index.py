from dash import dcc, html
import pandas as pd
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from app import app
from rootInformation import rootDirectory
from static import errorpage
from cities import amaravati
# , amritsar, bengaluru, chennai, delhi, gandhinagar, hyderabad, jaipur, jodhpur, kanpur, kolkata, lucknow, mumbai, nagpur, patna, pune, thiruvananthapuram, visakhapatnam
# ahmedabad, 
from dataAnalysis import dataAnalysisFrontEnd 
import firstPage, about

cities = ["amaravati"]
# , "amritsar", "bengaluru","chennai", "delhi", "gandhinagar", "hyderabad", "jaipur", "jodhpur", "kanpur", "kolkata", "lucknow", "mumbai", "nagpur", "patna", "pune", "thiruvananthapuram", "visakhapatnam"] 
# , "delhi", "gandhinagar", "hyderabad", "jaipur", "jodhpur", "kanpur", "kolkata", "lucknow", "mumbai", "nagpur", "patna", "pune", "thiruvananthapuram", "visakhapatnam"]

citiesMean = pd.read_csv(f"{rootDirectory}/Air-Quality-Index-Prediction/datasets/citiesMean.csv")

cityAQI = dict(zip(citiesMean.City, citiesMean.AQI))

def makeNavigationBar():



    return dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Cities", href="/cities")),
        dbc.NavItem(dbc.NavLink("Home", href="/")),
        dbc.NavItem(dbc.NavLink("Data Analysis", href="/dataAnalysis/dataAnalysisFrontEnd")),
        dbc.NavItem(dbc.NavLink("About", href="/about"))

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
        # 'width':"100%",
        'position': 'sticky',
        'top': '0',
        'box-shadow': '0 2px 2px -2px rgba(0,0,0,.2)',
        'border-radius':'5px',
        'z-index': '3',
        'margin-top': '',
    }, id='theNavbar'
)
    # <link rel="website icon" type="png" href="logo.png">

app.layout = html.Div(id='mainDiv', className='cards', children=[
    dcc.Location(id='url', refresh=True),
    makeNavigationBar(),
    html.Div(id='page-content', children=[])
    ])
 
home_layout =  html.Div(id="home-page", children=[
    # html.Div(id="headerDiv", children=[
    #     html.H1(id="homeHeader", children=["Analysis and Prediction of Air Quality in India"])
    # ]),

    html.Div(className="container", children=[
        html.Div(className="card", children=[
            html.Div(className="content", children=[
                html.H5(id="cardCity", children=[city.capitalize()], style={'font-family':'bold'}),
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
        return firstPage.layout

    elif pathname == '/cities':
        return home_layout

    elif pathname == '/dataAnalysis/dataAnalysisFrontEnd':
        return dataAnalysisFrontEnd.layout

    elif pathname == '/about':
        return about.layout
        
    # elif pathname == '/cities/ahmedabad':    # Input contains nan at \backendBluePrint.py", line 53, in theBluePrint auto_arima(y=lim_city,start_p=0,start_P=0,start_q=0,start_Q=0,seasonal=True, m=12).summary()
    #     return ahmedabad.layout
        
    elif pathname == '/cities/amaravati':
        return amaravati.layout
        
    # elif pathname == '/cities/amritsar':
    #     return amritsar.layout
        
    # elif pathname == '/cities/bengaluru':
    #     return bengaluru.layout

    # elif pathname == '/cities/chennai':
    #     return chennai.layout

    # elif pathname == '/cities/delhi':
    #     return delhi.layout
        
    # elif pathname == '/cities/gandhinagar':
    #     return gandhinagar.layout

    # elif pathname == '/cities/hyderabad':
    #     return hyderabad.layout

    # elif pathname == '/cities/jaipur':
    #     return jaipur.layout
        
    # elif pathname == '/cities/jhodhpur':
    #     return jodhpur.layout

    # elif pathname == '/cities/kanpur':
    #     return kanpur.layout

    # elif pathname == '/cities/kolkata':
    #     return kolkata.layout
        
    # elif pathname == '/cities/lucknow':
    #     return lucknow.layout

    # elif pathname == '/cities/mumbai':
    #     return mumbai.layout
    
    # elif pathname == '/cities/nagpur':
    #     return nagpur.layout

    # elif pathname == '/cities/patna':
    #     return patna.layout
        
    # elif pathname == '/cities/pune':
    #     return pune.layout
    
    # elif pathname == '/cities/thiruvananthapuram':
    #     return thiruvananthapuram.layout

    # elif pathname == '/cities/visakhapatnam':
    #     return visakhapatnam.layout

    else:
        return errorpage.layout


if __name__ == '__main__':
    app.run_server(debug=True)