import numpy as np
from sklearn.linear_model import LinearRegression
from matplotlib import pyplot as plt
import pandas

data = pandas.read_csv('data.csv')
# y = np.array([item for item in data['Y/Ymax']])
# x = np.array([item for item in data['ET/Etmax']])
# x = np.array(x).reshape((-1, 1))
# y = np.array(y)
X = data.iloc[:,1:2].values
# y = data.iloc[:, 2].values
print('amin',X)
# lin = LinearRegression()
# lin.fit(x, y)

