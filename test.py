import os
cityName = "Delhi"
BASE_DIR = str((os.path.dirname(os.path.dirname(os.path.abspath(__file__))))).replace('\\', '/')

file = f"{BASE_DIR}/Air-Quality-Index-Prediction/datasets/{cityName}.csv"
print(file)

