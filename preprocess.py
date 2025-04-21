import pandas as pd

# Load dataset
df = pd.read_csv("bigmart_data.csv")

# 1. Handle missing values
df['Item_Weight'].fillna(df['Item_Weight'].mean(), inplace=True)
df['Outlet_Size'].fillna(df['Outlet_Size'].mode()[0], inplace=True)

# 2. Remove duplicate rows
df = df.drop_duplicates()

# 3. Standardize text values
df['Item_Fat_Content'] = df['Item_Fat_Content'].replace({
    'low fat': 'Low Fat',
    'LF': 'Low Fat',
    'reg': 'Regular'
})

# 4. Convert 'Outlet_Establishment_Year' to datetime
df['Outlet_Establishment_Year'] = pd.to_datetime(df['Outlet_Establishment_Year'], format='%Y')

# 5. Rename column headers
df.columns = df.columns.str.lower().str.replace(' ', '_')

# 6. Fix data types
df['item_weight'] = df['item_weight'].astype(float)
df['item_visibility'] = df['item_visibility'].astype(float)
df['item_mrp'] = df['item_mrp'].astype(float)
df['item_outlet_sales'] = df['item_outlet_sales'].astype(float)

# Save the cleaned dataset
df.to_csv("bigmart_data_cleaned.csv", index=False)

# Display first few rows
print(df.head())
