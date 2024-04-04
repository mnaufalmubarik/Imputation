import pandas as pd
import matplotlib.pyplot as plt

# Import Dataset
data = pd.read_csv('df_0.2.csv')
print(data)
X = data.drop('Time', axis=1)
# Check for missing data
missing_data = X.isnull().sum()
print(missing_data)
X1 = X['LIMS:1110SUEZ0002.SALT']
print('X1 is \n', X1)
X2 = X['LIMS:1110SUEZ0002.SALT']
X3 = X['LIMS:1110SUEZ0002.SALT']
X4 = X['LIMS:1110SUEZ0002.SALT']
X5 = X['LIMS:1110SUEZ0002.SALT']
X6 = X['LIMS:1110SUEZ0002.SALT']
X7 = X['LIMS:1110SUEZ0002.SALT']
X8 = X['LIMS:1110SUEZ0002.SALT']
X9 = X['LIMS:1110SUEZ0002.SALT']

# Imputation
missing_columns = ['LIMS:1110SUEZ0002.SALT', 'LIMS:1110SUEZ0005.SALT', 'LIMS:1110SUEZ0005.BSW CRUDE', 'LIMS:1110SUEZ0007.SALT'
                   , 'LIMS:1110SUEZ0010.BSW CRUDE',
                   'LIMS:1110SUEZ0010.SALT', 'LIMS:1110SUEZ0016.Cl', 'LIMS:1110SUEZ0016.pH', 'LIMS:1110SUEZ0016.Tfe']
for col in missing_columns:
    mean = X[col].mean()
    X[col] = X[col].fillna(mean)

# access the imputed X1 column
X1_i = X['LIMS:1110SUEZ0002.SALT']
X2_i = X['LIMS:1110SUEZ0002.SALT']
X3_i = X['LIMS:1110SUEZ0002.SALT']
X4_i = X['LIMS:1110SUEZ0002.SALT']
X5_i = X['LIMS:1110SUEZ0002.SALT']
X6_i = X['LIMS:1110SUEZ0002.SALT']
X7_i = X['LIMS:1110SUEZ0002.SALT']
X8_i = X['LIMS:1110SUEZ0002.SALT']
X9_i = X['LIMS:1110SUEZ0002.SALT']

# print the imputed X1
print('The new X1 is \n', X1_i)

# 2nd Check for missing data
missing_data = X.isnull().sum()
print(missing_data)

# Create a new column with the first day of each month
data['Time'] = pd.to_datetime(data['Time'])
data['Month'] = data['Time'].dt.to_period('M').apply(lambda x: x.start_time)

#Plot for every variables
import matplotlib.pyplot as plt
plt.scatter(data['Time'], X1_i, label='Imputted', color='red')
plt.scatter(data['Time'], X1, label='Raw', color='blue')
plt.xlabel('Time')
plt.ylabel('Value')
plt.title('LIMS:1110SUEZ0002.SALT')
plt.legend()
plt.show()
plt.savefig('LIMS:1110SUEZ0002.SALT - Mean.png')
plt.close()