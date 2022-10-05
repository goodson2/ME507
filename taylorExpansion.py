# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 09:42:57 2022

@author: Matt Goodson

Notes: Not a core requirement (so rigorous testing has not been implemented)
- Top half of code runs the different taylor expansions for sin, exp, and erfc
- Bottom half computes error of taylor expansions compared to analytical solution
"""

import numpy as np
import sympy 
import math
import matplotlib.pyplot as plt

def taylorExpansion( fun, a, order ):
    x = list( fun.atoms( sympy.Symbol ) )[0]
    t = 0
    for i in range( 0, order + 1 ):
       df = sympy.diff( fun, x, i )
       term = ( df.subs( x, a ) / sympy.factorial( i ) ) * ( x - a )**i
       t += term
    return t
   
# # Section to show the Taylor Expansion of sin(pi*x) about 0 for order[0,1,3,5,7]
# xx = np.arange(-1,1.01,0.01)  
# xxx = sympy.Symbol('xxx')
# plt.figure(0)  
# plt.plot(xx,np.sin(np.pi*xx), "-k", label = "sin(x)")
# Order0 = taylorExpansion(sympy.sin(np.pi*xxx),0,0)
# Orders0 = np.zeros(len(xx))
# for j in range(0,len(xx)):
#     Orders0[j] = float(Order0.subs(xxx,xx[j]))
# plt.figure(0)
# plt.plot(xx, Orders0, "m", label = "Order 0")
# Orders = np.zeros((len(xx),4))
# colors = ["b","r","g","c"]
# for i in range(1,5):
#     k = 2*i - 1
#     Order = taylorExpansion(sympy.sin(np.pi*xxx),0,k)
#     for j in range(0,len(xx)):
#         Orders[j,i-1] = float(Order.subs(xxx,xx[j]))
#     plt.figure(0)    
#     plt.plot(xx, Orders[:,i-1], colors[i-1], label = f"Order {str(k)}")
# plt.legend(loc="upper left")
# plt.xlim(-1, 1)
# #plt.ylim(-3, 3)
# plt.xlabel('x')
# plt.ylabel('f(x)')

# plt.savefig('sine.png', dpi=600)

# # Section to show the Taylor Expansion of exp(x) about 0 for order[0,1,2,3,4]
# xx = np.arange(-1,1.01,0.01)  
# xxx = sympy.Symbol('xxx')
# plt.figure(1)  
# plt.plot(xx,np.exp(xx), "-k", label = "exp(x)")
# Orders = np.zeros((len(xx),5))
# colors = ["m","b","r","g","c"]
# for i in range(0,5):
#     k = i
#     Order = taylorExpansion(sympy.exp(xxx),0,k)
#     for j in range(0,len(xx)):
#         Orders[j,i] = float(Order.subs(xxx,xx[j]))
#     plt.figure(1)    
#     plt.plot(xx, Orders[:,i], colors[i], label = f"Order {str(k)}")
# plt.legend(loc="upper left")
# plt.xlim(-1, 1)
# #plt.ylim(-3, 3)
# plt.xlabel('x')
# plt.ylabel('f(x)')

# plt.savefig('exp_x.png', dpi=600)

# # Section to show the Taylor Expansion of erfc(x) about 0 for order[0,1,3,5,7,9,11]
# xx = np.arange(-2,2.01,0.01)  
# xxx = sympy.Symbol('xxx')
# error_fun = np.zeros(len(xx))
# for i in range(0,len(xx)):
#     error_fun[i] = math.erfc(xx[i])
# plt.figure(2) 
# plt.plot(xx,error_fun, "-k", label = "erfc(x)")
# Order0 = taylorExpansion(sympy.erfc(xxx),0,0)
# Orders0 = np.zeros(len(xx))
# for j in range(0,len(xx)):
#     Orders0[j] = float(Order0.subs(xxx,xx[j]))
# plt.figure(2)
# plt.plot(xx, Orders0, "m", label = "Order 0")
# Orders = np.zeros((len(xx),6))
# colors = ["b","r","g","c","y","m"]
# for i in range(1,7):
#     k = 2*i - 1
#     Order = taylorExpansion(sympy.erfc(xxx),0,k)
#     for j in range(0,len(xx)):
#         Orders[j,i-1] = float(Order.subs(xxx,xx[j]))
#     plt.figure(2)    
#     plt.plot(xx, Orders[:,i-1], colors[i-1], label = f"Order {str(k)}")
# plt.legend(loc="upper left")
# plt.xlim(-2, 2)
# plt.ylim(-1, 3)
# plt.xlabel('x')
# plt.ylabel('f(x)')

# plt.savefig('erfc.png', dpi=600)

# Next problem to look at error between TE and functions
# Error between sin TE and function from [-1,1] at x = 0
xmin = -1
xmax = 1  
xxx = sympy.Symbol('xxx')
orderVal = np.arange(0,7,1)
errVal1 = np.zeros(len(orderVal))
for i in range(0,len(orderVal)):
    Order = taylorExpansion(sympy.sin(np.pi*xxx),0,i)
    sinx = sympy.sin(np.pi*xxx)
    errVal1[i] = float(sympy.integrate(abs(sinx - Order),(xxx,xmin,xmax)))
    
plt.figure(3)    
plt.semilogy(orderVal, errVal1)
plt.xlabel('Order')
plt.ylabel('|Error|')
plt.xlim(0,10)
plt.savefig('sinError.png', dpi=600)

# Error between exp TE and function from [-1,1] at x = 0
xmin = -1
xmax = 1  
xxx = sympy.Symbol('xxx')
orderVal = np.arange(0,7,1)
errVal2 = np.zeros(len(orderVal))
for i in range(0,len(orderVal)):
    Order = taylorExpansion(sympy.exp(xxx),0,i)
    sinx = sympy.exp(xxx)
    errVal2[i] = float(sympy.integrate(abs(sinx - Order),(xxx,xmin,xmax)))
    
plt.figure(4)    
plt.semilogy(orderVal, errVal2)
plt.xlabel('Order')
plt.ylabel('|Error|')
plt.xlim(0,10)
plt.savefig('expError.png', dpi=600)

# # Error between erfc TE and function from [-2,2] at x = 0
# # I NEED TO DO THIS PROBLEM STILL
xmin = -1
xmax = 1  
xxx = sympy.Symbol('xxx')
orderVal = np.arange(0,11,1)
errVal3 = np.zeros(len(orderVal))
for i in range(0,len(orderVal)):
    Order = taylorExpansion(sympy.erfc(xxx),0,i)
    sinx = sympy.erfc(xxx)
    errVal3[i] = float(sympy.integrate(abs(sinx - Order),(xxx,xmin,xmax)))
    
plt.figure(5)    
plt.semilogy(orderVal, errVal3)
plt.xlabel('Order')
plt.ylabel('|Error|')
plt.xlim(0,10)
plt.savefig('erfcError.png', dpi=600)






