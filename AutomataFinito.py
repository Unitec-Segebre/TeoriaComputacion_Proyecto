import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog
from ui_mainwindow import Ui_MainWindow
from DFA_graph import DFA_graph
from NFA_graph import NFA_graph
from NFAEpsilon_graph import NFAEpsilon_graph
from RegEx_graph import RegEx_graph
import pickle

class Main(QMainWindow, Ui_MainWindow):
    def __init__(self, app):
        super(Main, self).__init__()
        self.setupUi(self)

        self.actionDFA.triggered.connect(self.new_DFA_graph)
        self.actionDFA.setShortcut("Ctrl+1")

        self.actionNFA.triggered.connect(self.new_NFA_graph)
        self.actionNFA.setShortcut("Ctrl+2")

        self.actionNFA_Epsilon.triggered.connect(self.new_NFAEpsilon_graph)
        self.actionNFA_Epsilon.setShortcut("Ctrl+3")

        self.actionRegular_Expression.triggered.connect(self.new_RegularExpression_graph)

        self.actionDFA_2.triggered.connect(self.open_DFA_graph)
        self.actionNFA_2.triggered.connect(self.open_NFA_graph)
        self.actionNFA_Epsilon_2.triggered.connect(self.open_NFAEpsilon_graph)

        self.show()
        sys.exit(app.exec_())

    def new_DFA_graph(self):
        DFA_graph(self)

    def open_DFA_graph(self):
        self.open_graph(DFA_graph)

    def new_NFA_graph(self):
        NFA_graph(self)

    def open_NFA_graph(self):
        self.open_graph(NFA_graph)

    def new_NFAEpsilon_graph(self):
        NFAEpsilon_graph(self)

    def open_NFAEpsilon_graph(self):
        self.open_graph(NFAEpsilon_graph)

    def new_RegularExpression_graph(self):
        RegEx_graph(self, "", NFAEpsilon_graph)

    def open_graph(self, function):
        try:
            file_name = QFileDialog.getOpenFileName(self, 'Open graph')[0]
            if file_name != '':
                file = open(str(file_name), 'rb')
                items = None
                try:
                    items = pickle.load(file)
                except:
                    QMessageBox.critical(self, "Open graph", "The file '%s' was not generated by this program." % (file_name))
                    return
                file.close()
                function(self, items, file_name)
            return
        except Exception as exception:
            QMessageBox.warning(self, "Open graph", "%s." % (exception))
            print(exception)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    Main(app)