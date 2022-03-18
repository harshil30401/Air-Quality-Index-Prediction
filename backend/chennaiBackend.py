from datetime import datetime
from backend.backendBluePrint import theBluePrint

theBluePrint(
    "Chennai",
    "2015-05-01",
    datetime(2015,5,1),
    (0,1,0),
    (0,1,0,12),
    78,

    {'mae': 14.106801404663463,
    'mape': 0.1789,
    'me': 6.074765554898316,
    'mpe': 0.05609557716237731,
    'mse': 297.8977683413905,
    'rmse': 17.259715187145773},

    {'mae': 19.447999719225574,
    'mape': 0.2401,
    'me': -18.341274860688987,
    'mpe': -0.219958640354482,
    'mse': 574.9841278038505,
    'rmse': 23.978826656111647},

    {'mae': 12.755610688090018,
    'mape': 0.1553,
    'me': -10.822380779027384,
    'mpe': -0.12114454119110055,
    'mse': 274.6000563005241,
    'rmse': 16.571060807942384}
)

class ChennaiMainElements():
    def accuracyArima():
        return theBluePrint.accuracyARIMA
    def comparativeAnalysis():
        return theBluePrint.comparativeAnalysis
    def comparingScenarios():
        return theBluePrint.comparingScenarios   
    def html_arima():
        return theBluePrint.html_arima