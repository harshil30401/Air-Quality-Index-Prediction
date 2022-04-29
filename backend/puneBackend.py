from datetime import datetime
from multiprocessing.dummy import Value
from backend.backendBluePrint import theBluePrint


theBluePrint(
    "Pune",
    "2018-06-01",
    datetime(2018,6,1),
    (0,1,0),
    (1,0,0,12),
    39,

    {'mae': 73.70752586803128,
    'mape': 2.5371,
    'me': -73.70752586803128,
    'mpe': -2.537091988644651,
    'mse': 5734.422329275121,
    'rmse': 75.7259686585462},

    {'mae': 29.086859512189324,
    'mape': 0.9423,
    'me': 22.691133545861387,
    'mpe': 0.8463530216151827,
    'mse': 1072.7836114797326,
    'rmse': 32.753375573820364},

    {'mae': 31.26101026020937,
    'mape': 0.9511,
    'me': 31.26101026020937,
    'mpe': 0.9511043226092339,
    'mse': 1244.6778659659096,
    'rmse': 35.279992431488836},

)

class PuneMainElements:
    def accuracyArima():
        return theBluePrint.accuracyARIMA

    def comparativeAnalysisMAE():
        return theBluePrint.comparativeAnalysisMAE
    def comparativeAnalysisMAPE():
        return theBluePrint.comparativeAnalysisMAPE
    def comparativeAnalysisME():
        return theBluePrint.comparativeAnalysisME
    def comparativeAnalysisMPE():
        return theBluePrint.comparativeAnalysisMPE
    def comparativeAnalysisMSE():
        return theBluePrint.comparativeAnalysisMSE
    def comparativeAnalysisRMSE():
        return theBluePrint.comparativeAnalysisRMSE

    def comparingScenarios():
        return theBluePrint.comparingScenarios   
    def html_arima():
        return theBluePrint.html_arima

