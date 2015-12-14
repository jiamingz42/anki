# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer/exporting.ui'
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

class Ui_ExportDialog(object):
    def setupUi(self, ExportDialog):
        ExportDialog.setObjectName(_fromUtf8("ExportDialog"))
        ExportDialog.resize(295, 202)
        self.vboxlayout = QtGui.QVBoxLayout(ExportDialog)
        self.vboxlayout.setObjectName(_fromUtf8("vboxlayout"))
        self.gridlayout = QtGui.QGridLayout()
        self.gridlayout.setObjectName(_fromUtf8("gridlayout"))
        self.label = QtGui.QLabel(ExportDialog)
        self.label.setMinimumSize(QtCore.QSize(100, 0))
        self.label.setObjectName(_fromUtf8("label"))
        self.gridlayout.addWidget(self.label, 0, 0, 1, 1)
        self.format = QtGui.QComboBox(ExportDialog)
        self.format.setObjectName(_fromUtf8("format"))
        self.gridlayout.addWidget(self.format, 0, 1, 1, 1)
        self.label_2 = QtGui.QLabel(ExportDialog)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridlayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.deck = QtGui.QComboBox(ExportDialog)
        self.deck.setObjectName(_fromUtf8("deck"))
        self.gridlayout.addWidget(self.deck, 1, 1, 1, 1)
        self.vboxlayout.addLayout(self.gridlayout)
        self.vboxlayout1 = QtGui.QVBoxLayout()
        self.vboxlayout1.setObjectName(_fromUtf8("vboxlayout1"))
        self.includeSched = QtGui.QCheckBox(ExportDialog)
        self.includeSched.setChecked(True)
        self.includeSched.setObjectName(_fromUtf8("includeSched"))
        self.vboxlayout1.addWidget(self.includeSched)
        self.includeMedia = QtGui.QCheckBox(ExportDialog)
        self.includeMedia.setChecked(True)
        self.includeMedia.setObjectName(_fromUtf8("includeMedia"))
        self.vboxlayout1.addWidget(self.includeMedia)
        self.includeTags = QtGui.QCheckBox(ExportDialog)
        self.includeTags.setChecked(True)
        self.includeTags.setObjectName(_fromUtf8("includeTags"))
        self.vboxlayout1.addWidget(self.includeTags)
        self.vboxlayout.addLayout(self.vboxlayout1)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.vboxlayout.addItem(spacerItem)
        self.buttonBox = QtGui.QDialogButtonBox(ExportDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.vboxlayout.addWidget(self.buttonBox)

        self.retranslateUi(ExportDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), ExportDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), ExportDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(ExportDialog)
        ExportDialog.setTabOrder(self.format, self.deck)
        ExportDialog.setTabOrder(self.deck, self.includeSched)
        ExportDialog.setTabOrder(self.includeSched, self.includeMedia)
        ExportDialog.setTabOrder(self.includeMedia, self.includeTags)
        ExportDialog.setTabOrder(self.includeTags, self.buttonBox)

    def retranslateUi(self, ExportDialog):
        ExportDialog.setWindowTitle(_("Export"))
        self.label.setText(_("<b>Export format</b>:"))
        self.label_2.setText(_("<b>Include</b>:"))
        self.includeSched.setText(_("Include scheduling information"))
        self.includeMedia.setText(_("Include media"))
        self.includeTags.setText(_("Include tags"))

