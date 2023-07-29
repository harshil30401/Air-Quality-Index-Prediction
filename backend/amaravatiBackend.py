from datetime import datetime
from backend.backendBluePrint import theBluePrint

theBluePrint(
    "Amaravati",
    "2017-11-01",
    datetime(2017,11,1),
    (1,1,1),
    (2,0,0,12),
    46,
    
    {'mae': 17.798488599983635,
    'mape': 0.3088,
    'me': 14.525220107308119,
    'mpe': 0.23211024229172414,
    'mse': 477.0949685520834,
    'rmse': 21.84250371528144},

    {'mae': 21.790125344389114,
    'mape': 0.3567,
    'me': -9.051464985686508,
    'mpe': -0.07302008432877397,
    'mse': 763.5154118653711,
    'rmse': 27.631782640021093},

    {'mae': 11.444298407689432,
    'mape': 0.2429,
    'me': 4.554796385200771,
    'mpe': 0.15038300021136866,
    'mse': 166.8560081789864,
    'rmse': 12.917275571070952}
)


class AmaravatiMainElements:
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

