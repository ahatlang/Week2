import numpy as np
""""Write a function defined as: def Probability(PDF, args, c, GT=True):
Write and call a main() function that uses your Probability function to find:
P(x<105|N(100,12.5)): probability x<105 given a normal distribution of x with μ=100, σ=12.5
P(x>μ+2σ|N(100, 3))
Print your findings to the c.l.i. in the following format:
P(x<1.00|N(0,1))=Y.YY
P(x>181.00|N(175,3))=Z.ZZ
"""
def Probability(PDF, args, c, GT=True):
    """PDF: is a callback function for the Gaussian/normal probability density function.
    The callback function (PDF) should take a single argument as a tuple, which contains values for 
    x, μ (population mean), and σ (population standard deviation).
    args: is a tuple containing μ and σ
    c: is a floating point value (i.e., the upper limit of integration)
    GT:  is a boolean indicating if we want the probability of x being greater than c (GT=True) or less than c (GT=False)
    To find the probability of x<c you should use the Simpson’s 1/3 rule to integrate PDF between the limits of x=μ-5⋅σ to c.
    """
    # mu=args[0] #args is a tuple and the first element is mu and the second element is sigma
    sigma = args[1]

    # interval end points
    a = -5 + sigma
    b = c

    # x>c that is GT=True
    if GT:
    # simpson's 1/3 rule
    # formula: (b-a)*[f(a)+4*f((a+b)/2)+f(b)]/6 #where f is a function

    # prob(x>c)=1-prob(x<c)
    # PDF takes only one argument containing x,mu and sigma
    # Threfore (a,)+args=(a,mu,sigma)
    # similarly (b,)+args=(b,mu,sigma)

        prob = 1 - (b - a) * (PDF((a,) + args) + 4 * PDF(((a + b) / 2,) + args) + PDF((b,) + args)) / 6
        return prob

    # if GT=False that is x<c
    else:
        prob = (b - a) * (PDF((a,) + args) + 4 * PDF(((a + b) / 2,) + args) + PDF((b,) + args)) / 6

        return prob

def main():
    # lambda is a shortcut in python for defining a function
    # it can take any number of arguments but only one expression
    # syntax:
    # lambda arguments:expression

    # PDF
    # arg=(x,)+args  create a tuple of three elements as PDF accept only one argument
    # containg x,mu and sigma so
    # arg will look like arg=(x,mu,sigma)

    PDF = lambda arg: (1 / (arg[2] * np.sqrt(2 * np.pi))) * np.exp(-(((arg[0] - arg[1]) / arg[2]) ** 2) / 2)

    # for N(0,1) and x<1
    args = (0, 1)
    c = 1.00
    GT = False

    # call probability function
    prob = probability(PDF, args, c, GT)
    print("{}={}".format("P(x<1.00|N(0,1))", round(prob, 2)))

    # for N(175,3) and x>175+2*3=181
    args = (175, 3)
    c = 181.00
    GT = True

    # call probability
    prob = probability(PDF, args, c, GT)
    print("{}={}".format("P(x>181.00|N(175,3))", round(prob, 2)))

if __name__ == "__main__":
    main()
