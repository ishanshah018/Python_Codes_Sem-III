import numpy as np

arr = np.array([[34, 43, 73], [82, 22, 12], [53, 94, 66]])
max_axis_0 = np.max(arr, axis=0)
min_axis_1 = np.min(arr, axis=1)
print("Max from axis 0:", max_axis_0)
print("Min from axis 1:", min_axis_1)
