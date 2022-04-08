from datetime import datetime
from backend.backendBluePrint import theBluePrint

theBluePrint(
    "Nagpur",
    "2017-01-01",
    datetime(2017,1,1),
    (1,0,0),
    (1,0,0,12),
    56,

    {'mae': 20.651033834162817,
    'mape': 0.2929,
    'me': -3.119725860533758,
    'mpe': -0.062024268805242144,
    'mse': 614.8652050894744,
    'rmse': 24.79647565863896},

    {'mae': 28.36523427714895,
    'mape': 0.4363,
    'me': 22.606883289436336,
    'mpe': 0.3660213584132262,
    'mse': 1086.7680143509438,
    'rmse': 32.96616468973823},

    {'mae': 20.452053201207296,
    'mape': 0.291,
    'me': -17.13441148722685,
    'mpe': -0.23024530394124176,
    'mse': 627.71014218497,
    'rmse': 25.054144211786}
)

class NagpurMainElements():
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