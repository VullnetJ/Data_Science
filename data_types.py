
# The python parser takes the code as input and translates it into instructions. 
# The most basic build0nts types are Numeric: Booleans, integers, floating point nummbers and imaginary numbers
# Sequences: Strings and Binary Strings

# For example: 

# Integer
number = 10
print(type(number))

#Float
number = 10.23
print(type(number))

something = True
#Prints bool 
print(type(something))

#String, str
greeting = "Hello there"
print(type(greeting))


#NoneType  has None value. 
type(None)
a, b, c = 3, 4, 5

# evaluating conditions and assign a variable based on the evaluation 

evaluate = a**2 if (a < b) and (b or c ) else a // 2 

# using f to insert values in print

a = 12//2
b = a**2
print(f' a is {a}, b is {b}')

# finding current folder. 

import os 
os.getcwd()


# Assert Statements, it takes an expression as an argument and ensures that the result evaluates to True. 

# if assert is false it will throw an error. 

assert(True)

# assert do have an impact on performance, to disable them in production environment  can run the comand line 

#python -o data_types.py

# Assigning values to variables
a = "It's snowing"
b = 2

checking = b - 4 
print(f'{a} and it is {checking} degree celcius outside')

a, b, c = 2, 'v', 4.4

# Pass Statements are placeholder and they do not perform any action themselves, it just consist of the keyword pass. 

# Delete Statements consist of the del keword. 
fruit = "Apple"
del(fruit)
# it will throw an error because it is deleted already, and show that it is not defined. 
print(fruit)

# Yield Statements are used in writing generator functions, and helpt to omptimize for performance amnd memory usage. 

# Raise Statements. It consist of the raise keword followed by the exception. 
# For example: 
# raise NotImplementedError

# Break Statements, It will break a loop before its condition is met. 
# Continue Statements, It skips a single iteration of a loop. 

# import Statements. For reausing pieces of code in different contexts.
# import os, this module interacts with the operating system. 

# import os 
# # to list the current directory: 
# os.listdir()

# to install different packages we can use pip, 
# pip install pandas 
# import pandas as pd, and can use pd as alias for pandas. 

# to read files with pandas: 
#pd.read_excel("/excel_file.xls")

# importing a module by using from keyword with import
# import os from path 
# path

# All math operations can be performed in Python. 

a = 2 + 3 
b = 4 - 3 
c = 4 * 3 
d = 8/ 3
e = 4**2
f = 7//2
g = 7%2
18 % 8 is 0 # it will return True

# accessing the numerator. 
nr = 5 
nr.numerator 
# accessing object methods, in similar way as above. 
nr.to_bytes(8, 'little')

