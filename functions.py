#Functions. 

def order(nr1, nr2, nr3):
    '''
    Printing numbers in order. 
    '''
    print(f"The first number is: {nr1}")
    print(f"The second number is: {nr2}")
    print(f"The third number is: {nr3}")

order(1,2,3)

# another way how to assign values to the function: 
order(nr1=5, nr2=6, nr3=7)

# appending 2 to the list. 
def lists(my_list=[]):
    my_list.append(2)
    print(my_list)
lists() # [2]
lists() # [2, 2]
lists() # [2, 2, 2] , it is called third time 

# using wildcard , args 
def wildcard(*args):
    for i in args:
        print(i)
wildcard("It's snowing", 5, ['What is this'])

def wildcard2(**kwargs):
    for key, value in kwargs.items():
        print(f" The key is: {key}, and the value is: {value}")

wildcard2(name="Helga", age=24) # The key is: name, and the value is: Helga
                                # The key is: age, and the value is: 24

# using both * and ** (args and kwargs)
def both_wildcards(*args, **kwargs):
    print(f"Position is {args}")
    print(f"Keywords is {kwargs}")

both_wildcards(4, 5, 6, greeting="Hello there", x = 8, y= 9)
# Position is (4, 5, 6)
# Keywords is {'greeting': 'Hello there', 'x': 8, 'y': 9}

# Using return statement
def use_return(add_something):
    return add_something + 5
print(use_return(2)) # 7

def no_return():
    pass
no_return() == None # True

# Scope in function. 
outer_scope = 'This is a global scope'

def scope():
    inner_scope = "This is inner scope"
    print(outer_scope)
    print(inner_scope)
scope()

# Nested fuctions 
def nested():
    print(outer_scope)
    def nested_function():
        print("This is a function inside another function")
    return nested_function

my_function = nested()

my_function() # This is a function inside another function

# lambda function
lambda x: x+1
def a_list(data, my_function):
    for i in data:
        print(f'{my_function(i)}')
a_list([3,4,5], lambda x: x+3) 
# 6
# 7
# 8
