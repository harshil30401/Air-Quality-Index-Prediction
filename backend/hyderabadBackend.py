from datetime import datetime
from backend.backendBluePrint import theBluePrint

theBluePrint(
    "Hyderabad",
    "2015-03-01",
    datetime(2015,3,1),
    (0,1,0), #  (1,0,0),
    (0,1,0,12),   #(1,0,1,12),
    78,

    {'mae': 26.041836392529817,
    'mape': 0.3159,
    'me': 14.611560018371542,
    'mpe': 0.06158831938968663,
    'mse': 964.6141162750653,
    'rmse': 31.05823749466581},

    {'mae': 81.20754932409851,
    'mape': 1.1534,
    'me': 49.477460027879864,
    'mpe': 0.8493745730955761,
    'mse': 8332.201573681661,
    'rmse': 91.2808938041344},

    {'mae': 24.019815725628426,
    'mape': 0.2768,
    'me': -12.58373470937385,
    'mpe': -0.03551237344948001,
    'mse': 801.3953690394828,
    'rmse': 28.308927373524465}
)

class HyderabadMainElements():
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