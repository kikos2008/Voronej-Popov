def main():
    import sys
    from random import randint
    from PyQt6 import uic
    from PyQt6.QtGui import QPainter, QColor, QBrush
    from PyQt6.QtCore import QRectF
    from PyQt6.QtWidgets import QApplication, QMainWindow
    from PyQt6.QtCore import Qt

    class MyNotes(QMainWindow):
        def __init__(self):
            super().__init__()
            uic.loadUi('UI.ui', self)
            self.color = QColor(255, 255, 0)
            self.do_paint = False
            self.btn.clicked.connect(self.paint)

        def paintEvent(self, event):
            if self.do_paint:
                qp = QPainter()
                qp.begin(self)
                qp.setPen(self.color)
                brush = QBrush(self.color, Qt.BrushStyle.SolidPattern)
                qp.setBrush(brush)
                self.draw_circles(qp)
                qp.end()

        def paint(self):
            self.do_paint = True
            self.repaint()

        def draw_circles(self, qp):
            self.do_paint = False
            side = randint(20, 400)
            cords = (randint(0, 800 - side), randint(0, 600 - side))
            rectangle = QRectF(cords[0], cords[1], side, side)
            qp.drawEllipse(rectangle)

    app = QApplication(sys.argv)
    ex = MyNotes()
    ex.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()