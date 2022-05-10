from datetime import datetime
from backend.backendBluePrint import theBluePrint

theBluePrint(
    "Gandhinagar",
    "2019-02-01",
    datetime(2019,2,1),
    (1,0,0),
    (1,0,0,12),
    31,

    {'mae': 44.27785353726125,
    'mape': 0.5774,
    'me': 42.1035581347669,
    'mpe': 0.520012513382431,
    'mse': 2795.6136011762874,
    'rmse': 52.87356240292768},

    {'mae': 19.819866161346653,
    'mape': 0.2845,
    'me': -6.315225196114137,
    'mpe': 0.019238910386321167,
    'mse': 584.1743011407224,
    'rmse': 24.16969799440453},

    {'mae': 25.690374292770407,
    'mape': 0.3653,
    'me': 25.690374292770407,
    'mpe': 0.36533184061750174,
    'mse': 887.462962636596,
    'rmse': 29.790316591748333}
)



class GandhinagarMainElements:
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
