# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GraphWindow.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
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
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuGraph = QtWidgets.QMenu(self.menubar)
        self.menuGraph.setObjectName("menuGraph")
        self.menuNode = QtWidgets.QMenu(self.menuGraph)
        self.menuNode.setObjectName("menuNode")
        self.menuConnection = QtWidgets.QMenu(self.menuGraph)
        self.menuConnection.setObjectName("menuConnection")
        self.menuSolve = QtWidgets.QMenu(self.menubar)
        self.menuSolve.setObjectName("menuSolve")
        self.menuTransform = QtWidgets.QMenu(self.menuSolve)
        self.menuTransform.setObjectName("menuTransform")
        self.menuProperties = QtWidgets.QMenu(self.menuSolve)
        self.menuProperties.setObjectName("menuProperties")
        GraphWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(GraphWindow)
        self.statusbar.setObjectName("statusbar")
        GraphWindow.setStatusBar(self.statusbar)
        self.actionSave = QtWidgets.QAction(GraphWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionDFA = QtWidgets.QAction(GraphWindow)
        self.actionDFA.setObjectName("actionDFA")
        self.actionSave_as = QtWidgets.QAction(GraphWindow)
        self.actionSave_as.setObjectName("actionSave_as")
        self.actionExit = QtWidgets.QAction(GraphWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionNFA = QtWidgets.QAction(GraphWindow)
        self.actionNFA.setObjectName("actionNFA")
        self.actionEpsilon_NFA = QtWidgets.QAction(GraphWindow)
        self.actionEpsilon_NFA.setObjectName("actionEpsilon_NFA")
        self.actionDFA_to_Regular_Expression = QtWidgets.QAction(GraphWindow)
        self.actionDFA_to_Regular_Expression.setObjectName("actionDFA_to_Regular_Expression")
        self.actionNFA_to_DFA = QtWidgets.QAction(GraphWindow)
        self.actionNFA_to_DFA.setObjectName("actionNFA_to_DFA")
        self.actionEpsilon_NFA_to_DFA = QtWidgets.QAction(GraphWindow)
        self.actionEpsilon_NFA_to_DFA.setObjectName("actionEpsilon_NFA_to_DFA")
        self.actionNew = QtWidgets.QAction(GraphWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionChange_state = QtWidgets.QAction(GraphWindow)
        self.actionChange_state.setObjectName("actionChange_state")
        self.actionChange_name = QtWidgets.QAction(GraphWindow)
        self.actionChange_name.setObjectName("actionChange_name")
        self.actionDelete = QtWidgets.QAction(GraphWindow)
        self.actionDelete.setObjectName("actionDelete")
        self.actionConnect = QtWidgets.QAction(GraphWindow)
        self.actionConnect.setObjectName("actionConnect")
        self.actionDisconnect = QtWidgets.QAction(GraphWindow)
        self.actionDisconnect.setObjectName("actionDisconnect")
        self.actionUnion = QtWidgets.QAction(GraphWindow)
        self.actionUnion.setObjectName("actionUnion")
        self.actionIntersection = QtWidgets.QAction(GraphWindow)
        self.actionIntersection.setObjectName("actionIntersection")
        self.actionDifference = QtWidgets.QAction(GraphWindow)
        self.actionDifference.setObjectName("actionDifference")
        self.actionComplement = QtWidgets.QAction(GraphWindow)
        self.actionComplement.setObjectName("actionComplement")
        self.actionMinimize = QtWidgets.QAction(GraphWindow)
        self.actionMinimize.setObjectName("actionMinimize")
        self.actionReflection = QtWidgets.QAction(GraphWindow)
        self.actionReflection.setObjectName("actionReflection")
        self.actionRegular_Expression_to_Epsilon_NFA = QtWidgets.QAction(GraphWindow)
        self.actionRegular_Expression_to_Epsilon_NFA.setObjectName("actionRegular_Expression_to_Epsilon_NFA")
        self.actionPDA_Connect = QtWidgets.QAction(GraphWindow)
        self.actionPDA_Connect.setObjectName("actionPDA_Connect")
        self.actionPDA = QtWidgets.QAction(GraphWindow)
        self.actionPDA.setObjectName("actionPDA")
        self.actionLanguage_Descrition_to_PDA = QtWidgets.QAction(GraphWindow)
        self.actionLanguage_Descrition_to_PDA.setObjectName("actionLanguage_Descrition_to_PDA")
        self.actionPDA_to_Language_Description = QtWidgets.QAction(GraphWindow)
        self.actionPDA_to_Language_Description.setObjectName("actionPDA_to_Language_Description")
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_as)
        self.menuFile.addAction(self.actionExit)
        self.menuNode.addAction(self.actionNew)
        self.menuNode.addAction(self.actionChange_state)
        self.menuNode.addAction(self.actionChange_name)
        self.menuNode.addAction(self.actionDelete)
        self.menuConnection.addAction(self.actionConnect)
        self.menuConnection.addAction(self.actionPDA_Connect)
        self.menuConnection.addAction(self.actionDisconnect)
        self.menuGraph.addAction(self.menuNode.menuAction())
        self.menuGraph.addAction(self.menuConnection.menuAction())
        self.menuTransform.addAction(self.actionDFA_to_Regular_Expression)
        self.menuTransform.addAction(self.actionRegular_Expression_to_Epsilon_NFA)
        self.menuTransform.addAction(self.actionNFA_to_DFA)
        self.menuTransform.addAction(self.actionEpsilon_NFA_to_DFA)
        self.menuTransform.addSeparator()
        self.menuTransform.addAction(self.actionLanguage_Descrition_to_PDA)
        self.menuTransform.addAction(self.actionPDA_to_Language_Description)
        self.menuProperties.addAction(self.actionUnion)
        self.menuProperties.addAction(self.actionIntersection)
        self.menuProperties.addAction(self.actionDifference)
        self.menuProperties.addAction(self.actionComplement)
        self.menuProperties.addAction(self.actionReflection)
        self.menuSolve.addAction(self.actionDFA)
        self.menuSolve.addAction(self.actionNFA)
        self.menuSolve.addAction(self.actionEpsilon_NFA)
        self.menuSolve.addAction(self.actionPDA)
        self.menuSolve.addSeparator()
        self.menuSolve.addAction(self.menuTransform.menuAction())
        self.menuSolve.addAction(self.menuProperties.menuAction())
        self.menuSolve.addAction(self.actionMinimize)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuGraph.menuAction())
        self.menubar.addAction(self.menuSolve.menuAction())

        self.retranslateUi(GraphWindow)
        QtCore.QMetaObject.connectSlotsByName(GraphWindow)

    def retranslateUi(self, GraphWindow):
        _translate = QtCore.QCoreApplication.translate
        GraphWindow.setWindowTitle(_translate("GraphWindow", "Finite Automata"))
        self.menuFile.setTitle(_translate("GraphWindow", "File"))
        self.menuGraph.setTitle(_translate("GraphWindow", "Graph"))
        self.menuNode.setTitle(_translate("GraphWindow", "Node"))
        self.menuConnection.setTitle(_translate("GraphWindow", "Conection"))
        self.menuSolve.setTitle(_translate("GraphWindow", "Solve"))
        self.menuTransform.setTitle(_translate("GraphWindow", "Transform"))
        self.menuProperties.setTitle(_translate("GraphWindow", "Properties"))
        self.actionSave.setText(_translate("GraphWindow", "Save"))
        self.actionDFA.setText(_translate("GraphWindow", "DFA"))
        self.actionSave_as.setText(_translate("GraphWindow", "Save as"))
        self.actionExit.setText(_translate("GraphWindow", "Exit"))
        self.actionNFA.setText(_translate("GraphWindow", "NFA"))
        self.actionEpsilon_NFA.setText(_translate("GraphWindow", "Ɛ-NFA"))
        self.actionDFA_to_Regular_Expression.setText(_translate("GraphWindow", "DFA ⇨ Regular Expression"))
        self.actionNFA_to_DFA.setText(_translate("GraphWindow", "NFA ⇨ DFA"))
        self.actionEpsilon_NFA_to_DFA.setText(_translate("GraphWindow", "Ɛ-NFA ⇨ DFA"))
        self.actionNew.setText(_translate("GraphWindow", "New"))
        self.actionChange_state.setText(_translate("GraphWindow", "Change state"))
        self.actionChange_name.setText(_translate("GraphWindow", "Change name"))
        self.actionDelete.setText(_translate("GraphWindow", "Delete"))
        self.actionConnect.setText(_translate("GraphWindow", "Connect"))
        self.actionDisconnect.setText(_translate("GraphWindow", "Disconnect"))
        self.actionUnion.setText(_translate("GraphWindow", "Union"))
        self.actionIntersection.setText(_translate("GraphWindow", "Intersection"))
        self.actionDifference.setText(_translate("GraphWindow", "Difference"))
        self.actionComplement.setText(_translate("GraphWindow", "Complement"))
        self.actionMinimize.setText(_translate("GraphWindow", "Minimize"))
        self.actionReflection.setText(_translate("GraphWindow", "Reflection"))
        self.actionRegular_Expression_to_Epsilon_NFA.setText(_translate("GraphWindow", "Regular Expression ⇨ Ɛ-NFA"))
        self.actionPDA_Connect.setText(_translate("GraphWindow", "PDA Connect"))
        self.actionPDA.setText(_translate("GraphWindow", "PDA"))
        self.actionLanguage_Descrition_to_PDA.setText(_translate("GraphWindow", "Language Descrition ⇨ PDA"))
        self.actionPDA_to_Language_Description.setText(_translate("GraphWindow", "PDA ⇨ Language  Description"))

