import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
from time import time
import plotly.express as px
import plotly.graph_objects as go
from plotly.offline import iplot

file = "/content/drive/MyDrive/FinalCities/Delhi.csv"
delhi = pd.read_csv(file, parse_dates=True)
delhi = delhi[delhi['Date']>='2015-01-01']
delhi['Date'] = pd.to_datetime(delhi['Date'])
delhi.set_index('Date', inplace=True)

# delhi['AQI'].plot(figsize=(20,8))
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
fig.show()

delhi=delhi.resample(rule='MS').mean()
delhi

delhi.count()

delhi = delhi.AQI.asfreq(pd.infer_freq(delhi.AQI.index))
d = pd.DataFrame(delhi)
d

start_date = datetime(2015,1,1)
end_date = datetime(2021,8,1)
lim_delhi = delhi[start_date:end_date]

fig = px.line(x=lim_delhi.index, y=lim_delhi,  title = "delhi AQI")
fig.update_layout(
    xaxis_title="Date",
    yaxis_title="AQI",
)
fig.show()

# px.ylabel('AQI', fontsize=16)
# for year in range(start_date.year,end_date.year):
#     px.axvline(pd.to_datetime(str(year)+'-01-01'), color='k', linestyle='--', alpha=0.2)
#     px.axvline(pd.to_datetime('2021-01-01'), color='k', linestyle='--', alpha=0.03)

from statsmodels.tsa.seasonal import seasonal_decompose
result=seasonal_decompose(lim_delhi,model='multiplicative')
result.plot()

first_diff = lim_delhi.diff()[1:]

plt.figure(figsize=(25,8))
plt.plot(first_diff)
plt.title('delhi AQI', fontsize=20)
plt.ylabel('AQI', fontsize=16)
for year in range(start_date.year,end_date.year):
    plt.axvline(pd.to_datetime(str(year)+'-01-01'), color='k', linestyle='--', alpha=0.2)
    plt.axhline(0, color='k', linestyle='--', alpha=0.02)

"""####ARIMA"""

from pmdarima import auto_arima

auto_arima(y=lim_delhi,start_p=0,start_P=0,start_q=0,start_Q=0,seasonal=True, m=12).summary()

train_end = datetime(2020,3,1)
test_end = datetime(2021,8,1)

train_arima = lim_delhi[:train_end]
test_arima = lim_delhi[train_end + timedelta(days=1):test_end]

from statsmodels.tsa.statespace.sarimax import SARIMAX
my_order = (2,0,0)
my_seasonal_order = (2, 0, 0, 12)
# define model
model = SARIMAX(train_arima, order=my_order, seasonal_order=my_seasonal_order)

start = time()
model_fit = model.fit()
end = time()
print('Model Fitting Time:', end - start)

#summary of the model
print(model_fit.summary())

#get the predictions and residuals
predictions_arima = model_fit.forecast(len(test_arima))
predictions_arima = pd.Series(predictions_arima, index=test_arima.index)
residuals_arima = test_arima - predictions_arima

plt.figure(figsize=(25,8))
plt.plot(residuals_arima)
plt.axhline(0, linestyle='--', color='k')
plt.title('Residuals from SARIMA Model', fontsize=20)
plt.ylabel('Error', fontsize=16)

trainNL_arima = train_arima
predNL_arima = predictions_arima
predNL_arima = predNL_arima.rename('AQI')
# merged = pd.concat([trainNL, predNL], axis = 1)
# merged
merged = trainNL_arima.append(predNL_arima)
merged

plt.figure(figsize=(25,8))

plt.plot(lim_delhi)
plt.plot(predictions_arima)

plt.legend(('AQI', 'Predictions'), fontsize=16)

plt.title('delhi AQI', fontsize=20)
plt.ylabel('AQI', fontsize=16)
for year in range(start_date.year,end_date.year):
    plt.axvline(pd.to_datetime(str(year)+'-01-01'), color='k', linestyle='--', alpha=0.2)

# dict for the dataframes and their names
dfs = { "Data to be predicted":test_arima,  "Predicted Forecast": predictions_arima}

# plot the data
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
fig.show()

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

plt.figure(figsize=(25,8))
plt.plot(rolling_residuals_arima)
plt.axhline(0, linestyle='--', color='k')
plt.title('Rolling Forecast Residuals from SARIMA Model', fontsize=20)
plt.ylabel('Error', fontsize=16)

