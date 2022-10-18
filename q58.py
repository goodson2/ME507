# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 14:11:49 2022

Author: Matt Goodson
Notes: Solves question 58
"""
import numpy
from basis import evaluateBernsteinBasis1D
import matplotlib.pyplot as plt




xElem0 = numpy.linspace(-1,1,100)
xElem1 = numpy.linspace(0,1,100)
xElem2 = numpy.linspace(1,2,100)
xElem3 = numpy.linspace(2,3,100)
xElem4 = numpy.linspace(3,4,100)
val00 = numpy.zeros(len(xElem1))
val01 = numpy.zeros(len(xElem1))
val02 = numpy.zeros(len(xElem1))
val03 = numpy.zeros(len(xElem1))
val04 = numpy.zeros(len(xElem1))
val05 = numpy.zeros(len(xElem1))
val06 = numpy.zeros(len(xElem1))
val07 = numpy.zeros(len(xElem1))
val08 = numpy.zeros(len(xElem1))
val09 = numpy.zeros(len(xElem1))
val10 = numpy.zeros(len(xElem1))
val11 = numpy.zeros(len(xElem1))
val12 = numpy.zeros(len(xElem1))
val13 = numpy.zeros(len(xElem1))
# Up to 13

for i in range(0,len(xElem1)):
    val00[i] = evaluateBernsteinBasis1D(xElem0[i],1,0)
    val01[i] = evaluateBernsteinBasis1D(xElem0[i],1,1)
    val02[i] = evaluateBernsteinBasis1D(xElem0[i],2,0)
    val03[i] = evaluateBernsteinBasis1D(xElem0[i],2,1)
    val04[i] = evaluateBernsteinBasis1D(xElem0[i],2,2)
    val05[i] = evaluateBernsteinBasis1D(xElem0[i],3,0)
    val06[i] = evaluateBernsteinBasis1D(xElem0[i],3,1)
    val07[i] = evaluateBernsteinBasis1D(xElem0[i],3,2)
    val08[i] = evaluateBernsteinBasis1D(xElem0[i],3,3)
    val09[i] = evaluateBernsteinBasis1D(xElem0[i],4,0)
    val10[i] = evaluateBernsteinBasis1D(xElem0[i],4,1)
    val11[i] = evaluateBernsteinBasis1D(xElem0[i],4,2)
    val12[i] = evaluateBernsteinBasis1D(xElem0[i],4,3)
    val13[i] = evaluateBernsteinBasis1D(xElem0[i],4,4)






plt.figure(0)
plt.plot(xElem1,val00)
plt.plot(xElem1,val01)
plt.plot(xElem2,val02)
plt.plot(xElem2,val03)
plt.plot(xElem2,val04)
plt.plot(xElem3,val05)
plt.plot(xElem3,val06)
plt.plot(xElem3,val07)
plt.plot(xElem3,val08)
plt.plot(xElem4,val09)
plt.plot(xElem4,val10)
plt.plot(xElem4,val11)
plt.plot(xElem4,val12)
plt.plot(xElem4,val13)


