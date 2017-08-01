from PyQt5.QtWidgets import QGraphicsItem, QGraphicsProxyWidget, QStyle, QLabel
from PyQt5.QtCore import QPointF, Qt, QRectF, QRect
from PyQt5.QtGui import QPen, QRadialGradient, QBrush, QColor, QPainterPath, QFont
from Edge import Edge
from itertools import count
from enum import Enum

class State(Enum):
    INITIAL = 0
    TRANSITION = 1
    FINAL = 2

class Node(QGraphicsItem):
    Type = QGraphicsItem.UserType + 1
    __draw_size = 40
    __node_count = count(0)

    def __init__(self, graphWidget, name=None, state=State.TRANSITION):
        super(Node, self).__init__()

        self.graph = graphWidget
        self.edgeList = []
        self.newPos = QPointF()
        self.name = ("Unnamed %d"%(next(self.__node_count))) if (name is None) else name
        self.state = state
        self.nodesToUpdate = []

        font = QFont()
        font.setBold(True)
        font.setPointSize(self.__draw_size*0.2)
        line = QLabel(self.name)
        line.setGeometry(-self.__draw_size*0.7, -self.__draw_size*0.8, self.__draw_size, self.__draw_size*0.5)
        line.setAttribute(Qt.WA_TranslucentBackground)
        line.setFont(font)
        prox = QGraphicsProxyWidget(self)
        prox.setWidget(line)

        self.setFlag(QGraphicsItem.ItemIsMovable)
        self.setFlag(QGraphicsItem.ItemSendsGeometryChanges)
        self.setCacheMode(QGraphicsItem.DeviceCoordinateCache)
        self.setZValue(1)

    # noinspection PyMethodOverriding
    def paint(self, painter, option, widget):
        start_draw = -self.__draw_size
        end_draw = self.__draw_size

        painter.setPen(Qt.NoPen)
        painter.setBrush(Qt.darkGray)
        painter.drawEllipse(start_draw+3, start_draw+3, end_draw, end_draw)

        gradient = QRadialGradient(start_draw*0.6, start_draw*0.6, end_draw/2)
        if option.state & QStyle.State_Sunken:
            gradient.setCenter(3, 3)
            gradient.setFocalPoint(3, 3)
            if self.state == State.INITIAL:
                gradient.setColorAt(1, QColor(Qt.blue)) #.light(120))
                gradient.setColorAt(0, QColor(Qt.darkBlue)) #.light(120))
            elif self.state == State.TRANSITION:
                gradient.setColorAt(1, QColor(Qt.yellow))  # .light(120))
                gradient.setColorAt(0, QColor(Qt.darkYellow))  # .light(120))
            elif self.state == State.FINAL:
                gradient.setColorAt(1, QColor(Qt.green))  # .light(120))
                gradient.setColorAt(0, QColor(Qt.darkGreen))  # .light(120))
        else:
            if self.state == State.INITIAL:
                gradient.setColorAt(1, QColor(Qt.blue)) #.light(120))
                gradient.setColorAt(0, QColor(Qt.darkBlue)) #.light(120))
            elif self.state == State.TRANSITION:
                gradient.setColorAt(1, QColor(Qt.yellow))  # .light(120))
                gradient.setColorAt(0, QColor(Qt.darkYellow))  # .light(120))
            elif self.state == State.FINAL:
                gradient.setColorAt(1, QColor(Qt.green))  # .light(120))
                gradient.setColorAt(0, QColor(Qt.darkGreen))  # .light(120))

        painter.setBrush(QBrush(gradient))
        painter.setPen(QPen(Qt.black, 0))
        painter.drawEllipse(start_draw, start_draw, end_draw, end_draw)

    def boundingRect(self):
        adjust = 2.0
        start_draw = -self.__draw_size
        end_draw = self.__draw_size + 3
        return QRectF(start_draw - adjust, start_draw - adjust, end_draw + adjust,
                      end_draw + adjust)

    def shape(self):
        path = QPainterPath()
        path.addEllipse(-self.__draw_size, -self.__draw_size, self.__draw_size, self.__draw_size)
        return path

    def type(self):
        return Node.Type

    def advance(self):
        if self.newPos == self.pos():
            return False

        self.setPos(self.newPos)
        return True

    def addEdge(self, edge):
        self.edgeList.append(edge)
        edge.adjust()

    def edges(self):
        return self.edgeList

    def itemChange(self, change, value):
        if change == QGraphicsItem.ItemPositionHasChanged:
            for edge in self.edgeList:
                edge.adjust()
            for node in self.nodesToUpdate:
                for edge_back in node.edges():
                    edge_back.adjust()
                # self.graph.itemMoved()
        return super(Node, self).itemChange(change, value)

    def getDrawSize(self):
        return self.__draw_size

    def setState(self, state):
        self.state = state

    def addNodeToUpdate(self, node):
        self.nodesToUpdate.append(node)

        #Uncomment to color when clicked
        # def mousePressEvent(self, event):
        #     self.update()
        #     super(Node, self).mousePressEvent(event)
        #
        # def mouseReleaseEvent(self, event):
        #     self.update()
        #     super(Node, self).mouseReleaseEvent(event)