plt.figure(figsize=(25,8))

plt.plot(lim_delhi)
plt.plot(rolling_predictions_arima)

plt.legend(('AQI', 'Predictions'), fontsize=16)

plt.title('delhi_AQI', fontsize=20)
plt.ylabel('AQI', fontsize=16)
for year in range(start_date.year,end_date.year):
    plt.axvline(pd.to_datetime(str(year)+'-01-01'), color='k', linestyle='--', alpha=0.2)

# dict for the dataframes and their names
dfs = { "Data to be predicted":test_arima,  "Predicted Forecast": rolling_predictions_arima}

# plot the data
fig = go.Figure(
    layout=go.Layout(
        title=go.layout.Title(text="Accuracy of the Rolling Forecast ARIMA Model")
    )
)
fig = fig.add_trace(go.Scatter(x = train_arima.index,
                                   y = train_arima, 
                                   name = "Actual Data"))
for i in dfs:
    fig = fig.add_trace(go.Scatter(x = test_arima.index,
                                   y = dfs[i], 
                                   name = i))
fig.show()

arima_rolling_acc_parameters = forecast_accuracy_parameters(rolling_residuals_arima, test_arima)
arima_rolling_acc_parameters

merged.count()

model=SARIMAX(lim_delhi,order=(2,0,0),seasonal_order=(2,0,0,12))
results=model.fit()
results.summary()
#Obtaining predicted values:
pred1_arima = results.predict(start=80, end=92, typ='levels').rename('Predictions')
#Plotting predicted values against the true values:
# predictions.plot(legend=True)
# delhi_aqi.plot(legend=True,figsize=(12,8),grid=True)
plt.figure(figsize=(20,8))
plt.plot(pred1_arima)
plt.plot(lim_delhi)
plt.legend(('Forecasted', 'Current'), fontsize=16)

plt.title('delhi AQI', fontsize=20)
plt.ylabel('AQI', fontsize=16)

start_date = datetime(2015,1,1)
end_date = datetime(2023,1,1)

for year in range(start_date.year,end_date.year):
    plt.axvline(pd.to_datetime(str(year)+'-01-01'), color='k', linestyle='--', alpha=0.2)

def output_arima(data, forecast):     #lim_delhi.index and pred1_arima.index
  fig = go.Figure(
      layout=go.Layout(
          title=go.layout.Title(text="Forecast")
      )
  )
  fig = fig.add_trace(go.Scatter(x = data.index,
                                    y = data, 
                                    name = "Actual Data"))
  fig = fig.add_trace(go.Scatter(x = forecast.index,
                                    y = forecast, 
                                    name = "Forecast"))
  fig.show()

output_arima(lim_delhi, pred1_arima)

model=SARIMAX(merged,order=(0,0,1),seasonal_order=(1,0,1,12))
results=model.fit()
results.summary()
#Obtaining predicted values:
pred2_arima = results.predict(start=80, end=92, typ='levels').rename('Predictions')
#Plotting predicted values against the true values:
# predictions.plot(legend=True)
# delhi_aqi.plot(legend=True,figsize=(12,8),grid=True)
plt.figure(figsize=(20,8))
plt.plot(pred2_arima)
plt.plot(merged)
plt.legend(('Forecasted', 'Current'), fontsize=16)

plt.title('delhi AQI', fontsize=20)
plt.ylabel('AQI', fontsize=16)

start_date = datetime(2015,1,1)
end_date = datetime(2023,1,1)

for year in range(start_date.year,end_date.year):
    plt.axvline(pd.to_datetime(str(year)+'-01-01'), color='k', linestyle='--', alpha=0.2)

plt.plot(pred2_arima)

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
fig.show()

resi = pred2_arima - pred1_arima
plt.figure(figsize=(25,8))
plt.plot(resi)
plt.axhline(0, linestyle='--', color='k')
plt.title('Rolling Forecast Residuals from SARIMA Model', fontsize=20)
plt.ylabel('Error', fontsize=16)

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
fig.show()

"""####PROPHET"""

d.reset_index(inplace=True)
d

delhi_ad = d[['Date', 'AQI']]
delhi_ad.columns = ['ds', 'y']
delhi=delhi_ad

from fbprophet import Prophet

train_prophet = delhi[:63]
test_prophet=delhi[63:]

m = Prophet(seasonality_mode='multiplicative')
m.fit(train_prophet)

