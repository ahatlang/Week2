import math
def Secant(fcn, x0, x1, maxiter=10, xtol=1e-5):
    """fcn: the function for which we want to find the root x0 and x1: two x values in the neighborhood of the root
    xtol: exit if the |xnewest - xprevious| < xtol
    maxiter: exit if the number of iterations (new x values) equals this number
    return value: the final estimate of the root (most recent new x value) """
    #The function for which we are trying to discover the root is fcn.
    #Two x values close to the root are x0 and x1.
    #If the | xnewest - xprevious | is xtol, exit.
    #If the number of iterations(new x values) equals maxnew, the programme will terminate.
    #return value: the final root estimate(most recent new x value)
    iter = 0
    while abs(x0 - x1) >= xtol and iter <= maxiter:
        x2 = x1 - (fcn(x1) * (x1 - x0)) / (fcn(x1) - fcn(x0))
    x0 = x1
    x1 = x2
    iter += 1
    return x2

def main():
    f1 = lambda x: x - 3 * math.cos(x) - 3
    print('Solution of 1st function: ', Secant(f1, 1, 2, 5, 1e-4))
    f2 = lambda x: math.cos(2 * x) * x ** 3
    print('Solution of 1st function: ', Secant(f2, 1, 2, 15, 1e-8))
    print('Solution of 3rd function: ', Secant(f2, 1, 2, 3, 1e-8))
    main()
