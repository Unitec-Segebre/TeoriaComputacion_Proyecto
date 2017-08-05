import math
from PyQt5.QtWidgets import QGraphicsItem
from PyQt5.QtCore import Qt, QPointF, QLineF, QRectF, QSizeF
from PyQt5.QtGui import QPolygonF, QPen

class Edge(QGraphicsItem):
    Pi = math.pi
    TwoPi = Pi * 2.0

    Type = QGraphicsItem.UserType + 2

    def __init__(self, sourceNode, destNode, condition=None):
        super(Edge, self).__init__()

        self.arrowSize = sourceNode.getDrawSize()*0.35
        self.sourcePoint = QPointF()
        self.destPoint = QPointF()
        self.setAcceptedMouseButtons(Qt.NoButton)
        self.source = sourceNode
        self.dest = destNode
        self.condition = condition
        self.source.addEdge(self)
        if self.source not in self.dest.getNodesToUpdate():
            self.dest.addNodeToUpdate(self.source)

        self.adjust()

    def type(self):
        return Edge.Type

    def sourceNode(self):
        return self.source

    def setSourceNode(self, node):
        self.source = node
        self.adjust()

    def destNode(self):
        return self.dest

    def setDestNode(self, node):
        self.dest = node
        self.adjust()

    def adjust(self):
        if not self.source or not self.dest:
            return

        line = QLineF(self.mapFromItem(self.source, self.source.getDrawSize()*-0.5, self.source.getDrawSize()*-0.5), self.mapFromItem(self.dest, self.dest.getDrawSize()*-0.5, self.dest.getDrawSize()*-0.5))
        length = line.length()

        self.prepareGeometryChange()

        if length > self.source.getDrawSize():
            edgeOffset = QPointF((line.dx() * self.source.getDrawSize()/2) / length,
                                        (line.dy() * self.source.getDrawSize()/2) / length)

            self.sourcePoint = line.p1() + edgeOffset
            self.destPoint = line.p2() - edgeOffset
        else:
            self.sourcePoint = line.p1()
            self.destPoint = line.p1()

    def boundingRect(self):
        if not self.source or not self.dest:
            return QRectF()

        penWidth = 1.0
        extra = (penWidth + self.arrowSize) / 2.0

        return QRectF(self.sourcePoint, QSizeF(self.destPoint.x() - self.sourcePoint.x(), self.destPoint.y() - self.sourcePoint.y())).normalized().adjusted(-extra, -extra, extra, extra)

    # noinspection PyMethodOverriding
    def paint(self, painter, option, widget):
        if not self.source or not self.dest:
            return

        # Draw the line itself.
        line = QLineF(self.sourcePoint, self.destPoint)

        if line.length() == 0.0:
            return

        painter.setPen(QPen(Qt.black, 1, Qt.SolidLine,
                                  Qt.RoundCap, Qt.RoundJoin))
        painter.drawLine(line)

        # Draw the arrows if there's enough room.
        angle = math.acos(line.dx() / line.length())
        if line.dy() >= 0:
            angle = Edge.TwoPi - angle

        destArrowP1 = self.destPoint + QPointF(math.sin(angle - Edge.Pi / 3) * self.arrowSize, math.cos(angle - Edge.Pi / 3) * self.arrowSize)
        destArrowP2 = self.destPoint + QPointF(math.sin(angle - Edge.Pi + Edge.Pi / 3) * self.arrowSize, math.cos(angle - Edge.Pi + Edge.Pi / 3) * self.arrowSize)

        conditionPoint = self.sourcePoint + QPointF(math.sin(angle + Edge.Pi / 3) * self.arrowSize * 2, math.cos(angle + Edge.Pi / 3) * self.arrowSize * 2)
        textToPrint = self.condition
        for path in self.source.edges():
            if path.destNode().name == self.dest.name and path.condition != self.condition:
                textToPrint += ", %c"%(path.condition)
                if path.condition > self.condition:
                    return

        painter.setBrush(Qt.black)
        painter.drawPolygon(QPolygonF([line.p2(), destArrowP1, destArrowP2]))
        painter.drawText(conditionPoint, textToPrint)