future = m.make_future_dataframe(periods=17,freq = 'MS')
forecast_prophet = m.predict(future)

forecast_prophet

plt.figure(figsize=(25,8))
plt.plot(forecast_prophet.yhat)
plt.plot(delhi.y)

dfs = {"Accuracy of the Model" : forecast_prophet.yhat, "Actual Data": delhi.y}

# plot the data
fig = go.Figure(
  layout=go.Layout(
        title=go.layout.Title(text="Testing the Accuracy of the Model")
    )
)

for i in dfs:
    fig = fig.add_trace(go.Scatter(x = forecast_prophet.index,
                                   y = dfs[i], 
                                   name = i))
fig.show()

m.plot(forecast_prophet, figsize=(25,8));

from fbprophet.plot import plot_plotly
fig = plot_plotly(m, forecast_prophet, trend=True, changepoints=True)  
annotations = []
annotations.append(dict(xref='paper', yref='paper', x=0.0, y= 1.1,
                              xanchor='left', yanchor='bottom',
                              text='Forecast on current Data',
                              font=dict(family='Arial',
                                        size=25,
                                        color='rgb(37,37,37)'),
                              showarrow=False))
                   
fig.update_layout(annotations=annotations, xaxis_title = 'Date', yaxis_title = 'AQI')
fig

from sklearn.metrics import mean_squared_error
RMSE_prophet=np.sqrt(mean_squared_error(forecast_prophet['yhat'][-17:],test_prophet['y']))
print('RMSE = ',RMSE_prophet)
print('Mean AQI',test_prophet['y'].mean())

residuals_prophet = test_prophet['y'] - forecast_prophet['yhat'][-17:]
residuals_prophet

prophet_acc_parameters = forecast_accuracy_parameters(residuals_prophet, test_prophet['y'])
prophet_acc_parameters

m = Prophet(seasonality_mode='multiplicative',weekly_seasonality=False,daily_seasonality=False)
m.fit(delhi)
future = m.make_future_dataframe(periods=12,freq = 'MS')
forecast_prophet = m.predict(future)
m.plot(forecast_prophet, figsize=(25,8));

from fbprophet.plot import plot_plotly

def output_prophet(model, forecast):
  fig = plot_plotly(model, forecast, trend=True, changepoints=True)  
  annotations = []
  annotations.append(dict(xref='paper', yref='paper', x=0.0, y= 1.1,
                                xanchor='left', yanchor='bottom',
                                text='Forecast of the year 2022 (Considering the Lockdown)',
                                font=dict(family='Arial',
                                          size=30,
                                          color='rgb(37,37,37)'),
                                showarrow=False))
                    
  fig.update_layout(annotations=annotations, xaxis_title = 'Date', yaxis_title = 'AQI')
  fig

output_prophet(m, forecast_prophet)

pred1_prophet = forecast_prophet

pred1_prophet['yhat'][-17:]

test_prophet['y']

pred1_prophet[-29:-12]

from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_squared_error
RMSE_prophet =np.sqrt(mean_squared_error(pred1_prophet['yhat'][-29:-12],test_prophet['y']))
print('RMSE = ',RMSE_prophet )
print('Mean AQI',test_prophet['y'].mean())

m.plot_components(forecast_prophet);

from fbprophet.diagnostics import cross_validation
delhi_cv = cross_validation(m, initial='730 days', period='180 days', horizon = '365 days')
delhi_cv.head()

delhi_cv.tail()

from fbprophet.diagnostics import performance_metrics
df_p = performance_metrics(delhi_cv)
df_p.describe()

from fbprophet.plot import plot_cross_validation_metric
fig = plot_cross_validation_metric(delhi_cv, metric='rmse',figsize=(25,8))

m = Prophet(seasonality_mode='multiplicative',weekly_seasonality=False,daily_seasonality=False)
m.fit(train_prophet)
# future = m.make_future_dataframe(periods=5,freq = 'MS')
forecast_prophet_nl = m.predict(test_prophet)
m.plot(forecast_prophet_nl, figsize=(25,8));

from fbprophet.plot import plot_plotly
fig = plot_plotly(m, forecast_prophet_nl, trend=True, changepoints=True)  
annotations = []
annotations.append(dict(xref='paper', yref='paper', x=0.0, y= 1.1,
                              xanchor='left', yanchor='bottom',
                              text='Train data and Predictions',
                              font=dict(family='Arial',
                                        size=25,
                                        color='rgb(37,37,37)'),
                              showarrow=False))
                   
