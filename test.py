import pandas as pd
from rootInformation import rootDirectory

citiesMean = pd.read_csv(f"{rootDirectory}/Air-Quality-Index-Prediction/datasets/citiesMean.csv")

cityAQI = dict(zip(citiesMean.City, citiesMean.AQI))

city = "Mumbai"

# for c in cityAQI:
#     if c.keys() == city:
#         print(c.values())

print(cityAQI[city])
