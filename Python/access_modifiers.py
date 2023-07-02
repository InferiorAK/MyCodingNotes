# Author : InferiorAK
# public, protected and private access modifiers in python

# Access modifiers in object-oriented programming languages like Python determine the accessibility of class members (variables and methods) from other parts of the program. Python does not have strict access modifiers like some other languages (e.g., Java), but it uses naming conventions to indicate the intended accessibility of members. The three commonly used access modifiers in Python are:

# Public: Public members can be accessed from anywhere within the program. By convention, public members are not prefixed or suffixed with any special characters. They are accessible using the member name directly.

# Protected: Protected members should not be accessed from outside the class, but they can be accessed from derived classes. Conventionally, protected members are prefixed with a single underscore (e.g., _protected_member). However, it is more of a naming convention, and there are no strict restrictions on accessing protected members in Python.

# Private: Private members should not be accessed from outside the class. Conventionally, private members are prefixed with a double underscore (e.g., __private_member). Python uses name mangling to make private members harder to access from outside the class. However, it is still possible to access private members using the name mangling convention (_ClassName__private_member).

# It's important to note that access modifiers in Python are mainly conventions, and they do not provide strict enforcement of access control. Python developers are encouraged to follow these conventions to indicate the intended visibility of class members, but it is still possible to access protected and private members if needed.

# public    -> variable = "data"
# protected -> _variable = "data"
# private   -> __variable = "data" -> Can't be normally accessible from outside

class info: # Class
    # default
    # name = None
    # _name = None
    __name = None
    study = None
    addr = None
    def __init__(self, name, study, addr):
        # initialize value
        self.__name = name
        self.study = study
        self.addr = addr
    def __grab(self):
        # print(f"Hey guys! I am {self.name}, from {self.addr}")
        # print(f"Hey guys! I am {self._name}, from {self.addr}")
        print(f"Hey guys! I am {self.__name}, from {self.addr}")
    def accessPrivate(self):
        self.__grab()
        
        
get = info("InferiroAK", "Unknown", "Unknown")
# print(get.name) # Accessing public modifier
# print(get._name) # Accessing protected modifier
print(get._info__name) # Accessing private modifier

get._info__grab()
get.accessPrivate()

# -----------------------------

class info2:
    def __init__(self):
        self.mark = 99
        self.id = 8617
    def __private(self):
        print(f"I got {self.mark} and my ID is {self.id}")

class gather:
    def __init__(self):
        info2()._info2__private() # Accessing private method from info2 class
        
gather
# print(gather().__dir__())
# print(dir(gather))