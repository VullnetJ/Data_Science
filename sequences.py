
# Build-in types known as sequences. 
# checking if an item is a member of a sequence, 
'apple' in ['apple', 'orange', 'kiwi'] # True

'g' in 'orange' # True
'm' in 'orange' # False 

'c' not in 'apple' # True

# Indexing, counting start from 0. 
name = 'John'
name[0] # 'J'
name[2] # 'h'
name[-1] # 'n'
name[-2] # 'h'

# Slicing
name = 'John Doe'
name[2:4] # 'hn'
# the subsequence starting at the beginning of the parent sequence. 
name[:4] # 'John'

# by the end of the sequence. 
name[3:] # 'Doe'

# creating slice counting from the end of a sequence. 
name[-3:] # 'Doe'

scores = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
scores[2: 6] # [2, 3, 4, 5]

# with three steps 
scores[3: 10: 3] # [3, 6, 9]

# counting backward, using a negative step: 
scores[10:0: -4] # [10, 6, 2]

name = 'John'
# to find the length of the variable 
len(name) # 4

# to find max and min of scores: 
min(scores) # 0
max(scores) # 10

max(name) # 'o'

# mixed item types will result in error. 
max(['Apple', 4, 'e'])

# counting how many times an item appears in a sequence. 
name.count('J') # 1
name.index('J') # 0 
name[:name.index('n')] # 'Joh'
 
"post" + "_" + "code" # "post_code"

[0,3]* 3 # [0, 3, 0, 3, 0, 3]

nr_people = 5
points = [0] * nr_people # [0, 0, 0, 0, 0]

# List nad Tuples

a_list = [0, 1, 2, 3, 4, 5, 6]

a_tup = (1, 2)

a_tup(1, ) # (1, )

name = "John"
letters = list(name) # letters ['J','o','h','n']

#Adding and removing people from the List. append, insert

fruits = ['Apples', 'Grapes', 'Bananas']
fruits.append('Oranges')
fruits.insert(0, 'Kiwi')

# To remove an item from a list, pop method. 
fruits.pop() # last item
fruits.pop(0) # removes first item from the list. 

# Extending the list. 
berries = ['Blueberries', 'Strawberries']
fruits.extend(berries) 

lists = [[]] * 3 # [[], [], []]
lists[-1].append(5) # [[5], [5], [5]]

lists = [[] for _ in range(3)]
list[-1].append(3) # [[], [], [5]]


# unpacking
a, b, c = (4, 5, 6)
a # 4 
b # 5
c # 6

# using • can assign multivalues to the varliable 

*first, second, third = ['I ', 'wrote', 'this','again', 'today' ]
first # ['I ', 'wrote', 'this']
second # 'again'
third # 'today'

# Sorting, Reversing 
name = 'John'
letters = list(name) # ['J', 'o','h', 'n']
letters.sort() # ['J', 'h', 'n', 'o']
letters.reverse() # ['o', 'n', 'h', 'J']

strings = "this is a string"
strings2 = "this is a string"
strings == strings2 # True

""" This is a long comment """
# special characters in python. 
# \t for tab, \r for carriage return , \n for newline. 

# r: for raw string: 
# mac_path = r"/path/
name = "John Doe"
name.capitalize() # "John doe"
name.lower() # 'john doe'
name.upper() # 'JOHN DOE'
name.swapcase() # "jOHN, dOE"
name = 'john doe'
name.title() # 'John Doe'