import Edge

class PDAEdge(Edge.Edge):

    Type = Edge.QGraphicsItem.UserType + 3

    def __init__(self, sourceNode, destNode, condition=None, popValue = None, pushValues = None):
        super().__init__(sourceNode, destNode, condition)

        self.popValue = popValue
        self.pushValues = pushValues

        print("Source: %s\nDest: %s\nCondition: %c\npopValue: %c\npushValues: %s\n"%(sourceNode.name, destNode.name, condition, popValue, pushValues))

    def getCondition(self):
        return self.condition

    # noinspection PyMethodOverriding
    def paint(self, painter, option, widget):
        if not self.source or not self.dest:
            return

        # Draw the line itself.
        line = Edge.QLineF(self.sourcePoint, self.destPoint)

        if line.length() == 0.0:
            return

        painter.setPen(Edge.QPen(Edge.Qt.black, 1, Edge.Qt.SolidLine,
                            Edge.Qt.RoundCap, Edge.Qt.RoundJoin))
        painter.drawLine(line)

        # Draw the arrows if there's enough room.
        angle = Edge.math.acos(line.dx() / line.length())
        if line.dy() >= 0:
            angle = Edge.Edge.TwoPi - angle

        destArrowP1 = self.destPoint + Edge.QPointF(Edge.math.sin(angle - Edge.Edge.Pi / 3) * self.arrowSize, Edge.math.cos(angle - Edge.Edge.Pi / 3) * self.arrowSize)
        destArrowP2 = self.destPoint + Edge.QPointF(Edge.math.sin(angle - Edge.Edge.Pi + Edge.Edge.Pi / 3) * self.arrowSize, Edge.math.cos(angle - Edge.Edge.Pi + Edge.Edge.Pi / 3) * self.arrowSize)

        conditionPoint = self.sourcePoint + Edge.QPointF(Edge.math.sin(angle + Edge.Edge.Pi / 3) * self.arrowSize * 2, Edge.math.cos(angle + Edge.Edge.Pi / 3) * self.arrowSize * 2)
        textToPrint = "%c,%c/%s"%(self.condition, self.popValue, self.pushValues)
        for path in self.source.edges():
            if path.destNode().name == self.dest.name and path.condition != self.condition:
                textToPrint += " | %c,%c/%s"%(self.condition, self.popValue, self.pushValues)
                if path.condition > self.condition:
                    return

        painter.setBrush(Edge.Qt.black)
        painter.drawPolygon(Edge.QPolygonF([line.p2(), destArrowP1, destArrowP2]))
        painter.drawText(conditionPoint, textToPrint)