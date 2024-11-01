import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Generate dataset to test the functionality of the program
# Set random seed for reproducibility
np.random.seed(42)

# Generate dates
start_date = datetime(2023, 1, 1)
dates = [start_date + timedelta(days=x) for x in range(1000)]

# Create sample data
data = {
    'Date': dates,
    'Product': np.random.choice(['Laptop', 'Smartphone', 'Tablet', 'TV', 'Headphones'], 1000),
    'Category': np.random.choice(['Electronics', 'Appliances', 'Accessories'], 1000),
    'Sales': np.random.normal(500, 200, 1000),
    'Quantity': np.random.randint(1, 10, 1000),
    'Customer_Age': np.random.randint(18, 70, 1000),
    'Customer_Gender': np.random.choice(['Male', 'Female'], 1000),
    'Region': np.random.choice(['North', 'South', 'East', 'West'], 1000),
    'Customer_Satisfaction': np.random.randint(1, 6, 1000),
    'Discount_Applied': np.random.choice([True, False], 1000),
    'Shipping_Cost': np.random.uniform(5, 50, 1000)
}

# Create DataFrame
df = pd.DataFrame(data)

# Add some correlations
df['Total_Amount'] = df['Sales'] * df['Quantity'] + df['Shipping_Cost']
df['Profit_Margin'] = df['Sales'] * 0.3 + np.random.normal(0, 10, 1000)

# Add some missing values
mask = np.random.random(len(df)) < 0.05
df.loc[mask, 'Customer_Age'] = np.nan

# Save to CSV
df.to_csv('assets/synthetic_sales_data.csv', index=False)