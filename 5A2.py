import numpy as np
import pandas as pd
from sklearn.metrics import mean_squared_error, mean_absolute_percentage_error, r2_score

# Load data
df = pd.read_excel(r'G:\My Drive\Google Drive Documents\Sneha Saragadam\Sneha Engineering Plan 2022-2025\Engineering Preparation\2nd Year\machinelearning\lab\Lab Session1 Data.xlsx', sheet_name='Purchase data')
A = df.iloc[:, 1:4]
C = df.iloc[:, 4]

# Perform calculations
dimensionality = A.shape[1]
num_vectors = A.shape[0]
rank_A = np.linalg.matrix_rank(A)
A_pseudo_inverse = np.linalg.pinv(A)
cost_per_product = np.dot(A_pseudo_inverse, C)

# Calculate metrics
predicted_prices = np.dot(A, cost_per_product)

mse = mean_squared_error(C, predicted_prices)
rmse = np.sqrt(mse)
mape = mean_absolute_percentage_error(C, predicted_prices) * 100
r2 = r2_score(C, predicted_prices)

# Print results
print("Dimensionality of the vector space:", dimensionality)
print("Number of vectors in the vector space:", num_vectors)
print("Rank of Matrix A:", rank_A)
print("Cost of each product using Pseudo-Inverse:")
print(cost_per_product)
print("MSE:", mse)
print("RMSE:", rmse)
print("MAPE:", mape)
print("R2 score:", r2)
