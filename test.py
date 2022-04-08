# import dash
import pandas as pd
# from dash import dcc, html
# import dash_bootstrap_components as dbc
# from cities.frontEndBluePrint import headerComponent
# from dash import dash_table

# testPath = "C:/Users/DELL/Desktop/Air-Quality-Index-Prediction/test.css"
# js = "C:/Users/DELL/Desktop/Air-Quality-Index-Prediction/assets/index.js"
# thisIsTest = dash.Dash(
#     __name__,
#     external_stylesheets=[dbc.themes.BOOTSTRAP],
#     external_scripts=[testPath, js]
#     )

# thisIsTest.layout = html.Div(className='main',children=[
   
#     dash_table.DataTable(theImpactDictionary, theImpactDictionary.keys)

# ], style={
#     'text-align':'center'
# })

# if __name__ == "__main__":
#     thisIsTest.run_server(debug=True, port=1234)

theImpactDictionary = {
    'AQI':'Associated Health Impacts',
    'Good (0 to 50)':'Minimal impact',
    'Satisfactory (51 to 100)': 'May cause minor breathing discomfort to sensitive people.',
    'Moderately polluted (101 to 200)':'May cause breathing discomfort to people with lung disease such as asthma, and discomfort to people with heart disease, children and older adults.',
    'Poor (201 to 300)':'May cause breathing discomfort to people on prolonged exposure, and discomfort to people with heart disease.',
    'Very poor (301 to 400)':'May cause respiratory illness to the people on prolonged exposure. Effect may be more pronounced in people with lung and heart diseases.',
    'Severe (401 to 500)':'May cause respiratory impact even on healthy people, and serious health impacts on people with lung/heart disease. The health impacts may be experienced even during light physical activity.'
}

theImpactDictionary = pd.DataFrame.from_dict(theImpactDictionary)
theImpactDictionary.set_index('AQI', inplace=True)

theImpactDictionary.to_csv('C:/Users/DELL/Desktop/Air-Quality-Index-Prediction/datasets/'+theImpactDictionary+'.csv', index=False)

