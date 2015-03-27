# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/media/Daten/Crap/Dropbox/pyconcert/ui/MainWindow.ui'
#
# Created: Mon Feb  9 16:26:40 2015
#      by: PyQt4 UI code generator 4.10.4
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.event_tree = QtGui.QTreeWidget(self.centralwidget)
        self.event_tree.setItemsExpandable(False)
        self.event_tree.setObjectName(_fromUtf8("event_tree"))
        self.event_tree.header().setDefaultSectionSize(80)
        self.event_tree.header().setMinimumSectionSize(1)
        self.verticalLayout.addWidget(self.event_tree)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuEdit = QtGui.QMenu(self.menubar)
        self.menuEdit.setObjectName(_fromUtf8("menuEdit"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionSettings = QtGui.QAction(MainWindow)
        self.actionSettings.setObjectName(_fromUtf8("actionSettings"))
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.actionUpdateLibrary = QtGui.QAction(MainWindow)
        self.actionUpdateLibrary.setObjectName(_fromUtf8("actionUpdateLibrary"))
        self.actionUpdateEvents = QtGui.QAction(MainWindow)
        self.actionUpdateEvents.setObjectName(_fromUtf8("actionUpdateEvents"))
        self.actionAddLastFm = QtGui.QAction(MainWindow)
        self.actionAddLastFm.setEnabled(False)
        self.actionAddLastFm.setObjectName(_fromUtf8("actionAddLastFm"))
        self.menuFile.addAction(self.actionExit)
        self.menuEdit.addAction(self.actionSettings)
        self.menuEdit.addAction(self.actionUpdateLibrary)
        self.menuEdit.addAction(self.actionUpdateEvents)
        self.menuEdit.addAction(self.actionAddLastFm)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.event_tree.setSortingEnabled(True)
        self.event_tree.headerItem().setText(0, _translate("MainWindow", "Artist", None))
        self.event_tree.headerItem().setText(1, _translate("MainWindow", "Date", None))
        self.event_tree.headerItem().setText(2, _translate("MainWindow", "Time", None))
        self.event_tree.headerItem().setText(3, _translate("MainWindow", "Location", None))
        self.event_tree.headerItem().setText(4, _translate("MainWindow", "City", None))
        self.event_tree.headerItem().setText(5, _translate("MainWindow", "Country", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit", None))
        self.menuHelp.setTitle(_translate("MainWindow", "Help", None))
        self.actionExit.setText(_translate("MainWindow", "Exit", None))
        self.actionSettings.setText(_translate("MainWindow", "Settings", None))
        self.actionAbout.setText(_translate("MainWindow", "About", None))
        self.actionUpdateLibrary.setText(_translate("MainWindow", "Update Library", None))
        self.actionUpdateEvents.setText(_translate("MainWindow", "Update Events", None))
        self.actionAddLastFm.setText(_translate("MainWindow", "Add to Last.fm", None))

