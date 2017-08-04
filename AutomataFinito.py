import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog
from ui_mainwindow import Ui_MainWindow
from DFA_graph import DFA_graph
import pickle

class Main(QMainWindow, Ui_MainWindow):
    def __init__(self, app):
        super(Main, self).__init__()
        self.setupUi(self)

        self.actionAFD.triggered.connect(self.new_DFA_graph)
        self.actionAFD.setShortcut("Ctrl+1")

        self.actionOpen.triggered.connect(self.open_DFA_graph)


        self.show()
        sys.exit(app.exec_())

    def new_DFA_graph(self):
        DFA_graph(self)

    def open_DFA_graph(self):
        try:
            file_name = QFileDialog.getOpenFileName(self, 'Open graph')[0]
            if file_name != '':
                file = open(str(file_name), 'rb')
                items = pickle.load(file)
                file.close()
                DFA_graph(self, items)
            return
        except Exception as exception:
            QMessageBox.warning(self, "Open graph", "%s." % (exception))
            print(exception)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    Main(app)