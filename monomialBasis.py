# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 09:42:57 2022

@author: Matt Goodson

Notes: Solution for question 33 and 34
"""

import unittest
import numpy as np
import sympy 
import math
import matplotlib.pyplot as plt

def evaluateMonomialBasis1D(degree,variate):
    return variate**degree

class Test_evaluateMonomialBasis1D( unittest.TestCase ):
   def test_basisAtBounds( self ):
       self.assertAlmostEqual( first = evaluateMonomialBasis1D( degree = 0, variate = 0 ), second = 1.0, delta = 1e-12 )
       for p in range( 1, 11 ):
           self.assertAlmostEqual( first = evaluateMonomialBasis1D( degree = p, variate = 0 ), second = 0.0, delta = 1e-12 )
           self.assertAlmostEqual( first = evaluateMonomialBasis1D( degree = p, variate = 1 ), second = 1.0, delta = 1e-12 )

   def test_basisAtMidpoint( self ):
       for p in range( 0, 11 ):
           self.assertAlmostEqual( first = evaluateMonomialBasis1D( degree = p, variate = 0.5 ), second = 1 / ( 2**p ), delta = 1e-12 )

# unittest.main()

xx = np.arange(0,1.01,0.01) 
power = np.arange(0,11) 
for i in range(0,11):
    monomial = xx**i
    plt.figure(0)    
    plt.plot(xx, monomial, "k", label = f"Order {str(i)}")
plt.legend(loc="upper left")
plt.xlim(0, 1)
#plt.ylim(-3, 3)
plt.xlabel('x')
plt.ylabel('f(x)')

plt.savefig('monomialBasis.png', dpi=600)