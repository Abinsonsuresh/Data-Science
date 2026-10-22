import numpy as np

A = np.array([[1, 2],
              [3, 4]])

print("Original Matrix:")
print(A)

A_inv = np.linalg.inv(A)
print("Inverse of Matrix:")
print(A_inv)

# OUTPUT
# Original Matrix:
# [[1 2]
#  [3 4]]
# Inverse of Matrix:
# [[-2.   1. ]
#  [ 1.5 -0.5]]
