import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Create the dataset
data = {
    'Hours': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Marks': [35, 40, 45, 50, 55, 60, 65, 75, 85, 95]
}
df = pd.DataFrame(data)

# --- Matplotlib Scatter Plot ---
plt.figure(figsize=(8, 5))
plt.scatter(df['Hours'], df['Marks'], color='blue')
plt.title('Study Hours vs Marks (Matplotlib)', fontsize=14)
plt.xlabel('Study Hours')
plt.ylabel('Marks')
plt.grid(True)
plt.show()

# --- Seaborn Scatter Plot ---
plt.figure(figsize=(8, 5))
sns.scatterplot(x='Hours', y='Marks', data=df, color='green')
plt.title('Study Hours vs Marks (Seaborn)', fontsize=14)
plt.xlabel('Study Hours')
plt.ylabel('Marks')
plt.grid(True)
plt.show()

# --- Bonus: Seaborn with Regression Line ---
plt.figure(figsize=(8, 5))
sns.regplot(x='Hours', y='Marks', data=df, color='purple' ci="None" )
plt.title('Study Hours vs Marks with Regression Line')
plt.xlabel('Study Hours')
plt.ylabel('Marks')
plt.grid(True)
plt.show()
