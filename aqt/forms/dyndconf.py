# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer/dyndconf.ui'
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
        Dialog.resize(445, 301)
        self.verticalLayout = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.groupBox = QtGui.QGroupBox(Dialog)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout = QtGui.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 1, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.limit = QtGui.QSpinBox(self.groupBox)
        self.limit.setMaximumSize(QtCore.QSize(60, 16777215))
        self.limit.setMinimum(1)
        self.limit.setMaximum(99999)
        self.limit.setObjectName(_fromUtf8("limit"))
        self.gridLayout.addWidget(self.limit, 1, 1, 1, 1)
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 1, 2, 1, 1)
        self.search = QtGui.QLineEdit(self.groupBox)
        self.search.setObjectName(_fromUtf8("search"))
        self.gridLayout.addWidget(self.search, 0, 1, 1, 4)
        self.order = QtGui.QComboBox(self.groupBox)
        self.order.setObjectName(_fromUtf8("order"))
        self.gridLayout.addWidget(self.order, 1, 3, 1, 2)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtGui.QGroupBox(Dialog)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.resched = QtGui.QCheckBox(self.groupBox_2)
        self.resched.setChecked(True)
        self.resched.setObjectName(_fromUtf8("resched"))
        self.gridLayout_2.addWidget(self.resched, 0, 0, 1, 2)
        self.stepsOn = QtGui.QCheckBox(self.groupBox_2)
        self.stepsOn.setObjectName(_fromUtf8("stepsOn"))
        self.gridLayout_2.addWidget(self.stepsOn, 1, 0, 1, 1)
        self.steps = QtGui.QLineEdit(self.groupBox_2)
        self.steps.setEnabled(False)
        self.steps.setObjectName(_fromUtf8("steps"))
        self.gridLayout_2.addWidget(self.steps, 1, 1, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_2)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Help)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QObject.connect(self.stepsOn, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.steps.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.search, self.limit)
        Dialog.setTabOrder(self.limit, self.order)
        Dialog.setTabOrder(self.order, self.resched)
        Dialog.setTabOrder(self.resched, self.stepsOn)
        Dialog.setTabOrder(self.stepsOn, self.steps)
        Dialog.setTabOrder(self.steps, self.buttonBox)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_("Dialog"))
        self.groupBox.setTitle(_("Filter"))
        self.label_5.setText(_("Limit to"))
        self.label_2.setText(_("Search"))
        self.label.setText(_("cards selected by"))
        self.groupBox_2.setTitle(_("Options"))
        self.resched.setText(_("Reschedule cards based on my answers in this deck"))
        self.stepsOn.setText(_("Custom steps (in minutes)"))
        self.steps.setText(_("1 10"))

