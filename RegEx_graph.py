from PyQt5.QtWidgets import QInputDialog, QLineEdit, QMessageBox
# from NFAEpsilon_graph import NFAEpsilon_graph
from AutomataSolver import Automata_BARE
from parser import parse
import ast

class RegEx_graph(QInputDialog):
    def __init__(self, parent=None, expression=None, classToTransform=None):
        super(RegEx_graph, self).__init__(parent)
        self.Epsilon_NFA = classToTransform
        self.lastNode = 0
        self.setWindowTitle("Regular Expression")
        if expression == "()*":
            expression = "The only solution is no input!"
        while True:
            expression, ok = self.getText(parent, "Regular Expression to Epsilon NFA", "Expression:", QLineEdit.Normal, expression)
            if not ok:
                break
            if expression == "":
                QMessageBox.warning(self, "Warning!", "Expression can not be blank.")
                continue
            try:
                expression_tree = parse(expression)
            except Exception:
                QMessageBox.warning(self, "Warning!", "Invalid expression '%s'."%(expression))
                continue
            self.transform_graph(expression_tree)


    def transform_graph(self, expression_tree):
        transitions = {}
        def desipherObject(object):
            if isinstance(object, ast.Digit):
                # global lastNode
                # lastNode+=1
                return ("%d"%object.number)#, lastNode-1
            elif isinstance(object, ast.Letter):
                # global lastNode
                # lastNode+=1
                return object.letter#, lastNode-1
            elif isinstance(object, ast.Concat):
                left = desipherObject(object.left_expr)
                transitions[("q%d"%self.lastNode)] = {}
                transitions[("q%d"%self.lastNode)][left] = set(list(["q%d"%(self.lastNode+1)]))
                self.lastNode += 1
                transitions[("q%d" % self.lastNode)] = {}
                transitions[("q%d" % self.lastNode)][self.Epsilon_NFA.Epsilon] = set(list(["q%d"%(self.lastNode+1)]))
                self.lastNode += 1
                right = desipherObject(object.right_expr)
                transitions[("q%d" % self.lastNode)] = {}
                transitions[("q%d" % self.lastNode)][right] = set(list(["q%d"%(self.lastNode+1)]))
                self.lastNode += 1
                transitions[("q%d" % self.lastNode)] = {}
                return self.Epsilon_NFA.Epsilon
            elif isinstance(object, ast.Or):
                root = self.lastNode
                transitions[("q%d" % self.lastNode)] = {}
                transitions[("q%d" % self.lastNode)][self.Epsilon_NFA.Epsilon] = set(list(["q%d"%(self.lastNode+1)]))
                self.lastNode += 1
                left = desipherObject(object.left_expr)
                transitions[("q%d" % self.lastNode)] = {}
                transitions[("q%d" % self.lastNode)][left] = set(list(["q%d" % (self.lastNode + 1)]))
                self.lastNode += 1
                transitions[("q%d" % self.lastNode)] = {}
                transitions[("q%d" % self.lastNode)][self.Epsilon_NFA.Epsilon] = set(list(["q%d"%(self.lastNode+1)]))
                self.lastNode += 1
                tail = self.lastNode
                transitions[("q%d"%root)][self.Epsilon_NFA.Epsilon] = transitions[("q%d"%root)][self.Epsilon_NFA.Epsilon] | set(list(["q%d"%(self.lastNode+1)]))
                self.lastNode += 1
                right = desipherObject(object.right_expr)
                transitions[("q%d" % self.lastNode)] = {}
                transitions[("q%d" % self.lastNode)][right] = set(list(["q%d" % (self.lastNode + 1)]))
                self.lastNode += 1
                transitions[("q%d" % self.lastNode)] = {}
                transitions[("q%d" % self.lastNode)][self.Epsilon_NFA.Epsilon] = set(list(["q%d"%(tail)]))
                transitions[("q%d" % tail)] = {}
                transitions[("q%d" % tail)][self.Epsilon_NFA.Epsilon] = set(list(["q%d" % (self.lastNode + 1)]))
                self.lastNode += 1
                transitions[("q%d" % self.lastNode)] = {}
                return self.Epsilon_NFA.Epsilon




        expression_tree.printable("")
        desipherObject(expression_tree)
        states = list()
        for node in range(self.lastNode+1):
            states.append("q%d"%(node)) ##Change to |=
        states = set(states)
        input_symbols = set()
        for node in transitions:
            input_symbols = input_symbols | set(transitions[node])
        initial_states = set(list(["q0"]))
        final_states = set(list(["q%d" % self.lastNode]))

        self.Epsilon_NFA(self.parent(), Automata_BARE(states, input_symbols, transitions, initial_states, final_states))


