from datetime import datetime
from backend.backendBluePrint import CityMainElements, theBluePrint

theBluePrint(
    "Kolkata",
    "2018-04-01",
    datetime(2018,4,1),
    (2,0,0),
    (1,0,0,12),
    40,

    {'mae': 105.5665660810663,
    'mape': 1.9299,
    'me': -97.31231533891076,
    'mpe': -1.8939949288429365,
    'mse': 13566.319277677147,
    'rmse': 116.47454347486041},

    {'mae': 44.66590038581038,
    'mape': 0.6984,
    'me': 18.678382465805072,
    'mpe': 0.5706368577246677,
    'mse': 2277.474866984645,
    'rmse': 47.7228966742867},

    {'mae': 20.512644708863945,
    'mape': 0.2568,
    'me': 14.897241355032254,
    'mpe': 0.2030300342853921,
    'mse': 734.9699846395266,
    'rmse': 27.1103298511753}
)

class KolkataMainElements():
    
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