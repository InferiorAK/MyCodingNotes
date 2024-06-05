# Author : InferiorAK
# Data Types in Python
# 5 June 2024

#                                                   Data Types
#     ------------------------------------------------------------------------------------------------------
#     Numbers                  Bool                  Sequence                  Mapping                  Sets
#     -------                 ------                ----------                ---------                ------
#   - int     69           - True, False           - string "demo"           - dict {"id":1,"n":5}    - set        {1,2,3}
#   - float   69.69                                - list   [1,1.1,"a"]                               - frozenset  frozenset({1, 2, 3})
#   - complex 1+6j                                 - tuple  (1,1.1,"a")

x = 69
z = 69 + 69j  # It means z=69+69i

print(int(x))
print(float(x))
print(complex(x))

# Complex
print(z.real)
print(z.imag)