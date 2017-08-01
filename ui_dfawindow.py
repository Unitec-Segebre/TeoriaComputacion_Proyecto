# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DFAWindow.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DFAWindow(object):
    def setupUi(self, DFAWindow):
        DFAWindow.setObjectName("DFAWindow")
        DFAWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(DFAWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setObjectName("graphicsView")
        self.verticalLayout.addWidget(self.graphicsView)
        DFAWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(DFAWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 27))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuNode = QtWidgets.QMenu(self.menubar)
        self.menuNode.setObjectName("menuNode")
        self.menuEdit = QtWidgets.QMenu(self.menuNode)
        self.menuEdit.setObjectName("menuEdit")
        self.menuDFA = QtWidgets.QMenu(self.menubar)
        self.menuDFA.setObjectName("menuDFA")
        DFAWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(DFAWindow)
        self.statusbar.setObjectName("statusbar")
        DFAWindow.setStatusBar(self.statusbar)
        self.actionSave = QtWidgets.QAction(DFAWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionNew = QtWidgets.QAction(DFAWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionConnect = QtWidgets.QAction(DFAWindow)
        self.actionConnect.setObjectName("actionConnect")
        self.actionDisconnect = QtWidgets.QAction(DFAWindow)
        self.actionDisconnect.setObjectName("actionDisconnect")
        self.actionDelete = QtWidgets.QAction(DFAWindow)
        self.actionDelete.setObjectName("actionDelete")
        self.actionSolve = QtWidgets.QAction(DFAWindow)
        self.actionSolve.setObjectName("actionSolve")
        self.actionChange_Name = QtWidgets.QAction(DFAWindow)
        self.actionChange_Name.setObjectName("actionChange_Name")
        self.actionChange_State = QtWidgets.QAction(DFAWindow)
        self.actionChange_State.setObjectName("actionChange_State")
        self.menuFile.addAction(self.actionSave)
        self.menuEdit.addAction(self.actionChange_Name)
        self.menuEdit.addAction(self.actionChange_State)
        self.menuNode.addAction(self.actionNew)
        self.menuNode.addAction(self.actionConnect)
        self.menuNode.addAction(self.menuEdit.menuAction())
        self.menuNode.addAction(self.actionDisconnect)
        self.menuNode.addAction(self.actionDelete)
        self.menuDFA.addAction(self.actionSolve)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuNode.menuAction())
        self.menubar.addAction(self.menuDFA.menuAction())

        self.retranslateUi(DFAWindow)
        QtCore.QMetaObject.connectSlotsByName(DFAWindow)

    def retranslateUi(self, DFAWindow):
        _translate = QtCore.QCoreApplication.translate
        DFAWindow.setWindowTitle(_translate("DFAWindow", "DFA"))
        self.menuFile.setTitle(_translate("DFAWindow", "File"))
        self.menuNode.setTitle(_translate("DFAWindow", "Node"))
        self.menuEdit.setTitle(_translate("DFAWindow", "Edit"))
        self.menuDFA.setTitle(_translate("DFAWindow", "DFA"))
        self.actionSave.setText(_translate("DFAWindow", "Save"))
        self.actionNew.setText(_translate("DFAWindow", "New"))
        self.actionConnect.setText(_translate("DFAWindow", "Connect"))
        self.actionDisconnect.setText(_translate("DFAWindow", "Disconnect"))
        self.actionDelete.setText(_translate("DFAWindow", "Delete"))
        self.actionSolve.setText(_translate("DFAWindow", "Solve"))
        self.actionChange_Name.setText(_translate("DFAWindow", "Change Name"))
        self.actionChange_State.setText(_translate("DFAWindow", "Change State"))

