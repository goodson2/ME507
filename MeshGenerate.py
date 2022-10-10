# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 10:49:03 2022

@author: mgood
"""
import numpy
import unittest

def generateMesh1D(xmin, xmax, num_elems, degree):
    # sort first by degree and then deal with number of elements
    if degree == 1:
        # Create linear elements
        points = num_elems + 1
        node_coords = numpy.linspace(xmin,xmax,points)
        ien_array = []
        for i in range(0,num_elems):
            ien = [i, i+1]
            ien_array.append(ien)
    elif degree == 2:
        # Create quadratic elements
        points = 2*num_elems + 1
        node_coords = numpy.linspace(xmin,xmax,points)
        ien_array = []
        for i in range(0,len(node_coords)-1,2):
            ien = [i, i+1, i+2]
            ien_array.append(ien)
    ien_array = numpy.asarray(ien_array)
    return node_coords, ien_array




class Test_generateMesh1D( unittest.TestCase ):
    def test_make_1_linear_elem( self ):
        gold_node_coords = numpy.array( [ 0.0, 1.0 ] )
        gold_ien_array = numpy.array( [ [ 0, 1 ] ], dtype = int )
        node_coords, ien_array = generateMesh1D( xmin = 0.0, xmax = 1.0, num_elems = 1, degree = 1 )
        self.assertIsInstance( obj = node_coords, cls = numpy.ndarray )
        self.assertIsInstance( obj = ien_array, cls = numpy.ndarray )
        self.assertTrue( numpy.allclose( node_coords, gold_node_coords ) )
        self.assertTrue( numpy.array_equiv( ien_array, gold_ien_array ) )
    
    def test_make_1_quadratic_elem( self ):
        gold_node_coords = numpy.array( [ 0.0, 0.5, 1.0 ] )
        gold_ien_array = numpy.array( [ [ 0, 1, 2 ] ], dtype = int )
        node_coords, ien_array = generateMesh1D( xmin = 0.0, xmax = 1.0, num_elems = 1, degree = 2 )
        self.assertIsInstance( obj = node_coords, cls = numpy.ndarray )
        self.assertIsInstance( obj = ien_array, cls = numpy.ndarray )
        self.assertTrue( numpy.allclose( node_coords, gold_node_coords ) )
        self.assertTrue( numpy.array_equiv( ien_array, gold_ien_array ) )
    
    def test_make_2_linear_elems( self ):
        gold_node_coords = numpy.array( [ 0.0, 0.5, 1.0 ] )
        gold_ien_array = numpy.array( [ [ 0, 1 ], [ 1, 2 ] ], dtype = int )
        node_coords, ien_array = generateMesh1D( xmin = 0.0, xmax = 1.0, num_elems = 2, degree = 1 )
        self.assertIsInstance( obj = node_coords, cls = numpy.ndarray )
        self.assertIsInstance( obj = ien_array, cls = numpy.ndarray )
        self.assertTrue( numpy.allclose( node_coords, gold_node_coords ) )
        self.assertTrue( numpy.array_equiv( ien_array, gold_ien_array ) )
    
    def test_make_2_quadratic_elems( self ):
        gold_node_coords = numpy.array( [ 0.0, 0.25, 0.5, 0.75, 1.0 ] )
        gold_ien_array = numpy.array( [ [ 0, 1, 2 ], [ 2, 3, 4 ] ], dtype = int )
        node_coords, ien_array = generateMesh1D( xmin = 0.0, xmax = 1.0, num_elems = 2, degree = 2 )
        self.assertIsInstance( obj = node_coords, cls = numpy.ndarray )
        self.assertIsInstance( obj = ien_array, cls = numpy.ndarray )
        self.assertTrue( numpy.allclose( node_coords, gold_node_coords ) )
        self.assertTrue( numpy.array_equiv( ien_array, gold_ien_array ) )
    
    def test_make_4_linear_elems( self ):
        gold_node_coords = numpy.array( [ 0.0, 0.25, 0.5, 0.75, 1.0 ] )
        gold_ien_array = numpy.array( [ [ 0, 1 ], [ 1, 2 ], [ 2, 3 ], [ 3, 4 ] ], dtype = int )
        node_coords, ien_array = generateMesh1D( xmin = 0.0, xmax = 1.0, num_elems = 4, degree = 1 )
        self.assertIsInstance( obj = node_coords, cls = numpy.ndarray )
        self.assertIsInstance( obj = ien_array, cls = numpy.ndarray )
        self.assertTrue( numpy.allclose( node_coords, gold_node_coords ) )
        self.assertTrue( numpy.array_equiv( ien_array, gold_ien_array ) )
    
    def test_make_4_quadratic_elems( self ):
        gold_node_coords = numpy.array( [ 0.0, 0.125, 0.25, 0.375, 0.5, 0.625, 0.75, 0.875, 1.0 ] )
        gold_ien_array = numpy.array( [ [ 0, 1, 2 ], [ 2, 3, 4 ], [ 4, 5, 6 ], [ 6, 7, 8 ] ], dtype = int )
        node_coords, ien_array = generateMesh1D( xmin = 0.0, xmax = 1.0, num_elems = 4, degree = 2 )
        self.assertIsInstance( obj = node_coords, cls = numpy.ndarray )
        self.assertIsInstance( obj = ien_array, cls = numpy.ndarray )
        self.assertTrue( numpy.allclose( node_coords, gold_node_coords ) )
        self.assertTrue( numpy.array_equiv( ien_array, gold_ien_array ) )
        
        
unittest.main()