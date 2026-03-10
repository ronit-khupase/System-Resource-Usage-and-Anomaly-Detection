import os

print("\n==============================")
print("System Resource ML Pipeline")
print("==============================\n")

print("Step 1: Collecting system data...")
os.system("python data_collector.py")

print("\nStep 2: Training ML model...")
os.system("python train_model.py")

print("\nStep 3: Generating visualizations and anomaly detection...")
os.system("python visualize_results.py")

print("\nStep 4: Launching monitoring dashboard...")
os.system("streamlit run dashboard.py")