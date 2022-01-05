# dictionaries, with a key/value pair. 

from typing import ItemsView


person = {'name:': 'John', 'age': 21}

dictionary = dict()
print(dictionary) # {}

dictionary = {}
print(dictionary)

person_1 = dict(name="Ola", height = 167)

person_3 = {'name':'Ola', 'height':170}

# accessing, adding and updating by using keys. 
print(person_3['name']) # Ola
person_3['height'] # 170

# adding new key/pair to an exising dictionary. 
person_3['birth_year'] = '2000'
print(person_3)

# updating the value for an exising key. 
person_3['height'] = 172

# Incrementing numeric data by using +=
person_3['height'] += 1
print(person_3)

# To remove items from Dictionaries. 
del(person_3['height'])

# Dicionary Views 
keys = person_3.keys()
print(keys) # dict_keys(['name', 'birth_year'])

# values 
val = person_3.values()
print(val)
items = person_3.items()
print(items) # dict_items([('name', 'Ola'), ('birth_year', '2000')])

print('birth_year' in keys) # True
print(('birth_year', 1) in items) # False

# Length
len(keys)
len(val)
len(items)

# Reversing keys
print(list(reversed(keys))) # ['birth_year', 'name']

# Tesing for equality of keys, symmetric difference, intersection, difference, 
diff = person_1.keys() == person_3.keys
print(diff) # False

symmetric_difference = person_1.keys() ^ person_3.keys()
print(symmetric_difference) # {'birth_year', 'height'}

intersection = person_1.keys() & person_3.keys() 
print(intersection) # {'name'}

difference = person_1.keys() - person_3.keys()
print(difference) # {'height'}

union =  person_1.keys() | person_3.keys()
print(union) # {'birth_year', 'name', 'height'}


# Itertion through a dictionary
for k, v in person_3.items():
    print(f"{k} => {v}")

if 'name' in person_3:
    print(person_3['name'])

# accessing the key with get() method
print(person_3.get('name'))

# Hash method: __hash__()
this_is_a_hash = "Have a great day."
print(f"This is hashed code of {this_is_a_hash.__hash__()} ")  # This is hashed code of 2845379526240474675 

number = 8
print(number.__hash__())

# hashing a list will throw an error. 

# Sets. 
a_set  = {1, 3, 'v', 'j', 5.1}

an_empty_set = set()

# Finding unique letters 

letters = 'b', 'b', 'b', 'd', 'e'
unique= set(letters)
print(unique) #{'e', 'd', 'b'}

unique_characters = set('europe')
print(unique_characters) # {'e', 'p', 'o', 'u', 'r'}

unique_numbers = {1, 2, 3, 4, 5, 6, 6, 6, 6, 7, }
print(unique_numbers) # {1, 2, 3, 4, 5, 6, 7}

# adding numbers to a set using the add() method
unique_numbers.add(8)
# checking if there is a number in the set. 

5 in unique_numbers # True 

unique_numbers.pop()
print(unique_numbers) # Removes number 1 

people = {'John', 'Ola', 'Helga'}

# removing a particular item from the set
people.remove('John')
print(people)

# if the item does not exist it will throw an error. 
# The discard() method doesn't throw an error when attepmt to remove a missing item. 
# person.discard("Elsa") # It will throw an error. 

# removing all of the content from the set. 
person.clear()

# Sets do not support indexing and it will throw an error if using indexing 

# With disjoint()method can test a set of nummbers against another one. 

even_numbers = set(range(0, 8, 2))
odd_numbers = set(range(1,9,2))

print(even_numbers.isdisjoint(odd_numbers)) # True

# updating sets. 
some_numbers = {1, 2, 3, 4 }
some_numbers.update({5, 6, 7, 8})

# Frozensets are set-like objects that are immutable

freeze = frozenset(range(10))
print(f"frozen set: {freeze}")  # frozen set: frozenset({0, 1, 2, 3, 4, 5, 6, 7, 8, 9})