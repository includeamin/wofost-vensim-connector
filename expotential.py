import numpy
import numpy as np
from plotly.figure_factory._distplot import scipy
from scipy.optimize import curve_fit
from sklearn.linear_model import LinearRegression
from matplotlib import pyplot as plt
import pandas

data = pandas.read_csv('data.csv')
y = np.array([item for item in data['Y/Ymax']])
x = np.array([item for item in data['ET/Etmax']])

# temp = numpy.polyfit(x, numpy.log(y), 1)

temp = scipy.optimize.curve_fit(lambda t,a,b: a*numpy.exp(b*t),  x,  y,  p0=(4, 0.1))
print(temp)


# popt, pcov = curve_fit(lambda fx,a,b: a*fx**-b,  x,  y)
# power_y = popt[0]*x**-popt[1]
#
# plt.scatter(x, y, label='actual data')
# plt.plot(x, temp, label='power-fit')
# plt.legend()
# plt.show()
