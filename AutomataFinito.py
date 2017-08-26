import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog
from ui_mainwindow import Ui_MainWindow
from GraphGenerator import GraphGenerator
from NFA_graph import NFA_graph
from NFAEpsilon_graph import NFAEpsilon_graph
from RegEx_graph import RegEx_graph
import pickle

class Main(QMainWindow, Ui_MainWindow):
    def __init__(self, app):
        super(Main, self).__init__()
        self.setupUi(self)

        self.actionNew.triggered.connect(self.new)
        self.actionNew.setShortcut("Ctrl+n")

        self.actionOpen.triggered.connect(self.open)
        self.actionOpen.setShortcut("Ctrl+o")

        self.actionExit.triggered.connect(quit)
        self.actionExit.setShortcut("Ctrl+q")

        self.show()
        sys.exit(app.exec_())

    def new(self):
        GraphGenerator(self)

    def open(self):
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
                GraphGenerator(self, items, file_name)
            return
        except Exception as exception:
            QMessageBox.warning(self, "Open graph", "%s." % (exception))
            print(exception)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    Main(app)