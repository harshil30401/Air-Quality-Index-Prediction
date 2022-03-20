import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from time import time
import plotly.express as px
import plotly.graph_objects as go
from rootInformation import rootDirectory

file = f"{rootDirectory}/Air-Quality-Index-Prediction/datasets/Thiruvananthapuram.csv"
thiruvananthapuram = pd.read_csv(file, parse_dates=True)
thiruvananthapuram = thiruvananthapuram[thiruvananthapuram['Date']>='2017-06-01']
thiruvananthapuram['Date'] = pd.to_datetime(thiruvananthapuram['Date'])
thiruvananthapuram.set_index('Date', inplace=True)

fig = px.line(thiruvananthapuram, x=thiruvananthapuram.index, y='AQI')
fig.update_xaxes(
    rangeslider_visible= True,
    rangeselector=dict(
                        buttons = list([
                        dict(count = 17,label = 'The Lockdown Period',step='month',stepmode = "backward"),
                        dict(step= 'all', label = 'thiruvananthapuram AQI'),
                        dict(step='all', label = 'Monthly')
                            ])        
                        )
                   )
fig.update_layout(
    xaxis_title="Date",
)

thiruvananthapuram=thiruvananthapuram.resample(rule='MS').mean()

thiruvananthapuram = thiruvananthapuram.AQI.asfreq(pd.infer_freq(thiruvananthapuram.AQI.index))
d = pd.DataFrame(thiruvananthapuram)

start_date = datetime(2017,6,1)
end_date = datetime(2021,8,1)
lim_thiruvananthapuram = thiruvananthapuram[start_date:end_date]

fig = px.line(x=lim_thiruvananthapuram.index, y=lim_thiruvananthapuram,  title = "Thiruvananthapuram AQI")
fig.update_layout(
    xaxis_title="Date",
    yaxis_title="AQI",
)

#ARIMA

from pmdarima import auto_arima

auto_arima(y=lim_thiruvananthapuram,start_p=0,start_P=0,start_q=0,start_Q=0,seasonal=True, m=12).summary()

train_end = datetime(2020,3,1)
test_end = datetime(2021,8,1)

train_arima = lim_thiruvananthapuram[:train_end]
test_arima = lim_thiruvananthapuram[train_end + timedelta(days=1):test_end]

from statsmodels.tsa.statespace.sarimax import SARIMAX
my_order = (1,1,0)
my_seasonal_order = (1, 0, 0, 12)

model = SARIMAX(train_arima, order=my_order, seasonal_order=my_seasonal_order)

start = time()
model_fit = model.fit()
end = time()

predictions_arima = model_fit.forecast(len(test_arima))
predictions_arima = pd.Series(predictions_arima, index=test_arima.index)
residuals_arima = test_arima - predictions_arima

trainNL_arima = train_arima
predNL_arima = predictions_arima
predNL_arima = predNL_arima.rename('AQI')

merged = trainNL_arima.append(predNL_arima)

dfs = { "Data to be predicted":test_arima,  "Predicted Forecast": predictions_arima}

fig = go.Figure(
    layout=go.Layout(
        title=go.layout.Title(text="Accuracy of the ARIMA Model")
    )
)
fig = fig.add_trace(go.Scatter(x = train_arima.index,
                                   y = train_arima, 
                                   name = "Actual Data"))
for i in dfs:
    fig = fig.add_trace(go.Scatter(x = test_arima.index,
                                   y = dfs[i], 
                                   name = i))

accuracyARIMA = fig.to_html(full_html=False, include_plotlyjs='cdn')

def forecast_accuracy_parameters(residuals_arima, test_arima):
  mape = (round(np.mean(abs(residuals_arima/test_arima)),4))
  rmse = (np.sqrt(np.mean(residuals_arima**2)))
  me = np.mean(residuals_arima)             
  mae = np.mean(np.abs(residuals_arima))    
  mpe = np.mean((residuals_arima)/test_arima)
  mse = ((np.mean(residuals_arima**2)))
  return({'mape':mape, 'me':me, 'mae': mae, 
            'mpe': mpe, 'rmse':rmse, 'mse':mse})
arima_acc_parameters = forecast_accuracy_parameters(residuals_arima, test_arima)
arima_acc_parameters

"""##ROLLING FORECAST ORIGIN"""

rolling_predictions_arima = test_arima.copy()

for train_end in test_arima.index:
    train_arima = lim_thiruvananthapuram[:train_end-timedelta(days=1)]
    model = SARIMAX(train_arima, order=my_order, seasonal_order=my_seasonal_order)
    model_fit = model.fit()

    pred_arima = model_fit.forecast()
    rolling_predictions_arima[train_end] = pred_arima

