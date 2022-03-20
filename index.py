from dash import dcc, html
# import dash_core_components as dcc
# import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from app import app, server
from assets import errorpage
#from cities import amritsar, delhi, jaipur, thiruvananthapuram, kanpur, kolkata, nagpur, hyderabad, visakhapatnam, chennai, mumbai
from cities import amritsar, chennai, delhi

cities = ["amritsar","chennai",  "delhi"]
#, "jaipur", "thiruvananthapuram", "kanpur", "kolkata", "nagpur", "hyderabad", "visakhapatnam", "mumbai"

prev_dump = html.Div(id="flip-container", children=[
        html.Div(className="flip-inner-container", children=[
           
            html.Div(className="flip-front", children=[
                html.Img(src="delhiCard.jpg")
            ]),

            html.Div(className="flip-back", children=[
                html.Div(className="profile-image", children=[
                    html.Img(src="delhi.jpg"),
                    html.H2("Code Info"),
                    html.P("Web Developer | Content Creator | Youtuber"),
                    html.Ul(children=[
                        html.I(className="fab fa-facebook-f"),
                        html.I(className="fab fa-instagram"),
                        html.I(className="fab fa-youtube")
                    ])
                ])
            ])

        ])
    ])

home_layout =  html.Div(id="home-page", children=[
    html.Div(id="headerDiv", children=[
        html.H1(id="homeHeader", children=["Analysis and Prediction of Air Quality in India"])
    ]),

    html.Div(id="cardDiv", children=[
        # dbc.Button("Amritsar", id="amritsar", href="/cities/amritsar", style={"color":"white"}),
        # dbc.Button("Chennai", id="chennai", href="/cities/chennai", style={"color":"white"}),
        # dbc.Button("Delhi", id="delhi", href="/cities/delhi", style={"color":"white"})
        dbc.Button(city.capitalize(), id=city, href=f'/cities/{city}', style={'color':'white'}) for city in cities
    ])

])


app.layout = html.Div(id='mainDiv', className='cards', children=[
    html.Div(id='headerDiv', children=[
            html.H1(id='header', children=["Analysis and Prediction of Air Quality in India"])
    ], style={'align':'center'}),

    # html.Div(id="elements", children=[

        # html.H1(id="header",children=["Analysis and Prediction of Air Quality in India"]),

        # dbc.Button(city.capitalize(), id=city, href=f'/cities/{city}', style={'color':'white'}
        # )for city in cities
        # dbc.Button(id='chennai', children=[
        #     dcc.Link("Chennai", href='/cities/chennai'),
        # ]),
        # # dcc.Link("Delhi", href='/cities/delhi'),
        # # dcc.Link("Hyderabad", href='/cities/hyderabad'),
        # # dcc.Link("Jaipur", href='/cities/jaipur'),
        # # dcc.Link("Kanpur", href='/cities/kanpur'),
        # # dcc.Link("Kolkata", href='/cities/kolkata'),
        # # dcc.Link("Mumbai", href='/cities/mumbai'),        
        # # dcc.Link("Nagpur", href='/cities/nagpur'),
        # # dcc.Link("Thiruvananthapuram", href='/cities/thiruvananthapuram'),
        # # dcc.Link("Visakhapatnam", href='/cities/visakhapatnam')
    # ], hidden=False)

    # html.Div(id='page-content', children=[])
    dcc.Location(id='url', refresh=False)

    ])

@app.callback(Output(component_id='mainDiv', component_property='children'),
            [Input(component_id='url', component_property='pathname')])
def display_page(pathname):

    if pathname == '/':
        return home_layout
        
    elif pathname == '/cities/amritsar':
        return amritsar.layout

    elif pathname == '/cities/chennai':
        return chennai.layout

    elif pathname == '/cities/delhi':
        return delhi.layout
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
    
    # elif pathname == '/cities/thiruvananthapuram':
    #     return thiruvananthapuram.layout

    # elif pathname == '/cities/visakhapatnam':
    #     return visakhapatnam.layout

    else:
        return errorpage.layout


# @app.callback(
#     Output(component_id='elements', component_property='hidden'),
#     [Input(component_id= "amritsar" , component_property='n_clicks')],
#     [Input(component_id='chennai', component_property='n_clicks')],
#     [Input(component_id='delhi', component_property='n_clicks')]
# )

# def hideDiv(n1, n2, n3):
#     if (n1 or n2 or n3) != None:
#         return True 
#     return False

if __name__ == '__main__':
    app.run_server(debug=True)