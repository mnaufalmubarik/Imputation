# Import Dataset
import pandas as pd
data = pd.read_csv('df_0.2.csv')
print(data)
X = data.drop('Time', axis=1)

# Check for missing data
missing_data = X.isnull().sum()
print(missing_data)
X1 = X['LIMS:1110SUEZ0002.SALT']
print('X1 is \n', X1)
X2 = X['LIMS:1110SUEZ0005.SALT']
X3 = X['LIMS:1110SUEZ0005.BSW CRUDE']
X4 = X['LIMS:1110SUEZ0007.SALT']
X5 = X['LIMS:1110SUEZ0010.BSW CRUDE']
X6 = X['LIMS:1110SUEZ0010.SALT']
X7 = X['LIMS:1110SUEZ0016.Cl']
X8 = X['LIMS:1110SUEZ0016.pH']
X9 = X['LIMS:1110SUEZ0016.Tfe']

# Function to perform random imputation on multiple columns
import random
import numpy as np
# Identify units with complete observations
complete_units = X.isnull().sum(axis=1) == 0

# Function to perform cold deck imputation on multiple columns
def cold_deck_imputation(data, columns, complete_units):
    imputed_data = data.copy()
    for col in columns:
        missing_indices = imputed_data[col].isnull()
        donors = imputed_data[complete_units][col].values
        imputed_data.loc[missing_indices, col] = np.random.choice(donors, size=np.sum(missing_indices), replace=True)
    return imputed_data

# Perform cold deck imputation
X_imputed = cold_deck_imputation(X, X.columns, complete_units)

# access the imputed X1 column
X1_i = X_imputed['LIMS:1110SUEZ0002.SALT']
X2_i = X_imputed['LIMS:1110SUEZ0005.SALT']
X3_i = X_imputed['LIMS:1110SUEZ0005.BSW CRUDE']
X4_i = X_imputed['LIMS:1110SUEZ0007.SALT']
X5_i = X_imputed['LIMS:1110SUEZ0010.BSW CRUDE']
X6_i = X_imputed['LIMS:1110SUEZ0010.SALT']
X7_i = X_imputed['LIMS:1110SUEZ0016.Cl']
X8_i = X_imputed['LIMS:1110SUEZ0016.pH']
X9_i = X_imputed['LIMS:1110SUEZ0016.Tfe']

# print the imputed X1
print('The new X1 is \n', X1_i)

# 2nd Check for missing data
missing_data = X_imputed.isnull().sum()
print(missing_data)

# Create a new column with the first day of each month
data['Time'] = pd.to_datetime(data['Time'])
data['Month'] = data['Time'].dt.to_period('M').apply(lambda x: x.start_time)

#Plot for every variables
import matplotlib.pyplot as plt

# Create a new figure with a specified width and height
fig, ax = plt.subplots(figsize=(22, 6))  # 20 is the width, 8 is the height

# Plot the data
ax.plot(data['Time'], X1_i, label='Imputted', color='red')
ax.plot(data['Time'], X1, label='Raw', color='blue')

# Set the labels
ax.set_xlabel('Time', fontsize=15)
ax.set_ylabel('Value', fontsize=15)
ax.set_title('LIMS:1110SUEZ0002.SALT', fontsize=20)
ax.legend()

# Add a grid
ax.grid(True, linestyle='--', linewidth=1, color='gray')

# Show the plot
# Specify the path to the folder
import os
folder_path = 'df2_visual'

# Create the folder if it doesn't exist
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

# Save the plot with the full path
plt.savefig(os.path.join(folder_path, 'LIMS:1110SUEZ0002.SALT - Coldeck.png'))
plt.close()

