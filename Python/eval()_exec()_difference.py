# Author: InferiorAK
# eval() and exec() function difference in python

print("5+5")	# It will just print 5+5 as a string
eval("5+5")	# It will execute the given Value. So it will print the Calculation
exec("5+5")	# It can't execute value so that It will return None.

print("print('hello')")
eval("print('hello')")
exec("print('hello')")

print("import os; os.system('clear')")
exec("import os; os.system('clear')")	# It will execute the code
eval("import os; os.system('clear')")	# It can't execute codes. So there will be an error!

# eval -> 'e' 'val'  -> e for execute, v for value -> It executes Value
# exec -> 'e' xe 'c' -> e for execute, c for code  -> It executes codes
