# Author : InferiorAK
# Decorators in Python

def MyFunc(func):		# In decorators, It takes another function as an argument
	def loop():
		for _ in range(1, 10, 2):
			print(_, end=" ")
			func()
	return loop

#   method-1
# <---------->

@MyFunc		# Now it will decorate or influence another function 
def function():
	print("This is a decorator")

function()

# #   method-2
# # <---------->

# def function():
# 	print("This is a decorator")
# MyFunc(function)()


#   More Practical
# <---------------->

from time import sleep
from time import perf_counter as p
def elaspse(func):
	def time_taken():
		start = p()
		func()
		end = p()
		print(f"Time Taken: {end - start} sec")
	return time_taken

@elaspse
def test_func():
	for k in range(1, 5):
		print(k)
		sleep(1)

test_func()
