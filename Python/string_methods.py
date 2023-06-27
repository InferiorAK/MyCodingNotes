# Author : InferiorAK
# All String Methods (47) is Python


# #  Method    -    Description
# # <------>       <----------->

# [Note: for same working functions, but starts with r. that means it will work from right to left. and the main ones will work normally as usual left to right. ex: find and rfind, split and rsplit etc...]

# capitalize()    Converts the first character to upper case
# casefold()      Converts the string into lower case
# lower()         Converts a string into lower case
# upper()         Converts a string into upper case
# count()         It will check the given string that how many times it is in the main string
# encode()        Returns an encoded version of the string. ex: bytecode
# expandtabs()    Sets the tab size of the string
# format()        Formats specified values in a string
# format_map()    Formats specified values in a string

# isalnum()       Returns True if all characters in the string are alphanumeric
# isalpha()       Returns True if all characters in the string are in the alphabet
# isascii()       Returns True if all characters in the string are ascii characters
# isdecimal()     Returns True if all characters in the string are decimals
# isdigit()       Returns True if all characters in the string are digits
# isidentifier()  Returns True if the string is an identifier
# islower()       Returns True if all characters in the string are lower case
# isnumeric()     Returns True if all characters in the string are numeric
# isprintable()   Returns True if all characters in the string are printable
# isspace()       Returns True if all characters in the string are whitespaces
# istitle()       Returns True if the string follows the rules of a title
# isupper()       Returns True if all characters in the string are upper case

# startswith()    Returns true if the string starts with the specified value
# endswith()      Returns true if the string ends with the specified value

# center()        Returns a centered string
# ljust()         Returns a left justified version of the string
# rjust()         Returns a right justified version of the string
# zfill()         Fills the string with a specified number of 0 values at the beginning

# swapcase()      Swaps cases, lower case becomes upper case and vice versa
# title()         Converts the first character of each word to upper case
# translate()     Returns a translated string
# maketrans()     Returns a translation table to be used in translations

# join()          Converts the elements of an iterable into a string
# replace()       Returns a string where a specified value is replaced with a specified value
# find()          Searches the string for a specified value and returns the position of where it was found
# rfind()         Searches the string for a specified value and returns the last position of where it was found
# index()         Searches the string for a specified value and returns the position of where it was found
# rindex()        Searches the string for a specified value and returns the last position of where it was found
# partition()     Returns a tuple where the string is parted into three parts
# rpartition()    Returns a tuple where the string is parted into three parts

# split()         Splits the string at the specified separator, and returns a list
# rsplit()        Splits the string at the specified separator, and returns a list
# splitlines()    Splits the string at line breaks and returns a list
# strip()         Returns a trimmed version of the string
# lstrip()        Returns a left trim version of the string
# rstrip()        Returns a right trim version of the string
# removeprefic()  Remove the given string from begining part of a string
# removesuffix()  Remove the given string from ending part of a string


# #  Examples
# # <-------->

txt = "This is an Example man!"
txt2 = "This\tis\tExample2 man!"
txt3 = "Demo, {x} go {y}"
txt4 = "tHis iS foR swapCase"
txt5 = "hey replace, I am replace(). replace me man"
txt6 = """I am the demo,
you are the example,
goodbye lollypop,
be healty wealthy and wise
"""

print(1, txt.capitalize())
print(2, txt.casefold())
print(3, txt.lower())
print(4, txt.upper())
print(5, txt.count("i"))
print(6, txt.encode("utf-8")) # txt.encode(encoding="utf-8", errors="strict")
print(7, txt2.expandtabs(10))
print(8, txt3.format(x="don't", y="there"))
dct = {"x":"don't", "y":"there"}; print(10, txt3.format_map(dct))
print(9, position2:=txt.index("ample"), txt[position2:])

print(10, txt.isalnum())
print(11, txt.isalpha())
print(12, txt.isascii())
print(13, txt.isdecimal())
print(14, txt.isdigit())
print(15, txt.isidentifier())
print(16, txt.islower())
print(17, txt.isnumeric())
print(18, txt.isprintable())
print(19, txt.isspace())
print(20, txt.istitle())
print(21, txt.isupper())

print(22, txt.startswith("T"))
print(23, txt.endswith("e"))

print(24, txt.center(30, "-")) # This means it will take 30 Characters. For extras it will replace the blank places with the given symbol
print(25, txt.ljust(50, "*")) # * will cover the blank CharacterSpaces from left to right if the string length is less than given char length. such as - 50, for this one
print(26, txt.rjust(30, "*")) # " " " from right to left " " " "
print(27, txt.zfill(30))

print(28, txt4.swapcase())
print(29, txt.title())
print(30, txt.translate({97:115, 84:72})) # txt.translate(dictionary); dict = {targeted char ascii: replacement char ascii, ...}
dict_t = str.maketrans({"a":"b", "T":"H"}); # it will convert asciis to decimal and make dict format
print(31, txt.translate(dict_t)) # then it will translate

print(32, "|".join(txt))
print(33, txt.replace("ample", "apple")); print(txt5.replace("replace", "repl", 2)) # (txt, replace with, occurences)
print(34, position:=txt.find("a"), txt[position:]) # serach from begining to end
print(35, position:=txt.rfind("a"), txt[position:]) # search from end to begining
try:
    print(36, txt.index("A")) # same as find. the difference is that it will raise an error if the given string isn't found
except Exception as e:
    print("Raised Error:", e)
try:
    print(37, txt.rindex("a")) # same as rfind. the difference is that it will raise an error if the given string isn't found
except Exception as e:
    print("Raised Error:", e)
print(38, txt.partition("h")) # it will return a tuple of 3 partitions. the given string will be at the middle.
print(39, txt.rpartition("h")) # it will return a tuple of 3 partitions. the given string will be at the middle.
# difference between partition() and rpartition:
#     partition -> it will make parts from left to right
#     rpartition -> it will make part from right to left
#     clear ex:
#         print("I am InferiorAK".partition("demo"))
#         print("I am InferiorAK2".rpartition("demo"))
#     demo is not in the string. so it will print blank part and you will se the difference then

print(40, txt.split("a")); print(txt.split("a", 1)) # (given sting, occurances count) # works left to right
print(41, txt.rsplit("a")) # works right to left
print(42, txt6.splitlines()) # it will split newlines
print(43, txt6.rstrip()) # whole
print(44, txt6.lstrip()) # begining to end
print(45, txt6.rstrip()) # end to begining
print(46, txt.removeprefix("This"))
print(47, txt.removesuffix("n!"))