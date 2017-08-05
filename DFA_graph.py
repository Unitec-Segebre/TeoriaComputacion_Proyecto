from GraphGenerator import GraphGenerator
from PyQt5.QtWidgets import QMessageBox, QInputDialog, QLineEdit
from Node import Node
from Edge import Edge
from AutomataSolver import Automata_DFA

class DFA_graph(GraphGenerator):
    def __init__(self, parent=None, load=None):
        super(DFA_graph, self).__init__(parent, "DFA", load)

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