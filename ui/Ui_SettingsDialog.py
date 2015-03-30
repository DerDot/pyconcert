# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SettingsDialog.ui'
#
# Created: Wed Oct 01 13:00:27 2014
#      by: PyQt4 UI code generator 4.11.2
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

class Ui_SettingsDialog(object):
    def setupUi(self, SettingsDialog):
        SettingsDialog.setObjectName(_fromUtf8("SettingsDialog"))
        SettingsDialog.resize(403, 160)
        self.formLayout = QtGui.QFormLayout(SettingsDialog)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.dir_edit = QtGui.QLineEdit(SettingsDialog)
        self.dir_edit.setMaximumSize(QtCore.QSize(300, 16777215))
        self.dir_edit.setObjectName(_fromUtf8("dir_edit"))
        self.horizontalLayout.addWidget(self.dir_edit)
        self.dir_button = QtGui.QPushButton(SettingsDialog)
        self.dir_button.setMaximumSize(QtCore.QSize(50, 16777215))
        self.dir_button.setObjectName(_fromUtf8("dir_button"))
        self.horizontalLayout.addWidget(self.dir_button)
        self.formLayout.setLayout(0, QtGui.QFormLayout.FieldRole, self.horizontalLayout)
        self.label = QtGui.QLabel(SettingsDialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.location_edit = QtGui.QLineEdit(SettingsDialog)
        self.location_edit.setMaximumSize(QtCore.QSize(300, 16777215))
        self.location_edit.setObjectName(_fromUtf8("location_edit"))
        self.horizontalLayout_2.addWidget(self.location_edit)
        self.location_button = QtGui.QPushButton(SettingsDialog)
        self.location_button.setMaximumSize(QtCore.QSize(50, 16777215))
        self.location_button.setObjectName(_fromUtf8("location_button"))
        self.horizontalLayout_2.addWidget(self.location_button)
        self.formLayout.setLayout(2, QtGui.QFormLayout.FieldRole, self.horizontalLayout_2)
        self.label_2 = QtGui.QLabel(SettingsDialog)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.cancel_button = QtGui.QPushButton(SettingsDialog)
        self.cancel_button.setObjectName(_fromUtf8("cancel_button"))
        self.horizontalLayout_3.addWidget(self.cancel_button)
        self.ok_button = QtGui.QPushButton(SettingsDialog)
        self.ok_button.setObjectName(_fromUtf8("ok_button"))
        self.horizontalLayout_3.addWidget(self.ok_button)
        self.formLayout.setLayout(4, QtGui.QFormLayout.FieldRole, self.horizontalLayout_3)
        spacerItem1 = QtGui.QSpacerItem(20, 10000, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.formLayout.setItem(3, QtGui.QFormLayout.FieldRole, spacerItem1)

        self.retranslateUi(SettingsDialog)
        QtCore.QMetaObject.connectSlotsByName(SettingsDialog)

    def retranslateUi(self, SettingsDialog):
        SettingsDialog.setWindowTitle(_translate("SettingsDialog", "Dialog", None))
        self.dir_button.setText(_translate("SettingsDialog", "...", None))
        self.label.setText(_translate("SettingsDialog", "Music directory", None))
        self.location_button.setText(_translate("SettingsDialog", "+", None))
        self.label_2.setText(_translate("SettingsDialog", "Location", None))
        self.cancel_button.setText(_translate("SettingsDialog", "Cancel", None))
        self.ok_button.setText(_translate("SettingsDialog", "OK", None))

