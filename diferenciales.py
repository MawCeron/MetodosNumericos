#!/usr/bin/env python
# -*- coding: utf-8 -*-

from math import *

def Euler(X0,Xn,Y0,n,eq):
    
    def f(x, y):
        return eval(eq)
        
    Dx = (Xn - X0)/n    
    Xi = X0
    Yi = Y0
    
    cadena = u'''<table cellspacing="10"><tr>
<td align="center"><strong>i</strong></td>
<td align="center"><strong>x_i</strong></td>
<td align="center"><strong>y_i</strong></td>
<td align="center"><strong>f(x_i,y_i)</strong></td>
<td align="center"><strong>y_i+1</strong></td></tr>'''
    
    for i in range(n+1):
        Fxy = f(Xi, Yi)
        Yi1 = Yi + (Fxy*Dx)
        
        cadena = cadena + u'''<tr>
<td align="right">%d</td>
<td align="right">%f</td>
<td align="right">%f</td>
<td align="right">%f</td>
<td align="right">%f</td></tr>''' %(i, Xi, Yi, Fxy, Yi1)

        Xi = Xi + Dx
        Yi = Yi1
        
    cadena = cadena + u'</table>'
    
    return cadena
    
def RK4(X0,Xn,Y0,n,eq):
    
    def f(x, y):
        return eval(eq)
        
    Dx = (Xn - X0)/n    
    Xi = X0
    Yi = Y0
    
    cadena = u'''<table cellspacing="10"><tr>
<td align="center"><strong>i</strong></td>
<td align="center"><strong>x_i</strong></td>
<td align="center"><strong>y_i</strong></td>
<td align="center"><strong>f(x_i,y_i)</strong></td>
<td align="center"><strong>k₁</strong></td>
<td align="center"><strong>k₂</strong></td>
<td align="center"><strong>k₃</strong></td>
<td align="center"><strong>k₄</strong></td>
<td align="center"><strong>y_i+1</strong></td></tr>'''
    
    for i in range(n+1):
        Fxy = f(Xi, Yi)
        kU = Fxy * Dx
        kD = f(Xi + (Dx/2), Yi + (kU/2)) * Dx
        kT = f(Xi + (Dx/2), Yi + (kD/2)) * Dx
        kC = f(Xi + Dx, Yi + kT) * Dx
        Yi1 = Yi + ((kU + (2*kD) + (2*kT) + kC)/6)
        
        cadena = cadena + u'''<tr>
<td align="right">%d</td>
<td align="right">%f</td>
<td align="right">%f</td>
<td align="right">%f</td>
<td align="right">%f</td><td align="right">%f</td>
<td align="right">%f</td><td align="right">%f</td>
<td align="right">%f</td></tr>''' %(i, Xi, Yi, Fxy,kU,kD,kT,kC, Yi1)

        Xi = Xi + Dx
        Yi = Yi1
        
    cadena = cadena + u'</table>'
    
    return cadena