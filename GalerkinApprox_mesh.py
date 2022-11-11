# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 14:56:24 2022

@author: mgood
"""

import numpy
import unittest
import basis ## USER DEFINED MODULE
import scipy
# from scipy import integrate
from assembleGramMatrix_mesh import assembleGramMatrix
from assembleForceVector_mesh import assembleForceVector
import matplotlib.pyplot as plt
import meshGenerate_New


def computeSolution(target_fun, domain, degree, solution_basis):
    node_coords, ien_array = meshGenerate_New.generateMesh(domain[0], domain[-1], degree)
    M = assembleGramMatrix(node_coords, ien_array, solution_basis)
    F = assembleForceVector(target_fun, node_coords, ien_array, solution_basis)
    d = numpy.matmul(numpy.linalg.inv(M), F)
    return d, node_coords, ien_array

# Referenced Functions (need new compute fit error function)
def computeFitError( target_fun, coeff, node_coords, ien_array, eval_basis ):
    # num_elems = ien_array.shape[0]
    num_elems = len(ien_array)
    domain = [ min( node_coords ), max( node_coords ) ]
    abs_err_fun = lambda x : abs( target_fun( x ) - evaluateSolutionAt( x, coeff, node_coords, ien_array, eval_basis ) )
    fit_error, residual = scipy.integrate.quad( abs_err_fun, domain[0], domain[1], epsrel = 1e-12, limit = num_elems * 100 )
    return fit_error, residual

def evaluateSolutionAt(x,coeff,node_coords,ien_array,eval_basis):
    for element in range(0,len(ien_array)):
        if x >= node_coords[ien_array[element][0]] and x <= node_coords[ien_array[element][-1]]:
            elem_idx = element
            break            
    elem_nodes = ien_array[elem_idx]
    elem_domain = [node_coords[elem_nodes[0]] , node_coords[elem_nodes[-1]]]
    param_coord = 2*((x - elem_domain[0]) / (elem_domain[-1] - elem_domain[0])) - 1 #now exists between [-1,1] for Lagrange input
    sol_at_point = 0
    for n in range(0,len(elem_nodes)):
        curr_node = elem_nodes[n]
        sol_at_point += coeff[curr_node]*basis.evalLagrangeBasis1D(param_coord,len(elem_nodes)-1,n,elem_domain) #added elem_domain argument
    return sol_at_point

def computeElementFitError( target_fun, coeff, node_coords, ien_array, elem_idx, eval_basis ):
    elem_nodes = ien_array[elem_idx]
    domain = [ node_coords[elem_nodes[0]], node_coords[elem_nodes[-1]] ]
    abs_err_fun = lambda x : abs( target_fun( x ) - evaluateSolutionAt( x, coeff, node_coords, ien_array, eval_basis ) )
    abs_error, residual = scipy.integrate.quad( abs_err_fun, domain[0], domain[1], epsrel = 1e-12, limit = 100 )
    return abs_error, residual

def plotCompareGoldTestSolution( gold_coeff, test_coeff, node_coords, ien_array, solution_basis ):
    domain = [ min( node_coords ), max( node_coords ) ]
    x = numpy.linspace( domain[0], domain[1], 1000 )
    yg = numpy.zeros( 1000 )
    yt = numpy.zeros( 1000 )
    for i in range(0, len(x) ):
        yg[i] = evaluateSolutionAt( x[i], gold_coeff, node_coords, ien_array, solution_basis )
        yt[i] = evaluateSolutionAt( x[i], test_coeff, node_coords, ien_array, solution_basis )
    plt.plot( x, yg )
    plt.plot( x, yt )
    plt.show()

def plotCompareFunToTestSolution( fun, test_coeff, node_coords, ien_array, solution_basis ):
    x = numpy.linspace( min( node_coords ), max( node_coords ), 1000 )
    y = numpy.zeros( 1000 )
    yt = numpy.zeros( 1000 )
    for i in range(0, len(x) ):
        y[i] = fun( x[i] )
        yt[i] = evaluateSolutionAt( x[i], test_coeff, node_coords, ien_array, solution_basis )
    plt.plot( x, y )
    plt.plot( x, yt )
    plt.show()


class Test_computeSolution( unittest.TestCase ):
    def test_cubic_polynomial_target( self ):
        # print( "POLY TEST" )
        target_fun = lambda x: x**3 - (8/5)*x**2 + (3/5)*x
        domain = [ 0, 1 ]
        degree = [2]*2
        solution_basis = basis.evalBernsteinBasis1D
        test_sol_coeff, node_coords, ien_array = computeSolution( target_fun = target_fun, domain = domain, degree = degree, solution_basis =solution_basis )
        gold_sol_coeff = numpy.array( [ 1.0 / 120.0, 9.0 / 80.0, 1.0 / 40.0, -1.0 / 16.0, -1.0 / 120.0 ] )
        abs_err, rel_err = computeFitError( target_fun, test_sol_coeff, node_coords, ien_array, solution_basis )
        plotCompareGoldTestSolution( gold_sol_coeff, test_sol_coeff, node_coords, ien_array, solution_basis )
        # plotCompareFunToTestSolution( target_fun, test_sol_coeff, node_coords, ien_array, solution_basis )
        self.assertTrue( numpy.allclose( gold_sol_coeff, test_sol_coeff ) )
        self.assertAlmostEqual( first = rel_err, second = 0, delta = 1e-1 )

    def test_sin_target( self ):
        # print( "SIN TEST" )
        target_fun = lambda x: numpy.sin( numpy.pi * x )
        domain = [ 0, 1 ]
        degree = [2]*2
        solution_basis = basis.evalBernsteinBasis1D
        test_sol_coeff, node_coords, ien_array = computeSolution( target_fun = target_fun, domain = domain, degree = degree, solution_basis = solution_basis )
        gold_sol_coeff = numpy.array( [ -0.02607008, 0.9185523, 1.01739261, 0.9185523, -0.02607008 ] )
        abs_err, rel_err = computeFitError( target_fun, test_sol_coeff, node_coords, ien_array, solution_basis )
        plotCompareGoldTestSolution( gold_sol_coeff, test_sol_coeff, node_coords, ien_array, solution_basis )
        # plotCompareFunToTestSolution( target_fun, test_sol_coeff, node_coords, ien_array, solution_basis )
        self.assertAlmostEqual( first = rel_err, second = 0, delta = 1e-1 )
        
    def test_erfc_target( self ):
        # print( "ERFC TEST" )
        target_fun = lambda x: numpy.real( scipy.special.erfc( x ) )
        domain = [ -2, 2 ]
        degree = [3]*2
        solution_basis = basis.evalBernsteinBasis1D
        test_sol_coeff, node_coords, ien_array = computeSolution( target_fun = target_fun, domain = domain, degree = degree, solution_basis = solution_basis )
        gold_sol_coeff = numpy.array( [ 1.98344387, 2.0330054, 1.86372084, 1., 0.13627916, -0.0330054, 0.01655613 ] )
        abs_err, rel_err = computeFitError( target_fun, test_sol_coeff, node_coords, ien_array, solution_basis )
        plotCompareGoldTestSolution( gold_sol_coeff, test_sol_coeff, node_coords, ien_array, solution_basis )
        # plotCompareFunToTestSolution( target_fun, test_sol_coeff, node_coords, ien_array, solution_basis )
        self.assertAlmostEqual( first = rel_err, second = 0, delta = 1e-2 )
    
    def test_exptx_target( self ):
        # print( "EXPT TEST" )
        target_fun = lambda x: float( numpy.real( float( x )**float( x ) ) )
        domain = [ -1, 1 ]
        degree = [5]*2
        solution_basis = basis.evalBernsteinBasis1D
        test_sol_coeff, node_coords, ien_array = computeSolution( target_fun = target_fun, domain = domain, degree = degree, solution_basis = solution_basis )
        gold_sol_coeff = ( [ -1.00022471, -1.19005562, -0.9792369, 0.70884334, 1.73001439, 0.99212064, 0.44183573, 0.87014465, 0.5572111, 0.85241908, 0.99175228 ] )
        abs_err, rel_err = computeFitError( target_fun, test_sol_coeff, node_coords, ien_array, solution_basis )
        plotCompareGoldTestSolution( gold_sol_coeff, test_sol_coeff, node_coords, ien_array, solution_basis )
        # plotCompareFunToTestSolution( target_fun, test_sol_coeff, node_coords, ien_array, solution_basis )
        self.assertAlmostEqual( first = rel_err, second = 0, delta = 1e-2 )
        
unittest.main()