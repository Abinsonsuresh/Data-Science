import numpy as np

m = np.array([
    [1,2],
    [3,4]
])

n = np.array([
    [4,1],
    [7,2]
])

print(m)

# Inverse
inv = np.linalg.inv(m)
print(inv)

# Transpose

trans = np.transpose(m)
print(trans)

# RANK
rank = np.linalg.matrix_rank(m)
print(rank)

# PRODUCT
dot = np.dot(m,n)
print(dot)