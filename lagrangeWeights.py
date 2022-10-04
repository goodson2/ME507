# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 07:44:04 2022

@author: mgood
"""
import numpy as np
import sympy


def evaluateLagrangeBasis1D(variate,degree):
    step = 2/degree
    xj = np.arange(-1,1+step,step)
    val = 1 
    for j in range(0,degree+1):
        if j == basis_idx:
            val = val
        else:
            val = val*(variate - xj[j])/(xj[basis_idx] - xj[j])
    
    return val

x = sympy.Symbol('x')