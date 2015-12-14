# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer/taglimit.ui'
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(361, 394)
        self.verticalLayout = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.activeCheck = QtGui.QCheckBox(Dialog)
        self.activeCheck.setObjectName(_fromUtf8("activeCheck"))
        self.verticalLayout.addWidget(self.activeCheck)
        self.activeList = QtGui.QListWidget(Dialog)
        self.activeList.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.activeList.sizePolicy().hasHeightForWidth())
        self.activeList.setSizePolicy(sizePolicy)
        self.activeList.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)
        self.activeList.setObjectName(_fromUtf8("activeList"))
        self.verticalLayout.addWidget(self.activeList)
        self.label = QtGui.QLabel(Dialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.inactiveList = QtGui.QListWidget(Dialog)
        self.inactiveList.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.inactiveList.sizePolicy().hasHeightForWidth())
        self.inactiveList.setSizePolicy(sizePolicy)
        self.inactiveList.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)
        self.inactiveList.setObjectName(_fromUtf8("inactiveList"))
        self.verticalLayout.addWidget(self.inactiveList)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QObject.connect(self.activeCheck, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.activeList.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_("Selective Study"))
        self.activeCheck.setText(_("Require one or more of these tags:"))
        self.label.setText(_("Select tags to exclude:"))

