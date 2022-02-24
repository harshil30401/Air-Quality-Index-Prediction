from gettext import install

import dash

# import dash_html_components as html
# import dae'], y = df['GOOG'],\
                     line = dict(color = 'firebrick', width = 4), name = 'Google')
                     ])
    fig.update_layout(title = 'Prices over time',
                      xaxis_title = 'Dates',
                      yaxis_title = 'Prices'
                      )
    return fig  

app.layout = html.Div(id = 'parent', children = [
    html.H1(id = 'H1', children = 'Styling using html components this is harshil', style = {'textAlign':'center',\
                                           
app.run_server(debug=True, port=1000)