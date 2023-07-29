from datetime import datetime
from backend.backendBluePrint import theBluePrint, CityMainElements

theBluePrint(
    "Visakhapatnam",
    "2017-10-01",
    datetime(2017,10,1),
    (0,0,1),   #(1,0,0),
    (1,0,1,12),
    47,

    {'mae': 47.93068549062837,
    'mape': 0.4524,
    'me': 43.35504696998869,
    'mpe': 0.3934977420665994,
    'mse': 3190.2029553406333,
    'rmse': 56.481881655453314},
    
    {'mae': 31.21804231498486,
    'mape': 0.2959,
    'me': -7.061329729106839,
    'mpe': 0.0429088518608593,
    'mse': 1625.306127499759,
    'rmse': 40.315085607000256},

    {'mae': 19.107548280165798,
    'mape': 0.1647,
    'me': -14.376618118335728,
    'mpe': -0.08927051509294781,
    'mse': 801.6259660144088,
    'rmse': 28.31299994727526}
)

class VisakhapatnamMainElements():
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
