from GraphGenerator import GraphGenerator
from AutomataSolver import Automata_NFA

class NFA_graph(GraphGenerator):
    def __init__(self, parent=None, load=None):
        super(NFA_graph, self).__init__(parent, "NFA", load)

    def solve(self):
        super(NFA_graph, self).solve(Automata_NFA)