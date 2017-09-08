
class Digit:
    def __init__(self, number):
        self.number = number

    def printable(self, padding):
        print (padding,"digit: ",self.number)

class Letter:
    def __init__(self, letter):
        self.letter = letter

    def printable(self, padding):
        print (padding,"letter: ",self.letter)

class Kleene:
    def __init__(self, expression):
        self.expression = expression

    def printable(self, padding):
        print (padding,"klenne: ")
        print(padding,"expr-"),self.expression.printable(padding+"\t")

class Concat:
    def __init__(self, left_expr, right_expr):
        self.left_expr = left_expr
        self.right_expr = right_expr

    def printable(self, padding):
        print (padding,"concat: ")
        print(padding,"left_expr:-"),self.left_expr.printable(padding+"\t")
        print(padding,"right_expr:-"),self.right_expr.printable(padding+"\t")

class Or:
    def __init__(self, left_expr, right_expr):
        self.left_expr = left_expr
        self.right_expr = right_expr

    def printable(self, padding):
        print (padding, "or: ")
        print(padding,"left_expr:-"),self.left_expr.printable(padding+"\t")
        print(padding,"right_expr:-"),self.right_expr.printable(padding+"\t")
