import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from time import time
import plotly.express as px
import plotly.graph_objects as go

file = r"C:\Users\DELL\Desktop\Text Editors & Softwares\Python\Dash\Air-Quality-Index-Prediction\datasets\Delhi.csv"
delhi = pd.read_csv(file, parse_dates=True)
delhi = delhi[delhi['Date']>='2015-01-01']
delhi['Date'] = pd.to_datetime(delhi['Date'])
delhi.set_index('Date', inplace=True)

fig = px.line(delhi, x=delhi.index, y='AQI')
fig.update_xaxes(
    rangeslider_visible= True,
    rangeselector=dict(
                        buttons = list([
                        dict(count = 17,label = 'The Lockdown Period',step='month',stepmode = "backward"),
                        dict(step= 'all', label = 'Delhi AQI'),
                        dict(step='all', label = 'Monthly')
                            ])        
                        )
                   )
fig.update_layout(
    xaxis_title="Date",
)

delhi=delhi.resample(rule='MS').mean()

delhi = delhi.AQI.asfreq(pd.infer_freq(delhi.AQI.index))
d = pd.DataFrame(delhi)

start_date = datetime(2015,1,1)
end_date = datetime(2021,8,1)
lim_delhi = delhi[start_date:end_date]

fig = px.line(x=lim_delhi.index, y=lim_delhi,  title = "delhi AQI")
fig.update_layout(
    xaxis_title="Date",
    yaxis_title="AQI",
)

#ARIMA

from pmdarima import auto_arima

auto_arima(y=lim_delhi,start_p=0,start_P=0,start_q=0,start_Q=0,seasonal=True, m=12).summary()

train_end = datetime(2020,3,1)
test_end = datetime(2021,8,1)

train_arima = lim_delhi[:train_end]
test_arima = lim_delhi[train_end + timedelta(days=1):test_end]

from statsmodels.tsa.statespace.sarimax import SARIMAX
my_order = (2,0,0)
my_seasonal_order = (2, 0, 0, 12)

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
    train_arima = lim_delhi[:train_end-timedelta(days=1)]
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

model=SARIMAX(lim_delhi,order=(2,0,0),seasonal_order=(2,0,0,12))
results=model.fit()

pred1_arima = results.predict(start=80, end=92, typ='levels').rename('Predictions')


start_date = datetime(2015,1,1)
end_date = datetime(2023,1,1)    

fig = go.Figure(
    layout=go.Layout(
       title=go.layout.Title(text="Forecast")
           )
)
fig = fig.add_trace(go.Scatter(x = lim_delhi.index,
                                 y = lim_delhi, 
                                name = "Actual Data"))
fig = fig.add_trace(go.Scatter(x = pred1_arima.index,
                                y = pred1_arima, 
                                name = "Forecast"))

html_arima = fig.to_html(full_html=False, include_plotlyjs='cdn')


model=SARIMAX(merged,order=(0,0,1),seasonal_order=(1,0,1,12))
results=model.fit()
results.summary()
pred2_arima = results.predict(start=80, end=92, typ='levels').rename('Predictions')

start_date = datetime(2015,1,1)
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

prophet_acc_parameters = {'mae': 41.69193476852795,
 'mape': 0.2467,
 'me': 1.261357203846724,
 'mpe': -0.06800267230846918,
 'mse': 3176.3696999993804,
 'rmse': 56.359291159483014}

lstm_acc_parameters = {'mae': 71.75630977927034,
 'mape': 0.3376,
 'me': 49.39377931640239,
 'mpe': 0.20589205593491092,
 'mse': 10630.393332266402,
 'rmse': 103.10379882558354}

ets_acc_parameters = {'mae': 41.64887741946393,
 'mape': 0.2642,
 'me': 12.382197031361038,
 'mpe': 0.15714855346690304,
 'mse': 2906.7908331410863,
 'rmse': 53.91466250604826}

acc_parameters = {"ARIMA": arima_rolling_acc_parameters, "Prophet" : prophet_acc_parameters, "LSTM" : lstm_acc_parameters, "ETS" : ets_acc_parameters}

acc_parameters = pd.DataFrame.from_dict(acc_parameters, orient ='index')

comparativeAnalysis = px.bar(acc_parameters, y=acc_parameters.rmse, x=acc_parameters.index, text_auto='.2s',
            title='Comparison')  

comparativeAnalysis = comparativeAnalysis.to_html(full_html=False, include_plotlyjs='cdn')    

# delhiMainElements = [accuracyARIMA, comparativeAnalysis, comparingScenarios, html_arima]

class delhiMainElements():

    def accuracyArima():
        return accuracyARIMA
    
    def comparativeAnalysis():
        return comparativeAnalysis
    
    def comparingScenarios():
        return comparingScenarios
    
    def html_arima():
        return html_arima
    
    