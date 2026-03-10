import streamlit as st
import pandas as pd
import pickle
from sklearn.ensemble import IsolationForest
import matplotlib.pyplot as plt

st.title("System Resource Monitoring Dashboard")

# Load dataset
data = pd.read_csv("dataset/system_metrics.csv")

# ----------------------------
# Anomaly Detection
# ----------------------------
features = data[["cpu","memory","disk","processes"]]

model_anomaly = IsolationForest(contamination=0.05, random_state=42)

data["anomaly"] = model_anomaly.fit_predict(features)

# ----------------------------
# Load prediction model
# ----------------------------
model = pickle.load(open("model.pkl","rb"))

st.subheader("Predict CPU Usage")

memory = st.slider("Memory Usage (%)", 0, 100, 50)
disk = st.slider("Disk Usage (%)", 0, 100, 50)
processes = st.slider("Running Processes", 50, 400, 200)

if st.button("Predict"):

    prediction = model.predict([[memory, disk, processes]])

    st.success(f"Predicted CPU Usage: {prediction[0]:.2f}%")

    if prediction[0] > 85:
        st.error("⚠️ Potential system overload detected!")

# ----------------------------
# Show Dataset
# ----------------------------
st.subheader("Recent System Metrics")

st.dataframe(data.tail())

# ----------------------------
# Visualization
# ----------------------------
st.subheader("System Resource Usage")

fig, ax = plt.subplots()

ax.plot(data["cpu"], label="CPU")
ax.plot(data["memory"], label="Memory")
ax.plot(data["disk"], label="Disk")

# anomaly points
anomalies = data[data["anomaly"] == -1]

ax.scatter(
    anomalies.index,
    anomalies["cpu"],
    color="red",
    marker="x",
    label="Anomaly"
)

ax.set_xlabel("Time Index")
ax.set_ylabel("Usage %")

ax.legend()

st.pyplot(fig)

# ----------------------------
# Anomaly Summary
# ----------------------------
st.subheader("Detected Anomalies")

anomaly_rows = data[data["anomaly"] == -1]

if len(anomaly_rows) > 0:
    st.warning(f"{len(anomaly_rows)} anomalies detected in dataset")
    st.dataframe(anomaly_rows)
else:
    st.success("No anomalies detected")