# This program prints the the lower-triangular matrix in Cholesky decomposition of -
# a Hilbert matrix of any given order.

import numpy as np # To perform matrix decomposition
from scipy.linalg import hilbert # To create Hilbert matrix

n = int(input(" Please enter the order of Hilbert matrix: ")) # Inputting the order of Hilbert matrix
print(np.linalg.cholesky(hilbert(n))) # Prints out the lower-triangular matrix in Cholesky decomposition for Hilbert matrix

# Lines 7 & 8 can be merged into one line as the following (but it violates the clean, readable coding paradigms I guess!):
# print(np.linalg.cholesky(hilbert(int(input()))))