fig.update_layout(annotations=annotations, xaxis_title = 'Date', yaxis_title = 'AQI')
fig

part2 = forecast_prophet_nl[['ds', 'yhat']]
part2.rename(columns={'yhat':'y'}, inplace=True)

delhi_nl = pd.concat([train_prophet, part2], axis=0)
delhi_nl.reset_index(inplace=True)
delhi_nl.drop('index', inplace=True, axis=1)

m = Prophet(seasonality_mode='multiplicative',weekly_seasonality=False,daily_seasonality=False)
m.fit(delhi_nl)
future = m.make_future_dataframe(periods=12,freq = 'MS')
forecast_prophet_nl = m.predict(future)
m.plot(forecast_prophet_nl, figsize=(25,8));
pred2_prophet = forecast_prophet_nl

from fbprophet.plot import plot_plotly
fig = plot_plotly(m, forecast_prophet_nl, trend=True, changepoints=True)  
annotations = []
annotations.append(dict(xref='paper', yref='paper', x=0.0, y= 1.1,
                              xanchor='left', yanchor='bottom',
                              text='Forecast of the year 2022 (If Lockdown did not exist)',
                              font=dict(family='Arial',
                                        size=25,
                                        color='rgb(37,37,37)'),
                              showarrow=False))
                   
fig.update_layout(annotations=annotations, xaxis_title = 'Date', yaxis_title = 'AQI')
fig

pred1_prophet.set_index('ds', inplace=True)
pred2_prophet.set_index('ds', inplace=True)

import plotly.graph_objects as go


dfs = {"CONSIDERING THE LOCKDOWN" : pred1_prophet.yhat[80:], "IF LOCKDOWN DID NOT EXIST": pred2_prophet.yhat[80:]}

# plot the data
fig = go.Figure(
  layout=go.Layout(
        title=go.layout.Title(text="COMPARING SCENARIOS")
    )
)

for i in dfs:
    fig = fig.add_trace(go.Scatter(x = pred1_prophet[80:].index,
                                   y = dfs[i], 
                                   name = i))
fig.show()

"""###RNN (LSTM)"""

delhi_ad.set_index('ds', inplace=True)

delhi = delhi_ad

delhi = d[['Date', 'AQI']]
delhi.columns = ['ds', 'y']
delhi.set_index('ds', inplace=True)

train_lstm=delhi[63:]
test_lstm=delhi[63:]

from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
scaler.fit(train_lstm)

scaled_train = scaler.transform(train_lstm)
scaled_test = scaler.transform(test_lstm)

from keras.preprocessing.sequence import TimeseriesGenerator
n_input = 12
n_features = 1  
generator = TimeseriesGenerator(scaled_train, scaled_train, length=n_input, batch_size=1)

X,y = generator[0]

# We can see that the x array gives the list of values that we are going to predict y of:
print(f'Given the Array: \n{X.flatten()}')
print(f'Predict this y: \n {y}')

from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM

# defining the model(note that  I am using a very basic model here, a 2 layer model only):
model = Sequential()
model.add(LSTM(50, activation='relu', input_shape=(n_input, n_features)))
model.add(Dense(1))
model.compile(optimizer='adam', loss='mse')

model.summary()

# Fitting the model with the generator object:
model.fit_generator(generator,epochs=250)

loss_per_epoch = model.history.history['loss']
plt.plot(range(len(loss_per_epoch)),loss_per_epoch)

test_predictions = []

first_eval_batch = scaled_train[-n_input:]
current_batch = first_eval_batch.reshape((1, n_input, n_features))

for i in range(len(test_lstm)):
    
    
    current_pred = model.predict(current_batch)[0]
    
    
    test_predictions.append(current_pred) 
    
    
    current_batch = np.append(current_batch[:,1:,:],[[current_pred]],axis=1)

true_predictions = scaler.inverse_transform(test_predictions)

test_lstm['Predictions'] = true_predictions

test_lstm

import plotly.graph_objects as go

dfs = {"Actual Data" : test_lstm.y, "Predictions": test_lstm.Predictions}

# plot the data
fig = go.Figure(
  layout=go.Layout(
        title=go.layout.Title(text="Testing the accuracy of the Model")
    )
)

