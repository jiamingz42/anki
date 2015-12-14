# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer/browserdisp.ui'
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
        Dialog.resize(412, 241)
        self.verticalLayout = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.qfmt = QtGui.QLineEdit(Dialog)
        self.qfmt.setObjectName(_fromUtf8("qfmt"))
        self.verticalLayout.addWidget(self.qfmt)
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.afmt = QtGui.QLineEdit(Dialog)
        self.afmt.setObjectName(_fromUtf8("afmt"))
        self.verticalLayout.addWidget(self.afmt)
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout.addWidget(self.label_3)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.font = QtGui.QFontComboBox(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.font.sizePolicy().hasHeightForWidth())
        self.font.setSizePolicy(sizePolicy)
        self.font.setObjectName(_fromUtf8("font"))
        self.horizontalLayout.addWidget(self.font)
        self.fontSize = QtGui.QSpinBox(Dialog)
        self.fontSize.setMinimum(6)
        self.fontSize.setObjectName(_fromUtf8("fontSize"))
        self.horizontalLayout.addWidget(self.fontSize)
        self.verticalLayout.addLayout(self.horizontalLayout)
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
        Dialog.setTabOrder(self.qfmt, self.afmt)
        Dialog.setTabOrder(self.afmt, self.font)
        Dialog.setTabOrder(self.font, self.fontSize)
        Dialog.setTabOrder(self.fontSize, self.buttonBox)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_("Browser Appearance"))
        self.label.setText(_("Override front template:"))
        self.label_2.setText(_("Override back template:"))
        self.label_3.setText(_("Override font:"))

