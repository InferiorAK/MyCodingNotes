# Author: InferiorAK
# *args and **kwargs Argument in python

# simple func
def func(a, b, c):
    print(a, type(a))
    print(b, type(b))
    print(c, type(c))

func("I am a boy", 69, "Hi")
print("\n")


# *args
def func_1(*args):
    print(args, type(args))
    for item in args:
        print(item, type(item))


func_1("I am a boy", 69, "Hi", {1, 6, 12}, ["leave", "me", "alone"])
print("\n")


# **kargs
def func_2(**kwargs):
    print(kwargs, type(kwargs))
    for key in kwargs.keys():
        print(key, type(key))
    for val in kwargs.values():
        print(val, type(val))
    for key, val in kwargs.items():
        print(key, val)


func_2(don=0, me="AK", tomato=500)
print("\n")


# *args and **kwargs together
def args_kwargs(*args, **kwargs):
    print(args)
    print(kwargs)

args_kwargs("I am a boy", 69, "Hi", don=0, me="AK", tomato=500)
print("\n")
