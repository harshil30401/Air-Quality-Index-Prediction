from datetime import datetime
from backend.backendBluePrint import theBluePrint

theBluePrint(
    "Mumbai",
    "2018-06-18",
    datetime(2018,6,18),
    (1,0,0),
    (1,1,0,12),
    40,

    {'mae': 62.18911629669222,
    'mape': 1.1955,
    'me': -45.045407179363316,
    'mpe': -1.1010275738722892,
    'mse': 4983.533585894527,
    'rmse': 70.59414696626433},

    #delhi

    {'mae': 71.75630977927034,
    'mape': 0.3376,
    'me': 49.39377931640239,
    'mpe': 0.20589205593491092,
    'mse': 10630.393332266402,
    'rmse': 103.10379882558354},

    {'mae': 41.64887741946393,
    'mape': 0.2642,
    'me': 12.382197031361038,
    'mpe': 0.15714855346690304,
    'mse': 2906.7908331410863,
    'rmse': 53.91466250604826}
)

class MumbaiMainElements():
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