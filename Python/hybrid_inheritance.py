# Author : InferiorAK
# Hybrid Inheritance in python

# 	   class1
#     /      \
# class2   class3
#     \      /
#    HybridClass

# 	_________class1_________
# 	\/		   ||		  \/
#   class1     ||     	class2
# 	|          \/         |
# 	|___> CenterClass <___|
#		(hybridization)

# Mix of Multilevel and Multiple Inheritance

class class1:
    pass
class class2(class1):
    pass
class class3(class1):
    pass

class HybridClass(class2, class3):
	pass