#!/usr/bin/python
"""
author  : Bhekimpilo Ndhlela
author  : 18998712
module  : Applied Mathematics(Numerical Methods) TW324
task    : computer assignment 04 question 5(a)
since   : Friday-23-03-2018
"""
def question_a(n=8.0, debug=True):
    h = (1.0 / (n - 1.0))
    f = array([exp(x) for x in linspace(0.0, 1.0, 8.0)])
    A = matrix([[1,-2, 1, 0, 0, 0, 0, 0],\
                [0, 1,-2, 1, 0, 0, 0, 0],\
                [0, 0, 1,-2, 1, 0, 0, 0],\
                [0, 0, 0, 1,-2, 1, 0, 0],\
                [0, 0, 0, 0, 1,-2, 1, 0],\
                [0, 0, 0, 0, 0, 1,-2, 1]])
    f_ = (1. / h**2.) * matmul(A, f).T

    """
    plot the approximation of the curve unnecessary for question
    5. I am doing it as a means of viewing the solution of the
    approximation.
    """
    plt.plot(linspace(0.0, 1.0, 6.0), f_, 'ro')
    plt.plot(linspace(0.0, 1.0, 6.0), f_, 'k--')
    plt.title("The Approximation of the Function exp(x) between [0;1]")
    plt.xlabel("x")
    plt.ylabel("f\"(x) = exp(x)")
    plt.show()

    if debug is True:
        print "DEBUG MODE: [ON] \t [QUESTION 5 A.)]"
        print "f\"(x) = ",
        for i in f_:
            print i,
        print "\nDim(f_) = ", shape(f_), "\t",\
              "Dim(A)  = ", shape(A),  "\t",\
              "Dim(f)  = ", shape(f)

if __name__ == "__main__":
    from numpy import (linspace, exp, array, shape, matrix, matmul)
    import matplotlib.pyplot as plt

    question_a()
else:
    from sys import exit
    exit("USAGE: python q5.py")
