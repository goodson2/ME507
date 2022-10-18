# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 14:02:23 2022

Author: Matt Goodson
Notes: Solves problem 55
"""
import scipy
from scipy import integrate
import numpy
import mesh
import basis
import math
import matplotlib.pyplot as plt

def computeFitError( target_fun, coeff, node_coords, ien_array, eval_basis ):
    num_elems = ien_array.shape[0]
    domain = [ min( node_coords ), max( node_coords ) ]
    abs_err_fun = lambda x : abs( target_fun( x ) - evaluateSolutionAt( x, coeff, node_coords, ien_array, eval_basis ) )
    fit_error, residual = scipy.integrate.quad( abs_err_fun, domain[0], domain[-1], epsrel = 1e-12, limit = num_elems * 100 )
    return fit_error, residual

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

# Comment the section of code I want to run for the various different tests:
    # h-refinement: Linear elements approximating f(x) = x^2, domanin x = [0.0, 1.0]
# Problem setup:
target_fun = lambda x : x**2
xmin = 0
xmax = 1
domain = [xmin, xmax]
degree = 1
eval_basis = basis.evalLagrangeBasis1D
# Setup the variable that will be changing
elems_array = []
error_array = []
n = 2 ** numpy.array(range(0,10))
for i in range(0,len(n)):
    num_elems = int(n[i])
    elems_array.append(num_elems)
    coeff, node_coords, ien_array = mesh.computeSolution(target_fun,domain,num_elems,degree)
    fit_error, residual = computeFitError(target_fun, coeff, node_coords, ien_array, eval_basis)
    error_array.append(fit_error)
elems_array = numpy.asarray(elems_array)
node_array = elems_array + 1
error_array = numpy.asarray(error_array)
# Plot portion
plt.figure(0)
plt.plot(elems_array, error_array, '--or', label = 'x^2 deg = 1 [0,1]')
plt.xlim(1, 1000)
plt.ylim(1e-11, 10)
plt.legend(loc="upper right")
plt.yscale('log')
plt.xscale('log')
plt.xlabel('Number of Elements')
plt.ylabel('|Error|')
plt.savefig('fig_0', dpi=325)
plt.figure(1)
plt.plot(node_array, error_array, '--or', label = 'x^2 deg = 1 [0,1]')
plt.xlim(1, 1000)
plt.ylim(1e-11, 10)
plt.legend(loc="upper right")
plt.yscale('log')
plt.xscale('log')
plt.xlabel('Number of Nodes')
plt.ylabel('|Error|')
plt.savefig('fig_0', dpi=325)

# Repeat the above process to do all these different cases
    # h-refinement: Quadratic elements approximating f(x) = x^3, domain x = [0.0, 1.0]
target_fun = lambda x : x**3
xmin = 0
xmax = 1
domain = [xmin, xmax]
degree = 2
eval_basis = basis.evalLagrangeBasis1D
# Setup the variable that will be changing
elems_array = []
error_array = []
n = 2 ** numpy.array(range(0,10))
for i in range(0,len(n)):
    num_elems = int(n[i])
    elems_array.append(num_elems)
    coeff, node_coords, ien_array = mesh.computeSolution(target_fun,domain,num_elems,degree)
    fit_error, residual = computeFitError(target_fun, coeff, node_coords, ien_array, eval_basis)
    error_array.append(fit_error)
elems_array = numpy.asarray(elems_array)
node_array = elems_array + 1
error_array = numpy.asarray(error_array)
# Plot portion
plt.figure(2)
plt.plot(elems_array, error_array, '--or', label = 'x^3 deg = 2 [0,1]')
plt.xlim(1, 1000)
plt.ylim(1e-11, 10)
plt.legend(loc="upper right")
plt.yscale('log')
plt.xscale('log')
plt.xlabel('Number of Elements')
plt.ylabel('|Error|')
plt.savefig('fig_0', dpi=325)
plt.figure(3)
plt.plot(node_array, error_array, '--or', label = 'x^3 deg = 2 [0,1]')
plt.xlim(1, 1000)
plt.ylim(1e-11, 10)
plt.legend(loc="upper right")
plt.yscale('log')
plt.xscale('log')
plt.xlabel('Number of Nodes')
plt.ylabel('|Error|')
plt.savefig('fig_0', dpi=325)

    # h-refinement: Linear elements approximating f(x) = sin(pi*x), domain x = [-1.0, 1.0]
target_fun = lambda x : math.sin(math.pi*x)
xmin = -1
xmax = 1
domain = [xmin, xmax]
degree = 1
eval_basis = basis.evalLagrangeBasis1D
# Setup the variable that will be changing
elems_array = []
error_array = []
n = 2 ** numpy.array(range(0,10))
for i in range(0,len(n)):
    num_elems = int(n[i])
    elems_array.append(num_elems)
    coeff, node_coords, ien_array = mesh.computeSolution(target_fun,domain,num_elems,degree)
    fit_error, residual = computeFitError(target_fun, coeff, node_coords, ien_array, eval_basis)
    error_array.append(fit_error)
elems_array = numpy.asarray(elems_array)
node_array = elems_array + 1
error_array = numpy.asarray(error_array)
# Plot portion
plt.figure(4)
plt.plot(elems_array, error_array, '--or', label = 'sin(pi*x) deg = 1 [-1,1]')
plt.xlim(1, 1000)
plt.ylim(1e-11, 10)
plt.legend(loc="upper right")
plt.yscale('log')
plt.xscale('log')
plt.xlabel('Number of Elements')
plt.ylabel('|Error|')
plt.savefig('fig_0', dpi=325)
plt.figure(5)
plt.plot(node_array, error_array, '--or', label = 'sin(pi*x) deg = 1 [-1,1]')
plt.xlim(1, 1000)
plt.ylim(1e-11, 10)
plt.legend(loc="upper right")
plt.yscale('log')
plt.xscale('log')
plt.xlabel('Number of Nodes')
plt.ylabel('|Error|')
plt.savefig('fig_0', dpi=325)



    # h-refinement: Quadratic elements approximating f(x) = sin(pi*x), domain x = [-1.0, 1.0]
target_fun = lambda x : math.sin(math.pi*x)
xmin = -1
xmax = 1
domain = [xmin, xmax]
degree = 2
eval_basis = basis.evalLagrangeBasis1D
# Setup the variable that will be changing
elems_array = []
error_array = []
n = 2 ** numpy.array(range(0,10))
for i in range(0,len(n)):
    num_elems = int(n[i])
    elems_array.append(num_elems)
    coeff, node_coords, ien_array = mesh.computeSolution(target_fun,domain,num_elems,degree)
    fit_error, residual = computeFitError(target_fun, coeff, node_coords, ien_array, eval_basis)
    error_array.append(fit_error)
elems_array = numpy.asarray(elems_array)
node_array = elems_array + 1
error_array = numpy.asarray(error_array)
# Plot portion
plt.figure(6)
plt.plot(elems_array, error_array, '--or', label = 'sin(pi*x) deg = 1 [-1,1]')
plt.xlim(1, 1000)
plt.ylim(1e-11, 10)
plt.legend(loc="upper right")
plt.yscale('log')
plt.xscale('log')
plt.xlabel('Number of Elements')
plt.ylabel('|Error|')
plt.savefig('fig_0', dpi=325)
plt.figure(7)
plt.plot(node_array, error_array, '--or', label = 'sin(pi*x) deg = 1 [-1,1]')
plt.xlim(1, 1000)
plt.ylim(1e-11, 10)
plt.legend(loc="upper right")
plt.yscale('log')
plt.xscale('log')
plt.xlabel('Number of Nodes')
plt.ylabel('|Error|')
plt.savefig('fig_0', dpi=325)

    # p-refinement: Two elements approximating f(x) = sin(pi*x), domain x = [-1.0, 1.0]
target_fun = lambda x : math.sin(math.pi*x)
xmin = -1
xmax = 1
domain = [xmin, xmax]
degree = numpy.linspace(1,8,8)
degree = degree.astype(int)
eval_basis = basis.evalLagrangeBasis1D
# Setup the variable that will be changing
elems_array = []
nodes_array = []
error_array = []
num_elems = 2
for i in range(0,len(degree)):
    elems_array.append(num_elems)
    nodes_array.append(num_elems*degree[i]+1)
    coeff, node_coords, ien_array = mesh.computeSolution(target_fun,domain,num_elems,degree[i])
    fit_error, residual = computeFitError(target_fun, coeff, node_coords, ien_array, eval_basis)
    error_array.append(fit_error)
error_array = numpy.asarray(error_array)
elems_array = numpy.asarray(elems_array)
nodes_array = numpy.asarray(nodes_array)
# Plot portion
plt.figure(8)
plt.plot(elems_array, error_array, '--or', label = 'sin(pi*x) deg = 1 [-1,1]')
plt.xlim(1, 1000)
plt.ylim(1e-11, 10)
plt.legend(loc="upper right")
plt.yscale('log')
plt.xscale('log')
plt.xlabel('Number of Elements')
plt.ylabel('|Error|')
plt.savefig('fig_0', dpi=325)
plt.figure(9)
plt.plot(nodes_array, error_array, '--or', label = 'sin(pi*x) deg = 1 [-1,1]')
plt.xlim(1, 1000)
plt.ylim(1e-11, 10)
plt.legend(loc="upper right")
plt.yscale('log')
plt.xscale('log')
plt.xlabel('Number of Nodes')
plt.ylabel('|Error|')
plt.savefig('fig_0', dpi=325)

    # hp-refinement: Approximating f(x) = sin(pi*x), domain x = [-1.0, 1.0] 
    # where number of elements and the polynomial degree of the basis are increasing
target_fun = lambda x : math.sin(math.pi*x)
xmin = -1
xmax = 1
domain = [xmin, xmax]
degree = numpy.linspace(1,6,6)
degree = degree.astype(int)
eval_basis = basis.evalLagrangeBasis1D
# Setup the variable that will be changing
elems_array = []
nodes_array = []
error_array = []
n = 2 ** numpy.array(range(1,7))
for i in range(0,len(degree)):
    num_elems = n[i]
    elems_array.append(num_elems)
    nodes_array.append(num_elems*degree[i]+1)
    coeff, node_coords, ien_array = mesh.computeSolution(target_fun,domain,num_elems,degree[i])
    fit_error, residual = computeFitError(target_fun, coeff, node_coords, ien_array, eval_basis)
    error_array.append(fit_error)
error_array = numpy.asarray(error_array)
elems_array = numpy.asarray(elems_array)
nodes_array = numpy.asarray(nodes_array)
# Plot portion
plt.figure(10)
plt.plot(elems_array, error_array, '--or', label = 'sin(pi*x) deg = 1 [-1,1]')
plt.xlim(1, 1000)
plt.ylim(1e-16, 10)
plt.legend(loc="upper right")
plt.yscale('log')
plt.xscale('log')
plt.xlabel('Number of Elements')
plt.ylabel('|Error|')
plt.savefig('fig_0', dpi=325)
plt.figure(11)
plt.plot(nodes_array, error_array, '--or', label = 'sin(pi*x) deg = 1 [-1,1]')
plt.xlim(1, 1000)
plt.ylim(1e-16, 10)
plt.legend(loc="upper right")
plt.yscale('log')
plt.xscale('log')
plt.xlabel('Number of Nodes')
plt.ylabel('|Error|')
plt.savefig('fig_0', dpi=325)




