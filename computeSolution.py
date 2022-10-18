# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 10:19:33 2022

Author: Matt Goodson
Notes: Solution to question 53
"""
import unittest
import numpy
import mesh

def computeSolution(target_fun, domain, num_elems, degree):
    xmin = domain[0]
    xmax = domain[1]
    node_coords, ien_array = mesh.generateMesh(xmin, xmax, num_elems, degree)
    solution = target_fun(node_coords)    
    return solution, node_coords, ien_array

class Test_computeSolution( unittest.TestCase ):
    def test_single_linear_element_poly( self ):
        test_solution, node_coords, ien_array = computeSolution( target_fun = lambda x : x, domain = [-1.0, 1.0 ], num_elems = 1, degree = 1 )
        gold_solution = numpy.array( [ -1.0, 1.0 ] )
        self.assertTrue( numpy.allclose( test_solution, gold_solution ) )
    
    def test_single_quad_element_poly( self ):
        test_solution, node_coords, ien_array = computeSolution( target_fun = lambda x : x**2, domain = [-1.0, 1.0 ], num_elems = 1, degree = 2 )
        gold_solution = numpy.array( [ 1.0, 0.0, 1.0 ] )
        self.assertTrue( numpy.allclose( test_solution, gold_solution ) )
    
    def test_two_linear_element_poly( self ):
        test_solution, node_coords, ien_array = computeSolution( target_fun = lambda x : x**2, domain = [-1.0, 1.0 ], num_elems = 2, degree = 1 )
        gold_solution = numpy.array( [ 1.0, 0.0, 1.0 ] )
        self.assertTrue( numpy.allclose( test_solution, gold_solution ) )
    
    def test_four_quad_element_poly( self ):
        test_solution, node_coords, ien_array = computeSolution( target_fun = lambda x : x**2, domain = [-1.0, 1.0 ], num_elems = 4, degree = 1 )
        gold_solution = numpy.array( [ 1.0, 0.25, 0.0, 0.25, 1.0 ] )
        self.assertTrue( numpy.allclose( test_solution, gold_solution ) )
        
unittest.main()
        
