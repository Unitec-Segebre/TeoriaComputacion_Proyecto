import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog
from ui_descriptionwindow import Ui_MainWindow
from GraphGenerator import GraphGenerator
import pickle

class Main(QMainWindow, Ui_MainWindow):
    def __init__(self, app):
        super(Main, self).__init__()
        self.setupUi(self)

        self.button_add.clicked.connect(self.add)

        self.show()
        sys.exit(app.exec_())

    def new(self):
        GraphGenerator(self)

    def add(self):
        producer = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        producer.setObjectName("producer1")
        self.horizontalLayout.addWidget(producer)
        label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        label.setObjectName("label1")
        self.horizontalLayout.addWidget(label)
        production = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        production.setObjectName("production1")
        self.horizontalLayout.addWidget(production)