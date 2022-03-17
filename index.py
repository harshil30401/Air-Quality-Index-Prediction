from pydoc import classname
from dash import dcc, html
# import dash_core_components as dcc
# import dash_html_components as html
from dash.dependencies import Input, Output
from app import app, server

from cities import delhi, jaipur, thiruvananthapuram, kanpur, kolkata, nagpur, hyderabad, visakhapatnam, chennai

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

app.layout = html.Div(className='cards', children=[

    html.Div(className="row", children=[
        dcc.Link("Amritsar", href='/cities/amritsar'),
        dcc.Link("Chennai", href='/cities/chennai'),
        dcc.Link("Delhi", href='/cities/delhi'),
        dcc.Link("Hyderabad", href='/cities/hyderabad'),
        dcc.Link("Jaipur", href='/cities/jaipur'),
        dcc.Link("Kanpur", href='/cities/kanpur'),
        dcc.Link("Kolkata", href='/cities/kolkata'),
        dcc.Link("Nagpur", href='/cities/nagpur'),
        dcc.Link("Thiruvananthapuram", href='/cities/thiruvananthapuram'),
        dcc.Link("Visakhapatnam", href='/cities/visakhapatnam')
    ]),

    dcc.Location(id='url', refresh=False),

    html.Div(id='page-content', children=[])
])

@app.callback(Output(component_id='page-content', component_property='children'),
            [Input(component_id='url', component_property='pathname')])

def display_page(pathname):
    
    if pathname == '/':
        pass

    elif pathname == '/cities/amritsar':
        return kanpur.layout

    elif pathname == '/cities/chennai':
        return chennai.layout

    elif pathname == '/cities/delhi':
        return delhi.layout
    
    elif pathname == '/cities/hyderabad':
        return hyderabad.layout

    elif pathname == '/cities/jaipur':
        return jaipur.layout

    elif pathname == '/cities/kanpur':
        return kanpur.layout

    elif pathname == '/cities/kolkata':
        return kolkata.layout
    
    elif pathname == '/cities/nagpur':
        return nagpur.layout
    
    elif pathname == '/cities/thiruvananthapuram':
        return thiruvananthapuram.layout

    elif pathname == '/cities/visakhapatnam':
        return visakhapatnam.layout

    else:
        return "404 Page Error! Please choose a link"

if __name__ == '__main__':
    app.run_server(debug=True)



