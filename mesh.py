# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 10:36:11 2022

Author: Matt Goodson
Notes: Create this file to be used in question 54
"""
import numpy

def generateMesh(xmin, xmax, num_elems, degree):
    # sort first by degree and then deal with number of elements
    if degree == 1:
        # Create linear elements
        points = num_elems + 1
        node_coords = numpy.linspace(xmin,xmax,points)
        ien_array = []
        for i in range(0,num_elems):
            ien = [i, i+1]
            ien_array.append(ien)
    else:
        # Create higher degree elements
        points = degree*num_elems + 1
        node_coords = numpy.linspace(xmin,xmax,points)
        ien_array = []
        for i in range(0,len(node_coords)-1,degree):
            if degree == 2:
                ien = [i, i+1, i+2]
                ien_array.append(ien)
            elif degree == 3:
                ien = [i, i+1, i+2, i+3]
                ien_array.append(ien)
            elif degree == 4:
                ien = [i, i+1, i+2, i+3, i+4]
                ien_array.append(ien)
            elif degree == 5:
                ien = [i, i+1, i+2, i+3, i+4, i+5]
                ien_array.append(ien)
            elif degree == 6:
                ien = [i, i+1, i+2, i+3, i+4, i+5, i+6]
                ien_array.append(ien)
            elif degree == 7:
                ien = [i, i+1, i+2, i+3, i+4, i+5, i+6, i+7]
                ien_array.append(ien)
            elif degree == 8:
                ien = [i, i+1, i+2, i+3, i+4, i+5, i+6, i+7, i+8]
                ien_array.append(ien)
    ien_array = numpy.asarray(ien_array)
    return node_coords, ien_array

def computeSolution(target_fun, domain, num_elems, degree):
    xmin = domain[0]
    xmax = domain[1]
    solution = []
    node_coords, ien_array = generateMesh(xmin, xmax, num_elems, degree)
    for i in range(0,len(node_coords)):
        solution_temp = target_fun(node_coords[i])
        solution.append(solution_temp)
    solution = numpy.asarray(solution)
    return solution, node_coords, ien_array

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