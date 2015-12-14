# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer/addfield.ui'
#
# Created: Sun Mar 30 10:19:27 2014
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
        Dialog.resize(434, 186)
        self.horizontalLayout = QtGui.QHBoxLayout(Dialog)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.radioQ = QtGui.QRadioButton(Dialog)
        self.radioQ.setChecked(True)
        self.radioQ.setObjectName(_fromUtf8("radioQ"))
        self.gridLayout.addWidget(self.radioQ, 3, 1, 1, 1)
        self.size = QtGui.QSpinBox(Dialog)
        self.size.setMinimum(6)
        self.size.setMaximum(200)
        self.size.setObjectName(_fromUtf8("size"))
        self.gridLayout.addWidget(self.size, 2, 1, 1, 1)
        self.label = QtGui.QLabel(Dialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.font = QtGui.QFontComboBox(Dialog)
        self.font.setObjectName(_fromUtf8("font"))
        self.gridLayout.addWidget(self.font, 1, 1, 1, 1)
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.fields = QtGui.QComboBox(Dialog)
        self.fields.setObjectName(_fromUtf8("fields"))
        self.gridLayout.addWidget(self.fields, 0, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 5, 1, 1, 1)
        self.radioA = QtGui.QRadioButton(Dialog)
        self.radioA.setObjectName(_fromUtf8("radioA"))
        self.gridLayout.addWidget(self.radioA, 4, 1, 1, 1)
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Vertical)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.horizontalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.fields, self.font)
        Dialog.setTabOrder(self.font, self.size)
        Dialog.setTabOrder(self.size, self.radioQ)
        Dialog.setTabOrder(self.radioQ, self.radioA)
        Dialog.setTabOrder(self.radioA, self.buttonBox)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_("Add Field"))
        self.radioQ.setText(_("Front"))
        self.label.setText(_("Field:"))
        self.label_2.setText(_("Font:"))
        self.label_3.setText(_("Size:"))
        self.radioA.setText(_("Back"))
        self.label_4.setText(_("Add to:"))

