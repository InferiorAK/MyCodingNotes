# AUthor : InferiorAK
# array slicing in numpy

import numpy as np

lst = [  
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]],  # matrix-1
    [[5, 1, 9], [3, 4, 6], [2, 8, 7]],  # matrix-2
    [[3, 2, 8], [9, 1, 5], [6, 4, 7]]   # matrix-3
]

print(lst[2][1][1:3])  # This is what we do in list

A = np.array([  
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]],  # matrix-1
    [[5, 1, 9], [3, 4, 6], [2, 8, 7]],  # matrix-2
    [[3, 2, 8], [9, 1, 5], [6, 4, 7]]   # matrix-3
]
)

print(A[2, 1, 1:3]) # It means: 3rd matrix's 2nd row's 2 to 3rd element
print(A[0:2, 0:2, 0:2])