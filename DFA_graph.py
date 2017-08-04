from PyQt5.QtWidgets import QMainWindow, QGraphicsScene, QGraphicsView, QInputDialog, QLineEdit, QMessageBox, QFileDialog
from PyQt5.QtGui import QPainter
from ui_dfawindow import Ui_DFAWindow
from Node import Node, State
from Edge import Edge
from AutomataSolver import Automata_DFA
import pickle

class DFA_graph(QMainWindow, Ui_DFAWindow):
    def __init__(self, parent=None, load=None):
        super(DFA_graph, self).__init__(parent)
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

    def new_node(self):
        while True:
            name, ok = QInputDialog.getText(self, "New Node", "Name: ", QLineEdit.Normal, "")
            if ok:
                if name == "":
                    QMessageBox.critical(self, "Warning!", "Name field must not be empty.")
                elif name in [item.name for item in self.graphicsView.scene().items() if isinstance(item, Node)]:
                    QMessageBox.warning(self, "Warning!", "Node %s already exists."%(name))
                else:
                    self.graphicsView.scene().addItem(Node(self, name))
                    return
            elif not ok:
                return

    def delete_node(self):
        nodes = [item for item in self.graphicsView.scene().items() if isinstance(item, Node)]
        if not nodes:
            QMessageBox.critical(self, "Warning!", "There are no nodes on the graph.")
            return
        node_selected, ok = QInputDialog.getItem(self, "Delete Node", "Node: ", [node.name for node in nodes], 0, False)
        if ok:
            delete_choice = QMessageBox.question(self, "Delete Node", "Are you sure you want to delete %s and all its edges?" % (node_selected), QMessageBox.Yes | QMessageBox.No)
            if delete_choice == QMessageBox.No:
                return
            node = [node for node in nodes if node.name == node_selected][0]
            node_count = node.getNodesToUpdate()
            while len(node_count) > 0:
                i = 0
                if node.getNodesToUpdate()[0].edges()[i].destNode() == node:
                    self.graphicsView.scene().removeItem(node.getNodesToUpdate()[0].edges()[i])
                    node.getNodesToUpdate()[0].deleteEdge(i)
                else:
                    if node_count != node.getNodesToUpdate():
                        node_count = node.getNodesToUpdate()
                    else:
                        i += 1
            while len(node.edges()):
                self.graphicsView.scene().removeItem(node.popEdge())
            self.graphicsView.scene().removeItem(node)
        return


    def change_name(self):
        nodes = [item for item in self.graphicsView.scene().items() if isinstance(item, Node)]
        if not nodes:
            QMessageBox.critical(self, "Warning!", "There are no nodes on the graph.")
            return
        while True:
            node_selected, ok = QInputDialog.getItem(self, "Change Name", "Node: ", [node.name for node in nodes], 0, False)
            if ok:
                node = [node for node in nodes if node.name == node_selected][0]
                while True:
                    name, ok = QInputDialog.getText(self, "Change Name", "Name: ", QLineEdit.Normal, "")
                    if ok:
                        if name == "":
                            QMessageBox.critical(self, "Warning!", "Name field must not be empty.")
                        elif name == node.name:
                            QMessageBox.critical(self, "Warning!", "Can not rename to same name.")
                        elif name in [item.name for item in self.graphicsView.scene().items() if isinstance(item, Node)]:
                            QMessageBox.warning(self, "Warning!", "Node %s already exists."%(name))
                        else:
                            node.setName(name)
                            return
                    elif not ok:
                        return
            elif not ok:
                return

    def change_state(self):
        nodes = [item for item in self.graphicsView.scene().items() if isinstance(item, Node)]
        if not nodes:
            QMessageBox.critical(self, "Warning!", "There are no nodes on the graph.")
            return
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
                        if path_condition[0] in [path.condition for path in node.edges()]:
                            QMessageBox.warning(self, "Warning!", "Connection through '%c' already exists." % (path_condition[0]))
                        else:
                            self.graphicsView.scene().addItem(Edge(node, [node for node in nodes if node.name == node_dest][0], path_condition[0]))
                            return
                    elif not ok:
                        return
            elif not ok:
                return
        elif not ok:
            return

    def delete_connection(self):
        nodes = [item for item in self.graphicsView.scene().items() if isinstance(item, Node)]
        if not nodes:
            QMessageBox.critical(self, "Warning!", "There are no nodes on the graph.")
            return
        while True:
            node_source, ok = QInputDialog.getItem(self, "Delete Connection", "Source: ", [node.name for node in nodes], 0, False)
            node = [node for node in nodes if node.name == node_source][0]
            if ok:
                if not node.edges():
                    QMessageBox.warning(self, "Warning!", "Node %s has no edges." % (node.name))
                else:
                    options = [("%c -> %s" % (connection.condition, connection.destNode().name)) for connection in node.edges()]
                    selected, ok = QInputDialog.getItem(self, "Delete Connection", "Connection: ", options, 0, False)
                    if ok:
                        self.graphicsView.scene().removeItem(node.edgeList[options.index(selected)])
                        node.deleteEdge(options.index(selected))
                    return
            elif not ok:
                return


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
        initial_state = [item.name for item in self.graphicsView.scene().items() if isinstance(item, Node) and item.state == State.INITIAL]
        if len(initial_state) == 0:
            QMessageBox.critical(self, "Warning!", "An initial state is required to solve.")
            return
        elif len(initial_state) > 1:
            QMessageBox.critical(self, "Warning!", "There must only be one initial state to solve.")
            return
        elif len(initial_state) == 1:
            initial_state = initial_state[0]
            print(initial_state)
        final_states = set([item.name for item in self.graphicsView.scene().items() if isinstance(item, Node) and item.state == State.FINAL])
        if len(final_states) == 0:
            QMessageBox.critical(self, "Warning!", "At least one final state is required to solve.")
            return
        print(states)
        print(input_symbols)
        print(transitions)
        print(initial_state)
        print(final_states)
        dfa = Automata_DFA(states, input_symbols, transitions, initial_state, final_states)
        statement, ok = QInputDialog.getText(self, "Solve", "Statement: ", QLineEdit.Normal, "")
        if ok:
            try:
                dfa.solve(statement)
                QMessageBox.information(self, "Result!", "'%s' is a solution"%(statement))
            except:
                QMessageBox.critical(self, "Result!", "'%s' is NOT a solution" % (statement))

    def save_graph(self):
        try:
            file_name = QFileDialog.getSaveFileName(self, 'Save graph')
            file_name = ("%s.af"%(file_name[0]))
            file = open(str(file_name), 'wb')
            pickle.dump(self.convert_graph_to_class(), file, pickle.HIGHEST_PROTOCOL)
            file.close()
        except Exception as exception:
            QMessageBox.warning(self, "Save graph", "%s." % (exception))
            print(exception)

    def convert_graph_to_class(self):
        states = set([item.name for item in self.graphicsView.scene().items() if isinstance(item, Node)])
        input_symbols = set([item.condition for item in self.graphicsView.scene().items() if isinstance(item, Edge)])
        transitions = {}
        for item in self.graphicsView.scene().items():
            if isinstance(item, Node):
                paths = {}
                for path in item.edges():
                    paths[path.condition] = path.destNode().name
                transitions[item.name] = paths
        initial_state = [item.name for item in self.graphicsView.scene().items() if
                         isinstance(item, Node) and item.state == State.INITIAL]
        if len(initial_state) == 1:
            initial_state = initial_state[0]
        else:
            initial_state = None
        final_states = set([item.name for item in self.graphicsView.scene().items() if
                            isinstance(item, Node) and item.state == State.FINAL])

        return Automata_DFA(states, input_symbols, transitions, initial_state, final_states)

    def open_graph(self, items):
        # try:
        #     file_name = QFileDialog.getOpenFileName(self, 'Open graph')
        #     file_name = file_name[0]
        #     file = open(str(file_name), 'rb')
        #     items = pickle.load(file)

        for state in items.states:
            self.graphicsView.scene().addItem(Node(self, state))

        nodes = [item for item in self.graphicsView.scene().items() if isinstance(item, Node)]
        for origin in items.transitions:
            for condition in items.transitions[origin]:
                self.graphicsView.scene().addItem(Edge([node for node in nodes if node.name == origin][0], [node for node in nodes if node.name == items.transitions[origin][condition]][0], condition))
                print("%s--%c-->%s"%(origin, condition, items.transitions[origin][condition]))

        node = [node for node in nodes if node.name == items.initial_state][0]
        node.setState(State(State.INITIAL))
        node.update()

        for final_state in items.final_states:
            node = [node for node in nodes if node.name == final_state][0]
            node.setState(State(State.FINAL))
            node.update()

        #     file.close()
        # except Exception as exception:
        #     QMessageBox.warning(self, "Open graph", "%s." % (exception))
        #     print(exception)

