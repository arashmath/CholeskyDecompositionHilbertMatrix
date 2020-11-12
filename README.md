# Cholesky Decomposition for the Hilbert Matrix 🧐

## 🔦 Introduction

This is my project for *Numerical Linear Algebra* course (Fall, 2018 taught by [Prof. Saeed Kazem](https://scholar.google.com/citations?user=AUYwTaMAAAAJ&hl=en)) at Amirkabir University of Technology (Tehran Polytechnic).
It contains 2 Python programs for performing Cholesky decompostion on Hilbert matrix of any order.

➡️ NOTE: A more theoretical description is available in [this Medium blog](https://medium.com/@arashmath16/cholesky-decomposition-for-hilbert-matrix-python-implementation-387f24c5069b) I wrote 🤓.

Both of the programs print out the lower-triangular matrix resulted from the Cholesky method.

* "CholeskyDecompositionHilbertMatrix.py" has the functions all coded by me and does not use any special libraries.
* "CDHM_numpy.py" is much more concise and uses **Numpy** & **Scipy** libraries in order to perform the task. Therefore these two famous libraries have to be installed on your operating system before running the code (Both of these libraries are avaiable in Anaconda).

## 🔘 Installation

Open up the command line and run the following:

* `pip install numpy`
* `pip install scipy`

## 💭 My thoughts on the code

The second program might work better and faster on large Hilbert matrices (as the order increases) because it uses Scipy & Numpy which perform matrix operations perfectly.

It was a cool experience having two programs doing the same task and one has almost 30 lines of code, while the other has only 4.
