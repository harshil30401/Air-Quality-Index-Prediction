from datetime import datetime
from backend.backendBluePrint import theBluePrint

theBluePrint(
    "Jaipur",
    "2017-06-01",
    datetime(2017,6,1),
    (0,1,2),
    (1,0,1,12),
    51,

    {'mae': 29.75789534511238,
    'mape': 0.2983,
    'me': 17.42420628258012,
    'mpe': 0.12961587404130231,
    'mse': 1333.929969253243,
    'rmse': 36.523006027067964},

    {'mae': 24.78105183292466,
    'mape': 0.3563,
    'me': 8.962645048795764,
    'mpe': 0.23176671995144218,
    'mse': 902.9308983195687,
    'rmse': 30.048808600667826},

    {'mae': 28.825015031734644,
    'mape': 0.3636,
    'me': 25.500536842018537,
    'mpe': 0.3379095528929673,
    'mse': 994.2415154877131,
    'rmse': 31.531595511291734}
)

class JaipurMainElements():
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