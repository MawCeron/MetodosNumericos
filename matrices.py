#!/usr/bin/env python
# -*- coding: utf-8 -*-

def diagonalFuerte(matriz):
    
    a = abs(matriz[0][0])
    b = abs(matriz[0][1])
    c = abs(matriz[0][2])
    diag = '1'
    
    if a >= (b+c):
        a = abs(matriz[1][0])
        b = abs(matriz[1][1])
        c = abs(matriz[1][2])
        if b >= (a+c):
            a = abs(matriz[2][0])
            b = abs(matriz[2][1])
            c = abs(matriz[2][2])
            if c >= (a+b):
                diag = '0'
    
    return diag

def Jacobi(matriz,iteraciones):
    
    R = [0,0,0]
       
    for i in range(iteraciones):
        
        x1 = (matriz[0][3] - (matriz[0][1]*R[1]) - (matriz[0][2]*R[2])) / matriz[0][0]
        x2 = (matriz[1][3] - (matriz[1][0]*R[0]) - (matriz[1][2]*R[2])) / matriz[1][1]
        x3 = (matriz[2][3] - (matriz[2][0]*R[0]) - (matriz[2][1]*R[1])) / matriz[2][2]
        
        R = [x1, x2, x3]
        
    cadena = u'''<p>Tras %d iteraciones estos son los valores correspondientes a:</p>
<p><strong>x₁:</strong> %f <strong>x₂:</strong> %f <strong>x₃:</strong> %f</p>''' %(iteraciones,x1,x2,x3)
    
    return cadena
    
def GaussSeidel(matriz, iteraciones):
    
    R = [0,0,0]
    
    for i in range(iteraciones):
        
        R[0] = (matriz[0][3] - (matriz[0][1]*R[1]) - (matriz[0][2]*R[2])) / matriz[0][0]
        R[1] = (matriz[1][3] - (matriz[1][0]*R[0]) - (matriz[1][2]*R[2])) / matriz[1][1]
        R[2] = (matriz[2][3] - (matriz[2][0]*R[0]) - (matriz[2][1]*R[1])) / matriz[2][2]
        
    cadena = u'''<p>Tras %d iteraciones estos son los valores correspondientes a:</p>
<p><strong>x₁:</strong> %f <strong>x₂:</strong> %f <strong>x₃:</strong> %f</p>''' %(iteraciones,R[0],R[1],R[2])
    
    return cadena