# Author: InferiorAK
# Walrus Operator :=
# new from python 3.8


# Ex-1
ak = "demo tutorial"
print(ak)   # It's as usual we do
# It's printed directly. Thus the code has become more shorter
print(ak2 := "demo tutorial as well")

# Ex-2
lst = ["burger", "cheese", "garlic", "onion", "capsicum"]
for ingredient in lst:
	print(ingredient)

for instrument in (lst2 := ["pen", "notebook", "wood", "tree", "bat"]):
	print(instrument)
