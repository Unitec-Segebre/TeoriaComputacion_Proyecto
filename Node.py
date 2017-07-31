from PyQt5.QtWidgets import QGraphicsItem, QStyle
from PyQt5.QtCore import QPointF, Qt, QRectF
from PyQt5.QtGui import QPen, QRadialGradient, QBrush, QColor, QPainterPath

class Node(QGraphicsItem):
    Type = QGraphicsItem.UserType + 1

    def __init__(self, graphWidget):
        super(Node, self).__init__()

        self.graph = graphWidget
        self.edgeList = []
        self.newPos = QPointF()
        self.__draw_size = 40

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
            gradient.setColorAt(1, QColor(Qt.yellow)) #.light(120))
            gradient.setColorAt(0, QColor(Qt.darkYellow)) #.light(120))
        else:
            gradient.setColorAt(0, Qt.yellow)
            gradient.setColorAt(1, Qt.darkYellow)

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

    #Uncomment to color when clicked
    # def mousePressEvent(self, event):
    #     self.update()
    #     super(Node, self).mousePressEvent(event)
    #
    # def mouseReleaseEvent(self, event):
    #     self.update()
    #     super(Node, self).mouseReleaseEvent(event)


