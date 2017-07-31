import sys
from PyQt5.QtWidgets import QMainWindow, QGraphicsScene, QGraphicsView
from PyQt5.QtGui import QPainter
from PyQt5.QtCore import *
from ui_dfawindow import Ui_DFAWindow
from Node import Node

class DFA(QMainWindow, Ui_DFAWindow):
    def __init__(self, parent=None):
        super(DFA, self).__init__(parent)
        self.setupUi(self)
        self.timerId = 0

        scene = QGraphicsScene(self.graphicsView)
        scene.setItemIndexMethod(QGraphicsScene.NoIndex)
        self.graphicsView.setScene(scene)
        self.graphicsView.setCacheMode(QGraphicsView.CacheBackground)
        self.graphicsView.setViewportUpdateMode(QGraphicsView.BoundingRectViewportUpdate)
        self.graphicsView.setRenderHint(QPainter.Antialiasing)
        self.graphicsView.setTransformationAnchor(QGraphicsView.AnchorUnderMouse)
        self.graphicsView.setResizeAnchor(QGraphicsView.AnchorViewCenter)

        self.actionNew.triggered.connect(self.new_node)
        self.actionNew.setShortcut("Ctrl+n")

        self.show()

    def new_node(self):
        self.graphicsView.scene().addItem(Node(self))