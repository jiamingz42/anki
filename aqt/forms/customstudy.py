# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer/customstudy.ui'
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
        Dialog.resize(332, 380)
        self.verticalLayout = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.radio4 = QtGui.QRadioButton(Dialog)
        self.radio4.setObjectName(_fromUtf8("radio4"))
        self.gridLayout.addWidget(self.radio4, 3, 0, 1, 1)
        self.radio3 = QtGui.QRadioButton(Dialog)
        self.radio3.setObjectName(_fromUtf8("radio3"))
        self.gridLayout.addWidget(self.radio3, 2, 0, 1, 1)
        self.radio1 = QtGui.QRadioButton(Dialog)
        self.radio1.setObjectName(_fromUtf8("radio1"))
        self.gridLayout.addWidget(self.radio1, 0, 0, 1, 1)
        self.radio2 = QtGui.QRadioButton(Dialog)
        self.radio2.setObjectName(_fromUtf8("radio2"))
        self.gridLayout.addWidget(self.radio2, 1, 0, 1, 1)
        self.radio6 = QtGui.QRadioButton(Dialog)
        self.radio6.setObjectName(_fromUtf8("radio6"))
        self.gridLayout.addWidget(self.radio6, 5, 0, 1, 1)
        self.radio5 = QtGui.QRadioButton(Dialog)
        self.radio5.setObjectName(_fromUtf8("radio5"))
        self.gridLayout.addWidget(self.radio5, 4, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.groupBox = QtGui.QGroupBox(Dialog)
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.title = QtGui.QLabel(self.groupBox)
        self.title.setObjectName(_fromUtf8("title"))
        self.verticalLayout_2.addWidget(self.title)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.preSpin = QtGui.QLabel(self.groupBox)
        self.preSpin.setObjectName(_fromUtf8("preSpin"))
        self.horizontalLayout.addWidget(self.preSpin)
        self.spin = QtGui.QSpinBox(self.groupBox)
        self.spin.setObjectName(_fromUtf8("spin"))
        self.horizontalLayout.addWidget(self.spin)
        self.postSpin = QtGui.QLabel(self.groupBox)
        self.postSpin.setObjectName(_fromUtf8("postSpin"))
        self.horizontalLayout.addWidget(self.postSpin)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.cardType = QtGui.QListWidget(self.groupBox)
        self.cardType.setObjectName(_fromUtf8("cardType"))
        item = QtGui.QListWidgetItem()
        self.cardType.addItem(item)
        item = QtGui.QListWidgetItem()
        self.cardType.addItem(item)
        item = QtGui.QListWidgetItem()
        self.cardType.addItem(item)
        self.verticalLayout_2.addWidget(self.cardType)
        self.verticalLayout.addWidget(self.groupBox)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        self.cardType.setCurrentRow(0)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.radio1, self.radio2)
        Dialog.setTabOrder(self.radio2, self.radio3)
        Dialog.setTabOrder(self.radio3, self.radio4)
        Dialog.setTabOrder(self.radio4, self.radio6)
        Dialog.setTabOrder(self.radio6, self.spin)
        Dialog.setTabOrder(self.spin, self.buttonBox)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_("Custom Study"))
        self.radio4.setText(_("Review ahead"))
        self.radio3.setText(_("Review forgotten cards"))
        self.radio1.setText(_("Increase today\'s new card limit"))
        self.radio2.setText(_("Increase today\'s review card limit"))
        self.radio6.setText(_("Study by card state or tag"))
        self.radio5.setText(_("Preview new cards"))
        self.title.setText(_("..."))
        self.preSpin.setText(_("..."))
        self.postSpin.setText(_("..."))
        __sortingEnabled = self.cardType.isSortingEnabled()
        self.cardType.setSortingEnabled(False)
        item = self.cardType.item(0)
        item.setText(_("New cards only"))
        item = self.cardType.item(1)
        item.setText(_("Due cards only"))
        item = self.cardType.item(2)
        item.setText(_("All cards in random order (cram mode)"))
        self.cardType.setSortingEnabled(__sortingEnabled)

