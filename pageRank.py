# Date: April 24th, 2018
# Author: Hasana Chaudry
# Class: Senior Colloquium
# Topic: Page Ranking
# Advisor: Kenneth Brakke
# Filename: pageRank.py

import numpy as np
import scipy as sc
#import pandas as pd
from fractions import Fraction


def float_format(vector, decimal):
    return np.round((vector).astype(np.float), decimals = decimal)

# Initializing three webpages. Each web page is assigned a probability of 1/3
n = Fraction(1, 3)

# Creates a 3x3 matrix that represents the transpose of an adjacency matrix
# Completely dense, rank-one teleportation matrix
E = np.matrix([[0, 0, 1], [Fraction(1,2), 0, 0], [Fraction(1,2), 1, 0]])

# Creates a 3x3 sparse matrix
# Sparse, stochastic matrix
S = np.zeros((3, 3))
S[:] = n

# Assigning the damping parameter (always between 0 and 1)
# The probability that when a user clicks on a link, they will continue browsing
a = 0.85

# The equation that gives the page rank values of links in the form of a matrix
# also called the Google Matrix
G = a * S + ((1 - a) * E) 

# Creating a matrix, r, that holds the current PageRank values of the three pages
r = np.matrix([n, n, n])
r = np.transpose(r)

# Saving the initial r value
old_r = r


# Setting up a for loop that will go through a hundred iterations
for k in range(1,100):
    # Calculating the page rank value through each iteration
    r = G * r
    print(r)
    print("\n")

    # An if statement that breaks the loop when an iteration returns
    # the same page rank values as the previous iteration
    if(old_r == r).all():
        break
    old_r = r

# Outputting the results
print("Final Ranks: \n ")
print("Node A's rank: ", float_format(r, 6)[0])
print("Node B's rank: ", float_format(r, 6)[1])
print("Node C's rank: ", float_format(r, 6)[2])
print("\n")
print("Sum:", np.sum(r))


