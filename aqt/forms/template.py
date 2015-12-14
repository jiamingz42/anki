# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer/template.ui'
#
# Created: Sun Mar 30 10:19:30 2014
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
        Form.resize(470, 569)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.verticalLayout_5 = QtGui.QVBoxLayout(Form)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setMargin(0)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.groupBox = QtGui.QGroupBox(Form)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.tlayout1 = QtGui.QVBoxLayout(self.groupBox)
        self.tlayout1.setSpacing(0)
        self.tlayout1.setMargin(0)
        self.tlayout1.setObjectName(_fromUtf8("tlayout1"))
        self.front = QtGui.QTextEdit(self.groupBox)
        self.front.setObjectName(_fromUtf8("front"))
        self.tlayout1.addWidget(self.front)
        self.horizontalLayout_2.addWidget(self.groupBox)
        self.label1 = QtGui.QLabel(Form)
        self.label1.setText(_fromUtf8(""))
        self.label1.setObjectName(_fromUtf8("label1"))
        self.horizontalLayout_2.addWidget(self.label1)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.groupBox_3 = QtGui.QGroupBox(Form)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.tlayout2 = QtGui.QVBoxLayout(self.groupBox_3)
        self.tlayout2.setSpacing(0)
        self.tlayout2.setMargin(0)
        self.tlayout2.setObjectName(_fromUtf8("tlayout2"))
        self.css = QtGui.QTextEdit(self.groupBox_3)
        self.css.setObjectName(_fromUtf8("css"))
        self.tlayout2.addWidget(self.css)
        self.horizontalLayout.addWidget(self.groupBox_3)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        spacerItem = QtGui.QSpacerItem(1, 15, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        self.verticalLayout_4.addItem(spacerItem)
        self.labelc1 = QtGui.QLabel(Form)
        self.labelc1.setText(_fromUtf8(""))
        self.labelc1.setObjectName(_fromUtf8("labelc1"))
        self.verticalLayout_4.addWidget(self.labelc1)
        spacerItem1 = QtGui.QSpacerItem(1, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem1)
        self.labelc2 = QtGui.QLabel(Form)
        self.labelc2.setText(_fromUtf8(""))
        self.labelc2.setObjectName(_fromUtf8("labelc2"))
        self.verticalLayout_4.addWidget(self.labelc2)
        spacerItem2 = QtGui.QSpacerItem(1, 10, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        self.verticalLayout_4.addItem(spacerItem2)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.verticalLayout_5.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.groupBox_2 = QtGui.QGroupBox(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.tlayout3 = QtGui.QVBoxLayout(self.groupBox_2)
        self.tlayout3.setSpacing(0)
        self.tlayout3.setMargin(0)
        self.tlayout3.setObjectName(_fromUtf8("tlayout3"))
        self.back = QtGui.QTextEdit(self.groupBox_2)
        self.back.setObjectName(_fromUtf8("back"))
        self.tlayout3.addWidget(self.back)
        self.horizontalLayout_3.addWidget(self.groupBox_2)
        self.label2 = QtGui.QLabel(Form)
        self.label2.setText(_fromUtf8(""))
        self.label2.setObjectName(_fromUtf8("label2"))
        self.horizontalLayout_3.addWidget(self.label2)
        self.verticalLayout_5.addLayout(self.horizontalLayout_3)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_("Form"))
        self.groupBox.setTitle(_("Front Template"))
        self.groupBox_3.setTitle(_("Styling"))
        self.groupBox_2.setTitle(_("Back Template"))

import icons_rc
