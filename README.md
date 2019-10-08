This is my project for <i>Numerical Linear Algebra</i> course at university ( Tehran Polytechnic (AUT) ).
It contains 2 python programs for performing <b>Cholesky decompostion on Hilbert matrix of any order</b>.

The description is available in [this](https://medium.com/@arashmath16/cholesky-decomposition-for-hilbert-matrix-python-implementation-387f24c5069b) Medium blog post I wrote.

Both of the programs print out the lower triangular matrix in Cholesky method.

"CholeskyDecompositionHilbertMatrix.py" has the functions all coded by me and does not use any special libraries.

"CDHM_numpy.py" is much more concise and uses <b>Numpy & Scipy</b> libraries in order to perform its task; Therefore these
two famous libraries have to be installed on your operating system before running the code. (Both of these libraries are
avaiable in Anaconda) 

The second program might work better and faster on large Hilbert matrices (as 'n' increases) because it uses Scipy & Numpy
built-in functions which perform matrix operations perfectly.

It was a cool experience having two programs doing the same task and one has almost 30 lines of code, while the other has only 4.
