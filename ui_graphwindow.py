# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GraphWindow.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_GraphWindow(object):
    def setupUi(self, GraphWindow):
        GraphWindow.setObjectName("GraphWindow")
        GraphWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(GraphWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setObjectName("graphicsView")
        self.verticalLayout.addWidget(self.graphicsView)
        GraphWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(GraphWindow)
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
        GraphWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(GraphWindow)
        self.statusbar.setObjectName("statusbar")
        GraphWindow.setStatusBar(self.statusbar)
        self.actionSave = QtWidgets.QAction(GraphWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionNew = QtWidgets.QAction(GraphWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionConnect = QtWidgets.QAction(GraphWindow)
        self.actionConnect.setObjectName("actionConnect")
        self.actionDisconnect = QtWidgets.QAction(GraphWindow)
        self.actionDisconnect.setObjectName("actionDisconnect")
        self.actionDelete = QtWidgets.QAction(GraphWindow)
        self.actionDelete.setObjectName("actionDelete")
        self.actionSolve = QtWidgets.QAction(GraphWindow)
        self.actionSolve.setObjectName("actionSolve")
        self.actionChange_Name = QtWidgets.QAction(GraphWindow)
        self.actionChange_Name.setObjectName("actionChange_Name")
        self.actionChange_State = QtWidgets.QAction(GraphWindow)
        self.actionChange_State.setObjectName("actionChange_State")
        self.actionOpen = QtWidgets.QAction(GraphWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionOpen)
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

        self.retranslateUi(GraphWindow)
        QtCore.QMetaObject.connectSlotsByName(GraphWindow)

    def retranslateUi(self, GraphWindow):
        _translate = QtCore.QCoreApplication.translate
        GraphWindow.setWindowTitle(_translate("GraphWindow", "Finite Automata"))
        self.menuFile.setTitle(_translate("GraphWindow", "File"))
        self.menuNode.setTitle(_translate("GraphWindow", "Node"))
        self.menuEdit.setTitle(_translate("GraphWindow", "Edit"))
        self.menuDFA.setTitle(_translate("GraphWindow", "DFA"))
        self.actionSave.setText(_translate("GraphWindow", "Save"))
        self.actionNew.setText(_translate("GraphWindow", "New"))
        self.actionConnect.setText(_translate("GraphWindow", "Connect"))
        self.actionDisconnect.setText(_translate("GraphWindow", "Disconnect"))
        self.actionDelete.setText(_translate("GraphWindow", "Delete"))
        self.actionSolve.setText(_translate("GraphWindow", "Solve"))
        self.actionChange_Name.setText(_translate("GraphWindow", "Change Name"))
        self.actionChange_State.setText(_translate("GraphWindow", "Change State"))
        self.actionOpen.setText(_translate("GraphWindow", "Open"))

