from PyQt5.QtWidgets import QMessageBox, QInputDialog, QLineEdit, QGraphicsScene, QGraphicsView
from PyQt5.QtGui import QPainter
from Node import Node
from Edge import Edge
from GraphGenerator import GraphGenerator
from AutomataSolver import Automata_DFA
from ui_dfawindow import Ui_DFAWindow
from RegEx_graph import RegEx_graph

class DFA_graph(GraphGenerator, Ui_DFAWindow):
    def __init__(self, parent=None, load=None, saveName=None):
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

        self.actionTransform.triggered.connect(self.transform_graph)

        self.actionDisconnect.triggered.connect(self.delete_connection)

        self.actionDelete.triggered.connect(self.delete_node)

        self.actionSave.triggered.connect(self.save_graph)
        self.actionSave.setShortcut("Ctrl+s")

        self.actionSave_as.triggered.connect(self.saveAs_graph)
        self.actionSave_as.setShortcut("Ctrl+Shift+s")

        self.actionOpen.triggered.connect(self.open_graph)

        self.saveName = saveName
        if load != None:
            self.open_graph(load)

        self.show()

    def save_graph(self, saveName):
        self.saveName = super(DFA_graph, self).save_graph(self.saveName)

    def saveAs_graph(self):
        super(DFA_graph, self).save_graph(super(DFA_graph, self).saveAs_graph())


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
        fa = self.convert_graph_to_class(Automata_DFA)
        # initial_states = [item.name for item in self.graphicsView.scene().items() if isinstance(item, Node) and item.state == State.INITIAL]
        if len(fa.initial_states) == 0:
            QMessageBox.critical(self, "Warning!", "An initial state is required to solve.")
            return
        elif len(fa.initial_states) > 1:
            QMessageBox.critical(self, "Warning!", "There must only be one initial state to solve.")
            return
        elif len(fa.final_states) == 0:
            QMessageBox.critical(self, "Warning!", "At least one final state is required to solve.")
            return

        for state in fa.transitions:
            for path in fa.transitions[state]:
                if len(fa.transitions[state][path]) > 1:
                    QMessageBox.critical(self, "Warning!", "DFA can not contain more than one path with the same condition from the same node.")
                    return

        while True:
            statement, ok = QInputDialog.getText(self, "Solve", "Statement: ", QLineEdit.Normal, "")
            if ok:
                try:
                    fa.solve(statement, self.Epsilon)
                    QMessageBox.information(self, "Result!", "'%s' is a solution" % (statement))
                except Exception as exception:
                    QMessageBox.critical(self, "Solve", str(exception))
            else:
                return

    def transform_graph(self):
        super(DFA_graph, self).transform(Automata_DFA, RegEx_graph)