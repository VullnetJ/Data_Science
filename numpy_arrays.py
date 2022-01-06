
# pip3 install numpy, to install numpy
# Numpy array is a data structure, that handles efficienlty large data sets. 
import numpy as np

# Creating Arrays. 
# An array from list
print(np.array([5, 6, 7, 8, 9, 10])) # [ 5  6  7  8  9 10]

# An array of zeros
print(np.zeros(5)) #[0. 0. 0. 0. 0.]

# arrays of ones
print(np.ones(5)) # [1. 1. 1. 1. 1.]

# arbitrary data
print(np.empty(5)) # [1. 1. 1. 1. 1.]

# range
print(np.arange(5)) # [0 1 2 3 4]

# range of numbers 
print(np.arange(1,10, 4)) # [1 5 9]

# array over an interval, spaced numbers over an interval. The first two are the interval, and the third is the number of items. 
print(np.linspace(0, 31, 5)) #[ 0.    7.75 15.5  23.25 31.  ]

first_array = np.arange(11)
print(first_array) # [ 0  1  2  3  4  5  6  7  8  9 10]

# data type
print(first_array.dtype) # int64

# number of elements 
print(first_array.size) # 11

print(first_array.shape) # (11,)
first_array.ndim # 1 

matrix = [[5, 6, 7], [8, 9, 10]]
array_mat = np.array(matrix)
# [[ 5  6  7]
# [ 8  9 10]]

print(array_mat.shape) # (2, 3)

print(array_mat.ndim) # 2, it has two dimentions

# Changing the shape fo the matrix

# one dimentional array
one_dimention = np.arange(8)
print(one_dimention) # [0 1 2 3 4 5 6 7]

# two dimentional array,
two = one_dimention.reshape(2,4)
print(two) 
# [[0 1 2 3]
# [4 5 6 7]]
three = two.reshape(2,2,2)
print(three)

#[[[0 1]
#  [2 3]]

# [[4 5]
#  [6 7]]]

np.ones(20).reshape(2, 5,2)

# Slicing and indexing data in arrays. 

one_dimentional = np.arange(16)
print(one_dimentional[3]) # 3

print(one_dimentional[-1]) # 15
print(one_dimentional[5:11]) # [ 5  6  7  8  9 10]

two_dim = np.arange(16).reshape(4, 4)
print(two_dim)
""" [[ 0  1  2  3]
    [ 4  5  6  7]
    [ 8  9 10 11]
    [12 13 14 15]]
"""
print(two_dim[3]) #[12 13 14 15], accesses row 3
print(two_dim[3,3]) # 15 row 3, column 3
print(two_dim[0:1]) # [[0 1 2 3]],  row 0, 
print(two_dim[:, 2]) # [ 2  6 10 14], colun 2
print(two_dim[0:1, -2:]) # [[[2 3]], 

two_dim[0,1] = 55
print(two_dim) # replaced 1 by 55, [ 0 55  2  3]

list_one = list(range(15))          # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
list_two = list(range(15, 0, -1))   #[15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print(list_one)
print(list_two)

# zip combines the two lists inot a list of tuples, that contain elements from each of the original lists. 
list_three = []
for index, j in zip(list_one, list_two):
    list_three.append(index*j)
print(list_three) # [0, 14, 26, 36, 44, 50, 54, 56, 56, 54, 50, 44, 36, 26, 14]

# add two arrays, 
print(np.array(list_one) + np.array(list_two))  # [15 15 15 15 15 15 15 15 15 15 15 15 15 15 15]

# multiply two arrays
print(np.array(list_one) * np.array(list_two)) # [ 0 14 26 36 44 50 54 56 56 54 50 44 36 26 14]

# divide two arrays 
print(np.array(list_one) / np.array(list_two)) 

""" [ 0.          0.07142857  0.15384615  0.25        0.36363636  0.5
  0.66666667  0.875       1.14285714  1.5         2.          2.75
  4.          6.5        14. 
"""

# Array Methods:
# finding the max value
my_arr = np.array(list_two)
print(my_arr.max()) # 15

# finding min value
print(my_arr.min()) # 1

# finding sum of all values
print(my_arr.sum()) # 120

# mean
print(my_arr.mean()) # 8.0

# standard deviation
print(my_arr.std()) # 4.320493798938574

# sum of each column
print(my_arr.sum(axis=0)) # 120

# sum of each row (axis = 1) if it is a matrix. 

print(np.array(two_dim.sum(axis=0))) # [24 82 32 36]

 
