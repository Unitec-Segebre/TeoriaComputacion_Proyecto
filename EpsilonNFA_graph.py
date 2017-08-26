from PyQt5.QtWidgets import QGraphicsView, QGraphicsScene
from PyQt5.QtGui import QPainter
from GraphGenerator import GraphGenerator
from AutomataSolver import Automata_EpsilonNFA
from ui_nfaepsilonwindow import Ui_NFAEpsilonWindow
# from DFA_graph import DFA_graph

class NFAEpsilon_graph(GraphGenerator, Ui_NFAEpsilonWindow):
    def __init__(self, parent=None, load=None):
        super(NFAEpsilon_graph, self).__init__(parent, load)
        self.setupUi(self)

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

        self.actionConnect.triggered.connect(self.new_connection)
        self.actionConnect.setShortcut("Ctrl+b")

        self.actionChange_State.triggered.connect(self.change_state)

        self.actionChange_Name.triggered.connect(self.change_name)

        self.actionSolve.triggered.connect(self.solve)

        self.actionDisconnect.triggered.connect(self.delete_connection)

        self.actionDelete.triggered.connect(self.delete_node)

        self.actionSave.triggered.connect(self.save_graph)

        self.actionOpen.triggered.connect(self.open_graph)

        self.actionTransform_to_DFA.triggered.connect(self.transform_graph)

        if load != None:
            self.open_graph(load)

        self.show()


    def solve(self):
        super(NFAEpsilon_graph, self).solve(Automata_NFAEpsilon)

    def transform_graph(self):
        super(NFAEpsilon_graph, self).transform(Automata_NFAEpsilon, DFA_graph)
