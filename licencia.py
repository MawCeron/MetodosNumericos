# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'licencia.ui'
#
# Created: Wed May 22 13:42:59 2013
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_FormLicencia(object):
    def setupUi(self, FormLicencia):
        FormLicencia.setObjectName(_fromUtf8("FormLicencia"))
        FormLicencia.resize(400, 253)
        FormLicencia.setMinimumSize(QtCore.QSize(400, 253))
        FormLicencia.setMaximumSize(QtCore.QSize(400, 253))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/Iconos/icons/metodos.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        FormLicencia.setWindowIcon(icon)
        self.verticalLayout = QtGui.QVBoxLayout(FormLicencia)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.textBrowser = QtGui.QTextBrowser(FormLicencia)
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.verticalLayout.addWidget(self.textBrowser)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.btnLicencia = QtGui.QPushButton(FormLicencia)
        self.btnLicencia.setObjectName(_fromUtf8("btnLicencia"))
        self.gridLayout.addWidget(self.btnLicencia, 0, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)

        self.retranslateUi(FormLicencia)
        QtCore.QObject.connect(self.btnLicencia, QtCore.SIGNAL(_fromUtf8("clicked()")), FormLicencia.close)
        QtCore.QMetaObject.connectSlotsByName(FormLicencia)

    def retranslateUi(self, FormLicencia):
        FormLicencia.setWindowTitle(QtGui.QApplication.translate("FormLicencia", "Licencia", None, QtGui.QApplication.UnicodeUTF8))
        self.textBrowser.setHtml(QtGui.QApplication.translate("FormLicencia", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">&quot;LICENCIA DEL CAFÉ&quot;</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; -qt-user-state:0;\">Haz lo que quieras con este programa: Míralo, compártelo, modifícalo, estúdialo... y si algún día nos encontramos y crees que te ha sido útil, invítame a un café, a una cerveza o a algo equivalente. Y si en tu código adaptado del mío quieres poner <span style=\" font-weight:600;\">&quot;Basado en el código original de Mauricio \'Maw\' Cerón - &lt;</span><a href=\"mailto:ceron.maw@gmail.com\"><span style=\" text-decoration: underline; color:#0000ff;\">ceron.maw@gmail.com</span></a><span style=\" font-weight:600;\">&gt;&quot;</span>, te lo agradeceré infinitamente, aunque si no quieres, no lo hagas...</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.btnLicencia.setText(QtGui.QApplication.translate("FormLicencia", "Cerrar", None, QtGui.QApplication.UnicodeUTF8))

import metnum_rc
