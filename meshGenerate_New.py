# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 20:20:19 2022

Author: Matt Goodson
Notes: Solution to question 56,57,58 
"""
import unittest
import numpy

def generateMesh(xmin, xmax, degree):
    num_elems = len(degree)
    elem_length = (xmax - xmin) / num_elems
    node_coords = []
    ien_array = []
    key = []
    num_nodes_elem = degree[0] + 1
    key.append(0)
    xmin_elem = xmin
    xmax_elem = xmin_elem + elem_length
    node_coords_elem = numpy.linspace(xmin_elem,xmax_elem,num_nodes_elem)
    node_coords_elem = list(node_coords_elem)
    node_coords.extend(node_coords_elem)
    ien = numpy.linspace(0,degree[0],degree[0]+1)
    ien = ien.astype(int)
    ien = list(ien)
    ien_array.append(ien)
    for i in range(1,num_elems):
        num_nodes_elem = degree[i] + 1
        key.append(i)
        xmin_elem = xmin + i*elem_length
        xmax_elem = xmin_elem + elem_length
        node_coords_elem = numpy.linspace(xmin_elem,xmax_elem,num_nodes_elem)
        node_coords_elem = list(node_coords_elem)
        node_coords.extend(node_coords_elem)
        ien = numpy.linspace(ien_array[-1][-1],ien_array[-1][-1] + (num_nodes_elem - 1), num_nodes_elem)
        ien = ien.astype(int)
        ien = list(ien)
        ien_array.append(ien)
    ien_array = dict(zip(key,ien_array)) 
    node_coords = numpy.unique(numpy.asarray(node_coords))   
    return node_coords, ien_array

class Test_generateMesh( unittest.TestCase ):
    def test_make_1_linear_elem( self ):
        gold_node_coords = numpy.array( [ 0.0, 1.0 ] )
        gold_ien_array = { 0: [ 0, 1 ] }
        node_coords, ien_array = generateMesh( xmin = 0.0, xmax = 1.0, degree = [ 1 ] )
        self.assertIsInstance( obj = node_coords, cls = numpy.ndarray )
        self.assertIsInstance( obj = ien_array, cls = dict )
        self.assertTrue( numpy.allclose( node_coords, gold_node_coords ) )
        self.assertDictEqual( d1 = gold_ien_array, d2 = ien_array )
    
    def test_make_1_quadratic_elem( self ):
        gold_node_coords = numpy.array( [ 0.0, 0.5, 1.0 ] )
        gold_ien_array = { 0: [ 0, 1, 2 ] }
        node_coords, ien_array = generateMesh( xmin = 0.0, xmax = 1.0, degree = [ 2 ] )
        self.assertIsInstance( obj = node_coords, cls = numpy.ndarray )
        self.assertIsInstance( obj = ien_array, cls = dict )
        self.assertTrue( numpy.allclose( node_coords, gold_node_coords ) )
        self.assertDictEqual( d1 = gold_ien_array, d2 = ien_array )
    
    def test_make_2_linear_elems( self ):
        gold_node_coords = numpy.array( [ 0.0, 0.5, 1.0 ] )
        gold_ien_array = { 0: [ 0, 1 ], 1: [ 1, 2 ] }
        node_coords, ien_array = generateMesh( xmin = 0.0, xmax = 1.0, degree = [ 1, 1 ] )
        self.assertIsInstance( obj = node_coords, cls = numpy.ndarray )
        self.assertIsInstance( obj = ien_array, cls = dict )
        self.assertTrue( numpy.allclose( node_coords, gold_node_coords ) )
        self.assertDictEqual( d1 = gold_ien_array, d2 = ien_array )
    
    def test_make_2_quadratic_elems( self ):
        gold_node_coords = numpy.array( [ 0.0, 0.25, 0.5, 0.75, 1.0 ] )
        gold_ien_array = { 0: [ 0, 1, 2 ], 1: [ 2, 3, 4 ] }
        node_coords, ien_array = generateMesh( xmin = 0.0, xmax = 1.0, degree = [ 2, 2 ] )
        self.assertIsInstance( obj = node_coords, cls = numpy.ndarray )
        self.assertIsInstance( obj = ien_array, cls = dict )
        self.assertTrue( numpy.allclose( node_coords, gold_node_coords ) )
        self.assertDictEqual( d1 = gold_ien_array, d2 = ien_array )
    
    def test_make_4_linear_elems( self ):
        gold_node_coords = numpy.array( [ 0.0, 0.25, 0.5, 0.75, 1.0 ] )
        gold_ien_array = { 0: [ 0, 1 ], 1: [ 1, 2 ], 2: [ 2, 3 ], 3: [ 3, 4 ] }
        node_coords, ien_array = generateMesh( xmin = 0.0, xmax = 1.0, degree = [ 1, 1, 1, 1 ] )
        self.assertIsInstance( obj = node_coords, cls = numpy.ndarray )
        self.assertIsInstance( obj = ien_array, cls = dict )
        self.assertTrue( numpy.allclose( node_coords, gold_node_coords ) )
        self.assertDictEqual( d1 = gold_ien_array, d2 = ien_array )
    
    def test_make_4_quadratic_elems( self ):
        gold_node_coords = numpy.array( [ 0.0, 0.125, 0.25, 0.375, 0.5, 0.625, 0.75, 0.875, 1.0 ] )
        gold_ien_array = { 0: [ 0, 1, 2 ], 1: [ 2, 3, 4 ], 2: [ 4, 5, 6 ], 3: [ 6, 7, 8 ] }
        node_coords, ien_array = generateMesh( xmin = 0.0, xmax = 1.0, degree = [ 2, 2, 2, 2 ] )
        self.assertIsInstance( obj = node_coords, cls = numpy.ndarray )
        self.assertIsInstance( obj = ien_array, cls = dict )
        self.assertTrue( numpy.allclose( node_coords, gold_node_coords ) )
        self.assertDictEqual( d1 = gold_ien_array, d2 = ien_array )
    
    def test_make_4_p_refine_elems( self ):
        gold_node_coords = numpy.array( [ 0.0, 1.0, 1.5, 2.0, (2.0 + 1.0/3.0), (2.0 + 2.0/3.0), 3.0, 3.25, 3.5, 3.75, 4.0 ] )
        gold_ien_array = { 0: [ 0, 1 ], 1: [ 1, 2, 3 ], 2: [ 3, 4, 5, 6 ], 3: [ 6, 7, 8, 9, 10 ] }
        node_coords, ien_array = generateMesh( xmin = 0.0, xmax = 4.0, degree = [ 1, 2, 3, 4 ] )
        self.assertIsInstance( obj = node_coords, cls = numpy.ndarray )
        self.assertIsInstance( obj = ien_array, cls = dict )
        self.assertTrue( numpy.allclose( node_coords, gold_node_coords ) )
        self.assertDictEqual( d1 = gold_ien_array, d2 = ien_array )
        
unittest.main()