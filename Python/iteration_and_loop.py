# Author: InferiorAK
# Python Iteration

list = [1, 2, 3, 4, 5]

# loop
for item in list:
	print(item)     # Here, all the values will be printed after one another

print("\n")

# iteration
iterate = iter(list)    # Here, the values will be printed one by one
print(next(iterate))
print(next(iterate))
print(next(iterate))
print(next(iterate))
print(next(iterate))

print("\n")

# with class
class numbers:
	def __iter__(self):
		self.i = 1
		return self

	def __next__(self):
		x = self.i
		self.i += 1
		return x


myclass = numbers()
iterate2 = iter(myclass)

print(next(iterate2))
print(next(iterate2))
print(next(iterate2))
print(next(iterate2))
print(next(iterate2))
print(next(iterate2))
print(next(iterate2))

print("\n")

# or,
for g in myclass:
	if g <= 10:
		print(g)
	else:
		raise StopIteration
