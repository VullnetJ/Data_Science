
# for loops, while loops, try statements, wwith statements, if statements.
# if statements, while loops , for loops rely on a controlling expression that must evaluate to False or True. 

# Equality opertions ==, !=, is, True, False, 
nr1, nr2, nr3 = 3, 3, 4
nr1 == nr2 # True
nr1 == nr3 # False

print(nr1 != nr2)# False
nr1 != nr3 

5 == 5.0 # True
'5' == 5 # False

nr1 > nr2 # False 
nr1 <= nr2 # True
nr1 < nr3 # True

# Boolean Operations: and, or, not, 
True and True # True
True and False # False
True or False # True
False or False # False
not False # True
not True # False

greeting = ""
second_greeting = "Good morning"
print(greeting or second_greeting) # 'Good morning'

if True: greeting="Yey it is True"
print(greeting) # Yey it is True

if True: 
    greeting ="Good morning"
    print(greeting) # 'Good morning'

# Since the controlling expression evaluates to False, the program will skip the controlled statement(s)
if False:
    greeting = "Nothing to show here"
    print(greeting)

# The Walrus Operator, None, Match

import re
dt = '2022-06-01'
matches = re.search(r'(\d\d\d\d)-(\d\d)-(\d\d)', dt)
if matches:
    print(f"It matched {matches.group(1)}") # It matched 2022
else: 
    print(f"Nothing is found")

# in python 3.8 can use := to assign a value to a variable and return the value. 
# Instead of using separate variable can use straight with if statement 
if there_is_a_match := re.search(r'(\d\d\d\d)-(\d\d)-(\d\d)', dt):
    print(f"Match found: {there_is_a_match.groups(1)}") # Match found: ('2022', '06', '01')

fav_fruit = 'pear'
list_of_fruits = {'orange', 'pear', 'grape', 'apple'}

if fav_fruit in list_of_fruits:
    print(f"My favorite fruit is {fav_fruit}") # My favorite fruit is pear
else: 
    print(f"Why there aren't any fruits for me")


bank_balance = 4000.58
my_account = None

if bank_balance > 0: 
   my_account = "You have money in your account"
else: 
    if bank_balance == 0:
        my_account = "Your account is empty"
    else:
        my_account = "You have taken too much money from the bank"
print(my_account) # You have money in your account

bank_balance = 5000.49
status = None

if bank_balance > 0:
    status = "You have money in your account"
elif bank_balance == 0:
    status = "Your account is empty"
else:
    status = "You have taken overdraft"

# while loop 
count = 0 
while count <= 10: 
    print(f"You counted till {count}")
    count+=1 

# for loop 
for index in range(10):
    count = index + 1
    print(count)

fruits = ["Apple", "Orange", "Pear"]
for fruit in fruits: 
    print(f"My favorite fruit is {fruit}")
    print("No, wait..., I changed my mind")

cities = ["Helsinki", "Oulu", "New York", "Tampere",  "Rome"]
capital_cities = ["Helsinki", "New York", "Paris", "Tirana", "Rome", ""]
index = 0

while True:
    capital_city = capital_cities[index]
    if capital_city not in cities:
        print(f"The capital city is {capital_city}")
        break
    print(f"I found a capital city and it is {capital_city}")
    index +=1
""" I found a capital city and it is Helsinki
I found a capital city and it is New York
The capital city is Paris """

# continue statement, skipping a single iteration of a loop. 

names = ['ela', 'elga', 'helga', 'elisa', 'ola', 'helena']

for name in names:
    if not name.startswith('e'):
        continue
    print(f"Finding the name that starts with 'e' {name}")


