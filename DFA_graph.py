from GraphGenerator import GraphGenerator
from PyQt5.QtWidgets import QMessageBox, QInputDialog, QLineEdit, QGraphicsScene, QGraphicsView
from PyQt5.QtGui import QPainter
from Node import Node
from Edge import Edge
from AutomataSolver import Automata_DFA
from ui_dfawindow import Ui_DFAWindow

class DFA_graph(GraphGenerator, Ui_DFAWindow):
    def __init__(self, parent=None, load=None):
        super(DFA_graph, self).__init__(parent, load)
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

        if load != None:
            self.open_graph(load)

        self.show()


    def new_connection(self):
        nodes = [item for item in self.graphicsView.scene().items() if isinstance(item, Node)]
        if not nodes:
            QMessageBox.critical(self, "Warning!", "There are no nodes on the graph.")
            return
        node_source, ok = QInputDialog.getItem(self, "New Connection", "Source: ", [node.name for node in nodes], 0, False)
        if ok:
            node_dest, ok = QInputDialog.getItem(self, "New Connection", "Destiny: ", [node.name for node in nodes], 0, False)
            if ok:
                node = [node for node in nodes if node.name == node_source][0]
                while True:
                    path_condition, ok = QInputDialog.getText(self, "New Connection", "Condition: ", QLineEdit.Normal, "")
                    if ok:
                        if path_condition == "":
                            QMessageBox.warning(self, "Warning!", "Connections must have a condition, condition can not be blank.")
                            continue
                        if path_condition[0] == GraphGenerator.Epsilon:
                            QMessageBox.warning(self, "Warning!", "Can not have Epsilon('%c') in DFA." % (GraphGenerator.Epsilon))
                            continue
                        if path_condition[0] in [path.condition for path in node.edges()]:
                            QMessageBox.warning(self, "Warning!", "Connection through '%c' already exists." % (path_condition[0]))
                            continue
                        self.graphicsView.scene().addItem(Edge(node, [node for node in nodes if node.name == node_dest][0], path_condition[0]))
                        return
                    elif not ok:
                        return
            elif not ok:
                return
        elif not ok:
            return

    def solve(self):
        super(DFA_graph, self).solve(Automata_DFA)