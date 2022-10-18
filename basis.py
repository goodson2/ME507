# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 13:37:17 2022

@author: mgood

Notes: Compiles all the different bases discussed in class
LIST OF BASIS:
    - Monomial basis (question 34)
    - 
"""

import unittest
import numpy
import sympy 
import math
import matplotlib.pyplot as plt

def evaluateMonomialBasis1D(degree,variate):
    return variate**degree

def evalLegendreBasis1D(degree,variate):
    if degree == 0:
        P = 1.0
    elif degree == 1:
        P = variate
    else:
        i = degree - 1
        term_1 = i * evalLegendreBasis1D(degree = i-1, variate = variate)
        term_2 = (2*i + 1) * variate * evalLegendreBasis1D(degree = i, variate = variate)
        P = ( term_2 - term_1 ) / (i + 1)
    return P

def evalLagrangeBasis1D(variate,degree,basis_idx):
    # To be more robust and allow for higher degrees the xj term 
    # should be a function of degree. As it currently stand the function is
    # only valid through degree 2.
    step = 2/degree
    xj = numpy.arange(-1,2,step)
    val = 1 
    for j in range(0,degree+1):
        if j == basis_idx:
            val = val
        else:
            val = val*(variate - xj[j])/(xj[basis_idx] - xj[j])
    return val

def evaluateBernsteinBasis1D(variate,degree,basis_idx):
    v = (variate + 1)/2
    term1 = math.comb(degree,basis_idx)
    term2 = v**basis_idx
    term3 = (1 - v)**(degree-basis_idx)
    val = term1 * term2 * term3 
    return val