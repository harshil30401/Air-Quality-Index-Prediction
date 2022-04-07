import dash
from dash import dcc, html

foo = dash.Dash()

foo.layout = html.Div([
    html.Div(className="container", children=[
        html.Div(className="clouds", children=[
            html.H1("Dxtcoder"),
            #style="--i:1"
            html.Img(src="C:/Users/DELL/Desktop/Air-Quality-Index-Prediction/photos/cloud1.png"),
            html.Img(src="C:/Users/DELL/Desktop/Air-Quality-Index-Prediction/photos/cloud2.png"),
            html.Img(src="C:/Users/DELL/Desktop/Air-Quality-Index-Prediction/photos/cloud3.png"),
            html.Img(src="C:/Users/DELL/Desktop/Air-Quality-Index-Prediction/photos/cloud4.png"),
            html.Img(src="C:/Users/DELL/Desktop/Air-Quality-Index-Prediction/photos/cloud5.png")
        ])
    ]),
    html.Section([
        html.H2("3D Cloud Animation"),
        html.P("The first thing well do is create the folder that will contain all of our files that make up the project. Create an empty folder on your desktop and name it “quote generator”. Open up Sublime Text and drag the file into sublime. Now we should have the folder accessible through the sidebar. Most web project consist of at least one HTML, JavaScript, and a CSS file. Lets create these files within the “quote generator” folder. In Sublime Text,right click the “quote generator” folder on the sidebar and click on create new file."),
        html.Br(),html.Br(),
        html.P("The first thing well do is create the folder that will contain all of our files that make up the project. Create an empty folder on your desktop and name it “quote generator”. Open up Sublime Text and drag the file into sublime. Now we should have the folder accessible through the sidebar. Most web project consist of at least one HTML, JavaScript, and a CSS file. Lets create these files within the “quote generator” folder. In Sublime Text,right click the “quote generator” folder on the sidebar and click on create new file."),
        html.Br(),html.Br(),
        html.P("The first thing well do is create the folder that will contain all of our files that make up the project. Create an empty folder on your desktop and name it “quote generator”. Open up Sublime Text and drag the file into sublime. Now we should have the folder accessible through the sidebar. Most web project consist of at least one HTML, JavaScript, and a CSS file. Lets create these files within the “quote generator” folder. In Sublime Text,right click the “quote generator” folder on the sidebar and click on create new file."),
        html.Br(),html.Br()
    ])
])

foo.run_server(debug=True)