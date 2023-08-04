# Author : InferiorAK
# Inheritance in python

# It's like father, his child, his grandchild .... All the characteristics will be presented in the relationship like tree.

class info():
	def __init__(self, n, a, c):
		self.name = n
		self.age = a
		self.clss = c
	def x(self):
		print(f"I am {self.name}")

class more(info): # using info class into more class. all will be added to more that contained in info
	def y(self):
		print(f"I am taking {self.clss}")
  
class further(more):
    def z(self):
        print(f"I am {self.age} years old")

obj1 = info("InferiorAK", 20, "HigherEducation")
obj1.x()

obj2 = more("GB", 21, "HigherDegree")
obj2.x()
obj2.y()

obj3 = further("Guti", 25, "risk")
obj3.x()
obj3.y()
obj3.z()