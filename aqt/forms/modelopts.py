# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer/modelopts.ui'
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
        Dialog.setWindowModality(QtCore.Qt.ApplicationModal)
        Dialog.resize(276, 323)
        Dialog.setWindowTitle(_fromUtf8(""))
        self.verticalLayout_2 = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.qtabwidget = QtGui.QTabWidget(Dialog)
        self.qtabwidget.setObjectName(_fromUtf8("qtabwidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.verticalLayout = QtGui.QVBoxLayout(self.tab)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_6 = QtGui.QLabel(self.tab)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.verticalLayout.addWidget(self.label_6)
        self.latexHeader = QtGui.QTextEdit(self.tab)
        self.latexHeader.setTabChangesFocus(True)
        self.latexHeader.setObjectName(_fromUtf8("latexHeader"))
        self.verticalLayout.addWidget(self.latexHeader)
        self.label_7 = QtGui.QLabel(self.tab)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.verticalLayout.addWidget(self.label_7)
        self.latexFooter = QtGui.QTextEdit(self.tab)
        self.latexFooter.setTabChangesFocus(True)
        self.latexFooter.setObjectName(_fromUtf8("latexFooter"))
        self.verticalLayout.addWidget(self.latexFooter)
        self.qtabwidget.addTab(self.tab, _fromUtf8(""))
        self.verticalLayout_2.addWidget(self.qtabwidget)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Close|QtGui.QDialogButtonBox.Help)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout_2.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        self.qtabwidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.qtabwidget, self.buttonBox)
        Dialog.setTabOrder(self.buttonBox, self.latexHeader)
        Dialog.setTabOrder(self.latexHeader, self.latexFooter)

    def retranslateUi(self, Dialog):
        self.label_6.setText(_("Header"))
        self.label_7.setText(_("Footer"))
        self.qtabwidget.setTabText(self.qtabwidget.indexOf(self.tab), _("LaTeX"))

