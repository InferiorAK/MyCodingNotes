# Author : InferiorAK
# Hierarchical Inheritance in python

#             <--Boss-->
#                 |
#     -------------------------
#     |           |           |
#     m1          m2          m3
#     |           |           |
# ---------   ---------   ---------
# |   |   |   |   |   |   |   |   |
# s1  s2  s3  s4  s5  s6  s7  s8  s9

# Like a tree priority connection

class Owner:
    pass

class manager1(Owner):
    pass
class stuff1(manager1):
    pass
class stuff2(manager1):
    pass
class stuff3(manager1):
    pass

class manager2(Owner):
    pass
class stuff4(manager2):
    pass
class stuff5(manager2):
    pass
class stuff6(manager2):
    pass

class manager3(Owner):
    pass
class stuff7(manager3):
    pass
class stuff8(manager3):
    pass
class stuff9(manager3):
    pass