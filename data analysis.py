import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('sales_data.csv')

# Display the first few rows of the dataframe
print("First few rows of the dataset:")
print(df.head())

# Data exploration tasks

# Filtering data for a specific store
store_a_data = df[df['store'] == 'Store A']
print("\nData for Store A:")
print(store_a_data)

# Sorting data by date and quantity
sorted_data = df.sort_values(by=['date', 'quantity'], ascending=[True, False])
print("\nData sorted by date and quantity:")
print(sorted_data)

# Grouping data by store and product, and calculating the total quantity sold
grouped_data = df.groupby(['store', 'product'])['quantity'].sum().reset_index()
print("\nTotal quantity sold by store and product:")
print(grouped_data)

# Summary statistics
print("\nSummary statistics for quantity:")
print("Mean:", df['quantity'].mean())
print("Median:", df['quantity'].median())
print("Standard Deviation:", df['quantity'].std())

# Data visualization

# Bar plot of total quantity sold by store and product
plt.figure(figsize=(10, 6))
sns.barplot(x='store', y='quantity', hue='product', data=grouped_data)
plt.title('Total Quantity Sold by Store and Product')
plt.show()

# Distribution of quantities sold
plt.figure(figsize=(10, 6))
sns.histplot(df['quantity'], kde=True)
plt.title('Distribution of Quantities Sold')
plt.xlabel('Quantity')
plt.ylabel('Frequency')
plt.show()

# Box plot of price distributions by store
plt.figure(figsize=(10, 6))
sns.boxplot(x='store', y='price', data=df)
plt.title('Price Distribution by Store')
plt.show()
