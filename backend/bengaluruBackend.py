from datetime import datetime
from backend.backendBluePrint import theBluePrint

theBluePrint(
    "Bengaluru",
    "2015-03-01",
    datetime(2015,3,1),
    (1,1,1),
    (2,0,0,12),
    61,

    {'mae': 16.332701885004962,
    'mape': 0.2848,
    'me': -0.22099522192201954,
    'mpe': -0.10954968356672748,
    'mse': 378.2927380420746,
    'rmse': 19.449749048305858},

    {'mae': 29.509291413888842,
    'mape': 0.5779,
    'me': 19.996706141771206,
    'mpe': 0.475171322286169,
    'mse': 1314.8839181397832,
    'rmse': 36.26132813535355},

    {'mae': 15.612130701718783,
    'mape': 0.3136,
    'me': 7.419749740162167,
    'mpe': 0.2269063105293638,
    'mse': 415.695595123447,
    'rmse': 20.388614350255562}
)


class BengaluruMainElements:
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
