from copy import deepcopy
import numpy as np

def GaussSeidel(Aaug, x, Niter = 15):
    """
    This should implement the Gauss-Seidel method (see page 860, Tabl 20.2) for solving a system of equations.
    :param Aaug: The augmented matrix from Ax=b -> [A|b]
    :param x:  An initial guess for the x vector. if A is nxn, x is nx1
    :param Niter:  Number of iterations to run the GS method
    :return: the solution vector x
    """
    (m, n) = Aug.shape          # Getting the shape of Aug
    x0 = np.empty(shape=n - 1)  # Initialising x0
    for i in range(n - 1):
        x0[i] = x[i]

    a = Aug[:m, :n - 1]         # Getting the matrix a and b from Aug
    b = Aug[:m, n - 1].reshape(m)

    (m, n) = a.shape            # Defining new value of n
    x = np.zeros(shape=n)       # Initialising the solution
    k = 1                       # Initialising the iteration number
        while k <= Niter:
            for i in range(n):
                s = 0
                for j in range(i):
                    if (i == j):
                        continue
                    else:
                        s += a[i][j] * x[j]
                for j in range(i + 1, n):
                    if (i == j):
                        continue
                    else:
                        s += a[i][j] * x0[j]
                x[i] = (-s + b[i]) / (a[i][i])
            k += 1              # Updating the number of iterations
            for i in range(n):  # Updating the parameters
                x0[i] = x[i]
        return x                # Returning the solution

if __name__ == "__main__":
# Part (i)
    # Defining the Aug matrix
    Aug = np.array([[3, 1, -1, 2], [1, 4, 1, 12], [2, 1, 2, 10]])
    x = np.zeros(shape=Aug.shape[0])                                # Defining intial x
    x = GaussSiedel(Aug, x)                                         # calling the function
    print("Solution of Part (i) is ")                               # Displaying the solution
    print(x)                                                        # Displaying the solution

# Part (ii)
    # Defining the Aug matrix
    Aug = np.array([[9, 2, 3, 4, 21], [1, -10, 2, 4, 2], [-1, 2, 7, 3, 37], [3, 1, 4, 12, 12]])
    x = np.zeros(shape=Aug.shape[0])        # Defining intial x
    x = GaussSiedel(Aug, x)                 # calling the function
    print("\nSolution of Part (ii) is ")    # Displaying the solution
    print(x)
