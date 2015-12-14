# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer/preview.ui'
#
# Created: Sun Mar 30 10:19:29 2014
#      by: PyQt4 UI code generator 4.10.3
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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(335, 282)
        self.verticalLayout_3 = QtGui.QVBoxLayout(Form)
        self.verticalLayout_3.setMargin(0)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.groupBox = QtGui.QGroupBox(Form)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.frontPrevBox = QtGui.QVBoxLayout(self.groupBox)
        self.frontPrevBox.setMargin(0)
        self.frontPrevBox.setObjectName(_fromUtf8("frontPrevBox"))
        self.verticalLayout_3.addWidget(self.groupBox)
        self.groupBox_2 = QtGui.QGroupBox(Form)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.backPrevBox = QtGui.QVBoxLayout(self.groupBox_2)
        self.backPrevBox.setMargin(0)
        self.backPrevBox.setObjectName(_fromUtf8("backPrevBox"))
        self.verticalLayout_3.addWidget(self.groupBox_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_("Form"))
        self.groupBox.setTitle(_("Front Preview"))
        self.groupBox_2.setTitle(_("Back Preview"))

