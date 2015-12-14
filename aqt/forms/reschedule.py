# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer/reschedule.ui'
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
        Dialog.resize(325, 144)
        self.verticalLayout_2 = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.asNew = QtGui.QRadioButton(Dialog)
        self.asNew.setChecked(True)
        self.asNew.setObjectName(_fromUtf8("asNew"))
        self.verticalLayout_2.addWidget(self.asNew)
        self.asRev = QtGui.QRadioButton(Dialog)
        self.asRev.setObjectName(_fromUtf8("asRev"))
        self.verticalLayout_2.addWidget(self.asRev)
        self.rangebox = QtGui.QWidget(Dialog)
        self.rangebox.setEnabled(False)
        self.rangebox.setObjectName(_fromUtf8("rangebox"))
        self.verticalLayout = QtGui.QVBoxLayout(self.rangebox)
        self.verticalLayout.setContentsMargins(20, 0, 0, 0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_3 = QtGui.QLabel(self.rangebox)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 0, 1, 1, 1)
        self.min = QtGui.QSpinBox(self.rangebox)
        self.min.setMaximum(9999)
        self.min.setObjectName(_fromUtf8("min"))
        self.gridLayout.addWidget(self.min, 0, 0, 1, 1)
        self.max = QtGui.QSpinBox(self.rangebox)
        self.max.setMaximum(9999)
        self.max.setObjectName(_fromUtf8("max"))
        self.gridLayout.addWidget(self.max, 0, 2, 1, 1)
        self.label_4 = QtGui.QLabel(self.rangebox)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 0, 3, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 4, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.verticalLayout_2.addWidget(self.rangebox)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout_2.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QObject.connect(self.asRev, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.rangebox.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.asNew, self.asRev)
        Dialog.setTabOrder(self.asRev, self.min)
        Dialog.setTabOrder(self.min, self.max)
        Dialog.setTabOrder(self.max, self.buttonBox)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_("Reschedule"))
        self.asNew.setText(_("Place at end of new card queue"))
        self.asRev.setText(_("Place in review queue with interval between:"))
        self.label_3.setText(_("~"))
        self.label_4.setText(_("days"))

