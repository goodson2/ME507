# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 12:39:15 2022

@author: mgood

Notes: Solution to Question 44
"""
import numpy
import unittest
import math

def getRiemannQuadrature(num_points):
    if num_points <= 0:
        raise ValueError('num_points_MUST_BE_INTEGER_GEQ_1')
    else:
        width = 2 / num_points
        node = width / 2 
        x = numpy.arange(-1 + node,1,width)
        w = numpy.full(num_points,width)
    return x, w

def riemannQuadrature(fun, num_points):
    x,w = getRiemannQuadrature(num_points)
    y = numpy.zeros(len(x))
    for i in range(len(x)):
        y[i] = fun(x[i])
    areas = numpy.multiply(w,y)
    val = numpy.sum(areas)
    return val

class Test_riemannQuadrature( unittest.TestCase ):
    def test_integrate_constant_one( self ):
        constant_one = lambda x : 1
        for num_points in range( 1, 100 ):
            self.assertAlmostEqual( first = riemannQuadrature( fun = constant_one, num_points = num_points ), second = 2.0, delta = 1e-12 )

    def test_integrate_linear( self ):
        linear = lambda x : x
        for num_points in range( 1, 100 ):
            self.assertAlmostEqual( first = riemannQuadrature( fun = linear, num_points = num_points ), second = 0.0, delta = 1e-12 )

    def test_integrate_quadratic( self ):
        linear = lambda x : x**2
        error = []
        for num_points in range( 1, 100 ):
            error.append( abs( (2.0 / 3.0) - riemannQuadrature( fun = linear, num_points = num_points ) ) )
        self.assertTrue( numpy.all( numpy.diff( error ) <= 0.0 ) )

    def test_integrate_sin( self ):
        sin = lambda x : math.sin(x)
        error = []
        for num_points in range( 1, 100 ):
            self.assertAlmostEqual( first = riemannQuadrature( fun = sin, num_points = num_points ), second = 0.0, delta = 1e-12 )

    def test_integrate_cos( self ):
        cos = lambda x : math.cos(x)
        error = []
        for num_points in range( 1, 100 ):
            error.append( abs( (2.0 / 3.0) - riemannQuadrature( fun = cos, num_points = num_points ) ) )
        self.assertTrue( numpy.all( numpy.diff( error ) <= 0.0 ) )
        
# class Test_getRiemannQuadrature( unittest.TestCase ):
#     def test_zero_points( self ):
#         with self.assertRaises( Exception ) as context:
#             getRiemannQuadrature( num_points = 0 )
#         self.assertEqual( "num_points_MUST_BE_INTEGER_GEQ_1", str( context.exception ) )

#     def test_one_point( self ):
#         x, w = getRiemannQuadrature( num_points = 1 )
#         self.assertAlmostEqual( first = x, second = 0.0 )
#         self.assertAlmostEqual( first = w, second = 2.0 )
#         self.assertIsInstance( obj = x, cls = numpy.ndarray )
#         self.assertIsInstance( obj = w, cls = numpy.ndarray )

#     def test_two_point( self ):
#         x, w = getRiemannQuadrature( num_points = 2 )
#         self.assertTrue( numpy.allclose( x, [ -0.50, 0.50 ] ) )
#         self.assertTrue( numpy.allclose( w, [ 1.0, 1.0 ] ) )
#         self.assertIsInstance( obj = x, cls = numpy.ndarray )
#         self.assertIsInstance( obj = w, cls = numpy.ndarray )

#     def test_three_point( self ):
#         x, w = getRiemannQuadrature( num_points = 3 )
#         self.assertTrue( numpy.allclose( x, [ -2.0/3.0, 0.0, 2.0/3.0 ] ) )
#         self.assertTrue( numpy.allclose( w, [ 2.0/3.0, 2.0/3.0, 2.0/3.0 ] ) )
#         self.assertIsInstance( obj = x, cls = numpy.ndarray )
#         self.assertIsInstance( obj = w, cls = numpy.ndarray )

#     def test_many_points( self ):
#         for num_points in range( 1, 100 ):
#             x, w = getRiemannQuadrature( num_points = num_points )
#             self.assertTrue( len( x ) == num_points )
#             self.assertTrue( len( w ) == num_points )
#             self.assertIsInstance( obj = x, cls = numpy.ndarray )
#             self.assertIsInstance( obj = w, cls = numpy.ndarray )
        
unittest.main()