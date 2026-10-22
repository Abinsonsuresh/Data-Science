import numpy as np

A = np.array([[1, 2],
              [3, 4]])

B = np.array([[5, 6],
              [7, 8]])

print("Matrix A:")
print(A)

print("Matrix B:")
print(B)

result = np.dot(A, B)
print("Dot Product (A . B):")
print(result)

# OUTPUT
# Matrix A:
# [[1 2]
#  [3 4]]
# Matrix B:
# [[5 6]
#  [7 8]]
# Dot Product (A . B):
# [[19 22]
#  [43 50]]
