# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 11:30:16 2022

@author: mgood
"""
import numpy

def affine_mapping_1D( domain, target_domain, x ):
    A = numpy.array( [ [ 1.0, domain[0] ], [ 1.0, domain[1] ] ] )
    b = numpy.array( [target_domain[0], target_domain[1] ] )
    c = numpy.linalg.solve( A, b )
    fx = c[0] + c[1] * x
    return fx  

domain = [-1,1]
target_domain = [0,1]