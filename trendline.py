# X = np.array(
#
#     [[0.27090301, 0.4656891496],
#      [0.3080357143, 0.5970809376],
#      [0.3826666667, 0.6700470844],
#      [0.3629402757, 0.7086261981],
#      [0.8174904943, 0.7212713936],
#      [1.739495798, 0.7240230233],
#      [0.58, 0.6905592841]]
#
# )
import numpy as np
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression

X = np.array(

    [
        [0.175292154, 0.028169014
         ],
        [0.06235012, 0.142099682
         ],
        [0.028179741, 0.276517922
         ],
        [0.012065574, 0.404278922
         ],
        [0.013648232, 0.511952555
         ],
        [0.961325967, 0.856195607
         ]]

)
import operator

import numpy as np
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import PolynomialFeatures

# np.random.seed(0)
# x = 2 - 3 * np.random.normal(0, 1, 20)
# y = x - 2 * (x ** 2) + 0.5 * (x ** 3) + np.random.normal(-3, 3, 20)
y = np.array([item[0] for item in X])
x = np.array([item[1] for item in X])
# transforming the data to include another axis
x = x[:, np.newaxis]
y = y[:, np.newaxis]

polynomial_features = PolynomialFeatures(degree=2)
x_poly = polynomial_features.fit_transform(x)

model = LinearRegression()
model.fit(x_poly, y)
y_poly_pred = model.predict(x_poly)

rmse = np.sqrt(mean_squared_error(y, y_poly_pred))
r2 = r2_score(y, y_poly_pred)
print(rmse)
print(r2)

plt.scatter(x, y, s=10)
# sort the values of x before line plot
sort_axis = operator.itemgetter(0)
sorted_zip = sorted(zip(x, y_poly_pred), key=sort_axis)
x, y_poly_pred = zip(*sorted_zip)
plt.plot(x, y_poly_pred, color='m')
plt.show()
