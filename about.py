# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'about.ui'
#
# Created: Tue May 28 00:25:45 2013
#      by: PyQt4 UI code generator 4.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_FormAbout(object):
    def setupUi(self, FormAbout):
        FormAbout.setObjectName(_fromUtf8("FormAbout"))
        FormAbout.resize(350, 230)
        FormAbout.setMinimumSize(QtCore.QSize(350, 230))
        FormAbout.setMaximumSize(QtCore.QSize(350, 230))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/Iconos/icons/metodos.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        FormAbout.setWindowIcon(icon)
        self.verticalLayout = QtGui.QVBoxLayout(FormAbout)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label = QtGui.QLabel(FormAbout)
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8(":/Iconos/icons/metodos.png")))
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_2.addWidget(self.label, 0, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 2, 1, 1)
        self.label_2 = QtGui.QLabel(FormAbout)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_2.addWidget(self.label_2, 2, 1, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 0, 0, 1, 1)
        self.label_4 = QtGui.QLabel(FormAbout)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_2.addWidget(self.label_4, 4, 1, 1, 1)
        self.label_3 = QtGui.QLabel(FormAbout)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_2.addWidget(self.label_3, 3, 0, 1, 3)
        self.label_5 = QtGui.QLabel(FormAbout)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setOpenExternalLinks(True)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_2.addWidget(self.label_5, 5, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.btnInfo = QtGui.QPushButton(FormAbout)
        self.btnInfo.setObjectName(_fromUtf8("btnInfo"))
        self.gridLayout.addWidget(self.btnInfo, 0, 0, 1, 1)
        self.btnLicencia = QtGui.QPushButton(FormAbout)
        self.btnLicencia.setObjectName(_fromUtf8("btnLicencia"))
        self.gridLayout.addWidget(self.btnLicencia, 0, 1, 1, 1)
        self.btnCerrar = QtGui.QPushButton(FormAbout)
        self.btnCerrar.setObjectName(_fromUtf8("btnCerrar"))
        self.gridLayout.addWidget(self.btnCerrar, 0, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)

        self.retranslateUi(FormAbout)
        QtCore.QObject.connect(self.btnCerrar, QtCore.SIGNAL(_fromUtf8("clicked()")), FormAbout.close)
        QtCore.QMetaObject.connectSlotsByName(FormAbout)

    def retranslateUi(self, FormAbout):
        FormAbout.setWindowTitle(_translate("FormAbout", "Acerca de Métodos Numéricos", None))
        self.label_2.setText(_translate("FormAbout", "Métodos Numéricos 0.6.2", None))
        self.label_4.setText(_translate("FormAbout", "<html><head/><body><p>Copyright © 2013 Mauricio Cerón Medina</p></body></html>", None))
        self.label_3.setText(_translate("FormAbout", "Permite resolver diversos tipos de problemas a través del uso de Métodos Numéricos", None))
        self.label_5.setText(_translate("FormAbout", "<html><head/><body><p><a href=\"http://www.pinguinolibre.org/\"><span style=\" text-decoration: underline; color:#0000ff;\">http://www.pinguinolibre.org/</span></a></p></body></html>", None))
        self.btnInfo.setText(_translate("FormAbout", "Más Info", None))
        self.btnLicencia.setText(_translate("FormAbout", "Licencia", None))
        self.btnCerrar.setText(_translate("FormAbout", "Cerrar", None))

import metnum_rc
