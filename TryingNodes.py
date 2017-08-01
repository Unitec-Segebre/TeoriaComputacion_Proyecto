from PyQt5.QtWidgets import QApplication, QGraphicsView, QGraphicsScene
from PyQt5.QtGui import QPainter
from PyQt5.QtCore import QTime, qsrand

from Node import Node
from Edge import Edge


class GraphWidget(QGraphicsView):
    def __init__(self, parent=None):
        super(GraphWidget, self).__init__(parent)
        self.timerId = 0

        scene = QGraphicsScene(self)
        scene.setItemIndexMethod(QGraphicsScene.NoIndex)
        scene.setSceneRect(10, 0, 781, 571)
        self.setScene(scene)
        self.setCacheMode(QGraphicsView.CacheBackground)
        self.setViewportUpdateMode(QGraphicsView.BoundingRectViewportUpdate)
        self.setRenderHint(QPainter.Antialiasing)
        self.setTransformationAnchor(QGraphicsView.AnchorUnderMouse)
        self.setResizeAnchor(QGraphicsView.AnchorViewCenter)

        node1 = Node(self)
        node2 = Node(self)
        # node3 = Node(self)
        # node4 = Node(self)
        # self.centerNode = Node(self)
        # node6 = Node(self)
        # node7 = Node(self)
        # node8 = Node(self)
        # node9 = Node(self)
        scene.addItem(node1)
        scene.addItem(node2)
        # scene.addItem(node3)
        # scene.addItem(node4)
        # scene.addItem(self.centerNode)
        # scene.addItem(node6)
        # scene.addItem(node7)
        # scene.addItem(node8)
        # scene.addItem(node9)
        scene.addItem(Edge(node1, node2))
        # scene.addItem(Edge(node2, node3))
        # scene.addItem(Edge(node2, self.centerNode))
        # scene.addItem(Edge(node3, node6))
        # scene.addItem(Edge(node4, node1))
        # scene.addItem(Edge(node4, self.centerNode))
        # scene.addItem(Edge(self.centerNode, node6))
        # scene.addItem(Edge(self.centerNode, node8))
        # scene.addItem(Edge(node6, node9))
        # scene.addItem(Edge(node7, node4))
        # scene.addItem(Edge(node8, node7))
        # scene.addItem(Edge(node9, node8))

        node1.setPos(-50, -50)
        node2.setPos(0, -50)
        # node3.setPos(50, -50)
        # node4.setPos(-50, 0)
        # self.centerNode.setPos(0, 0)
        # node6.setPos(50, 0)
        # node7.setPos(-50, 50)
        # node8.setPos(0, 50)
        # node9.setPos(50, 50)

        self.scale(0.8, 0.8)
        self.setMinimumSize(400, 400)
        self.setWindowTitle("Elastic Nodes")

    def timerEvent(self, event):
        nodes = [item for item in self.scene().items() if isinstance(item, Node)]

        # for node in nodes:
        #     node.calculateForces()

        print (len(nodes))

        itemsMoved = False
        for node in nodes: pass
            # if node.advance():
            #     itemsMoved = True

        if not itemsMoved:
            self.killTimer(self.timerId)
            self.timerId = 0
    #
    def itemMoved(self):
        if not self.timerId:
            self.timerId = self.startTimer(1000 / 25)

    def add_node(self):
        self.scene().addItem(Node(self))

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    # qsrand(QTime(0, 0, 0).secsTo(QTime.currentTime()))

    widget = GraphWidget()
    widget.show()

    sys.exit(app.exec_())