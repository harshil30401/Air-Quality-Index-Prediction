from cities.frontEndBluePrint import *
from backend.mumbaiBackend import MumbaiMainElements as mme

frontend(
    "Mumbai",
    "May 2018",
    mme.html_arima(),
    mme.comparingScenarios(),
    mme.comparativeAnalysisRMSE(),
    mme.comparativeAnalysisMAPE(),
    mme.comparativeAnalysisMAE(),
    mme.comparativeAnalysisME(),
    mme.comparativeAnalysisMSE(),
    mme.comparativeAnalysisMPE()
)