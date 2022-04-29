from datetime import datetime
from multiprocessing.dummy import Value
from backend.backendBluePrint import theBluePrint


theBluePrint(
    "Lucknow",
    "2015-03-01",
    datetime(2015,3,1),
    (1,0,0),
    (1,0,1,12),
    78,

    {'mae': 27.698479374214585,
    'mape': 0.2294,
    'me': -6.210791494990542,
    'mpe': -0.12553361828918563,
    'mse': 1416.846076058458,
    'rmse': 37.64101587442159},

    {'mae': 50.636641039003266,
    'mape': 0.4552,
    'me': 9.780684375456627,
    'mpe': 0.30401779196135337,
    'mse': 3216.106138189782,
    'rmse': 56.710723308645804},

    {'mae': 43.19592164061878,
    'mape': 0.2426,
    'me': -42.80691533643018,
    'mpe': -0.23525692599603928,
    'mse': 3130.0227806931875,
    'rmse': 55.94660651633115},

)

class LucknowMainElements:
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

