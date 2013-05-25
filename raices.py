#!/usr/bin/env python
# -*- coding: utf-8 -*-

from math import *

def Biseccion(ecuacion, aValor, bValor, tolerancia, iteraciones):
    
    def f(x):
        return eval(ecuacion)
    
    fa = f(aValor)
    fb = f(bValor)
    
    if ((fa*fb) > 0):
        cadena = '0'
    else:
        cadena = u'<table cellspacing="10"><tr><td align="center"><strong>a</strong></td><td align="center"><strong>b</strong></td><td align="center"><strong>f(a)</strong></td><td align="center"><strong>f(b)</strong></td><td align="center"><strong>c</strong></td><td align="center"><strong>f(c)</strong></td></tr>'
        i = 0
        
        while i <= iteraciones:
            cValor = (aValor + bValor)/2
            fc = f(cValor)
            cadena = cadena + u'<tr><td align="right">%.4f</td><td align="right">%.4f</td><td align="right">%.4f</td><td align="right">%.4f</td><td align="right">%.8f</td><td align="right">%.4f</td></tr>' %(aValor, bValor, fa, fb, cValor, fc)
            
            if (fc == 0.0) or abs(fc) < tolerancia:
                cadena = cadena + u'</table> <p>La última raíz encontrada es: <strong>%.8f' %(cValor) + '</strong> con ' + str(i) + ' iteraciones</p>'
                break
            
            i = i + 1
            
            if ((fa*fc) < 0):
                fb = fc
                bValor = cValor
            else:
                fa = fc
                aValor = cValor
            
            if (i > iteraciones):
                cadena = cadena + u'</table> <p>La última raíz encontrada es: <strong>%.8f' %(cValor) + '</strong> con ' + str(i-1) + ' iteraciones</p>'
                break
    
    return cadena
                    
def ReglaFalsa(ecuacion, aValor, bValor, tolerancia, iteraciones):
    
    def f(x):
        return eval(ecuacion)
    
    fa = f(aValor)
    fb = f(bValor)
    
    if ((fa*fb)>0):
        cadena = '0'
    else:
        cadena = u'<table cellspacing="10"><tr><td align="center"><strong>a</strong></td><td align="center"><strong>b</strong></td><td align="center"><strong>f(a)</strong></td><td align="center"><strong>f(b)</strong></td><td align="center"><strong>c</strong></td><td align="center"><strong>f(c)</strong></td></tr>'
        i = 0
        
        while i <= iteraciones:
            cValor = ((aValor*fb) - (bValor*fa))/(fb-fa)
            fc = f(cValor)
            cadena = cadena + u'<tr><td align="right">%.4f</td><td align="right">%.4f</td><td align="right">%.4f</td><td align="right">%.4f</td><td align="right">%.8f</td><td align="right">%.4f</td></tr>' %(aValor, bValor, fa, fb, cValor, fc)
            
            if (fc == 0.0) or abs(fc) < tolerancia:
                cadena = cadena + u'</table> <p>La última raíz encontrada es: <strong>%.8f' %(cValor) + '</strong> con ' + str(i) + ' iteraciones</p>'
                break
            
            i = i + 1
            
            if ((fa*fc) < 0):
                fb = fc
                bValor = cValor
            else:
                fa = fc
                aValor = cValor
            
            if (i > iteraciones):
                cadena = cadena + u'</table> <p>La última raíz encontrada es: <strong>%.8f' %(cValor) + '</strong> con ' + str(i-1) + ' iteraciones</p>'
                break
        
    return cadena


from sympy import Symbol, diff
    
def NewtonRaphson(ecuacion, x0, tolerancia, iteraciones):
    # Derivo ecuacion
    symx = Symbol('x')
    derivada = str(diff(ecuacion, symx))
    
    # Evaluo ecuaciones
    def f(x):
        return eval(ecuacion)
    
    def fp(x):
        return eval(derivada)
        
    fprimax0 = fp(x0)
    
    if (fprimax0 == 0):
        cadena = '0'
    else:
        cadena = u'<table cellspacing="10"><tr><td align="center"><strong>X₀</strong></td><td align="center"><strong>f(X₀)</strong></td><td align="center"><strong>f&#39;(X₀)</strong></td><td align="center"><strong>X₁</strong></td></tr>'
        i = 0
        while i <= iteraciones:
            fx = f(x0)
            fpx = fp(x0)
            x1 = x0 - (fx/fpx)
            cadena = cadena + u'<tr><td align="right">%.8f</td><td align="right">%.8f</td><td align="right">%.8f</td><td align="right">%.8f</td></tr>' %(x0, fx, fpx, x1)
            if (fx == 0.0) or abs(fx) < tolerancia:
                cadena = cadena + u"</table> <p>La raíz buscada es: <strong>%.8f" %(x0) + "</strong> con " + str(i) + "iteraciones.</p>"
                break
            else:
                x0 = x1
                i += 1
            
            if (i > iteraciones):
                cadena = cadena + u"</table> <p>La raíz buscada es: <strong>%.8f" %(x0) + "</strong> con " + str(i) + "iteraciones.</p>"
                break
    
    return cadena