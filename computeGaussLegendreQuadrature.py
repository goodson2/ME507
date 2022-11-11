# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 08:20:32 2022

@author: mgood
"""

import unittest
import numpy
import math

def computeGaussLegendreQuadrature(fun, num_points):
    x, w = getGaussLegendreQuadrature(num_points)
    f = numpy.zeros(len(x))
    for i in range (0, len(f)):
        f[i] = fun(x[i])
    s = numpy.sum(numpy.multiply(f,w))
    return s

# IGNORE THIS CODE, use LinearMomentFit as computeGaussLegendreQuadrature

def getGaussLegendreQuadrature(nodes):
    if nodes <= 2 or nodes >= 7:
        raise ValueError('nodes_MUST_BE_INTEGER_IN_[2,7]')
    elif nodes == 2:
        x = numpy.array([0])
        w = numpy.array([2])
    elif nodes == 3:
        x = numpy.array([-1/math.sqrt(3), 1/math.sqrt(3)])
        w = numpy.array([1, 1])
    elif nodes == 4:
        x = numpy.array([-math.sqrt(3/5), 0, math.sqrt(3/5)])
        w = numpy.array([5/9, 8/9, 5/9])
    else:
        # I need to generalize how to find x and w for this case 
        # (see section 2.5.1.1 in textbook)
        x = 1
        w = 1
    return x, w

class Test_getGaussLegendreQuadrature( unittest.TestCase ):
    def test_incorrect_num_points( self ):
        with self.assertRaises( Exception ) as context:
            getGaussLegendreQuadrature( nodes = 1 )
        self.assertEqual( "nodes_MUST_BE_INTEGER_IN_[2,7]", str( context.exception ) )
        with self.assertRaises( Exception ) as context:
            getGaussLegendreQuadrature( nodes = 7 )
        self.assertEqual( "num_points_MUST_BE_INTEGER_IN_[2,7]", str( context.exception ) )

    def test_return_types( self ):
        for num_points in range( 1, 7 ):
            x, w = getGaussLegendreQuadrature( num_points = num_points )
            self.assertIsInstance( obj = x, cls = numpy.ndarray )
            self.assertIsInstance( obj = w, cls = numpy.ndarray )
            self.assertTrue( len( x ) == num_points )
            self.assertTrue( len( w ) == num_points )

class Test_computeGaussLegendreQuadrature( unittest.TestCase ):
    def test_integrate_constant_one( self ):
        constant_one = lambda x : 1 * x**0
        for degree in range( 1, 6 ):
            num_points = degree + 1
            self.assertAlmostEqual( first = computeGaussLegendreQuadrature( fun = constant_one, num_points = num_points ), second = 2.0, delta = 1e-12 )

    def test_exact_poly_int( self ):
        for degree in range( 1, 6 ):
            num_points = degree + 1
            poly_fun = lambda x : ( x + 1.0 ) ** degree
            indef_int = lambda x : ( ( x + 1 ) ** ( degree + 1) ) / ( degree + 1 )
            def_int = indef_int(1.0) - indef_int(-1.0)
            self.assertAlmostEqual( first = computeGaussLegendreQuadrature( fun = poly_fun, num_points = num_points ), second = def_int, delta = 1e-12 )

    def test_integrate_sin( self ):
        sin = lambda x : math.sin(x)
        for num_points in range( 1, 7 ):
            self.assertAlmostEqual( first = computeGaussLegendreQuadrature( fun = sin, num_points = num_points ), second = 0.0, delta = 1e-12 )

    def test_integrate_cos( self ):
        cos = lambda x : math.cos(x)
        self.assertAlmostEqual( first = computeGaussLegendreQuadrature( fun = cos, num_points = 6 ), second = 2*math.sin(1), delta = 1e-4 )

unittest.main()