
# Natural language processing is a subset of data science to clisify text. 
#  
import nltk, nltk.data
# loading text from the current folder
text = nltk.data.load('data_science/text.txt', format= 'text')
print(text)

# Frequency distribution. 
distrib = nltk.FreqDist(text)
print(distrib) # <FreqDist with 39 samples and 659 outcomes>

print(distrib.most_common(15))
"""
[(' ', 133), 
('e', 69), 
('t', 36), 
('s', 36), 
('h', 33), 
('a', 30), 
('n', 28), 
('o', 28), 
('l', 27), 
('i', 26)]
"""

import string 
string.punctuation
words = []
for word in text:
    if word not in string.punctuation:
        words.append(word) # adding non punctuation 
print(len(text) - len(words))  # number punctuation 22

# # Text classification

# different_words = ['albanian', 'sea', 'mountain', 'country', 'city',
#               'word', 'check', 'government', 'international', 'snow',
#               'rain', 'weather', 'finalnd', 'hydropower', 'minister',
#               'public libray', 'count', 'flower', 'peace', 'flow',
#               'go', 'cat', 'huge', 'everyday', 'face', 'elevator',
#               'helsinki', 'today', 'brown', 'yesterday', 'funny', 'sleepy', 'vibe',
#               'appliance', 'new', 'achieve', 'day', 'light', 'storm',
#               'phantom', 'obvious', 'think', 'again', 'once', 'strong']

