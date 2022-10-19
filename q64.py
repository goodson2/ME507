# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 10:12:35 2022

Author: Matt Goodson
Notes: Solves question 64 add stuff for 65
"""
import numpy


R1 = numpy.array([[0, 0, 0, 1, -1, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, -3, 3, 3, -3, 0, 0, 0, 0, 0, 0],
      [0, 6, -12, 6, -6, 12, -6, 0, 0, 0, 0, 0]])

R2 = numpy.array([[0, 0, 0, 0, 0, 0, 0, 1, -1, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, -3, 3, 3, -3, 0, 0],
                 [0, 0, 0, 0, 0, 6, -12, 6, -6, 12, -6, 0]])

A = abs(R1)
B = abs(R2)

RB = numpy.vstack((R1,R2))

D = numpy.multiply(R1,R2)

