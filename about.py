import dash_html_components as html
from app import app


def createTile(image, name, summary):
    return html.Div(className="data", children=[
        html.Div(className="profile", children=[
            html.Img(className="photo", src=app.get_asset_url(f"photos/{image}")),
        ]),
        html.Br(),
        html.Div(className="name", children=[
            html.H2(name)
        ]),
        html.Div(className="summary", children=[
            html.P(summary)
        ])
    ])


layout = html.Div(className="about", children=[

    html.Br(),
    html.Br(),

    html.Div(className="title1", children=[
        html.H1("Meet the team")
    ]),

    html.Br(),

    html.Div(className="info", children=[
    createTile(
        "harshil.jpg",
        "HARSHIL PATEL",
        "IT Engineer & AI Enthusiast, Mumbai"
    ),

    createTile(
        "usashi.jpeg",
        "USASHI ROY",
        "Pursuing MS in DAE, Northeastern University, Boston"
    ),

    createTile(
        "tushar.jpg",
        "TUSHAR GADA",
        "Data Processor at Ipsos, Mumbai"
        
    )
])
])