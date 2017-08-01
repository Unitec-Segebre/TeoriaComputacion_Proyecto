import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from ui_mainwindow import Ui_MainWindow
from DFA_graph import DFA_graph

class Main(QMainWindow, Ui_MainWindow):
    def __init__(self, app):
        super(Main, self).__init__()
        self.setupUi(self)

        self.actionAFD.triggered.connect(self.new_DFA_graph)


        self.show()
        sys.exit(app.exec_())

    def new_DFA_graph(self):
        DFA_graph(self)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    Main(app)