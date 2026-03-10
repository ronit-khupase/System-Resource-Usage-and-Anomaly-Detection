import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import pickle

data = pd.read_csv("dataset/system_metrics.csv")

X = data[["memory", "disk", "processes"]]
y = data["cpu"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = RandomForestRegressor(n_estimators=100)
model.fit(X_train, y_train)

score = model.score(X_test, y_test)

print("Model accuracy:", score)

pickle.dump(model, open("model.pkl", "wb"))