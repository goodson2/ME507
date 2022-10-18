# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 10:14:34 2022

@author: mgood
"""

import numpy
import math
import mesh
import basis
import matplotlib.pyplot as plt

# 3 quadratic Lagrange elements
target_fun = lambda x : math.sin(math.pi*x)
# target_fun = lambda x : math.exp(x)
# target_fun = lambda x : math.erfc(x)
degree = 2
domain = [-1,1]
eval_basis = basis.evalLagrangeBasis1D
num_elems = 3

# Number points based on degree and element number
x = numpy.linspace(-1,1,2*num_elems + 1)

solns = []

for i in range(0,len(x)):
    xx = x[i]
    coeff, node_coords, ien_array = mesh.computeSolution(target_fun, domain, num_elems, degree)
    sol_at_point = mesh.evaluateSolutionAt(xx, coeff, node_coords, ien_array, eval_basis)
    solns.append(sol_at_point)

xElem1 = numpy.linspace(node_coords[0],node_coords[2],100)
xElem2 = numpy.linspace(node_coords[2],node_coords[4],100)
xElem3 = numpy.linspace(node_coords[4],node_coords[6],100)
xElem0 = numpy.linspace(-1.0,1.0,100)
val0 = numpy.zeros(len(xElem1))
lBasis1 = numpy.zeros(len(xElem1))
lBasis2 = numpy.zeros(len(xElem1))
val1 = numpy.zeros(len(xElem1))
lBasis3 = numpy.zeros(len(xElem1))
lBasis4 = numpy.zeros(len(xElem1))
val2 = numpy.zeros(len(xElem1))
lBasis5 = numpy.zeros(len(xElem1))
lBasis6 = numpy.zeros(len(xElem1))
for i in range(0,len(xElem1)):
    val0[i] = coeff[0]*basis.evalLagrangeBasis1D(xElem0[i], degree, 0)
    lBasis1[i] = coeff[1]*basis.evalLagrangeBasis1D(xElem0[i], degree, 1)
    lBasis2[i] = coeff[2]*basis.evalLagrangeBasis1D(xElem0[i], degree, 2)
    val1[i] = coeff[2]*basis.evalLagrangeBasis1D(xElem0[i], degree, 0)
    lBasis3[i] = coeff[3]*basis.evalLagrangeBasis1D(xElem0[i], degree, 1)
    lBasis4[i] = coeff[4]*basis.evalLagrangeBasis1D(xElem0[i], degree, 2)
    val2[i] = coeff[4]*basis.evalLagrangeBasis1D(xElem0[i], degree, 0)
    lBasis5[i] = coeff[5]*basis.evalLagrangeBasis1D(xElem0[i], degree, 1)
    lBasis6[i] = coeff[6]*basis.evalLagrangeBasis1D(xElem0[i], degree, 2)


    
plt.figure(0)
plt.plot(x, solns, 'ok', label = 'sin(pi*x)')
# plt.plot(x, solns, 'ok', label = 'exp(x)')
# plt.plot(x, solns, 'ok', label = 'erfc(x)')
x1 = numpy.linspace(-1,1,100)
y1 = numpy.sin(numpy.pi*x1)
# y1 = numpy.exp(x1)
# y1 = numpy.zeros(len(x1))
# for i in range(0,len(x1)):
    # y1[i] = math.erfc(x1[i])
plt.plot(x1, y1, '-r')
plt.plot(xElem1,val0)
plt.plot(xElem1,lBasis1)
plt.plot(xElem1,lBasis2)
plt.plot(xElem2,val1)
plt.plot(xElem2,lBasis3)
plt.plot(xElem2,lBasis4)
plt.plot(xElem3,val2)
plt.plot(xElem3,lBasis5)
plt.plot(xElem3,lBasis6)
for i in range(0, len(node_coords)+1, 2):
    plt.axvline(x[i], color = 'k', linestyle = '--')
# matplotlib.pyplot.axvline(x, color, xmin, xmax, linestyle)
plt.plot()
plt.xlim(-1, 1)
plt.ylim(-1, 1)
# plt.ylim(-1,3)
# plt.ylim(-0.5,2)
plt.legend(loc="upper left")
plt.xlabel('x')
plt.ylabel('f(x)')
plt.savefig('fig_q56', dpi=325)
