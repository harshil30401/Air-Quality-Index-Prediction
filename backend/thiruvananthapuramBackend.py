from datetime import datetime
from backend.backendBluePrint import theBluePrint

theBluePrint(
    "Thiruvananthapuram",
    "2017-06-01",
    datetime(2017,6,1),
    (1,1,0),
    (1,0,0,12),
    50,

    {'mae': 12.838280248492035,
    'mape': 0.2917,
    'me': -3.2461260289538085,
    'mpe': -0.11215723149093128,
    'mse': 313.83426838572603,
    'rmse': 17.715368141411176},

    {'mae': 24.206024445909907,
    'mape': 0.6679,
    'me': 24.206024445909907,
    'mpe': 0.667890972646559,
    'mse': 688.6018056054063,
    'rmse': 26.24122340146142},

    {'mae': 18.90090776886282,
    'mape': 0.4983,
    'me': 18.59079208643649,
    'mpe': 0.4914563925121641,
    'mse': 521.3978274978476,
    'rmse': 22.83413732764712}
)

class ThiruvananthapuramMainElements():
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