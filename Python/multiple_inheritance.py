# Author : InferiorAK
# Multiple Inheritance in python

class info:
	def __init__(self, name):
		self.name = name
		print(f"Hey I am {self.name}.")
	def priority_test():
		print(f"'info' class is boss")

class more:
	def __init__(self, age):
		self.age = age
		print(f"I am {str(self.age)} years old.")
		def priority_test():
			print(f"'more' class is boss")

class further(info, more):  # using multiple classes in one. the first one will get first priority
	def __init__(self, name, age, love):
		self.name = name
		self.age = age
		self.love = love
		print(f"Hey I am {self.name}. I am {str(self.age)} years old. I loved {str(self.age)} girls")

info("Guti")
further("Guti", 25, 5)
further.priority_test()