for i in dfs:
    fig = fig.add_trace(go.Scatter(x = test_lstm.index,
                                   y = dfs[i], 
                                   name = i))
fig.show()

residuals_lstm = test_lstm.Predictions -  test_lstm.y 
# residuals = pd.DataFrame(residuals)
# residuals.reset_index(inplace=True)
# residuals.drop('ds', axis=1, inplace=True)

lstm_acc_parameters = forecast_accuracy_parameters(residuals_lstm, test_lstm['y'])
lstm_acc_parameters

test_prophet['y']

plt.figure(figsize=(25,8))
plt.plot(residuals_lstm)
plt.axhline(0, linestyle='--', color='k')
plt.title('Residuals from SARIMA Model', fontsize=20)
plt.ylabel('Error', fontsize=16)

from sklearn.metrics import mean_squared_error
RMSE_lstm=np.sqrt(mean_squared_error(test_lstm['y'],test_lstm['Predictions']))
print('RMSE =',RMSE_lstm)
print('delhi=', delhi['y'].mean())

scaler.fit(delhi)
scaled_delhi=scaler.transform(delhi)

generator = TimeseriesGenerator(scaled_delhi, scaled_delhi, length=n_input, batch_size=1)

model.fit_generator(generator,epochs=250)

test_predictions = []

first_eval_batch = scaled_delhi[-n_input:]
current_batch = first_eval_batch.reshape((1, n_input, n_features))

for i in range(len(test_lstm)):
    
    
    current_pred = model.predict(current_batch)[0]
    
    
    test_predictions.append(current_pred) 
    
    
    current_batch = np.append(current_batch[:,1:,:],[[current_pred]],axis=1)

true_predictions = scaler.inverse_transform(test_predictions)

true_predictions=true_predictions.flatten()

true_preds=pd.DataFrame(true_predictions,columns=['Forecast'])
true_preds=true_preds.set_index(pd.date_range('2021-08-01',periods=17,freq='MS'))

def output_lstm(data, forecast):
  fig = go.Figure(
      layout=go.Layout(
          title=go.layout.Title(text="Forecast of 2022 considering the Lockdown")
      )
  )
  fig = fig.add_trace(go.Scatter(x = data.y.index,
                                    y = data.y, 
                                    name = "Actual Data"))
  fig = fig.add_trace(go.Scatter(x = forecast['Forecast'][:12].index,
                                    y = forecast['Forecast'], 
                                    name = "Forecast"))
  fig.show()

output_lstm(delhi, true_preds)

part2 = pd.DataFrame(test_lstm['Predictions'])
part2.rename(columns={"Predictions":"y"}, inplace=True)
delhi_rnn_nl = pd.concat([train_lstm, part2], axis = 0)

scaler.fit(delhi_rnn_nl)
scaled_delhi_nl=scaler.transform(delhi_rnn_nl)

generator = TimeseriesGenerator(scaled_delhi_nl, scaled_delhi_nl, length=n_input, batch_size=1)

model.fit_generator(generator,epochs=250)

test_predictions_nl = []

first_eval_batch = scaled_delhi_nl[-n_input:]
current_batch = first_eval_batch.reshape((1, n_input, n_features))

for i in range(len(test_lstm)):
    
    
    current_pred = model.predict(current_batch)[0]
    
    
    test_predictions_nl.append(current_pred) 
    
    
    current_batch = np.append(current_batch[:,1:,:],[[current_pred]],axis=1)

true_predictions_nl = scaler.inverse_transform(test_predictions_nl)

true_predictions_nl=true_predictions_nl.flatten()

true_preds_nl=pd.DataFrame(true_predictions_nl,columns=['Forecast'])
true_preds_nl = true_preds_nl.set_index(pd.date_range('2021-08-01',periods=17,freq='MS'))

fig = go.Figure(
    layout=go.Layout(
        title=go.layout.Title(text="Forecast of 2022 if Lockdown did not exist")
    )
)
fig = fig.add_trace(go.Scatter(x = delhi['y'].index,
                                   y = delhi.y, 
                                   name = "Actual Data"))
fig = fig.add_trace(go.Scatter(x = true_preds_nl['Forecast'][:12].index,
                                   y = true_preds_nl['Forecast'], 
                                   name = "Forecast"))
fig.show()

