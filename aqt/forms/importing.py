# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer/importing.ui'
#
# Created: Mon Sep 22 13:04:12 2014
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

class Ui_ImportDialog(object):
    def setupUi(self, ImportDialog):
        ImportDialog.setObjectName(_fromUtf8("ImportDialog"))
        ImportDialog.resize(553, 466)
        self.vboxlayout = QtGui.QVBoxLayout(ImportDialog)
        self.vboxlayout.setObjectName(_fromUtf8("vboxlayout"))
        self.groupBox = QtGui.QGroupBox(ImportDialog)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.toplayout = QtGui.QVBoxLayout(self.groupBox)
        self.toplayout.setObjectName(_fromUtf8("toplayout"))
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.deckArea = QtGui.QWidget(self.groupBox)
        self.deckArea.setObjectName(_fromUtf8("deckArea"))
        self.gridLayout_2.addWidget(self.deckArea, 0, 3, 1, 1)
        self.modelArea = QtGui.QWidget(self.groupBox)
        self.modelArea.setObjectName(_fromUtf8("modelArea"))
        self.gridLayout_2.addWidget(self.modelArea, 0, 1, 1, 1)
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_2.addWidget(self.label_2, 0, 2, 1, 1)
        self.toplayout.addLayout(self.gridLayout_2)
        self.autoDetect = QtGui.QPushButton(self.groupBox)
        self.autoDetect.setText(_fromUtf8(""))
        self.autoDetect.setObjectName(_fromUtf8("autoDetect"))
        self.toplayout.addWidget(self.autoDetect)
        self.importMode = QtGui.QComboBox(self.groupBox)
        self.importMode.setObjectName(_fromUtf8("importMode"))
        self.importMode.addItem(_fromUtf8(""))
        self.importMode.addItem(_fromUtf8(""))
        self.importMode.addItem(_fromUtf8(""))
        self.toplayout.addWidget(self.importMode)
        self.allowHTML = QtGui.QCheckBox(self.groupBox)
        self.allowHTML.setObjectName(_fromUtf8("allowHTML"))
        self.toplayout.addWidget(self.allowHTML)
        self.vboxlayout.addWidget(self.groupBox)
        self.mappingGroup = QtGui.QGroupBox(ImportDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mappingGroup.sizePolicy().hasHeightForWidth())
        self.mappingGroup.setSizePolicy(sizePolicy)
        self.mappingGroup.setObjectName(_fromUtf8("mappingGroup"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.mappingGroup)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.mappingArea = QtGui.QScrollArea(self.mappingGroup)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mappingArea.sizePolicy().hasHeightForWidth())
        self.mappingArea.setSizePolicy(sizePolicy)
        self.mappingArea.setMinimumSize(QtCore.QSize(400, 150))
        self.mappingArea.setFrameShape(QtGui.QFrame.NoFrame)
        self.mappingArea.setWidgetResizable(True)
        self.mappingArea.setObjectName(_fromUtf8("mappingArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 529, 251))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.mappingArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.mappingArea, 0, 0, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.vboxlayout.addWidget(self.mappingGroup)
        self.buttonBox = QtGui.QDialogButtonBox(ImportDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Close|QtGui.QDialogButtonBox.Help)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.vboxlayout.addWidget(self.buttonBox)

        self.retranslateUi(ImportDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), ImportDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), ImportDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(ImportDialog)

    def retranslateUi(self, ImportDialog):
        ImportDialog.setWindowTitle(_("Import"))
        self.groupBox.setTitle(_("Import options"))
        self.label.setText(_("Type"))
        self.label_2.setText(_("Deck"))
        self.importMode.setItemText(0, _("Update existing notes when first field matches"))
        self.importMode.setItemText(1, _("Ignore lines where first field matches existing note"))
        self.importMode.setItemText(2, _("Import even if existing note has same first field"))
        self.allowHTML.setText(_("Allow HTML in fields"))
        self.mappingGroup.setTitle(_("Field mapping"))

