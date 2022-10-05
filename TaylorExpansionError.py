# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 09:42:57 2022

@author: Matt Goodson

Notes: This is incomplete code that does not work - Use taylorExpansion.py and 
comment out the top half to run the error component.
"""

import numpy as np
import sympy 
import math
import matplotlib.pyplot as plt

import taylorExpansion as tE

xx = np.arange(-1,1.01,0.01)  
xxx = sympy.Symbol('xxx')
plt.figure(0)  
plt.plot(xx,np.sin(np.pi*xx), "-k", label = "sin(x)")
Order0 = tE.taylorExpansion(sympy.sin(np.pi*xxx),0,0)
Orders0 = np.zeros(len(xx))
for j in range(0,len(xx)):
    Orders0[j] = float(Order0.subs(xxx,xx[j]))
plt.figure(0)
plt.plot(xx, Orders0, "m", label = "Order 0")
Orders = np.zeros((len(xx),4))
colors = ["b","r","g","c"]
for i in range(1,5):
    k = 2*i - 1
    Order = tE.taylorExpansion(sympy.sin(np.pi*xxx),0,k)
    for j in range(0,len(xx)):
        Orders[j,i-1] = float(Order.subs(xxx,xx[j]))
    plt.figure(0)    
    plt.plot(xx, Orders[:,i-1], colors[i-1], label = f"Order {str(k)}")
plt.legend(loc="upper left")
plt.xlim(-1, 1)
#plt.ylim(-3, 3)
plt.xlabel('x')
plt.ylabel('f(x)')