# Author : InferiorAK
# Dunder Methods in Python

# Most used Dunder Methods:
    
#     Object Initialization and Representation:

#     __init__(self, ...): Initializes an object of a class.
#     __repr__(self): Returns a string representation that can be used to recreate the object.
#     __str__(self): Returns a string representation of an object.
    
#     Attribute Access:

#     __getattr__(self, name): Handles access to undefined attributes.
#     __setattr__(self, name, value): Handles attribute assignment.
#     __delattr__(self, name): Handles attribute deletion.
#     __getattribute__(self, name): Intercept attribute access for all attributes.
    
#     Comparison Operators:

#     __eq__(self, other): Handles equality comparison (==).
#     __ne__(self, other): Handles inequality comparison (!=).
#     __lt__(self, other): Handles less than comparison (<).
#     __gt__(self, other): Handles greater than comparison (>).
#     __le__(self, other): Handles less than or equal to comparison (<=).
#     __ge__(self, other): Handles greater than or equal to comparison (>=).
    
#     Numeric Operations:

#     __add__(self, other): Handles addition (+).
#     __sub__(self, other): Handles subtraction (-).
#     __mul__(self, other): Handles multiplication (*).
#     __truediv__(self, other): Handles true division (/).
#     __floordiv__(self, other): Handles floor division (//).
#     __mod__(self, other): Handles modulo division (%).
#     __pow__(self, other): Handles exponentiation (**).
    
#     Container Methods:

#     __len__(self): Returns the length of the object.
#     __getitem__(self, key): Enables indexing and slicing ([]).
#     __setitem__(self, key, value): Enables assignment to indexed/sliced objects.
#     __delitem__(self, key): Enables deletion of indexed/sliced objects.
#     __iter__(self): Returns an iterator object.
#     __next__(self): Retrieves the next item from an iterator.
#     __contains__(self, item): Checks if an item is present in the object.
    
#     Callable Objects:

#     __call__(self, ...): Allows an object to be called as a function.


class Dunder:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return f"This is my name: {self.name} <- repr"
    def __str__(self):
        return f"This is my name: {self.name} <- str"
    def __call__(self):
        print(f"This is my name: {self.name} <- call")