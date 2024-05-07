# Python script for data visualization using Matplotlib and Seaborn

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the extracted data into a Pandas DataFrame
df = pd.read_csv('customer_sales_data.csv')  # Replace 'customer_sales_data.csv' with the name of your CSV file

# Create a time series plot of monthly sales trends
df['order_date'] = pd.to_datetime(df['order_date'])  # Convert 'order_date' column to datetime format
monthly_sales = df.resample('M', on='order_date')['quantity'].sum()  # Resample data to monthly frequency
monthly_sales.plot(kind='line', figsize=(10, 6), color='blue')
plt.title('Monthly Sales Trends')
plt.xlabel('Month')
plt.ylabel('Total Sales Quantity')
plt.grid(True)
plt.show()

# Create a bar plot of top-selling products
top_products = df.groupby('product_name')['quantity'].sum().nlargest(10)  # Get top 10 best-selling products
top_products.plot(kind='bar', figsize=(10, 6), color='green')
plt.title('Top 10 Best-Selling Products')
plt.xlabel('Product Name')
plt.ylabel('Total Sales Quantity')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
