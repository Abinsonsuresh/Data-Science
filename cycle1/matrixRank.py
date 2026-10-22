import numpy as np

A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

print("Original Matrix:")
print(A)

rank = np.linalg.matrix_rank(A)
print("Rank of Matrix:")
print(rank)

# OUTPUT
# Original Matrix:
# [[1 2 3]
#  [4 5 6]
#  [7 8 9]]
# Rank of Matrix:
# 2
