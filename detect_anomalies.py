import pandas as pd
from sklearn.ensemble import IsolationForest

data = pd.read_csv("dataset/system_metrics.csv")

features = data[["cpu","memory","disk","processes"]]

model = IsolationForest(contamination=0.05)

data["anomaly"] = model.fit_predict(features)

print(data.head())

anomalies = data[data["anomaly"] == -1]

print("\nDetected Anomalies:")
print(anomalies)