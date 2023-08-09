# AUthor : InferiorAK
# array functions and Methods in numpy

# # Array Creation:
#     numpy.array()
#     numpy.zeros()
#     numpy.ones()
#     numpy.empty()
#     numpy.full()
#     numpy.arange()
#     numpy.linspace()
#     numpy.logspace()
#     numpy.eye()
#     numpy.random.rand()
#     numpy.random.randn()
#     numpy.random.randint()
#     numpy.random.random()
#     numpy.random.choice()

# # Array Operations:
#     Arithmetic: +, -, *, /, //, %, **
#     numpy.dot()
#     numpy.cross()
#     numpy.inner()
#     numpy.outer()
#     numpy.matmul()
#     numpy.tensordot()
#     numpy.kron()

# # Array Manipulation:
#     ndarray.shape
#     ndarray.ndim
#     ndarray.size
#     ndarray.reshape()
#     ndarray.resize()
#     ndarray.flatten()
#     ndarray.ravel()
#     ndarray.swapaxes()
#     ndarray.transpose()
#     numpy.concatenate()
#     numpy.vstack()
#     numpy.hstack()
#     numpy.dstack()
#     numpy.split()
#     numpy.hsplit()
#     numpy.vsplit()
#     numpy.dsplit()

# # Indexing and Slicing:
#     Indexing: ndarray[index]
#     Slicing: ndarray[start:end]
#     Fancy indexing
#     Boolean indexing

# # Broadcasting:
#     Element-wise operations on arrays with different shapes.

# # Mathematical Functions:
#     Trigonometric: numpy.sin(), numpy.cos(), numpy.tan()
#     Exponential: numpy.exp(), numpy.log(), numpy.log10()
#     Square root: numpy.sqrt()
#     Rounding: numpy.floor(), numpy.ceil(), numpy.round()

# # Statistical Functions:
#     ndarray.mean()
#     ndarray.median()
#     ndarray.std()
#     ndarray.sum()
#     ndarray.min()
#     ndarray.max()
#     ndarray.argmax()
#     ndarray.argmin()
#     numpy.percentile()
#     numpy.var()

# # Linear Algebra:
#     numpy.linalg.inv()
#     numpy.linalg.det()
#     numpy.linalg.eig()
#     numpy.linalg.solve()
#     numpy.dot() for matrix multiplication

# # Sorting and Searching:
#     numpy.sort()
#     numpy.argsort()
#     numpy.searchsorted()
#     numpy.argmax()
#     numpy.argmin()

# # Set Operations:
#     numpy.unique()
#     numpy.intersect1d()
#     numpy.union1d()
#     numpy.setdiff1d()
#     numpy.in1d()
    
# # Boolean Logic:
#     numpy.logical_and()
#     numpy.logical_or()
#     numpy.logical_not()
#     numpy.logical_xor()

# # Reshaping:
#     numpy.reshape()
#     numpy.ravel()
#     numpy.expand_dims()
#     numpy.squeeze()


# Example
import numpy as np

A = np.array([
    [1, 2, 3],
    [5, 6, 7],
    [8, 9, 0]
])
# print(np.transpose(A))
# print(A.transpose())
print("Transpose Matrix:\n", A.T)
print("Matrix total Elements:", A.size)

I = np.identity(4, dtype="int16")  # Identity Matrix
print("Identity Matrix:\n", I)
print(I.shape)

B = np.arange(15)
print(B)

C = B.reshape(3, 5)  # the multiplication of the shape must be equal to arange. ex: 3x5=15
D = B.reshape(5, 3)
E = np.array([
    [7, 2, 4, 1],
    [5, 3, 8, 6],
    [1, 0, 9, 5]
])
print(C)
print(D)
print(E.reshape(4, 3))

print(F :=E.ravel())    # It will make the matrix Straight single row
print(F.shape)

#       ======> axis1
#   |  [a11, a12, a13]
#   |  [a21, a22, a23]
#  \ / [a31, a32, a33]
#  axis0

# sum(axis=1) = [row summation]
# sum(axis=0) = [column summation]

G = np.array([
    [8, 2, 0, 1],
    [5, 4, 2, 3],
    [9, 1, 0, 5]
])
print(G.sum(axis=0))
print(G.sum(axis=1))