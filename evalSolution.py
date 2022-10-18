# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 10:32:12 2022

Author: Matt Goodson
Notes: Solution to problem 54
"""
import unittest
import numpy
import mesh
import basis 


def evaluateSolutionAt(x, coeff, node_coords, ien_array, eval_basis):
    for i in range(0, len(ien_array)):
        if x >= node_coords[ien_array[i,0]] and x <= node_coords[ien_array[i,-1]]:
            elem_idx = i
            break    
    elem_nodes = ien_array[elem_idx]
    elem_domain = [node_coords[elem_nodes[0]], node_coords[elem_nodes[-1]]]
    param_coord = 2*((x-elem_domain[0])/(elem_domain[-1]-elem_domain[0]))-1
    sol_at_point = 0
    for i in range(0, len(elem_nodes)):
        curr_node = elem_nodes[i]
        sol_at_point += coeff[curr_node]*eval_basis(param_coord,len(elem_nodes)-1,i)
    return sol_at_point

class Test_evaluateSolutionAt( unittest.TestCase ):
    def test_single_linear_element( self ):
        node_coords, ien_array = mesh.generateMesh( -1, 1, 1, 1 )
        coeff = numpy.array( [-1.0, 1.0 ] )
        self.assertAlmostEqual( first = evaluateSolutionAt( x = -1.0, coeff = coeff, node_coords = node_coords, ien_array = ien_array, eval_basis = basis.evalLagrangeBasis1D ), second = -1.0 )
        self.assertAlmostEqual( first = evaluateSolutionAt( x =  0.0, coeff = coeff, node_coords = node_coords, ien_array = ien_array, eval_basis = basis.evalLagrangeBasis1D ), second =  0.0 )
        self.assertAlmostEqual( first = evaluateSolutionAt( x = +1.0, coeff = coeff, node_coords = node_coords, ien_array = ien_array, eval_basis = basis.evalLagrangeBasis1D ), second = +1.0 )

    def test_two_linear_elements( self ):
        node_coords, ien_array = mesh.generateMesh( -1, 1, 2, 1 )
        coeff = numpy.array( [ 1.0, 0.0, 1.0 ] )
        self.assertAlmostEqual( first = evaluateSolutionAt( x = -1.0, coeff = coeff, node_coords = node_coords, ien_array = ien_array, eval_basis = basis.evalLagrangeBasis1D ), second = +1.0 )
        self.assertAlmostEqual( first = evaluateSolutionAt( x =  0.0, coeff = coeff, node_coords = node_coords, ien_array = ien_array, eval_basis = basis.evalLagrangeBasis1D ), second =  0.0 )
        self.assertAlmostEqual( first = evaluateSolutionAt( x = +1.0, coeff = coeff, node_coords = node_coords, ien_array = ien_array, eval_basis = basis.evalLagrangeBasis1D ), second = +1.0 )
    
    def test_single_quadratic_element( self ):
        node_coords, ien_array = mesh.generateMesh( -1, 1, 1, 2 )
        coeff = numpy.array( [+1.0, 0.0, 1.0 ] )
        self.assertAlmostEqual( first = evaluateSolutionAt( x = -1.0, coeff = coeff, node_coords = node_coords, ien_array = ien_array, eval_basis = basis.evalLagrangeBasis1D ), second = +1.0 )
        self.assertAlmostEqual( first = evaluateSolutionAt( x =  0.0, coeff = coeff, node_coords = node_coords, ien_array = ien_array, eval_basis = basis.evalLagrangeBasis1D ), second =  0.0 )
        self.assertAlmostEqual( first = evaluateSolutionAt( x = +1.0, coeff = coeff, node_coords = node_coords, ien_array = ien_array, eval_basis = basis.evalLagrangeBasis1D ), second = +1.0 )
    
    def test_two_quadratic_elements( self ):
        node_coords, ien_array = mesh.generateMesh( -2, 2, 2, 2 )
        coeff = numpy.array( [ 1.0, 0.25, 0.5, 0.25, 1.0 ] )
        self.assertAlmostEqual( first = evaluateSolutionAt( x = -2.0, coeff = coeff, node_coords = node_coords, ien_array = ien_array, eval_basis = basis.evalLagrangeBasis1D ), second = +1.00 )
        self.assertAlmostEqual( first = evaluateSolutionAt( x = -1.0, coeff = coeff, node_coords = node_coords, ien_array = ien_array, eval_basis = basis.evalLagrangeBasis1D ), second = +0.25 )
        self.assertAlmostEqual( first = evaluateSolutionAt( x =  0.0, coeff = coeff, node_coords = node_coords, ien_array = ien_array, eval_basis = basis.evalLagrangeBasis1D ), second = +0.50 )
        self.assertAlmostEqual( first = evaluateSolutionAt( x = +1.0, coeff = coeff, node_coords = node_coords, ien_array = ien_array, eval_basis = basis.evalLagrangeBasis1D ), second = +0.25 )
        self.assertAlmostEqual( first = evaluateSolutionAt( x = +2.0, coeff = coeff, node_coords = node_coords, ien_array = ien_array, eval_basis = basis.evalLagrangeBasis1D ), second = +1.00 )
        
unittest.main()