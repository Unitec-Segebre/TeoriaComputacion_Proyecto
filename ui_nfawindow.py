# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'NFAWindow.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_NFAWindow(object):
    def setupUi(self, NFAWindow):
        NFAWindow.setObjectName("NFAWindow")
        NFAWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(NFAWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setObjectName("graphicsView")
        self.verticalLayout.addWidget(self.graphicsView)
        NFAWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(NFAWindow)
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
        NFAWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(NFAWindow)
        self.statusbar.setObjectName("statusbar")
        NFAWindow.setStatusBar(self.statusbar)
        self.actionSave = QtWidgets.QAction(NFAWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionNew = QtWidgets.QAction(NFAWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionConnect = QtWidgets.QAction(NFAWindow)
        self.actionConnect.setObjectName("actionConnect")
        self.actionDisconnect = QtWidgets.QAction(NFAWindow)
        self.actionDisconnect.setObjectName("actionDisconnect")
        self.actionDelete = QtWidgets.QAction(NFAWindow)
        self.actionDelete.setObjectName("actionDelete")
        self.actionSolve = QtWidgets.QAction(NFAWindow)
        self.actionSolve.setObjectName("actionSolve")
        self.actionChange_Name = QtWidgets.QAction(NFAWindow)
        self.actionChange_Name.setObjectName("actionChange_Name")
        self.actionChange_State = QtWidgets.QAction(NFAWindow)
        self.actionChange_State.setObjectName("actionChange_State")
        self.actionOpen = QtWidgets.QAction(NFAWindow)
        self.actionOpen.setObjectName("actionOpen")
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

        self.retranslateUi(NFAWindow)
        QtCore.QMetaObject.connectSlotsByName(NFAWindow)

    def retranslateUi(self, NFAWindow):
        _translate = QtCore.QCoreApplication.translate
        NFAWindow.setWindowTitle(_translate("NFAWindow", "NFA"))
        self.menuFile.setTitle(_translate("NFAWindow", "File"))
        self.menuNode.setTitle(_translate("NFAWindow", "Node"))
        self.menuEdit.setTitle(_translate("NFAWindow", "Edit"))
        self.menuDFA.setTitle(_translate("NFAWindow", "DFA"))
        self.actionSave.setText(_translate("NFAWindow", "Save"))
        self.actionNew.setText(_translate("NFAWindow", "New"))
        self.actionConnect.setText(_translate("NFAWindow", "Connect"))
        self.actionDisconnect.setText(_translate("NFAWindow", "Disconnect"))
        self.actionDelete.setText(_translate("NFAWindow", "Delete"))
        self.actionSolve.setText(_translate("NFAWindow", "Solve"))
        self.actionChange_Name.setText(_translate("NFAWindow", "Change Name"))
        self.actionChange_State.setText(_translate("NFAWindow", "Change State"))
        self.actionOpen.setText(_translate("NFAWindow", "Open"))