train_arima.tail()

rolling_residuals_arima = test_arima - rolling_predictions_arima    

dfs = { "Data to be predicted":test_arima,  "Predicted Forecast": rolling_predictions_arima}

# fig = go.Figure(
#     layout=go.Layout(
#         title=go.layout.Title(text="Accuracy of the Rolling Forecast ARIMA Model")
#     )
# )
# fig = fig.add_trace(go.Scatter(x = train_arima.index,
#                                    y = train_arima, 
#                                    name = "Actual Data"))
# for i in dfs:
#     fig = fig.add_trace(go.Scatter(x = test_arima.index,
#                                    y = dfs[i], 
#                                    name = i))
 

arima_rolling_acc_parameters = forecast_accuracy_parameters(rolling_residuals_arima, test_arima)
arima_rolling_acc_parameters

merged.count()

model=SARIMAX(lim_thiruvananthapuram,order=(1,1,0),seasonal_order=(1,0,0,12))
results=model.fit()

pred1_arima = results.predict(start=50, end=62, typ='levels').rename('Predictions')


start_date = datetime(2017,6,1)
end_date = datetime(2023,1,1)    

fig = go.Figure(
    layout=go.Layout(
       title=go.layout.Title(text="Forecast")
           )
)
fig = fig.add_trace(go.Scatter(x = lim_thiruvananthapuram.index,
                                 y = lim_thiruvananthapuram, 
                                name = "Actual Data"))
fig = fig.add_trace(go.Scatter(x = pred1_arima.index,
                                y = pred1_arima, 
                                name = "Forecast"))

html_arima = fig.to_html(full_html=False, include_plotlyjs='cdn')


model=SARIMAX(merged,order=(1,1,0),seasonal_order=(1,0,0,12))
results=model.fit()
results.summary()
pred2_arima = results.predict(start=50, end=62, typ='levels').rename('Predictions')

start_date = datetime(2017,6,1)
end_date = datetime(2023,1,1)  

fig = go.Figure(
    layout=go.Layout(
        title=go.layout.Title(text="Forecast")
    )
)
fig = fig.add_trace(go.Scatter(x = merged.index,
                                   y = merged, 
                                   name = "Actual Data"))
fig = fig.add_trace(go.Scatter(x = pred2_arima.index,
                                   y = pred2_arima, 
                                   name = "Forecast"))
 

resi = pred2_arima - pred1_arima

# dict for the dataframes and their names
dfs = {"Considering the Lockdown" : pred1_arima, "Not considering the Lockdown": pred2_arima}

# plot the data
fig = go.Figure(
    layout=go.Layout(
        title=go.layout.Title(text="COMPARING SCENARIOS")
    )
)

for i in dfs:
    fig = fig.add_trace(go.Scatter(x = pred1_arima.index,
                                   y = dfs[i], 
                                   name = i))

comparingScenarios = fig.to_html(full_html=False, include_plotlyjs='cdn')
 
"""Comparative Analysis"""

arima_rolling_acc_parameters

prophet_acc_parameters = {'mae': 12.838280248492035,
 'mape': 0.2917,
 'me': -3.2461260289538085,
 'mpe': -0.11215723149093128,
 'mse': 313.83426838572603,
 'rmse': 17.715368141411176}

lstm_acc_parameters = {'mae': 24.206024445909907,
 'mape': 0.6679,
 'me': 24.206024445909907,
 'mpe': 0.667890972646559,
 'mse': 688.6018056054063,
 'rmse': 26.24122340146142}

ets_acc_parameters = {'mae': 18.90090776886282,
 'mape': 0.4983,
 'me': 18.59079208643649,
 'mpe': 0.4914563925121641,
 'mse': 521.3978274978476,
 'rmse': 22.83413732764712}

acc_parameters = {"ARIMA": arima_rolling_acc_parameters, "Prophet" : prophet_acc_parameters, "LSTM" : lstm_acc_parameters, "ETS" : ets_acc_parameters}

acc_parameters = pd.DataFrame.from_dict(acc_parameters, orient ='index')

comparativeAnalysis = px.bar(acc_parameters, y=acc_parameters.rmse, x=acc_parameters.index, text_auto='.2s',
            title='Comparison')  

comparativeAnalysis = comparativeAnalysis.to_html(full_html=False, include_plotlyjs='cdn')    

# thiruvananthapuramMainElements = [accuracyARIMA, comparativeAnalysis, comparingScenarios, html_arima]

class thiruvananthapuramMainElements():

    def accuracyArima():
        return accuracyARIMA
    
    def comparativeAnalysis():
        return comparativeAnalysis
    
    def comparingScenarios():
        return comparingScenarios
    
    def html_arima():
        return html_arima
    
    