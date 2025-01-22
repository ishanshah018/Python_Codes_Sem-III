# Original array:
# [[34 43 73]
#  [82 22 12]
#  [53 94 66]]

# Sorted array (by second row):
# [[73 43 34]
#  [12 22 82]
#  [66 94 53]]

# Sorted array: (by second column):
# [[82, 22, 12],
#  [34, 43, 73],
#  [53, 94, 66]]


import numpy as np

q=([[34,43,73],[82,22,12],[53,94,66]])

# Case 1:
si_r = np.argsort(q[1, :])
sa1 = q[:, si_r]

# Case 2:
si_c = np.argsort(array[:, 1])  
sa2 = q[si_c, :]  

print(sa1)
print(sa2)
