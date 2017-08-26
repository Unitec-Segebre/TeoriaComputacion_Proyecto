from PyQt5.QtWidgets import QMainWindow, QGraphicsScene, QGraphicsView, QInputDialog, QLineEdit, QMessageBox, QFileDialog
from PyQt5.QtGui import QPainter
from ui_graphwindow import Ui_GraphWindow
from Node import Node, State
from Edge import Edge
from AutomataSolver import Automata_BARE, Automata_DFA
from AutomataSaver import Saver_FA
import pickle

class GraphGenerator(QMainWindow, Ui_GraphWindow):

    Epsilon = "?"

    def __init__(self, parent=None, load=None, saveName=None):
        super().__init__(parent)
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

        self.actionChange_state.triggered.connect(self.change_state)
        self.actionChange_state.setShortcut("Ctrl+p")

        self.actionChange_name.triggered.connect(self.change_name)
        self.actionChange_name.setShortcut("Ctrl+c")

        self.actionDisconnect.triggered.connect(self.delete_connection)
        self.actionDisconnect.setShortcut("Ctrl+d")

        self.actionDelete.triggered.connect(self.delete_node)
        self.actionDelete.setShortcut("Ctrl+r")

        self.actionDFA.triggered.connect(self.solve_DFA)
        self.actionDFA.setShortcut("Ctrl+1")

        self.actionSave.triggered.connect(self.save)
        self.actionSave.setShortcut("Ctrl+s")

        self.actionSave_as.triggered.connect(self.saveAs)
        self.actionSave_as.setShortcut("Ctrl+Shift+s")


        # self.actionSolve.triggered.connect(self.solve)
        #
        # self.actionTransform.triggered.connect(self.transform_graph)
        #
        #
        #
        # self.actionSave.triggered.connect(self.save_graph)
        # self.actionSave.setShortcut("Ctrl+s")
        #
        # self.actionSave_as.triggered.connect(self.saveAs_graph)
        # self.actionSave_as.setShortcut("Ctrl+Shift+s")
        #
        # self.actionOpen.triggered.connect(self.open_graph)
        #
        self.saveName = saveName
        if load != None:
            self.open(load)
        self.show()

    def new_node(self):
        while True:
            name, ok = QInputDialog.getText(self, "New Node", "Name: ", QLineEdit.Normal, "")
            if ok:
                if name == "":
                    QMessageBox.critical(self, "Warning!", "Name field must not be empty.")
                elif len(name) > 5:
                    QMessageBox.critical(self, "Warning!", "Name field must be 5 characters or less.")
                elif name.lower() in [item.name for item in self.graphicsView.scene().items() if isinstance(item, Node)]:
                    QMessageBox.warning(self, "Warning!", "Node %s already exists."%(name.lower()))
                else:
                    self.graphicsView.scene().addItem(Node(self, name.lower()))
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
            i = 0
            while len(node_count) > 0:
                if i < len(node.getNodesToUpdate()[0].edges()) and node.getNodesToUpdate()[0].edges()[i].destNode() == node:
                    self.graphicsView.scene().removeItem(node.getNodesToUpdate()[0].edges()[i])
                    node.getNodesToUpdate()[0].deleteEdge(i)
                else:
                    if node_count != node.getNodesToUpdate():
                        node_count = node.getNodesToUpdate()
                        i = 0
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
                        elif len(name) > 5:
                            QMessageBox.critical(self, "Warning!", "Name field must be 5 characters or less.")
                        elif name.lower() == node.name:
                            QMessageBox.critical(self, "Warning!", "Can not rename to same name.")
                        elif name.lower() in [item.name for item in self.graphicsView.scene().items() if isinstance(item, Node)]:
                            QMessageBox.warning(self, "Warning!", "Node %s already exists."%(name.lower()))
                        else:
                            node.setName(name.lower())
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
            options = ["Initial", "Transitional", "Final", "Initial and Final"]
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

    def solve_DFA(self):
        fa = self.convert_graph_to_class(Automata_DFA)
        try:
            fa.check(self.Epsilon)
        except Exception as exception:
            QMessageBox.warning(self, "Solve", str(exception))
            return
        while True:
            statement, ok = QInputDialog.getText(self, "Solve", "Statement: ", QLineEdit.Normal, "")
            if ok:
                try:
                    fa.solve(statement, self.Epsilon)
                    QMessageBox.information(self, "Result!", "'%s' is a solution"%(statement))
                except Exception as exception:
                    QMessageBox.critical(self, "Solve", str(exception))
            else:
                return

    def save(self):
        try:
            if self.saveName == None:
                self.saveAs()
            file = open(str(self.saveName), 'wb')
            pickle.dump(self.convert_graph_to_save(), file, pickle.HIGHEST_PROTOCOL)
            file.close()
        except Exception as exception:
            QMessageBox.warning(self, "Save graph", "%s." % (exception))
            print(exception)

    def saveAs(self):
        self.saveName = QFileDialog.getSaveFileName(self, 'Save graph as...')
        self.saveName = self.saveName[0]
        if ".af" not in self.saveName:
            self.saveName = ("%s.af"%(self.saveName))

    def open(self, items):
        print("States: {}".format(items.states))
        print("Input Symbols: {}".format(items.input_symbols))
        print("Transitions: {}".format(items.transitions))
        print("Initial States: {}".format(items.initial_states))
        print("Final States: {}".format(items.final_states))
        for state in items.states:
            node = Node(self, state)
            if not isinstance(items.states, set):
                node.setPos(items.states[state])
            if node.name in items.initial_states:
                node.setState(State(State.INITIAL))
            elif node.name in items.final_states:
                node.setState(State(State.FINAL))
            if node.name in items.initial_states and node.name in items.final_states:
                node.setState(State(State.INITIAL_FINAL))
            self.graphicsView.scene().addItem(node)

        nodes = [item for item in self.graphicsView.scene().items() if isinstance(item, Node)]
        for origin in items.transitions:
            for condition in items.transitions[origin]:
                for destination in items.transitions[origin][condition]:
                    self.graphicsView.scene().addItem(Edge([node for node in nodes if node.name == origin][0], [node for node in nodes if node.name == destination][0], condition))

    def convert_graph_to_class(self, Automata_Class=Automata_BARE):
        states = set([item.name for item in self.graphicsView.scene().items() if isinstance(item, Node)])
        input_symbols = set([item.condition for item in self.graphicsView.scene().items() if isinstance(item, Edge)])
        transitions = {}
        for item in self.graphicsView.scene().items():
            if isinstance(item, Node):
                paths = {}
                for path in item.edges():
                    if path.condition not in paths:
                        paths[path.condition] = [path.destNode().name]
                    else:
                        temp = paths[path.condition]
                        temp.append(path.destNode().name)
                        paths[path.condition] = set(temp)
                transitions[item.name] = paths
        initial_states = set([item.name for item in self.graphicsView.scene().items() if isinstance(item, Node) and (item.state == State.INITIAL or item.state == State.INITIAL_FINAL)])
        final_states = set([item.name for item in self.graphicsView.scene().items() if isinstance(item, Node) and (item.state == State.FINAL or item.state == State.INITIAL_FINAL)])

        return Automata_Class(states, input_symbols, transitions, initial_states, final_states)


    def convert_graph_to_save(self):
        fa = self.convert_graph_to_class()
        nodes = [item for item in self.graphicsView.scene().items() if isinstance(item, Node)]
        states = {}
        for node in nodes:
            states[node.name] = node.pos()
        return Automata_BARE(states, fa.input_symbols, fa.transitions, fa.initial_states, fa.final_states)

    # def solve(self, Automata_Class):
    #     fa = self.convert_graph_to_class(Automata_Class)
    #     # initial_states = [item.name for item in self.graphicsView.scene().items() if isinstance(item, Node) and item.state == State.INITIAL]
    #     if len(fa.initial_states) == 0:
    #         QMessageBox.critical(self, "Warning!", "An initial state is required to solve.")
    #         return
    #     elif len(fa.initial_states) > 1:
    #         QMessageBox.critical(self, "Warning!", "There must only be one initial state to solve.")
    #         return
    #     elif len(fa.final_states) == 0:
    #         QMessageBox.critical(self, "Warning!", "At least one final state is required to solve.")
    #         return
    #     # fa.initial_states = fa.initial_states[0]
    #     while True:
    #         statement, ok = QInputDialog.getText(self, "Solve", "Statement: ", QLineEdit.Normal, "")
    #         if ok:
    #             try:
    #                 fa.solve(statement, self.Epsilon)
    #                 QMessageBox.information(self, "Result!", "'%s' is a solution"%(statement))
    #             except Exception as exception:
    #                 QMessageBox.critical(self, "Solve", str(exception))
    #         else:
    #             return
    #
    # def transform(self, Automata_Class, Class_to_Generate):
    #     fa = self.convert_graph_to_class(Automata_Class)
    #     # initial_states = [item.name for item in self.graphicsView.scene().items() if isinstance(item, Node) and item.state == State.INITIAL]
    #     if len(fa.initial_states) == 0:
    #         QMessageBox.critical(self, "Warning!", "An initial state is required to transform.")
    #         return
    #     elif len(fa.initial_states) > 1:
    #         QMessageBox.critical(self, "Warning!", "There must only be one initial state to transform.")
    #         return
    #     elif len(fa.final_states) == 0:
    #         QMessageBox.critical(self, "Warning!", "At least one final state is required to transform.")
    #         return
    #     Class_to_Generate(self.parent(), fa.transform(self.Epsilon))
    #
    # def convert_graph_to_class(self, Automata_Class=Automata_BARE):
    #     states = set([item.name for item in self.graphicsView.scene().items() if isinstance(item, Node)])
    #     input_symbols = set([item.condition for item in self.graphicsView.scene().items() if isinstance(item, Edge)])
    #     transitions = {}
    #     for item in self.graphicsView.scene().items():
    #         if isinstance(item, Node):
    #             paths = {}
    #             for path in item.edges():
    #                 if path.condition not in paths:
    #                     paths[path.condition] = [path.destNode().name] ############################change to {}############################
    #                 else:
    #                     temp = paths[path.condition]
    #                     temp.append(path.destNode().name)
    #                     paths[path.condition] = set(temp)
    #             transitions[item.name] = paths
    #     initial_states = set([item.name for item in self.graphicsView.scene().items() if isinstance(item, Node) and (item.state == State.INITIAL or item.state == State.INITIAL_FINAL)])
    #     final_states = set([item.name for item in self.graphicsView.scene().items() if isinstance(item, Node) and (item.state == State.FINAL or item.state == State.INITIAL_FINAL)])
    #
    #     return Automata_Class(states, input_symbols, transitions, initial_states, final_states)
    #
    # def convert_graph_to_save(self):
    #     fa = self.convert_graph_to_class()
    #     nodes = [item for item in self.graphicsView.scene().items() if isinstance(item, Node)]
    #     states = {}
    #     for node in nodes:
    #         states[node.name] = node.pos()
    #     return Saver_FA(states, fa.input_symbols, fa.transitions, fa.initial_states, fa.final_states)
    #
    # def saveAs_graph(self):
    #     file_name = QFileDialog.getSaveFileName(self, 'Save graph as...')
    #     file_name = file_name[0]
    #     if ".af" not in file_name:
    #         file_name = ("%s.af"%(file_name))
    #     return file_name
    #
    # def save_graph(self, file_name=None):
    #     try:
    #         if file_name == None:
    #             file_name = self.saveAs_graph()
    #         file = open(str(file_name), 'wb')
    #         pickle.dump(self.convert_graph_to_save(), file, pickle.HIGHEST_PROTOCOL)
    #         file.close()
    #         return file_name
    #     except Exception as exception:
    #         QMessageBox.warning(self, "Save graph", "%s." % (exception))
    #         print(exception)
    #
    # def open_graph(self, items):
    #     print("States: {}".format(items.states))
    #     print("Input Symbols: {}".format(items.input_symbols))
    #     print("Transitions: {}".format(items.transitions))
    #     print("Initial States: {}".format(items.initial_states))
    #     print("Final States: {}".format(items.final_states))
    #     for state in items.states:
    #         node = Node(self, state)
    #         if not isinstance(items.states, set):
    #             node.setPos(items.states[state])
    #         if node.name in items.initial_states:
    #             node.setState(State(State.INITIAL))
    #         elif node.name in items.final_states:
    #             node.setState(State(State.FINAL))
    #         if node.name in items.initial_states and node.name in items.final_states:
    #             node.setState(State(State.INITIAL_FINAL))
    #         self.graphicsView.scene().addItem(node)
    #
    #     nodes = [item for item in self.graphicsView.scene().items() if isinstance(item, Node)]
    #     for origin in items.transitions:
    #         for condition in items.transitions[origin]:
    #             for destination in items.transitions[origin][condition]:
    #                 # print("%s--%c-->%s"%(origin, condition, destination))
    #                 # print([node for node in nodes if node.name == origin][0].name)
    #                 # print([node for node in nodes if node.name == destination][0].name)
    #                 # print(condition)
    #                 self.graphicsView.scene().addItem(Edge([node for node in nodes if node.name == origin][0], [node for node in nodes if node.name == destination][0], condition))
