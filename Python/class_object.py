# Author : InferiorAK
# class and objects in python

class info(): # Class
    # name = "InferiorAK"
    # study = "Unknown"
    # addr = "Bangladesh"
    def __init__(self): # Initialize --> It's a method called Dunder. It's creating a Constructor
        self.name = "InferirAK"
        self.study = "Unknown"
        self.addr = "Bangladesh"
    def test(self):
        return f"Hey guys! I am {self.name}, from {self.addr}"
        
get = info() # Object

print(get.name, get.addr)
# print(get.occ)
print(get.test())

get.name = "GB" # changing the class name
get.addr = "US" # changing the class addr
get.occ = "student" # new adding to class
print(get.test())
print(get.occ)

# ----------------------------

class result():
    def __init__(self, subj, mark):
        self.subj = subj
        self.mark = mark
    def out(self):
        print(f"I got {self.mark} in my {self.subj} Exam")

get1 = result("physics", 49)
get2 = result("chemistry", 55)
get1.out()
get2.out()