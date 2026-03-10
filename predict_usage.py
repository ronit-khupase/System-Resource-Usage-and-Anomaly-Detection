import pickle
import pandas as pd

model = pickle.load(open("model.pkl","rb"))

memory = float(input("Memory usage %: "))
disk = float(input("Disk usage %: "))
processes = int(input("Running processes: "))

data = pd.DataFrame([[memory, disk, processes]],
columns=["memory","disk","processes"])

prediction = model.predict(data)

print("Predicted CPU usage:", prediction[0])