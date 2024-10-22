# filename: plot_cars_final.py
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

# Step 2: Print the fields in the dataset
print(data.columns.tolist())

# Step 3: Data Cleaning
# Selecting relevant columns and dropping rows with missing values
data = data[['weight', 'horsepower']].dropna() 

# Converting horsepower to numeric, coercing errors to handle invalid entries
data['horsepower'] = pd.to_numeric(data['horsepower'], errors='coerce')

# Dropping any rows that still have NaN values after conversion
data = data.dropna()

# Step 4: Plot the relationship between weight and horsepower
plt.figure(figsize=(10, 6))
sns.scatterplot(x='weight', y='horsepower', data=data, alpha=0.7, marker='o', color='blue')
sns.regplot(x='weight', y='horsepower', data=data, scatter=False, color='red', label='Trend Line')

plt.title('Relationship between Weight and Horsepower')
plt.xlabel('Weight')
plt.ylabel('Horsepower')
plt.grid(True)
plt.legend()

plt.annotate('Higher weight tends to correlate with higher horsepower', 
             xy=(data['weight'].mean(), data['horsepower'].mean()), 
             xytext=(data['weight'].mean() - 1000, data['horsepower'].mean() + 20),
             arrowprops=dict(facecolor='black', shrink=0.05))

# Step 5: Save the plot to a file
plt.savefig('weight_vs_horsepower_final.png')
plt.close()