from datetime import datetime
from multiprocessing.dummy import Value
from backend.backendBluePrint import theBluePrint


theBluePrint(
    "Amritsar",
    "2017-02-01",
    datetime(2017,2,1),
    (1,0,0),
    (1,0,1,12),
    55,

    {'mae': 36.39768433642671,
    'mape': 0.3449,
    'me': 30.978931689591985,
    'mpe': 0.27424657790671053,
    'mse': 1814.8618857026088,
    'rmse': 42.601195824795916},

    {'mae': 44.6550083132152,
    'mape': 0.4623,
    'me': 13.114878584995097,
    'mpe': 0.24351547606849114,
    'mse': 2958.1113623631727,
    'rmse': 54.3885223403171},

    {'mae': 18.44396369961101,
    'mape': 0.1998,
    'me': 6.310326487499946,
    'mpe': 0.08965609951943644,
    'mse': 504.0459109262858,
    'rmse': 22.450966814956672},

)

class AmritsarMainElements:
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

