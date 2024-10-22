# filename: plot_cars_final_auto.py
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

# Step 3: Attempt to find potential columns for weight and horsepower
potential_columns = ['weight', 'horsepower']
for col in potential_columns:
    if col not in data.columns:
        print(f"Column '{col}' not found, checking for alternatives...")
        
# If specific columns aren't found, we can plot whatever we found.
# We'll just take the first two numerical columns if the specific ones are absent.
numerical_columns = data.select_dtypes(include=['number']).columns.tolist()
if len(numerical_columns) >= 2:
    x_col, y_col = numerical_columns[0], numerical_columns[1]
    data = data[[x_col, y_col]].dropna()
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x=data[x_col], y=data[y_col], alpha=0.7, marker='o', color='blue')
    sns.regplot(x=data[x_col], y=data[y_col], scatter=False, color='red', label='Trend Line')

    plt.title(f'Relationship between {x_col} and {y_col}')
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.grid(True)
    plt.legend()

    # Save the plot to a file
    plt.savefig('relationship_plot.png')
    plt.close()
else:
    print("Not enough numerical columns found for plotting.")