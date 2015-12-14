# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer/stats.ui'
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
        Dialog.resize(607, 556)
        self.verticalLayout = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.web = QtWebKit.QWebView(Dialog)
        self.web.setUrl(QtCore.QUrl(_fromUtf8("about:blank")))
        self.web.setObjectName(_fromUtf8("web"))
        self.verticalLayout.addWidget(self.web)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(8)
        self.horizontalLayout_3.setMargin(6)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.groupBox_2 = QtGui.QGroupBox(Dialog)
        self.groupBox_2.setTitle(_fromUtf8(""))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.groups = QtGui.QRadioButton(self.groupBox_2)
        self.groups.setChecked(True)
        self.groups.setObjectName(_fromUtf8("groups"))
        self.horizontalLayout_2.addWidget(self.groups)
        self.all = QtGui.QRadioButton(self.groupBox_2)
        self.all.setObjectName(_fromUtf8("all"))
        self.horizontalLayout_2.addWidget(self.all)
        self.horizontalLayout_3.addWidget(self.groupBox_2)
        self.groupBox = QtGui.QGroupBox(Dialog)
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.month = QtGui.QRadioButton(self.groupBox)
        self.month.setChecked(True)
        self.month.setObjectName(_fromUtf8("month"))
        self.horizontalLayout.addWidget(self.month)
        self.year = QtGui.QRadioButton(self.groupBox)
        self.year.setObjectName(_fromUtf8("year"))
        self.horizontalLayout.addWidget(self.year)
        self.life = QtGui.QRadioButton(self.groupBox)
        self.life.setObjectName(_fromUtf8("life"))
        self.horizontalLayout.addWidget(self.life)
        self.horizontalLayout_3.addWidget(self.groupBox)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Close)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.horizontalLayout_3.addWidget(self.buttonBox)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_("Statistics"))
        self.groups.setText(_("deck"))
        self.all.setText(_("collection"))
        self.month.setText(_("1 month"))
        self.year.setText(_("1 year"))
        self.life.setText(_("deck life"))

from PyQt4 import QtWebKit
