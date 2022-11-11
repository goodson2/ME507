# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 08:12:56 2022

Author: Matthew Goodson
NOTES: Compilation of all quadrature routines I have made
"""

import numpy
import math
import scipy
from scipy import optimize

def computeGaussLegendreQuadrature( n ):
    M = numpy.zeros( 2*n, dtype = "double" )
    M[0] = 2.0
    x0 = numpy.linspace( -1, 1, n )
    sol = scipy.optimize.least_squares( lambda x : objFun( M, x ), x0, bounds = (-1, 1), ftol = 1e-14, xtol = 1e-14, gtol = 1e-14 )
    qp = sol.x
    w = solveLinearMomentFit( M, qp )
    return qp, w

def assembleLinearMomentFitSystem( degree, pts ):
    A = numpy.zeros( shape = ( degree + 1, len( pts ) ), dtype = "double" )
    for m in range(0, degree + 1):
        for n in range(0, len(pts)):
            A[m,n] = evalLegendreBasis1D(m, pts[n])
    return A

def evalLegendreBasis1D( degree, variate):
    if degree == 0:
        val = 1.0
    elif degree == 1:
        val = variate
    else:
        i = degree - 1
        term_1 = i * evalLegendreBasis1D(degree = i-1, variate = variate)
        term_2 = (2*i + 1) * variate * evalLegendreBasis1D( degree = i, variate = variate)
        val = (term_2 - term_1)/(i + 1)
    return val

def solveLinearMomentFit( M, pts ):
    degree = len( M ) - 1
    A = assembleLinearMomentFitSystem( degree, pts )
    sol = scipy.optimize.lsq_linear( A, M )
    w = sol.x
    return w

def objFun( M, pts ):
    degree = len( M ) - 1
    A = assembleLinearMomentFitSystem( degree, pts )
    w = solveLinearMomentFit( M, pts )
    obj_val = M - numpy.matmul(A,w)
    return obj_val


def computeNewtonCotesQuadrature(fun, num_points):
    x, w = getNewtonCotesQuadrature(num_points)
    f = numpy.zeros(len(x))
    for i in range (0, len(f)):
        f[i] = fun(x[i])
    s = numpy.sum(numpy.multiply(f,w))
    return s


def getNewtonCotesQuadrature(num_points):
    if num_points <= 0 or num_points >= 7:
        raise ValueError('num_points_MUST_BE_INTEGER_IN_[1,6]')
    elif num_points == 1:
        x = numpy.array([0])
        w = numpy.array([2])
    else:
        a = -1
        b = 1
        n = num_points - 1
        h = (b-a)/n
        x = numpy.arange(-1, 1+h, h)
        if num_points == 2:
            w = [h/2, h/2]
        elif num_points == 3:
            w = [h/3, 4*h/3, h/3]
        elif num_points == 4:
            w = [3*h/8, 9*h/8, 9*h/8, 3*h/8]
        elif num_points == 5:
            w = [14*h/45, 64*h/45, 24*h/45, 64*h/45, 14*h/45]
        elif num_points == 6:
            w = [95*h/288, 375*h/288, 250*h/288, 250*h/288, 375*h/288, 95*h/288]
        w = numpy.array(w)
    return x, w

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