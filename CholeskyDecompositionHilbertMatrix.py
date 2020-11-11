# This program prints the the lower-triangular matrix in Cholesky decomposition of -
# a Hilbert matrix of any given order.

# Code by: Arash Ashrafzadeh
# Homepage: https://arashmath.github.io/

#------------------------------ function make_hilbert ------------------------------
def make_hilbert(n):
    """Creates a Hilbert matrix of a given dimension.
    For more information `check here <https://en.wikipedia.org/wiki/Hilbert_matrix>`_

    Parameters
    ----------
    n : int
        The dimension (order) of the Hilbert matrix to be created.
      
    Returns
    -------
    hilbert: list of lists
        The Hilbert matrix of order `n`.
    """
    # Initializing an nXn matrix of zeros
    hilbert = [[0 for i in range(n)]for j in range(n)] 
    
    for i in range(0,n):
        for j in range(0,n):
            hilbert[i][j] = 1 / (i+j+1)
    
    return hilbert

#------------------------------ function cholesky_decompostion ------------------------------
def cholesky_decomposition(matrix):
    """Performs matrix decomposition using the Cholesky method.
    For more information, `check here <https://en.wikipedia.org/wiki/Cholesky_decomposition>`_

    Parameters
    ----------
    matrix : list of lists
        A matrix filled with numbers (no matter int or float) to perform Cholesky decomposition on.
  
    Returns
    -------
    L : list of lists
        The lower triangular matrix coming from the decomposition.
    """

    d = len(matrix)
    # Initializing an nxn matrix of zeros
    L = [[0 for i in range(d)] for j in range(d)]

    # Initializing the first element in the matrix
    L[0][0] = (matrix[0][0])**0.5

    # Initializing the first column of the matrix
    for i in range(1, d):
        L[i][0] = (matrix[0][i]) / (L[0][0])
    
    # Filling-in elsewhere
    for i in range(1, d):
        for j in range(1, i+1):
            # Filling the main diagonal
            if i == j:
                L[i][j] = (matrix[i][j] - sum((L[i][k]**2) for k in range(0, i)))**0.5
            
            # Filling below the main diagonal
            else:
                L[i][j] = (1 / L[j][j]) * (matrix[i][j] - sum(L[i][k]*L[j][k] for k in range(0, min(i,j))))
    
    return L

#------------------------------ function show_matrix ------------------------------
def show_matrix(matrix):
    """Prints a matrix of floats with 6 digits precision (each element in string format).
        
        Parameters
        ----------
        matrix: list of lists
            A matrix filled with floats.
      
        Returns
        -------
        None
            Just prints the matrix, and does not return anything.
    """
  
    for row in matrix:
        print([format(elem, "f") for elem in row])

#------------------------------ Main calls ------------------------------
# Inputting the order of Hilbert matrix from the user
order = int(input(" Enter the order of the Hilbert matrix: "))
# Main call
show_matrix(cholesky_decomposition(make_hilbert(order)))