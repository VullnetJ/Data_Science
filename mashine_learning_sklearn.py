
# There are two types of Machine Learning: supervised and unsupervised learning.
"""
The steps to training a Supervised model include:
Transform and separate out test data, 
train the model and test it. 
"""
import numpy as np
from sklearn.preprocessing import MinMaxScaler

# a range of data -33 to 80
dt = np.array([[80, 22, 6], [70,  8,  5],[30, -33, 23], [56,  66, 3]])

# creating a transform object
min_max = MinMaxScaler()

# fitting the transformer to the data. 
scaling = min_max.fit(dt)

# scaling the range between 0 and 1
scaling_01 = scaling.transform(dt)
print(scaling_01)
"""
[[1.         0.55555556 0.15      ]
 [0.8        0.41414141 0.1       ]
 [0.         0.         1.        ]
 [0.52       1.         0.        ]]
"""

# Split Test and Training Data
from sklearn import datasets
source, target = datasets.load_iris(return_X_y=True)

print(type(source))
# <class 'numpy.ndarray'>
print(source.shape)
# (150, 4)

# Split a data set
from sklearn.model_selection import train_test_split
train_a, test_a, train_b, test_b = train_test_split(source, target)
print(train_a.shape) # (112, 4)
print(train_b.shape) # (112,)
print(test_a.shape) # (38, 4)
print(test_b.shape) # (38,)

# Scikit-learn has many classes that represent different machine learning alrgorithms. 
"""Thes classes are estimators. that can be turned using parameters while instantiating. 
Each estimator has a .fit method, for training the model. 
The next are the targets or results, for the samples. When training is done the predicion is used with the .predict() method. 
"""
from sklearn.neighbors import KNeighborsClassifier # estimator
from sklearn import metrics # For testing the accuracy. 
neighbor = KNeighborsClassifier(n_neighbors=3) # three neighbour estimator
neighbor.fit(train_a, train_b) # to train the model using the training data
prediction = neighbor.predict(test_a)  # making predition from source data. 

print(metrics.accuracy_score(test_b, prediction)) # 0.9736842105263158, Arruracy against test data. 
