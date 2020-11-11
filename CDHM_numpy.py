# This program prints the the lower-triangular matrix in Cholesky decomposition of -
# a Hilbert matrix of any given order.

# Code by: Arash Ashrafzadeh
# Homepage: https://arashmath.github.io/

# Importing necessary libraries
from numpy.linalg import cholesky # To perform matrix decomposition
from scipy.linalg import hilbert # To create the Hilbert matrix

# Inputting the order of the Hilbert matrix
n = int(input(" Please enter the order of Hilbert matrix: "))

# Printing the lower-triangular matrix in Cholesky decomposition for Hilbert matrix
print(cholesky(hilbert(n)))

# Lines 12 & 15 can be merged into one line as the following (but it violates the clean, readable coding
# # paradigms I guess! So it's not recommended).
# print(cholesky(hilbert(int(input()))))