import pandas as pd

# Load original Kaggle training dataset
df = pd.read_csv("data/train.csv")

# Select only the required columns
selected_df = df[['GrLivArea', 'BedroomAbvGr', 'FullBath', 'SalePrice']]

# Rename them to simpler names for the task
selected_df = selected_df.rename(columns={
    'GrLivArea': 'square_feet',
    'BedroomAbvGr': 'bedrooms',
    'FullBath': 'bathrooms',
    'SalePrice': 'price'
})

# Show first 5 rows of the simplified dataset
print("Simplified dataset:")
print(selected_df.head())

# Check missing values
print("\nMissing values in simplified dataset:")
print(selected_df.isnull().sum())

# Save the simplified dataset as a new CSV file
selected_df.to_csv("simplified_house_data.csv", index=False)

print("\n'simplified_house_data.csv' has been created successfully!")