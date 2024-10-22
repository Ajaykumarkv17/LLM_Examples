# filename: plot_cars_final_debug.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Download the dataset
try:
    url = "https://raw.githubusercontent.com/uwdata/draco/master/data/cars.csv"
    data = pd.read_csv(url)
except Exception as e:
    print(f"Error fetching data: {e}")
    raise

# Step 2: Print the fields in the dataset and the first few rows
print("Columns in the dataset:", data.columns.tolist())
print(data.head())

# Stop the execution here for analysis
raise SystemExit("Check the columns and data printed above.")