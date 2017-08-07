# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'NFAEpsilonWindow.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_NFAEpsilonWindow(object):
    def setupUi(self, NFAEpsilonWindow):
        NFAEpsilonWindow.setObjectName("NFAEpsilonWindow")
        NFAEpsilonWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(NFAEpsilonWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setObjectName("graphicsView")
        self.verticalLayout.addWidget(self.graphicsView)
        NFAEpsilonWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(NFAEpsilonWindow)
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
        NFAEpsilonWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(NFAEpsilonWindow)
        self.statusbar.setObjectName("statusbar")
        NFAEpsilonWindow.setStatusBar(self.statusbar)
        self.actionSave = QtWidgets.QAction(NFAEpsilonWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionNew = QtWidgets.QAction(NFAEpsilonWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionConnect = QtWidgets.QAction(NFAEpsilonWindow)
        self.actionConnect.setObjectName("actionConnect")
        self.actionDisconnect = QtWidgets.QAction(NFAEpsilonWindow)
        self.actionDisconnect.setObjectName("actionDisconnect")
        self.actionDelete = QtWidgets.QAction(NFAEpsilonWindow)
        self.actionDelete.setObjectName("actionDelete")
        self.actionSolve = QtWidgets.QAction(NFAEpsilonWindow)
        self.actionSolve.setObjectName("actionSolve")
        self.actionChange_Name = QtWidgets.QAction(NFAEpsilonWindow)
        self.actionChange_Name.setObjectName("actionChange_Name")
        self.actionChange_State = QtWidgets.QAction(NFAEpsilonWindow)
        self.actionChange_State.setObjectName("actionChange_State")
        self.actionOpen = QtWidgets.QAction(NFAEpsilonWindow)
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

        self.retranslateUi(NFAEpsilonWindow)
        QtCore.QMetaObject.connectSlotsByName(NFAEpsilonWindow)

    def retranslateUi(self, NFAEpsilonWindow):
        _translate = QtCore.QCoreApplication.translate
        NFAEpsilonWindow.setWindowTitle(_translate("NFAEpsilonWindow", "NFA Epsilon"))
        self.menuFile.setTitle(_translate("NFAEpsilonWindow", "File"))
        self.menuNode.setTitle(_translate("NFAEpsilonWindow", "Node"))
        self.menuEdit.setTitle(_translate("NFAEpsilonWindow", "Edit"))
        self.menuDFA.setTitle(_translate("NFAEpsilonWindow", "NFA-Epsilon"))
        self.actionSave.setText(_translate("NFAEpsilonWindow", "Save"))
        self.actionNew.setText(_translate("NFAEpsilonWindow", "New"))
        self.actionConnect.setText(_translate("NFAEpsilonWindow", "Connect"))
        self.actionDisconnect.setText(_translate("NFAEpsilonWindow", "Disconnect"))
        self.actionDelete.setText(_translate("NFAEpsilonWindow", "Delete"))
        self.actionSolve.setText(_translate("NFAEpsilonWindow", "Solve"))
        self.actionChange_Name.setText(_translate("NFAEpsilonWindow", "Change Name"))
        self.actionChange_State.setText(_translate("NFAEpsilonWindow", "Change State"))
        self.actionOpen.setText(_translate("NFAEpsilonWindow", "Open"))

