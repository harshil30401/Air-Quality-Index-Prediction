from msilib.schema import Component
from os import link
from turtle import onclick
from click import style
from dash import dcc, html
# import dash_core_components as dcc
# import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
from app import app, server

#from cities import amritsar, delhi, jaipur, thiruvananthapuram, kanpur, kolkata, nagpur, hyderabad, visakhapatnam, chennai, mumbai
from cities import amritsar, chennai


# prev_dump = html.Div(id="flip-container", children=[
#         html.Div(className="flip-inner-container", children=[
           
#             html.Div(className="flip-front", children=[
#                 html.Img(src="delhiCard.jpg")
#             ]),

#             html.Div(className="flip-back", children=[
#                 html.Div(className="profile-image", children=[
#                     html.Img(src="delhi.jpg"),
#                     html.H2("Code Info"),
#                     html.P("Web Developer | Content Creator | Youtuber"),
#                     html.Ul(children=[
#                         html.I(className="fab fa-facebook-f"),
#                         html.I(className="fab fa-instagram"),
#                         html.I(className="fab fa-youtube")
#                     ])
#                 ])
#             ])

#         ])
#     ])


app.layout = html.Div(className='cards', children=[


    dbc.Collapse(
        html.Div(id = 'row', className="d-grid gap-2 d-md-flex justify-content-md-end", children=[
        dbc.Button(
            id="amritsar",
            className="mb-3",
            color="primary",
            children=[dcc.Link("Amritsar", href='/cities/amritsar', className="me-md-2"),
        ]),

        dbc.Button(
            id="chennai",
            className="mb-3",
            color="primary",
            children=[dcc.Link("Chennai", href='/cities/chennai', className="me-md-2"),
        ])

        # dcc.Link("Amritsar", href='/cities/amritsar', className='city'),
        # dcc.Link("Chennai", href='/cities/chennai')
        # dcc.Link("Delhi", href='/cities/delhi'),
        # dcc.Link("Hyderabad", href='/cities/hyderabad'),
        # dcc.Link("Jaipur", href='/cities/jaipur'),
        # dcc.Link("Kanpur", href='/cities/kanpur'),
        # dcc.Link("Kolkata", href='/cities/kolkata'),
        # dcc.Link("Mumbai", href='/cities/mumbai'),        
        # dcc.Link("Nagpur", href='/cities/nagpur'),
        # dcc.Link("Thiruvananthapuram", href='/cities/thiruvananthapuram'),
        # dcc.Link("Visakhapatnam", href='/cities/visakhapatnam')
    ]),id = "collapse-1", is_open=True
    ),

    dcc.Location(id='url', refresh=False),

    html.Div(id='page-content', children=[])
])


@app.callback(
    Output("collapse-1", "is_open"),
    [Input(component_id='amritsar', component_property="n_clicks")],
    [State("collapse-1", "is_open")]
)

@app.callback(
    Output(component_id='page-content', component_property='children'),
    [Input(component_id='url', component_property='pathname')]
)

def toggle_collapse(n_clicks, is_open):
    if n_clicks:
        return not is_open
    return 



def display_page(pathname):

    
    if pathname == '/':
        pass

    elif pathname == '/cities/amritsar':
        return amritsar.layout

    elif pathname == '/cities/chennai':
        return chennai.layout

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
    
    # elif pathname == '/cities/thiruvananthapuram':
    #     return thiruvananthapuram.layout

    # elif pathname == '/cities/visakhapatnam':
    #     return visakhapatnam.layout

    else:
        return "404 Page Error! Please choose a link"


if __name__ == '__main__':
    app.run_server(debug=True)