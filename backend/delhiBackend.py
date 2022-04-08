from datetime import datetime
from backend.backendBluePrint import theBluePrint

theBluePrint(
    "Delhi",
    "2015-01-01",
    datetime(2015,1,1),
    (0,0,1), # (2,0,0)
    (1,0,1,12), #   (2,0,0,12),
    80,

    {'mae': 41.69193476852795,
    'mape': 0.2467,
    'me': 1.261357203846724,
    'mpe': -0.06800267230846918,
    'mse': 3176.3696999993804,
    'rmse': 56.359291159483014},

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

class DelhiMainElements():
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