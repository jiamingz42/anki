# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer/changemodel.ui'
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
        Dialog.resize(362, 391)
        self.verticalLayout = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setVerticalSpacing(4)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_6 = QtGui.QLabel(Dialog)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 0, 0, 1, 1)
        self.oldModelLabel = QtGui.QLabel(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.oldModelLabel.sizePolicy().hasHeightForWidth())
        self.oldModelLabel.setSizePolicy(sizePolicy)
        self.oldModelLabel.setText(_fromUtf8(""))
        self.oldModelLabel.setMargin(4)
        self.oldModelLabel.setObjectName(_fromUtf8("oldModelLabel"))
        self.gridLayout.addWidget(self.oldModelLabel, 0, 1, 1, 1)
        self.label = QtGui.QLabel(Dialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.modelChooserWidget = QtGui.QWidget(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.modelChooserWidget.sizePolicy().hasHeightForWidth())
        self.modelChooserWidget.setSizePolicy(sizePolicy)
        self.modelChooserWidget.setObjectName(_fromUtf8("modelChooserWidget"))
        self.gridLayout.addWidget(self.modelChooserWidget, 1, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.tgroup = QtGui.QGroupBox(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tgroup.sizePolicy().hasHeightForWidth())
        self.tgroup.setSizePolicy(sizePolicy)
        self.tgroup.setObjectName(_fromUtf8("tgroup"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.tgroup)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.scrollArea = QtGui.QScrollArea(self.tgroup)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.templateMap = QtGui.QWidget()
        self.templateMap.setGeometry(QtCore.QRect(0, 0, 330, 120))
        self.templateMap.setObjectName(_fromUtf8("templateMap"))
        self.scrollArea.setWidget(self.templateMap)
        self.verticalLayout_2.addWidget(self.scrollArea)
        self.verticalLayout.addWidget(self.tgroup)
        self.fgroup = QtGui.QGroupBox(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fgroup.sizePolicy().hasHeightForWidth())
        self.fgroup.setSizePolicy(sizePolicy)
        self.fgroup.setObjectName(_fromUtf8("fgroup"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.fgroup)
        self.verticalLayout_3.setMargin(0)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.scrollArea_2 = QtGui.QScrollArea(self.fgroup)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea_2.sizePolicy().hasHeightForWidth())
        self.scrollArea_2.setSizePolicy(sizePolicy)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName(_fromUtf8("scrollArea_2"))
        self.fieldMap = QtGui.QWidget()
        self.fieldMap.setGeometry(QtCore.QRect(0, 0, 330, 119))
        self.fieldMap.setObjectName(_fromUtf8("fieldMap"))
        self.scrollArea_2.setWidget(self.fieldMap)
        self.verticalLayout_3.addWidget(self.scrollArea_2)
        self.verticalLayout.addWidget(self.fgroup)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Help|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_("Change Note Type"))
        self.label_6.setText(_("Current note type:"))
        self.label.setText(_("New note type:"))
        self.tgroup.setTitle(_("Cards"))
        self.fgroup.setTitle(_("Fields"))

