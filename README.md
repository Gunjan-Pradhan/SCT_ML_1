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
