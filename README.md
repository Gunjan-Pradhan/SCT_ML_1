# House Price Prediction using Linear Regression

## Project Overview
This project implements a **Linear Regression model** to predict **house prices** based on three key housing features:

- **Square Footage**
- **Number of Bedrooms**
- **Number of Bathrooms**

The task was completed as part of a **Machine Learning Internship**.  
The goal was to build a regression model, evaluate its performance, and understand how housing features influence selling price.

---

## Objective
To develop a machine learning model that predicts the **price of a house** using:
- `square_feet`
- `bedrooms`
- `bathrooms`

---

## Dataset
The dataset used for this project is based on the Kaggle dataset:

**House Prices – Advanced Regression Techniques**

Since the internship task specifically required prediction using only square footage, bedrooms, and bathrooms, the original dataset was filtered to keep only the relevant columns.

### Selected Features from Kaggle Dataset

| Kaggle Column | Used As |
|---|---|
| `GrLivArea` | `square_feet` |
| `BedroomAbvGr` | `bedrooms` |
| `FullBath` | `bathrooms` |
| `SalePrice` | `price` |

The cleaned dataset was saved as:

```text
simplified_house_data.csv


# Results - House Price Prediction using Linear Regression

## Dataset Summary
The simplified dataset used for this project contained:

- **Total records:** 1460
- **Input features:** 3
  - `square_feet`
  - `bedrooms`
  - `bathrooms`
- **Target variable:** `price`

The dataset was prepared from the Kaggle **House Prices – Advanced Regression Techniques** dataset by selecting only the features required for the internship task.

---

## Train-Test Split
The dataset was divided into training and testing sets as follows:

- **Training set size:** 1168 records
- **Testing set size:** 292 records

This split was performed using an **80:20 ratio**, where 80% of the data was used for training the model and 20% was used for testing its performance.

---

## Linear Regression Model Equation
After training, the model learned the following regression equation:

**Price = 52261.75 + 104.03(square_feet) - 26655.17(bedrooms) + 30014.32(bathrooms)**

### Coefficients Obtained
- **Intercept:** 52261.75
- **square_feet coefficient:** 104.03
- **bedrooms coefficient:** -26655.17
- **bathrooms coefficient:** 30014.32

---

## Model Evaluation Metrics
The model was evaluated on the test dataset using standard regression metrics.

- **MAE (Mean Absolute Error):** 35788.06
- **MSE (Mean Squared Error):** 2806426667.25
- **RMSE (Root Mean Squared Error):** 52975.72
- **R² Score:** 0.6341

---

## Interpretation of Results

### 1. Square Footage
The coefficient for **square_feet** is **104.03**, which means that, keeping the other features constant, an increase of 1 square foot increases the predicted house price by approximately **104.03** units.

### 2. Bedrooms
The coefficient for **bedrooms** is **-26655.17**. This negative coefficient suggests that, when square footage and bathrooms are already taken into account, an increase in the number of bedrooms may reduce the predicted price in this model. This can happen because of feature correlation in the dataset.

### 3. Bathrooms
The coefficient for **bathrooms** is **30014.32**, which means that adding one bathroom increases the predicted price by approximately **30014.32** units, assuming the other features remain constant.

---

## Model Performance Analysis
The **R² score of 0.6341** indicates that the model explains approximately **63.4% of the variation in house prices** using only the selected three features.

This is a reasonable result because house prices are influenced by many additional factors such as:
- location
- neighborhood
- year built
- overall quality
- garage area
- lot size
- basement features

Since this model intentionally uses only **square footage, bedrooms, and bathrooms**, the result is acceptable for a basic regression task.

---

## Actual vs Predicted Results
A comparison of actual and predicted house prices was generated and saved in:

```text
predicted_vs_actual.csv
