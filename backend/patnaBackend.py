from datetime import datetime
from multiprocessing.dummy import Value
from backend.backendBluePrint import theBluePrint


theBluePrint(
    "Patna",
    "2015-06-01",
    datetime(2015,6,1),
    (2,0,0),
    (1,0,1,12),
    75,

    {'mae': 41.69193476852795,
    'mape': 0.2467,
    'me': 1.261357203846724,
    'mpe': -0.06800267230846918,
    'mse': 3176.3696999993804,
    'rmse': 56.359291159483014},

    {'mae': 48.60316801796649,
    'mape': 0.3019,
    'me': 1.716938364855184,
    'mpe': 0.12698962657379284,
    'mse': 3183.955045805948,
    'rmse': 56.42654557746689},

    {'mae': 41.64887741946393,
    'mape': 0.2642,
    'me': 12.382197031361038,
    'mpe': 0.15714855346690304,
    'mse': 2906.7908331410863,
    'rmse': 53.91466250604826}

)

class PatnaMainElements:
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

