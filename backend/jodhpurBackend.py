from datetime import datetime
from multiprocessing.dummy import Value
from backend.backendBluePrint import theBluePrint


theBluePrint(
    "Jodhpur",
    "2018-01-01",
    datetime(2018,1,1),
    (0,1,0),
    (0,1,0,12),
    44,

    {'mae': 70.39733733516466,
    'mape': 0.4749,
    'me': 46.316941929504104,
    'mpe': 0.258247341777356,
    'mse': 6292.587775054104,
    'rmse': 79.32583296161538},

    {'mae': 47.77694544390112,
    'mape': 0.3793,
    'me': 17.259947624519683,
    'mpe': 0.23585175889803195,
    'mse': 2915.047902145366,
    'rmse': 53.991183559405016},

    {'mae': 35.11490890750422,
    'mape': 0.2477,
    'me': 6.450988393414766,
    'mpe': 0.10829950044728505,
    'mse': 1877.5416352958466,
    'rmse': 43.33060852671984},

)

class JodhpurMainElements:
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

