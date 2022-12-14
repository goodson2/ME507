# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 10:17:56 2022

@author: mgood
"""

import numpy
import unittest
import basis ## USER DEFINED MODULE
import scipy
from scipy import integrate
import matplotlib.pyplot as plt
import assembleGramMatrix
import assembleForceVector

def computeSolution(target_fun, domain, degree, solution_basis):
    M = assembleGramMatrix.assembleGramMatrix(domain,degree,solution_basis)
    F = assembleForceVector.assembleForceVector(target_fun, domain, degree, solution_basis)
    M_inv = numpy.linalg.inv(M)
    d = numpy.dot(M_inv,F)
    return d

# Given Reference Functions
def evaluateSolutionAt( x, domain, coeff, solution_basis ):
    degree = len( coeff ) - 1
    y = 0.0
    for n in range( 0, len( coeff ) ):
        y += coeff[n] * solution_basis(variate = x, degree = degree, basis_idx = n, domain = domain)
    return y

def computeFitError( gold_coeff, test_coeff, domain, solution_basis ):
    err_fun = lambda x: abs( evaluateSolutionAt( x, domain, gold_coeff, solution_basis ) - evaluateSolutionAt( x, domain, test_coeff, solution_basis ) )
    abs_err, _ = scipy.integrate.quad( err_fun, domain[0], domain[1], epsrel = 1e-12, limit = 1000 )
    return abs_err

def plotCompareGoldTestSolution( gold_coeff, test_coeff, domain, solution_basis ):
    x = numpy.linspace( domain[0], domain[1], 1000 )
    yg = numpy.zeros( 1000 )
    yt = numpy.zeros( 1000 )
    for i in range(0, len(x) ):
        yg[i] = evaluateSolutionAt( x[i], domain, gold_coeff, solution_basis )
        yt[i] = evaluateSolutionAt( x[i], domain, test_coeff, solution_basis )
    plt.plot( x, yg )
    plt.plot( x, yt )
    plt.show()

def plotCompareFunToTestSolution( fun, test_coeff, domain, solution_basis ):
    x = numpy.linspace( domain[0], domain[1], 1000 )
    y = numpy.zeros( 1000 )
    yt = numpy.zeros( 1000 )
    for i in range(0, len(x) ):
        y[i] = fun( x[i] )
        yt[i] = evaluateSolutionAt( x[i], domain, test_coeff, solution_basis )
    plt.plot( x, y )
    plt.plot( x, yt )
    plt.show()

class Test_computeSolution( unittest.TestCase ):
    def test_cubic_polynomial_target( self ):
        # print( "POLY TEST" )
        target_fun = lambda x: x**3 - (8/5)*x**2 + (3/5)*x
        domain = [ 0, 1 ]
        degree = 2
        solution_basis = basis.evalBernsteinBasis1D
        test_sol_coeff = computeSolution( target_fun = target_fun, domain = domain, degree = degree, solution_basis =solution_basis )
        gold_sol_coeff = numpy.array( [ 1.0 / 20.0, 1.0 / 20.0, -1.0 / 20.0 ] )
        fit_err = computeFitError( gold_sol_coeff, test_sol_coeff, domain, solution_basis )
        plotCompareGoldTestSolution( gold_sol_coeff, test_sol_coeff, domain, solution_basis )
        # plotCompareFunToTestSolution( target_fun, test_sol_coeff, domain, solution_basis )
        self.assertTrue( numpy.allclose( gold_sol_coeff, test_sol_coeff ) )
        self.assertAlmostEqual( first = fit_err, second = 0, delta = 1e-12 )

    def test_sin_target( self ):
        # print( "SIN TEST" )
        target_fun = lambda x: numpy.sin( numpy.pi * x )
        domain = [ 0, 1 ]
        degree = 2
        solution_basis = basis.evalBernsteinBasis1D
        test_sol_coeff = computeSolution( target_fun = target_fun, domain = domain, degree = degree, solution_basis = solution_basis )
        gold_sol_coeff = numpy.array( [ (12*(numpy.pi**2 - 10))/(numpy.pi**3), -(6*(3*numpy.pi**2 - 40))/(numpy.pi**3), (12*(numpy.pi**2 - 10))/(numpy.pi**3)] )
        fit_err = computeFitError( gold_sol_coeff, test_sol_coeff, domain, solution_basis )
        plotCompareGoldTestSolution( gold_sol_coeff, test_sol_coeff, [0, 1], solution_basis )
        # plotCompareFunToTestSolution( target_fun, test_sol_coeff, domain, solution_basis )
        self.assertAlmostEqual( first = fit_err, second = 0, delta = 1e-5 )
        
    def test_erfc_target( self ):
        # print( "ERFC TEST" )
        target_fun = lambda x: numpy.real( scipy.special.erfc( x ) )
        domain = [ -2, 2 ]
        degree = 3
        solution_basis = basis.evalBernsteinBasis1D
        test_sol_coeff = computeSolution( target_fun = target_fun, domain = domain, degree = degree, solution_basis = solution_basis )
        gold_sol_coeff = numpy.array( [ 1.8962208131568558391841630949727, 2.6917062016799657617278998883219, -0.69170620167996576172789988832194, 0.10377918684314416081583690502732] )
        fit_err = computeFitError( gold_sol_coeff, test_sol_coeff, domain, solution_basis )
        plotCompareGoldTestSolution( gold_sol_coeff, test_sol_coeff, [-2, 2], solution_basis )
        # plotCompareFunToTestSolution( target_fun, test_sol_coeff, domain, solution_basis )
        self.assertAlmostEqual( first = fit_err, second = 0, delta = 1e-4 )
    
    def test_exptx_target( self ):
        # print( "EXPT TEST" )
        target_fun = lambda x: float( numpy.real( float( x )**float( x ) ) )
        domain = [ -1, 1 ]
        degree = 5
        solution_basis = basis.evalBernsteinBasis1D
        test_sol_coeff = computeSolution( target_fun = target_fun, domain = domain, degree = degree, solution_basis = solution_basis )
        gold_sol_coeff = ( [ -0.74841381974620419634327921170757, -3.4222814978197825394922980704166, 7.1463655364038831935841354617843, -2.9824200396151998304868767455064, 1.6115460899636204992283970407553, 0.87876479932866366847320748048494 ] )
        fit_err = computeFitError( gold_sol_coeff, test_sol_coeff, domain, solution_basis )
        plotCompareGoldTestSolution( gold_sol_coeff, test_sol_coeff, [-1, 1], solution_basis )
        # plotCompareFunToTestSolution( target_fun, test_sol_coeff, domain, solution_basis )
        self.assertAlmostEqual( first = fit_err, second = 0, delta = 1e-2 )
        
    
unittest.main()