# dict for the dataframes and their names
dfs = {"Considering the Lockdown" : true_preds.Forecast, "Not considering the Lockdown": true_preds_nl.Forecast}

# plot the data
fig = go.Figure(
    layout=go.Layout(
        title=go.layout.Title(text="COMPARING SCENARIOS")
    )
)

for i in dfs:
    fig = fig.add_trace(go.Scatter(x = true_preds.index,
                                   y = dfs[i], 
                                   name = i))
fig.show()

"""###Exponential Smoothing (ETS)"""

file = '/content/drive/MyDrive/FinalCities/Delhi.csv'
delhi_ets = pd.read_csv(file, parse_dates=["Date"])
delhi_ets = delhi_ets[delhi_ets['Date'] >= '2015-1-01']
delhi_ets

delhi_es = delhi_ets[["Date", "AQI"]]
delhi_es = delhi_es.groupby('Date').sum()
delhi_es

delhi_es.plot(figsize=(25,8))

delhi_es=delhi_es.resample(rule='MS').mean()
delhi_es

import statsmodels.api as sm
from statsmodels.tsa.seasonal import seasonal_decompose

seasonal_decompose(delhi_es, period=12, extrapolate_trend='freq').plot();

train_ets = delhi_es[:63]
test_ets = delhi_es[63:]

train_ets.info()

train_ets

from statsmodels.tsa.holtwinters import ExponentialSmoothing
modelForTestPrediction = ExponentialSmoothing(train_ets.AQI, seasonal='mul', seasonal_periods=12).fit()
test_pred = modelForTestPrediction.forecast(17)

test_pred

test_ets.AQI.plot(legend=True, label="AQI", figsize=(25,8))
test_pred.plot(legend=True, label="Prediction")

dfs = {"Test" : test_ets.AQI, "Predicted": test_pred}    

fig = go.Figure(
    layout=go.Layout(
        title=go.layout.Title(text="Accuracy of the Model")
    )
)

for i in dfs:
    fig = fig.add_trace(go.Scatter(x = test_ets.index,
                                   y = dfs[i], 
                                   name = i))
fig.show()

dfs = { "Data to be predicted":test_ets.AQI,  "Predicted Forecast": test_pred}

# plot the data
fig = go.Figure(
    layout=go.Layout(
        title=go.layout.Title(text="Accuracy of the ARIMA Model") 
    )
)
fig = fig.add_trace(go.Scatter(x = train_ets.index,
                                   y = train_ets.AQI,
                                   name = "Actual Data"))
for i in dfs:
    fig = fig.add_trace(go.Scatter(x = test_ets.index,
                                   y = dfs[i], 
                                   name = i))
fig.show()

from sklearn.metrics import mean_absolute_error, mean_squared_error

rmse_ets = np.sqrt(mean_squared_error(test_ets, test_pred))
delhi_es.AQI.mean(), np.sqrt(delhi_es.AQI.var()), rmse_ets

residuals_ets = test_pred - test_ets.AQI
residuals_ets

ets_acc_parameters = forecast_accuracy_parameters(residuals_ets, test_ets.AQI)
ets_acc_parameters

modelConsideringLockdown = ExponentialSmoothing(delhi_es.AQI, seasonal='mul', seasonal_periods=12).fit()
pred1_ets = modelConsideringLockdown.forecast(12)

pred1_ets

def output_ets(data, forecast):  
  fig = go.Figure(
      layout=go.Layout(
          title=go.layout.Title(text="FORECAST IF LOCKDOWN EXISTED")
      )
  )
  fig = fig.add_trace(go.Scatter(x = data.index,
                                    y = data.AQI, 
                                    name = "Actual Data"))
  fig = fig.add_trace(go.Scatter(x = forecast.index,
                                    y = forecast, 
                                    name = "Forecast"))

  fig.show()

output_ets(delhi_es, pred1_ets)

test_pred = pd.DataFrame(test_pred)
test_pred.reset_index(inplace=True)
test_pred.rename(columns={"index":"Date", 0:"AQI"}, inplace=True)
test_pred.set_index('Date', inplace=True)
test_pred

secondPartCL = test_pred

delhi_nl_ets = pd.concat([train_ets, secondPartCL], axis = 0)
delhi_nl_ets

modelNoLockdown = ExponentialSmoothing(delhi_nl_ets.AQI, seasonal='mul', seasonal_periods=12).fit()
pred2_ets = modelNoLockdown.forecast(12)

