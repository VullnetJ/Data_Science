import pandas as pd

names = ['John', 'Ela', 'Helga', 'Will']
surnames = ['Doe', 'Smith', 'Mc', 'Helius']
ages = [24, 30, 39, 20]
df = {'first_name': names, 
    'last_name': surnames,
    'ages': ages}
students = pd.DataFrame(df, index=list('abcd'))

# loc uses index lables, iloc uses index position. 
print(students.loc['a'])

"""
first_name    John
last_name      Doe
ages            24
Name: a, dtype: object
"""
# slicing labels:
print(students.loc['b': 'c'])
"""
  first_name last_name  ages
b        Ela     Smith    30
c      Helga        Mc    39
"""
# returning the folumn first_name
print(students.loc[:, 'first_name'])
"""
a     John
b      Ela
c    Helga
d     Will
Name: first_name, dtype: object
"""

# A list of columns till index c
print(students.loc[:'c', ['first_name', 'last_name']])
"""
  first_name last_name
a       John       Doe
b        Ela     Smith
c      Helga        Mc
"""

# using list of Booleans
print(students.loc[:'b', [True, False, True]])
"""
  first_name  ages
a       John    24
b        Ela    30
"""

# Using index position to select rows and columns 
print(students.iloc[2])
"""
first_name    Helga
last_name        Mc
ages             39
Name: c, dtype: object
"""
print(students.iloc[0:2])
"""
  first_name last_name  ages
a       John       Doe    24
b        Ela     Smith    30
"""
# using second slicer
print(students.iloc[0:3, :2])
"""
  first_name last_name
a       John       Doe
b        Ela     Smith
c      Helga        Mc
"""
# Renaming
print(students.rename(columns={'ages': 'Student_age'}))

# adding another column 
students['City'] = ['Helsinki', 'Berlin', 'Stockholm', 'New York']

# Persons full name 
students['Full Name'] = (students.loc[:, 'first_name'] +" " + students.loc[:, 'last_name'])
print(students.loc[:, 'Full Name'])
"""
a       John Doe
b      Ela Smith
c       Helga Mc
d    Will Helius
Name: Full Name, dtype: object
"""
# to change values of a column can use operators such as +=, -=, /=, *=, 
# For example: students.Student_age +=1, it will add 1 to the students' age. 

# using Regular Expression. 
new_students_list = students.replace(r'(E)([a-z])', r'e\2', regex=True)
print(new_students_list)
"""
  first_name last_name  ages       City    Full Name
a       John       Doe    24   Helsinki     John Doe
b        ela     Smith    30     Berlin    ela Smith
c      Helga        Mc    39  Stockholm     Helga Mc
d       Will    Helius    20   New York  Will Helius
"""

# Capitalize, lower using apply as an argument. 
# There is first_name 'ela' in lower case. 

def changed_list(something):
    return something.capitalize()

print(new_students_list.loc[:, 'first_name'].apply(changed_list))
"""
a     John
b      Ela
c    Helga
d     Will
Name: first_name, dtype: object
"""
# using lower case to change first_name 
def lower(smth):
    return smth.lower()

print(new_students_list.loc[:, 'first_name'].apply(lower))
"""
a     john
b      ela
c    helga
d     will
Name: first_name, dtype: object
"""

# taking a row as an argument
def greeting(row):
    return f' So nice to meet you {row["first_name"]} and you are {row["ages"]} years old'

print(students.apply(greeting, axis=1))

"""
a     So nice to meet you John and you are 24 years...
b     So nice to meet you Ela and you are 30 years old
c     So nice to meet you Helga and you are 39 year...
d     So nice to meet you Will and you are 20 years...
dtype: object
"""