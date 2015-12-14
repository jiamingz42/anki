# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer/reposition.ui'
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(272, 229)
        self.verticalLayout = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setText(_fromUtf8(""))
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.start = QtGui.QSpinBox(Dialog)
        self.start.setMinimum(-20000000)
        self.start.setMaximum(200000000)
        self.start.setProperty("value", 0)
        self.start.setObjectName(_fromUtf8("start"))
        self.gridLayout.addWidget(self.start, 0, 1, 1, 1)
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.step = QtGui.QSpinBox(Dialog)
        self.step.setMinimum(1)
        self.step.setMaximum(10000)
        self.step.setObjectName(_fromUtf8("step"))
        self.gridLayout.addWidget(self.step, 1, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.randomize = QtGui.QCheckBox(Dialog)
        self.randomize.setObjectName(_fromUtf8("randomize"))
        self.verticalLayout.addWidget(self.randomize)
        self.shift = QtGui.QCheckBox(Dialog)
        self.shift.setChecked(True)
        self.shift.setObjectName(_fromUtf8("shift"))
        self.verticalLayout.addWidget(self.shift)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.start, self.step)
        Dialog.setTabOrder(self.step, self.randomize)
        Dialog.setTabOrder(self.randomize, self.shift)
        Dialog.setTabOrder(self.shift, self.buttonBox)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_("Reposition New Cards"))
        self.label_2.setText(_("Start position:"))
        self.label_3.setText(_("Step:"))
        self.randomize.setText(_("Randomize order"))
        self.shift.setText(_("Shift position of existing cards"))

