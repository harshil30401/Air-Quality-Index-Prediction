from datetime import datetime
from backend.backendBluePrint import theBluePrint

theBluePrint(
    "Kanpur",
    "2018-01-01",
    datetime(2018,1,1),
    (1,0,0),
    (1,0,0,12),
    43,

    {'mae': 29.867428898254914,
    'mape': 0.3015,
    'me': 23.622117314922864,
    'mpe': 0.23092944026153986,
    'mse': 1843.060952983975,
    'rmse': 42.93088576985077},

    {'mae': 17.82886198494054,
    'mape': 0.1871,
    'me': -14.913217921380786,
    'mpe': -0.1416911291976083,
    'mse': 678.3479406879862,
    'rmse': 26.045113566425204},

    {'mae': 17.255774875752532,
    'mape': 0.2027,
    'me': -9.522375178641955,
    'mpe': -0.07562394804473745,
    'mse': 451.8755894315973,
    'rmse': 21.257365533659087},
)

class KanpurMainElements:

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


