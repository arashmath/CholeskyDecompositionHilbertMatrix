This is my project for Numerical Linear Algebra course at university ( Tehran Polytechnic (AUT) ).
It contains 2 python programs for performing Cholesky decompostion on Hilbert matrix of any order.

-  As you might know, Cholesky Decomposition is one type of LU Decomposition used only for positive definite matrices.
A matrix is positive definite if it is symmetric and has positive eigenvalues.
In Cholesky method, a positive definite matrix is written as the matrix multipication of a lower triangular matrix -
and its transpose.
One purpose of matrix decomposition is reducing calculations cost while solving a system of linear equations by decomposing the -
coefficients matrix into a multipication of triangular matrices.
-  As a reminder, Hilbert matrix of order 'n' is a symmetric positive definite matrix defined by the following formula:
H[i][j] = 1 / (i+j-1)    for i & j in range 1 to n

Both of the programs print out the lower triangular matrix in Cholesky method.

"CholeskyDecompositionHilbertMatrix.py" has the functions all coded by me and does not use any special libraries.

"CDHM_numpy.py" is much more consise and uses Numpy & Scipy libraries in order to perform its task; Therefore these two famous libraries
have to be installed on your operating system before running the code. (Both of these libraries are avaiable in Anaconda) 

The second program might work better and faster on large Hilbert matrices (as 'n' increases) because it uses Scipy & Numpy
built-in functions which perform matrix operations perfectly.

