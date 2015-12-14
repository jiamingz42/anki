# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer/browseropts.ui'
#
# Created: Sun Mar 30 10:19:28 2014
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(288, 195)
        self.verticalLayout = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.fontCombo = QtGui.QFontComboBox(Dialog)
        self.fontCombo.setObjectName(_fromUtf8("fontCombo"))
        self.horizontalLayout.addWidget(self.fontCombo)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.fontSize = QtGui.QSpinBox(Dialog)
        self.fontSize.setMinimumSize(QtCore.QSize(75, 0))
        self.fontSize.setObjectName(_fromUtf8("fontSize"))
        self.gridLayout.addWidget(self.fontSize, 0, 1, 1, 1)
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.lineSize = QtGui.QSpinBox(Dialog)
        self.lineSize.setObjectName(_fromUtf8("lineSize"))
        self.gridLayout.addWidget(self.lineSize, 1, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.fullSearch = QtGui.QCheckBox(Dialog)
        self.fullSearch.setObjectName(_fromUtf8("fullSearch"))
        self.verticalLayout.addWidget(self.fullSearch)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.fontCombo, self.fontSize)
        Dialog.setTabOrder(self.fontSize, self.lineSize)
        Dialog.setTabOrder(self.lineSize, self.fullSearch)
        Dialog.setTabOrder(self.fullSearch, self.buttonBox)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_("Browser Options"))
        self.label.setText(_("<b>Font</b>:"))
        self.label_2.setText(_("<b>Font Size</b>:"))
        self.label_3.setText(_("<b>Line Size</b>:"))
        self.fullSearch.setText(_("Search within formatting (slow)"))

