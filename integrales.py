#!/usr/bin/env python
# -*- coding: utf-8 -*-

from math import *

def Riemann(a,b,n,funcion):
    
    def f(x):
        return eval(funcion)
        
    deltaX = (b-a)/n
    xi = a
    sumatoria = 0
    for i in range(n):
        fxi = f(xi)
        sumatoria = sumatoria + fxi
        xi = xi + deltaX
    
    areaRiemman = sumatoria * deltaX
    
    area = u"El área obtenida por Sumas de Riemann es: %f" %(areaRiemman)
    return area
    
def Trapecios(a,b,n,funcion):
    
    def f(x):
        return eval(funcion)
        
    deltaX = (b-a)/n
    xi = a + deltaX
    sumatoria = 0
    
    for i in range(1,n):
        fxi = f(xi)
        sumatoria = sumatoria + fxi
        xi = xi + deltaX
        
    fx0 = f(a)
    fxn = f(xi)
    
    areaTrapecios = (fx0 + fxn + (2*sumatoria)) * (deltaX/2)
    
    area = u"El área obtenida por el Método de Trapecios es: %f" %(areaTrapecios)
    return area
    
def Simpson(a,b,n,funcion):
    
    def f(x):
        return eval(funcion)
        
    deltaX = (b-a)/n
    xi = a + deltaX
    sumpar = 0
    sumnon = 0
    
    for i in range(1,n):
        fxi = f(xi)
        if (i % 2 == 0):
            sumpar = sumpar + fxi
        else:
            sumnon = sumnon + fxi
        xi = xi + deltaX
    
    fx0 = f(a)
    fxn = f(xi)
    
    areaSimpson = (fx0 + fxn + (4*sumnon) + (2*sumpar)) * (deltaX/3)
    
    area = u"El área obtenida por Simpson ⅓ es: %f" %(areaSimpson)    
    return area
