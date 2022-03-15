from asyncio.windows_events import NULL
from pydoc import classname
from dash import dcc, html
# import dash_core_components as dcc
# import dash_html_components as html
from dash.dependencies import Input, Output
from app import app, server

from cities import delhi

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
        dcc.Link("Delhi", href='/cities/delhi')
    ]),

    dcc.Location(id='url', refresh=False),

    html.Div(id='page-content', children=[])
])

@app.callback(Output(component_id='page-content', component_property='children'),
            [Input(component_id='url', component_property='pathname')])

def display_page(pathname):
    if pathname == '/cities/delhi':
        return delhi.layout
    
    elif pathname == '/':
        pass
    # if pathname == '/cities/mumbai':
    #     return cities.layout
    else:
        return "404 Page Error! Please choose a link"

if __name__ == '__main__':
    app.run_server(debug=True)



