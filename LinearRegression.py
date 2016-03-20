
# -*- coding: utf-8 -*-

# SciPy (pronounced “Sigh Pie”) is a Python-based ecosystem of open-source software for mathematics, science, and engineering.
from scipy import stats
# NumPy is the fundamental package for scientific computing with Python
import numpy as np
from matplotlib import pyplot as plt

# training data
x = np.array([112, 345, 198, 305, 372, 550, 302, 420, 578])
y = np.array([1120, 1523, 2102, 2230, 2600, 3200, 3409, 3689, 4460])

# use the linear regression model
slope, intercept, r_value, p_value, std_err = stats.linregress(x,y)

# setup the graph
plt.plot(x, y, 'ro', color='black')
plt.ylabel('Price')
plt.xlabel('Size of house')
plt.axis([0, 600, 0, 5000])

# plot our slope line with color blue
plt.plot(x, x*slope + intercept, 'b')

plt.plot()
plt.show()

# Linear regression prediction
newX = 150
newY = newX * slope + intercept

# our predicted price based off of the linear regression is 1549.684
print(newY)
