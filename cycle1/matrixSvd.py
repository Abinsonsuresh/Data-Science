import numpy as np

A = np.array([[1, 2],
              [3, 4]])

print("Original Matrix:")
print(A)

U, S, Vt = np.linalg.svd(A)

print("Left Singular Vectors (U):")
print(U)

print("Singular Values (S):")
print(S)

print("Right Singular Vectors Transpose (V^T):")
print(Vt)

# OUTPUT
# Original Matrix:
# [[1 2]
#  [3 4]]
# Left Singular Vectors (U):
# [[-0.40455358 -0.9145143 ]
#  [-0.9145143   0.40455358]]
# Singular Values (S):
# [5.4649857  0.36596619]
# Right Singular Vectors Transpose (V^T):
# [[-0.57604844 -0.81741556]
#  [ 0.81741556 -0.57604844]]
