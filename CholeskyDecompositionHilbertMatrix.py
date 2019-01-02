# This program prints the the lower triangular matrix in Cholesky decomposition of -
# a Hilbert matrix of any given order.
# Code by: Arash Ashrafzadeh

#------------------------------ function makeHilbert ------------------------------
# This function creates and returns Hilbert matrix of order n ('n' is inputted by user).

def makeHilbert(n):
    Hilbert = [[0 for i in range(n)]for j in range(n)]
    for i in range(0,n):
        for j in range(0,n):
            Hilbert[i][j] = 1/(i+j+1)
    return Hilbert

#------------------------------ function choleskyDecompostion ------------------------------
# This function decomposes the desired Hilbert matrix using Cholesky method.

def choleskyDecomposition(Hilbert):
    L = [[0 for i in range(len(Hilbert))]for j in range(len(Hilbert))]
    L[0][0] = (Hilbert[0][0])**0.5
    for i in range(1, len(Hilbert)):
        L[i][0] = (Hilbert[0][i])/(L[0][0])
    for i in range(1, len(Hilbert)):
        for j in range(1, i+1):
            if i == j:
                L[i][j] = (Hilbert[i][j] - sum((L[i][k]**2) for k in range(0, i)))**0.5
            else:
                L[i][j] = (1/L[j][j])*(Hilbert[i][j] - sum(L[i][k]*L[j][k] for k in range(0, min(i,j))))
    return L

#------------------------------ function showMatrix ------------------------------
# This function prints a 2-D string list in float format.

def showMatrix(matrix):
    for row in matrix:
        print([format(elem, "f") for elem in row])


order = int(input(" Enter the order of Hilbert matrix: ")) # Inputs the order of Hilbert matrix
showMatrix(choleskyDecomposition(makeHilbert(order))) # main call
