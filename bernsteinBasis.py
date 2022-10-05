# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 09:42:57 2022

@author: Matt Goodson

Notes: Solution to question 42
"""

import unittest
import math

def evaluateBernsteinBasis1D(variate,degree,basis_idx):
    v = (variate + 1)/2
    term1 = math.comb(degree,basis_idx)
    term2 = v**basis_idx
    term3 = (1 - v)**(degree-basis_idx)
    val = term1 * term2 * term3 
    return val



class Test_evaluateBernsteinBasis1D( unittest.TestCase ):
    def test_linearBernstein( self ):
        self.assertAlmostEqual( first = evaluateBernsteinBasis1D( variate = -1, degree = 1, basis_idx = 0 ), second = 1.0, delta = 1e-12 )
        self.assertAlmostEqual( first = evaluateBernsteinBasis1D( variate = -1, degree = 1, basis_idx = 1 ), second = 0.0, delta = 1e-12 )
        self.assertAlmostEqual( first = evaluateBernsteinBasis1D( variate = +1, degree = 1, basis_idx = 0 ), second = 0.0, delta = 1e-12 )
        self.assertAlmostEqual( first = evaluateBernsteinBasis1D( variate = +1, degree = 1, basis_idx = 1 ), second = 1.0, delta = 1e-12 )

    def test_quadraticBernstein( self ):
        self.assertAlmostEqual( first = evaluateBernsteinBasis1D( variate = -1, degree = 2, basis_idx = 0 ), second = 1.00, delta = 1e-12 )
        self.assertAlmostEqual( first = evaluateBernsteinBasis1D( variate = -1, degree = 2, basis_idx = 1 ), second = 0.00, delta = 1e-12 )
        self.assertAlmostEqual( first = evaluateBernsteinBasis1D( variate = -1, degree = 2, basis_idx = 2 ), second = 0.00, delta = 1e-12 )
        self.assertAlmostEqual( first = evaluateBernsteinBasis1D( variate =  0, degree = 2, basis_idx = 0 ), second = 0.25, delta = 1e-12 )
        self.assertAlmostEqual( first = evaluateBernsteinBasis1D( variate =  0, degree = 2, basis_idx = 1 ), second = 0.50, delta = 1e-12 )
        self.assertAlmostEqual( first = evaluateBernsteinBasis1D( variate =  0, degree = 2, basis_idx = 2 ), second = 0.25, delta = 1e-12 )
        self.assertAlmostEqual( first = evaluateBernsteinBasis1D( variate = +1, degree = 2, basis_idx = 0 ), second = 0.00, delta = 1e-12 )
        self.assertAlmostEqual( first = evaluateBernsteinBasis1D( variate = +1, degree = 2, basis_idx = 1 ), second = 0.00, delta = 1e-12 )
        self.assertAlmostEqual( first = evaluateBernsteinBasis1D( variate = +1, degree = 2, basis_idx = 2 ), second = 1.00, delta = 1e-12 )
        
unittest.main()