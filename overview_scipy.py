# The SciPy (library) is a collection of packages for science, maths, and engineering. 
# pip3 install matplotlib, to install as package. 

import matplotlib.pyplot as plt

# The tree submodules are scipy.misk, scipy.special, scipy.stats 
# scipy.misc 
from scipy import misc
face = misc.face()
# plt.imshow(face)
# plt.show()

# ascent, a grayscale image.

gray_image = misc.ascent()
print(gray_image)

"""
[[ 83  83  83 ... 117 117 117]
 [ 82  82  83 ... 117 117 117]
 [ 80  81  83 ... 117 117 117]
 ...
 [178 178 178 ...  57  59  57]
 [178 178 178 ...  56  57  57]
 [178 178 178 ...  57  57  58]]
"""
# plt.imshow(gray_image)
# plt.show()

# scipy.special includes Airy, elliptical, Bessel, Struve functions and many more others. 
from scipy import special

print(special.factorial(5)) # 120.0

# nr of combinations. 
print(special.comb(8, 4)) # 70

# nr of permutations
print(special.perm(8, 2)) # 56.0

# spicy.stats, probability distributions and statistical functions. 
from scipy import stats 

# a binomial distribution of 30 trails and 50% chances
binomial = stats.binom(30, 0.5)

# Probability mass function -> probl that the sample is equal to 3
print(binomial.pmf(3)) # 3.7811696529388487e-06

# Mean of the distribution
print(binomial.mean()) # 15.0

# Variance
print(binomial.var()) # 7.5

# Standard deviation
print(binomial.std()) # 2.7386127875258306

# Random sample from the distr
print(binomial.rvs()) # 12
# get 10 random samples
print(binomial.rvs(10)) # [15 19 10 11 13 18 15 14 19 12]

# random sample with size 
random_samples = binomial.rvs(size = 3000) 
print(random_samples) # [16 16 20 ... 15 17 12]

# to show the plot
# plt.hist(random_samples)
# plt.show()

# Poisson distribution shows the probability of a certain events. The mean controlls the shape of the distribution. 

pois = stats.poisson(mu = 4)
random_samples_1 = pois.rvs(size = 2800)
print(random_samples_1)

# plt.hist(random_samples_1)
# plt.show()

# Normal distribution. 
norm = stats. norm()
random_samples_2 = norm.rvs(size=4400)
# plt.hist(random_samples_2, bins = 800)
# plt.show()

# uniforms 
unif = stats.uniform()
random_samples_3 = unif.rvs(size = 5000)
plt.hist(random_samples_3, bins = 900)
plt.show()