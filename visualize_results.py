import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import IsolationForest

# Load dataset
data = pd.read_csv("dataset/system_metrics.csv")

# -----------------------------
# Anomaly Detection
# -----------------------------
features = data[["cpu","memory","disk","processes"]]

model = IsolationForest(contamination=0.05, random_state=42)
data["anomaly"] = model.fit_predict(features)

# -----------------------------
# Line Chart with Anomalies
# -----------------------------
plt.figure(figsize=(10,5))

plt.plot(data["cpu"], label="CPU Usage")
plt.plot(data["memory"], label="Memory Usage")
plt.plot(data["disk"], label="Disk Usage")

# Mark anomalies
anomaly_points = data[data["anomaly"] == -1]

plt.scatter(
    anomaly_points.index,
    anomaly_points["cpu"],
    color="red",
    label="Anomaly",
    marker="x"
)

plt.xlabel("Time Index")
plt.ylabel("Usage (%)")
plt.title("System Resource Usage with Anomaly Detection")
plt.legend()

plt.show()
