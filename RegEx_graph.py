from PyQt5.QtWidgets import QMessageBox, QInputDialog, QLineEdit

class RegEx_graph(QInputDialog):
    def __init__(self, parent=None, expresion=None):
        super(RegEx_graph, self).__init__(parent)
        self.setWindowTitle("Regular Expression")
        if expresion == "()*":
            expresion = "The only solution is no input!"
        self.getText(parent, "Regular Expression to Epsilon NFA", "Expression:", QLineEdit.Normal, expresion)
        # self.setText(expresion)
        # self.setStandardButtons(QMessageBox.Ok)
        # self.show()