# Author : InferiorAK
# Operators in Python
# 11 May 2024


#  Bitwise Operator
# ------------------
# &  - AND  ( x & y )   Sets each bit to 1 if both bits are 1            
# |  - OR   ( x | y )   Sets each bit to 1 if one of two bits is 1       
# ^  - XOR  ( x ^ y )   Sets each bit to 1 if only one of two bits is 1  
# ~  - NOT  ( ~x )      Inverts all the bits
# << - LEFT SHIFT   ( x << 2 )	  Zero fill left shift. Shift left by pushing zeros in from the right and let the leftmost bits fall off
# >> - RIGHT SHIFT  ( x >> 2 )    Signed right shift. Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off

# Bitwise Operation Priority Sequence if there are multiple Operators:
#     ~ , << >>, &, ^, |

# Left shift
x = 55
shift = 5
print(x << shift)  # The expression 55 << 5 means shifting the binary representation of the number 55 five positions to the left. This is a bitwise left shift operation.

# Suppose,
# 55 = 110111 (bin) --> (Before the bin, 0 is always presented there and after decimal point)

# #           1 1 0 1 1 1
# #         1 1 0 1 1 1 0    Shifted 1
# #       1 1 0 1 1 1 0 0    Shifted 2
# #     1 1 0 1 1 1 0 0 0    Shifted 3
# #   1 1 0 1 1 1 0 0 0 0    Shifted 4
# # 1 1 0 1 1 1 0 0 0 0 0    Shifted 5

# Shift the binary representation five positions to the left, padding with zeroes on the right:
# 110111 becomes 11011100000.
# Convert the result back to decimal:
# 11011100000 = 1760

# Right Shift
x = 55
shift = 5
print(x >> shift)  # The expression 55 >> 5 means shifting the binary representation of the number 55 five positions to the tight. This is a bitwise right shift operation.

# Suppose,
# 55 = 110111 (bin)

# # 1 1 0 1 1 1
# # 0 1 1 0 1 1    Shifted 1
# # 0 0 1 1 0 1    Shifted 2
# # 0 0 0 1 1 0    Shifted 3
# # 0 0 0 0 1 1    Shifted 4
# # 0 0 0 0 0 1    Shifted 5

# Shift the binary representation five positions to the right, padding with zeroes on the right:
# 110111 becomes 000001
# Convert the result back to decimal:
# 000001 = 1