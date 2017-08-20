from PyQt5.QtWidgets import QMessageBox

class RegEx_graph(QMessageBox):
    def __init__(self, parent=None, expresion=None):
        super(RegEx_graph, self).__init__(parent)
        self.setWindowTitle("Regular Expression")
        self.setText(expresion)
        self.setStandardButtons(QMessageBox.Ok)
        self.show()