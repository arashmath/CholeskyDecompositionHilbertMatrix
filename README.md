This is my project for <i>Numerical Linear Algebra</i> course at university ( Tehran Polytechnic (AUT) ).
It contains 2 python programs for performing <b>Cholesky decompostion on Hilbert matrix of any order</b>.

-  As you might know, Cholesky Decomposition is one type of <i>LU Decomposition</i> used only for positive definite matrices.
A matrix is <i>positive definite</i> if it is symmetric and has positive eigenvalues.
In <i>Cholesky method</i>, a positive definite matrix is written as the matrix multipication of a lower triangular matrix -
and its transpose.
One purpose of matrix decomposition is reducing calculations cost while solving a system of linear equations by decomposing the -
coefficients matrix into a multipication of triangular matrices.
-  As a reminder, <i>Hilbert matrix</i> of order 'n' is a symmetric positive definite matrix defined by the following formula:

H[i][j] = 1 / (i+j-1)    for i & j in range 1 to n

Both of the programs print out the lower triangular matrix in Cholesky method.

"CholeskyDecompositionHilbertMatrix.py" has the functions all coded by me and does not use any special libraries.

"CDHM_numpy.py" is much more concise and uses <b>Numpy & Scipy</b> libraries in order to perform its task; Therefore these
two famous libraries have to be installed on your operating system before running the code. (Both of these libraries are
avaiable in Anaconda) 

The second program might work better and faster on large Hilbert matrices (as 'n' increases) because it uses Scipy & Numpy
built-in functions which perform matrix operations perfectly.

It was a cool experience having two programs doing the same task and one has almost 30 lines of code, while the other has only 4.
