# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 27))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuNew = QtWidgets.QMenu(self.menuFile)
        self.menuNew.setObjectName("menuNew")
        self.menuOpen = QtWidgets.QMenu(self.menuFile)
        self.menuOpen.setObjectName("menuOpen")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionDFA = QtWidgets.QAction(MainWindow)
        self.actionDFA.setObjectName("actionDFA")
        self.actionNFA = QtWidgets.QAction(MainWindow)
        self.actionNFA.setObjectName("actionNFA")
        self.actionDFA_2 = QtWidgets.QAction(MainWindow)
        self.actionDFA_2.setObjectName("actionDFA_2")
        self.actionNFA_2 = QtWidgets.QAction(MainWindow)
        self.actionNFA_2.setObjectName("actionNFA_2")
        self.menuNew.addAction(self.actionDFA)
        self.menuNew.addAction(self.actionNFA)
        self.menuOpen.addAction(self.actionDFA_2)
        self.menuOpen.addAction(self.actionNFA_2)
        self.menuFile.addAction(self.menuNew.menuAction())
        self.menuFile.addAction(self.menuOpen.menuAction())
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuNew.setTitle(_translate("MainWindow", "New"))
        self.menuOpen.setTitle(_translate("MainWindow", "Open"))
        self.actionDFA.setText(_translate("MainWindow", "DFA"))
        self.actionNFA.setText(_translate("MainWindow", "NFA"))
        self.actionDFA_2.setText(_translate("MainWindow", "DFA"))
        self.actionNFA_2.setText(_translate("MainWindow", "NFA"))

