# Author : InferiorAK
# Intance Variable and Class Variable

class Student:
	institution = "KPC" # Class Variable
	def __init__(self, name):
		self.name = name
	def StudentInfo(self):
		print(f"I am {self.name} from {self.institution} {self.year}")

Student.year = "2023" # Instance Variable

std1 = Student("InferiorAK")
std1.StudentInfo()
# Student.StudentInfo(std1)
std1.institution = "BUET" # instance variable. only changing institution for InferiorAK (std1)
std1.StudentInfo()

std2 = Student("GB")
std2.StudentInfo()
std2.institution = "DU"
std2.StudentInfo()

print(Student.institution)
Student.institution = "MIT" # changing institution for all
print(Student.institution)
std3 = Student("AK")
std3.StudentInfo()
std4 = Student("Mi")
std4.StudentInfo()
