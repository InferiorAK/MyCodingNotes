# Author : InferiorAK
# super() keyword in class in Python

class ParentClass:
    # def ParentMethod(self, name, addr):
    #     self.name = name
    #     self.addr = addr
    #     print("This is ParentClass's Parent Method")
    def ParentMethod(self):
        print("This is ParentClass's Parent Method")

class ChildClass(ParentClass):
    # def ParentMethod(self, name, addr):
    #     self.name = name
    #     self.addr = addr
    #     print("This is ChildClass's Parent Method")
    def ParentMethod(self):
        print("This is ChildClass's Parent Method")

    # def ChildMethod(self, name, addr, id):
        # super().ParentMethod(name, addr)
        # self.id = id
    def ChildMethod(self):
        print("This is Child Method")
        super().ParentMethod() # At first it will search ParentMethod in ChildClass. If the method isn't here, then It will go to ParentClass for ParentMethod.

obj1 = ParentClass()
obj2 = ChildClass()
# obj2.ChildMethod("InferiorAK", "Unknown, Unknown", "17")
# print(obj2.id)
obj2.ParentMethod()
obj2.ChildMethod()

# ------------------------------

class Parent:
    def __init__(self, name, id):
        self.name = name
        self.id = id
class Child(Parent):
    def __init__(self, name, id, occupation):
        super().__init__(name, id)
        self.occ = occupation
        print(f"Hey! I am {self.name}. My id is {self.id} in {self.occ}")
        
Child("GB", "8617", "GutiCmp")