pred2_ets

fig = go.Figure(
    layout=go.Layout(
        title=go.layout.Title(text="FORECAST IF LOCKDOWN DID NOT EXIST")
    )
)
fig = fig.add_trace(go.Scatter(x = delhi_nl_ets.index,
                                   y = delhi_nl_ets.AQI, 
                                   name = "Actual Data"))
fig = fig.add_trace(go.Scatter(x = pred2_ets.index,
                                   y = pred2_ets, 
                                   name = "Forecast"))

fig.show()

dfs = {"CONSIDERING THE LOCKDOWN" : pred1_ets, "IF LOCKDOWN DID NOT EXIST": pred2_ets}

# plot the data
fig = go.Figure(
  layout=go.Layout(
        title=go.layout.Title(text="COMPARING SCENARIOS")
    )
)

for i in dfs:
    fig = fig.add_trace(go.Scatter(x = pred1_ets.index,
                                   y = dfs[i], 
                                   name = i))
d = fig.show()

arima_rolling_acc_parameters

prophet_acc_parameters

lstm_acc_parameters

ets_acc_parameters

acc_parameters = {"ARIMA": arima_acc_parameters, "Prophet" : prophet_acc_parameters, "LSTM" : lstm_acc_parameters, "ETS" : ets_acc_parameters}

acc_parameters = pd.DataFrame.from_dict(acc_parameters, orient ='index')

fig = px.bar(acc_parameters, y=acc_parameters.rmse, x=acc_parameters.index, text_auto='.2s',
            title='Comparison')
test = fig.show()

dictionary = {'ARIMA':acc_parameters.rmse['ARIMA'], 'Prophet':acc_parameters.rmse['Prophet'], 
              'LSTM':acc_parameters.rmse['LSTM'], 'ETS':acc_parameters.rmse['ETS']} 

def function(dictionary): 
  x = min(dictionary, key=dictionary.get)
  return x

variable = function(dictionary)

variable

def output(variable):
  if(variable == 'ARIMA'):
    fig = go.Figure(
    layout=go.Layout(
        title=go.layout.Title(text="Forecast ARIMA")
        )
    )
    fig = fig.add_trace(go.Scatter(x = lim_delhi.index,
                                      y = lim_delhi, 
                                      name = "Actual Data"))
    fig = fig.add_trace(go.Scatter(x = pred1_arima.index,
                                      y = pred1_arima, 
                                      name = "Forecast"))
    fig.show()

  elif(variable == 'Prophet'):
    fig = go.Figure(
    layout=go.Layout(
        title=go.layout.Title(text="Forecast PROPHET")
    )
    )
    fig = fig.add_trace(go.Scatter(x = lim_delhi.index,
                                      y = lim_delhi, 
                                      name = "Actual Data"))
    fig = fig.add_trace(go.Scatter(x = pred1_arima.index,
                                      y = pred1_arima, 
                                      name = "Forecast"))
    fig.show()

  elif(variable == 'LSTM'):
    fig = go.Figure(
    layout=go.Layout(
        title=go.layout.Title(text="Forecast LSTM")
    )
    )
    fig = fig.add_trace(go.Scatter(x = lim_delhi.index,
                                      y = lim_delhi, 
                                      name = "Actual Data"))
    fig = fig.add_trace(go.Scatter(x = pred1_arima.index,
                                      y = pred1_arima, 
                                      name = "Forecast"))
    fig.show()

  elif(variable == 'ETS'):
    fig = go.Figure(
    layout=go.Layout(
        title=go.layout.Title(text="Forecast ETS")
    )
    )
    fig = fig.add_trace(go.Scatter(x = lim_delhi.index,
                                      y = lim_delhi, 
                                      name = "Actual Data"))
    fig = fig.add_trace(go.Scatter(x = pred1_arima.index,
                                      y = pred1_arima, 
                                      name = "Forecast"))
    fig.show()

def output(variable):
  if(variable == 'ARIMA'):
    output_arima(lim_delhi, pred1_arima)
    print('ARIMA')

  elif(variable == 'Prophet'):
    output_prophet(m, forecast_prophet)
    print('Prophet')

  elif(variable == 'LSTM'):
    output_lstm(delhi, true_preds)
    print('LSTM')

  elif(variable == 'ETS'):
    output_ets(delhi_es, pred1_ets)
    print('ETS')

output(variable)

