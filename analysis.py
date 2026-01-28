# STEP 1: Import Libraries
import pandas as pd
import os

print("Current Folder:", os.getcwd())
print("Files here:", os.listdir())

data = pd.read_csv("sales_data.csv")
print(data.head())


# STEP 2: Load Dataset
data = pd.read_csv("sales_data.csv")

# STEP 3: Data Overview
print("First 5 rows:\n", data.head())
print("\nDataset Info:")
print(data.info())

# STEP 4: Data Cleaning
data.drop_duplicates(inplace=True)
data['OrderDate'] = pd.to_datetime(data['OrderDate'])

# Create TotalSales column
data['TotalSales'] = data['Quantity'] * data['Price']

# STEP 5: Basic Analysis
total_revenue = data['TotalSales'].sum()
print("\nTotal Revenue:", total_revenue)

# Monthly Sales
data['Month'] = data['OrderDate'].dt.month
monthly_sales = data.groupby('Month')['TotalSales'].sum()
print("\nMonthly Sales:\n", monthly_sales)

# Category-wise Sales
category_sales = data.groupby('Category')['TotalSales'].sum()
print("\nCategory Sales:\n", category_sales)

# Top Products
top_products = data.groupby('Product')['TotalSales'].sum().sort_values(ascending=False)
print("\nTop Products:\n", top_products)

# STEP 6: Visualization

# Monthly Sales Trend
plt.figure()
plt.plot(monthly_sales.index, monthly_sales.values, marker='o')
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales Amount")
plt.show()

# Category Sales Bar Chart
plt.figure()
category_sales.plot(kind='bar')
plt.title("Category-wise Sales")
plt.xlabel("Category")
plt.ylabel("Sales Amount")
plt.show()

# Top Products Bar Chart
plt.figure()
top_products.plot(kind='bar')
plt.title("Product-wise Sales")
plt.xlabel("Product")
plt.ylabel("Sales Amount")
plt.show()

print("\nAnalysis Completed Successfully!")

