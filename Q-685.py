import numpy as np
ar = np.array([[3, 6, 9, 12], [15, 18, 21, 24],
    [27, 30, 33, 36],
    [39, 42, 45, 48],
    [51, 54, 57, 60]
])
ans = ar[::2, 1::2]
print("Odd rows and even columns:")
print(ans)
