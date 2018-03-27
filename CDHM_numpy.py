# This program prints the the lower triangular matrix in Cholesky decomposition of -
# a Hilbert matrix of any given order.

import numpy as np # Here, to perform decomposition on matrix
from scipy.linalg import hilbert # Here, to create Hilbert matrix with

n = int(input(" Please enter the order of Hilbert matrix: ")) # Inputting the order of Hilbert matrix
print(np.linalg.cholesky(hilbert(n))) # Prints out the lower triangular matrix in Cholesky decomposition  for Hilbert matrix
