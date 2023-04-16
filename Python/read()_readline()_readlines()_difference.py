# Author: InferiorAK
# Difference between read, readline, readlines

def rd():       # This will just print the data from the file normally
    file = open("dummy.txt", "r")
    data = file.read()
    print(data)

def rdline():   # This will print the data from the file line by line
    file = open("dummy.txt", "r")
    line1 = file.readline()
    print(line1)
    line2 = file.readline()
    print(line2)
    line3 = file.readline()
    print(line3)

def rdlines():      # This will create a list of lines with the newline character '\n' (if there any new line) from the file
    file = open("dummy.txt", "r")
    lst_line = file.readlines()
    print(lst_line)


rd()
rdline()
rdlines()
