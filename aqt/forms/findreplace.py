# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer/findreplace.ui'
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
        Dialog.resize(367, 209)
        self.verticalLayout = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.find = QtGui.QLineEdit(Dialog)
        self.find.setObjectName(_fromUtf8("find"))
        self.gridLayout.addWidget(self.find, 0, 1, 1, 1)
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.replace = QtGui.QLineEdit(Dialog)
        self.replace.setObjectName(_fromUtf8("replace"))
        self.gridLayout.addWidget(self.replace, 1, 1, 1, 1)
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.field = QtGui.QComboBox(Dialog)
        self.field.setObjectName(_fromUtf8("field"))
        self.gridLayout.addWidget(self.field, 2, 1, 1, 1)
        self.re = QtGui.QCheckBox(Dialog)
        self.re.setObjectName(_fromUtf8("re"))
        self.gridLayout.addWidget(self.re, 4, 1, 1, 1)
        self.ignoreCase = QtGui.QCheckBox(Dialog)
        self.ignoreCase.setChecked(True)
        self.ignoreCase.setObjectName(_fromUtf8("ignoreCase"))
        self.gridLayout.addWidget(self.ignoreCase, 3, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Help|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.find, self.replace)
        Dialog.setTabOrder(self.replace, self.field)
        Dialog.setTabOrder(self.field, self.ignoreCase)
        Dialog.setTabOrder(self.ignoreCase, self.re)
        Dialog.setTabOrder(self.re, self.buttonBox)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_("Find and Replace"))
        self.label.setText(_("<b>Find</b>:"))
        self.label_2.setText(_("<b>Replace With</b>:"))
        self.label_3.setText(_("<b>In</b>:"))
        self.re.setText(_("Treat input as regular expression"))
        self.ignoreCase.setText(_("Ignore case"))

