#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtCore, QtGui
from gui import Ui_MainWindow
from about import Ui_FormAbout
from licencia import Ui_FormLicencia
from info import Ui_FormInfo
from raices import Biseccion, ReglaFalsa, NewtonRaphson
from matrices import diagonalFuerte, Jacobi, GaussSeidel
from integrales import Riemann, Trapecios, Simpson
from diferenciales import Euler, RK4

class principal(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        
        self.ventana = Ui_MainWindow()
        self.ventana.setupUi(self)
        self.center()
        
        self.connect(self.ventana.btnAcerca, QtCore.SIGNAL('clicked()'), self.acerca)
        self.connect(self.ventana.btnRaices, QtCore.SIGNAL('clicked()'), self.roots)
        self.connect(self.ventana.btnMatriz, QtCore.SIGNAL('clicked()'), self.matrix)
        self.connect(self.ventana.btnIntegral, QtCore.SIGNAL('clicked()'), self.integral)
        self.connect(self.ventana.btnEcuaciones, QtCore.SIGNAL('clicked()'), self.ecuations)
        
        self.connect(self.ventana.metodosRaices, QtCore.SIGNAL('currentIndexChanged(int)'), self.checkRoots)
    
    def center(self):
        screen = QtGui.QDesktopWidget().screenGeometry()
        mysize = self.geometry()
        hpos = ( screen.width() - mysize.width() ) / 2
        vpos = ( screen.height() - mysize.height() ) / 2
        self.move(hpos,vpos)

    def checkRoots(self):

        combo = self.ventana.metodosRaices
                
        if combo.currentIndex() > 1:
            self.ventana.raicesA.setEnabled(False)
            self.ventana.raicesB.setEnabled(False)
            self.ventana.raicesX.setEnabled(True)
        else:
            self.ventana.raicesA.setEnabled(True)
            self.ventana.raicesB.setEnabled(True)
            self.ventana.raicesX.setEnabled(False)
            
    def roots(self):
        ventana = self.ventana
        
        if ventana.metodosRaices.currentIndex() == 0:
            ecuacion = str(ventana.editRaices.text())
            valorA = float(ventana.raicesA.text())
            valorB = float(ventana.raicesB.text())
            iteraciones = ventana.raicesItera.value()
            tolerancia = float(ventana.raicesTolera.currentText())
            
            cadena = Biseccion(ecuacion, valorA, valorB, tolerancia, iteraciones)
            
            if cadena == '0':
                QtGui.QMessageBox.warning(self, u"Método de Bisección", 
                                          u"Al evaluar la función con los valores especificados en los extremos\nA y B no se consiguen valores con signo diferente. Por favor cambia\nel valor de por lo menos un extremo.",
                                          QtGui.QMessageBox.Ok)
            else:
                QtGui.QMessageBox.about(self, u"Método de Bisección",
                                        unicode(cadena))
        elif ventana.metodosRaices.currentIndex() == 1:
            ecuacion = str(ventana.editRaices.text())
            valorA = float(ventana.raicesA.text())
            valorB = float(ventana.raicesB.text())
            iteraciones = ventana.raicesItera.value()
            tolerancia = float(ventana.raicesTolera.currentText())
            
            cadena = ReglaFalsa(ecuacion, valorA, valorB, tolerancia, iteraciones)
            
            if cadena == '0':
                QtGui.QMessageBox.warning(self, u"Método de la Regla Falsa", 
                                          u"Al evaluar la función con los valores especificados en los extremos\nA y B no se consiguen valores con signo diferente. Por favor cambia\nel valor de por lo menos un extremo.",
                                          QtGui.QMessageBox.Ok)
            else:
                QtGui.QMessageBox.about(self, u"Método de la Regla Falsa",
                                        cadena)
        elif ventana.metodosRaices.currentIndex() == 2:
            ecuacion = str(ventana.editRaices.text())
            valorX = float(ventana.raicesX.text())
            iteraciones = ventana.raicesItera.value()
            tolerancia = float(ventana.raicesTolera.currentText())
            
            cadena = NewtonRaphson(ecuacion, valorX, tolerancia, iteraciones)
            
            if cadena == '0':
                QtGui.QMessageBox.warning(self, u"Método de Newton-Raphson", 
                                          u"El valor otorgado a X₀ es uno de los puntos críticos, cambielo por favor.",
                                          QtGui.QMessageBox.Ok)
            else:
                QtGui.QMessageBox.about(self, u"Método de Newton-Raphson",
                                        cadena)
        
    def matrix(self):
        ventana = self.ventana
        
        matriz = [[float(ventana.A11.text()),float(ventana.A12.text()),float(ventana.A13.text()),float(ventana.B1.text())],
                   [float(ventana.A21.text()),float(ventana.A22.text()),float(ventana.A23.text()),float(ventana.B2.text())],
                    [float(ventana.A31.text()),float(ventana.A32.text()),float(ventana.A33.text()),float(ventana.B3.text())]]
                    
        diagonal = diagonalFuerte(matriz)
        if diagonal == '0':
            if ventana.metodosMatriz.currentIndex() == 0:
                iteraciones = ventana.matrizItera.value()
                cadena = Jacobi(matriz, iteraciones)
                QtGui.QMessageBox.about(self, u"Método de Jacobi", unicode(cadena))
            elif ventana.metodosMatriz.currentIndex() == 1:
                iteraciones = ventana.matrizItera.value()
                cadena = GaussSeidel(matriz, iteraciones)
                QtGui.QMessageBox.about(self, u"Método de Gauss-Seidel", unicode(cadena))
        else:
            QtGui.QMessageBox.warning(self, u"Diagonal Fuerte",
                                      u"El sistema de ecuaciones no se encuentra en diagonal fuerte, por favor corrigelo",
                                      QtGui.QMessageBox.Ok)

    def integral(self):
        ventana = self.ventana
        funcion = str(ventana.fxIntegral.text())
        a = float(ventana.aIntegral.text())
        b = float(ventana.bIntegral.text())
        n = ventana.integralItera.value()
        
        if ventana.metodosIntegral.currentIndex() == 0:
            area = Riemann(a,b,n,funcion)
            QtGui.QMessageBox.about(self, u"Sumas de Riemman", unicode(area))
        elif ventana.metodosIntegral.currentIndex() == 1:
            area = Trapecios(a,b,n,funcion)
            QtGui.QMessageBox.about(self, u"Método de Trapecios", unicode(area))
        elif ventana.metodosIntegral.currentIndex() == 2:
            area = Simpson(a,b,n,funcion)
            QtGui.QMessageBox.about(self, u"Simpson ⅓", unicode(area))
            
    def ecuations(self):
        ventana = self.ventana
        eq = str(ventana.yPrima.text())
        x0 = float(ventana.ecuacionesX0.text())
        xn = float(ventana.ecuacionesXn.text())
        y0 = float(ventana.ecuacionesY0.text())
        n = ventana.ecuacionesItera.value()
        
        if ventana.metodosEcuaciones.currentIndex() == 0:
            cadena = Euler(x0,xn,y0,n,eq)
            QtGui.QMessageBox.about(self, u"Método de Euler", unicode(cadena))
        elif ventana.metodosEcuaciones.currentIndex() == 1:
            cadena = RK4(x0,xn,y0,n,eq)
            QtGui.QMessageBox.about(self, u"Método RK-4", unicode(cadena))
        
    def acerca(self):
        self.aboutV = aboutWin()
        self.aboutV.show()
        
class aboutWin(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.aboutW = Ui_FormAbout()
        self.aboutW.setupUi(self)
        self.center()
        
        self.connect(self.aboutW.btnInfo, QtCore.SIGNAL('clicked()'), self.info)
        self.connect(self.aboutW.btnLicencia, QtCore.SIGNAL('clicked()'), self.lic)
        
    def center(self):
        screen = QtGui.QDesktopWidget().screenGeometry()
        mysize = self.geometry()
        hpos = ( screen.width() - mysize.width() ) / 2
        vpos = ( screen.height() - mysize.height() ) / 2
        self.move(hpos,vpos)
        
    def info(self):
        self.infoW = infoWin()
        self.infoW.show()
        
    def lic(self):
        self.coffeware = licenseWin()
        self.coffeware.show()

class infoWin(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.informacion = Ui_FormInfo()
        self.informacion.setupUi(self)
        
class licenseWin(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.licen = Ui_FormLicencia()
        self.licen.setupUi(self)
        
def main():
    app = QtGui.QApplication(sys.argv)
    ventana = principal()
    ventana.show()
    sys.exit(app.exec_())
    
if __name__ == "__main__":
    main()
