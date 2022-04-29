from backend.backendBluePrint import theBluePrint
from datetime import datetime

theBluePrint(
    "Ahmedabad",
    "2017-11-01",
    datetime(2017,11,1),
    (0,1,0),
    (0,1,0,12),
    46,

    {'mae': 205.9327923088142,
    'mape': 1.8118,
    'me': -205.9327923088142,
    'mpe': -1.8117615231226982,
    'mse': 51077.484923997035,
    'rmse': 226.00328520620454},

    {'mae': 246.95537196411587,
    'mape': 2.1583,
    'me': 246.95537196411587,
    'mpe': 2.15825247678154,
    'mse': 67297.58275599235,
    'rmse': 259.41777648417303},  

    {'mae': 142.4595261588069,
    'mape': 1.2577,
    'me': 142.4595261588069,
    'mpe': 1.2576598749441321,
    'mse': 23404.514514389903,
    'rmse': 152.9853408480365}
)


class AhmedabadMainElements:
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

