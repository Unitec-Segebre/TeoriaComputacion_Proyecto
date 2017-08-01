import sys
from PyQt5.QtWidgets import QMainWindow, QGraphicsScene, QGraphicsView, QInputDialog, QLineEdit
from PyQt5.QtGui import QPainter
from PyQt5.QtCore import *
from ui_dfawindow import Ui_DFAWindow
from automata.fa.dfa import DFA
from Node import Node, State
from Edge import Edge

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

        self.actionConnect.triggered.connect(self.new_connection)
        self.actionConnect.setShortcut("Ctrl+b")

        self.actionChange_State.triggered.connect(self.change_state)

        self.actionSolve.triggered.connect(self.solve)

        self.actionDisconnect.triggered.connect(self.delete_connection)

        self.show()

    def new_node(self):
        name, ok = QInputDialog.getText(self, "New Node", "Name: ", QLineEdit.Normal, "")
        if ok and name not in [item.name for item in self.graphicsView.scene().items() if isinstance(item, Node)]:
            self.graphicsView.scene().addItem(Node(self, name))

    def change_state(self):
        nodes = [item for item in self.graphicsView.scene().items() if isinstance(item, Node)]
        name, ok = QInputDialog.getItem(self, "Change State", "Name: ", [node.name for node in nodes], 0, False)
        if ok:
            options = ["Initial", "Transitional", "Final"]
            state, ok = QInputDialog.getItem(self, "Change State", "State: ", options, 0, False)
            if ok:
                node = [node for node in nodes if node.name == name][0]
                node.setState(State(options.index(state)))
                node.update()

    def new_connection(self):
        nodes = [item for item in self.graphicsView.scene().items() if isinstance(item, Node)]
        node_source, ok = QInputDialog.getItem(self, "New Connection", "Source: ", [node.name for node in nodes], 0, False)
        if ok:
            node_dest, ok = QInputDialog.getItem(self, "New Connection", "Destiny: ", [node.name for node in nodes], 0, False)
            node = [node for node in nodes if node.name == node_source][0]
            if ok: # and node_dest not in [path.destNode().name for path in node.edges()]:
                path_condition, ok = QInputDialog.getText(self, "New Connection", "Condition: ", QLineEdit.Normal, "")
                if ok and path_condition[0] not in [path.condition for path in node.edges()]:
                    self.graphicsView.scene().addItem(Edge(node, [node for node in nodes if node.name == node_dest][0], path_condition[0]))
                else:
                    print("NAH!")
            else:
                print("NAH!")

    def delete_connection(self):
        nodes = [item for item in self.graphicsView.scene().items() if isinstance(item, Node)]
        node_source, ok = QInputDialog.getItem(self, "Delete Connection", "Source: ", [node.name for node in nodes], 0, False)
        if ok:
            node = [node for node in nodes if node.name == node_source][0]
            options = [("%s, %c"%(connection.destNode().name, connection.condition)) for connection in node.edges()]
            selected, ok = QInputDialog.getItem(self, "Delete Connection", "Connection: ", options, 0, False)
            if ok:
                self.graphicsView.scene().removeItem(node.edgeList[options.index(selected)])
                node.deleteEdge(options.index(selected))


    def solve(self):
        states = set([item.name for item in self.graphicsView.scene().items() if isinstance(item, Node)])
        input_symbols = set([item.condition for item in self.graphicsView.scene().items() if isinstance(item, Edge)])
        transitions = {}
        for item in self.graphicsView.scene().items():
            if isinstance(item, Node):
                paths = {}
                for path in item.edges():
                    paths[path.condition] = path.destNode().name
                transitions[item.name] = paths
        initial_state = [item.name for item in self.graphicsView.scene().items() if isinstance(item, Node) and item.state == State.INITIAL][0]
        final_states = set([item.name for item in self.graphicsView.scene().items() if isinstance(item, Node) and item.state == State.FINAL])
        print(states)
        print(input_symbols)
        print(transitions)
        print(initial_state)
        print(final_states)
        # dfa = DFA(states, input_symbols, transitions, initial_state, final_states)#(states=states, imput_symbols=imput_symbols, transitions=transitions, initial_state=initial_state, final_states=final_states) #
        # print(dfa.validate_input('01'))

