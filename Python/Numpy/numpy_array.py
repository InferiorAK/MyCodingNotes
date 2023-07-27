# AUthor : InferiorAK
# numpy array in python

import numpy as np

# 0Dimension Array
lst = np.array([1, 2, 3]) # simple numpy array --> called list in python

# 1D Array
A = np.array([
    [5, 6, 7],
    [8, 9, 4],
    [1, 7, 3]
])
B = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print(type(lst))
print(A)
print(A.shape) # ম্যাট্রিক্সের ক্রম -> (row, column)

print(lst[2])
print("3rd Element of 2nd Row:", A[1, 2])

# 2D Array
C = np.array([  
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]],  # matrix-1
    [[5, 1, 9], [4, 3, 6], [2, 8, 7]]   # matrix-2
]
)

print(C)
print("This is the Dimension count of C:", C.ndim)

# 3D Array
D = np.array([
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]],  # matrix-1
    [[5, 1, 9], [3, 4, 6], [2, 8, 7]],  # matrix-2
    [[3, 2, 8], [9, 1, 5], [6, 4, 7]]   # matrix-3
]
)

print(D)
print("This is the Dimension count of C:", D.ndim)
print("3rd Dimension's 2nd row's 3rd element :", D[2, 1, 2])

# Like this it can have more .... n Dimension

E = np.array([1, 2, 3], ndmin=10)
print(E)