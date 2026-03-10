# System Resource Usage Prediction & Anomaly Detection

A machine learning-based system monitoring tool that predicts CPU usage and detects abnormal system behavior using system performance metrics.
The project collects or generates system resource data, trains an ML model for prediction, and visualizes trends with an interactive dashboard.

---

## Features

* Predict CPU usage using machine learning
* Detect anomalies in system behavior using Isolation Forest
* Visualize system resource trends and correlations
* Interactive monitoring dashboard built with Streamlit
* Modular pipeline for dataset generation, training, and prediction

---

## Technologies Used

* Python
* Pandas
* Scikit-learn
* Matplotlib
* Seaborn
* Streamlit
* psutil

---

## Project Structure

```id="mlprojstruct"
System-Resource-Usage-and-Anomaly-Prediction
│
├── dataset/
│   └── system_metrics.csv
│
├── data_collector.py
├── train_model.py
├── predict_usage.py
├── detect_anomalies.py
├── visualize_results.py
├── dashboard.py
├── main.py
├── requirements.txt
└── README.md
```

---

## Installation

Clone the repository:

```id="clonecmd"
git clone https://github.com/ronit-khupase/System-Resource-Usage-and-Anomaly-Prediction-.git
```

Move into the project directory:

```id="cdcmd"
cd System-Resource-Usage-and-Anomaly-Prediction-
```

Install dependencies:

```id="installcmd"
pip install -r requirements.txt
```

---

## How to Run the Project

Run the main pipeline:

```id="runmain"
python main.py
```

This will:

1. Collect or generate system resource data
2. Train the machine learning model
3. Visualize system resource trends and anomalies
4. Launch the monitoring dashboard

---

## Launch Dashboard Directly

You can also run the dashboard separately:

```id="rundash"
streamlit run dashboard.py
```

The dashboard will open at:

```
http://localhost:8501
```

---

## Dataset

The dataset contains system performance metrics such as:

* CPU usage
* Memory usage
* Disk usage
* Number of running processes

These metrics are used to train the model and detect abnormal system behavior.

---

## Machine Learning Models

* **Regression Model:** Predict CPU usage from system metrics
* **Isolation Forest:** Detect anomalies in system performance

---

## Visualizations

The project provides:

* System resource usage trends over time
* Correlation heatmap between metrics
* Anomaly visualization on monitoring graphs

---

## Author

**Ronit Khupase**

GitHub:
https://github.com/ronit-khupase

