import numpy as np

f = np.array([0, 12, 45.21, 34, 99.91, 32])
c = (5 / 9) * (f - 32)
s_c = np.sort(celsius)
position_zero = np.where(s_c == 0.0)
print("Fahrenheit values:", fahrenheit)
print("Celsius values:", celsius)
print("Sorted Celsius:", s_c)
print("Position of 0.0:", position_zero)
