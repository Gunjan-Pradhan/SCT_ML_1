import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# --------------------------------------------------
# 1. Load the simplified dataset
# --------------------------------------------------
df = pd.read_csv("simplified_house_data.csv")

print("First 5 rows of dataset:")
print(df.head())

print("\nDataset shape:", df.shape)

print("\nMissing values:")
print(df.isnull().sum())

# --------------------------------------------------
# 2. Define input features (X) and target (y)
# --------------------------------------------------
X = df[['square_feet', 'bedrooms', 'bathrooms']]
y = df['price']

print("\nInput Features (X):")
print(X.head())

print("\nTarget (y):")
print(y.head())

# --------------------------------------------------
# 3. Split data into training and testing sets
# --------------------------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("\nTraining set size:", X_train.shape)
print("Testing set size:", X_test.shape)

# --------------------------------------------------
# 4. Create and train Linear Regression model
# --------------------------------------------------
model = LinearRegression()
model.fit(X_train, y_train)

# --------------------------------------------------
# 5. Print model parameters
# --------------------------------------------------
print("\nModel trained successfully!")

print("\nIntercept:")
print(model.intercept_)

print("\nCoefficients:")
for feature, coef in zip(X.columns, model.coef_):
    print(f"{feature}: {coef}")

# --------------------------------------------------
# 6. Predict on test data
# --------------------------------------------------
y_pred = model.predict(X_test)

print("\nFirst 10 predictions:")
print(y_pred[:10])

# --------------------------------------------------
# 7. Evaluate the model
# --------------------------------------------------
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

print("\nModel Evaluation:")
print("MAE  :", mae)
print("MSE  :", mse)
print("RMSE :", rmse)
print("R² Score:", r2)

# --------------------------------------------------
# 8. Compare actual vs predicted values
# --------------------------------------------------
results = pd.DataFrame({
    'Actual Price': y_test.values,
    'Predicted Price': y_pred
})

print("\nActual vs Predicted (first 10 rows):")
print(results.head(10))

# --------------------------------------------------
# 9. Save results to a CSV file
# --------------------------------------------------
results.to_csv("predicted_vs_actual.csv", index=False)
print("\n'predicted_vs_actual.csv' file created successfully!")

# --------------------------------------------------
# 10. Plot Actual vs Predicted values
# --------------------------------------------------
plt.figure(figsize=(8, 6))
plt.scatter(y_test, y_pred, alpha=0.7)
plt.xlabel("Actual Price")
plt.ylabel("Predicted Price")
plt.title("Actual vs Predicted House Prices")
plt.grid(True)
plt.show()

# --------------------------------------------------
# 11. Correlation Heatmap
# --------------------------------------------------
plt.figure(figsize=(6, 4))
sns.heatmap(df.corr(), annot=True, cmap='Blues')
plt.title("Correlation Heatmap")
plt.show()

# --------------------------------------------------
# 12. Predict price for a new sample house
# --------------------------------------------------
new_house = pd.DataFrame({
    'square_feet': [2000],
    'bedrooms': [3],
    'bathrooms': [2]
})

predicted_price = model.predict(new_house)

print("\nPredicted price for a new house (2000 sq ft, 3 bed, 2 bath):")
print(predicted_price[0])