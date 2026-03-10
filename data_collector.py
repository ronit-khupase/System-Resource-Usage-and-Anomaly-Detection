import psutil
import pandas as pd

data = []

print("Collecting system data...")

for i in range(100):

    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent
    processes = len(psutil.pids())

    data.append({
        "cpu": cpu,
        "memory": memory,
        "disk": disk,
        "processes": processes
    })

df = pd.DataFrame(data)

df.to_csv("dataset/system_metrics.csv", index=False)

print("Dataset created successfully!")