def main():
    import sys
    from random import randint
    from PyQt6.QtGui import QPainter, QColor, QBrush
    from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
    from PyQt6.QtCore import Qt, QCoreApplication, QRectF

    class Circle_Randomer(QMainWindow):
        def __init__(self):
            super().__init__()
            self.ui = Ui_form()
            self.ui.setupUi(self)
            self.color = QColor(randint(0, 255), randint(0, 255), randint(0, 255))
            self.do_paint = False
            self.ui.btn.clicked.connect(self.paint)

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
            self.color = QColor(randint(0, 255), randint(0, 255), randint(0, 255))

    class Ui_form(object):
        def setupUi(self, Form):
            Form.setObjectName('Form')
            Form.resize(800, 600)
            Form.setMaximumSize(800, 600)
            Form.setMinimumSize(800, 600)

            self.btn = QPushButton('', parent=Form)
            self.btn.setGeometry(334, 500, 113, 31)

            self.retranslateUi(Form)

            self.btn.raise_()

        def retranslateUi(self, Form):
            _translate = QCoreApplication.translate
            Form.setWindowTitle(_translate("Form", "Circle Randomer"))
            self.btn.setText(_translate("Form", "Наририсовать круг"))

    app = QApplication(sys.argv)
    ex = Circle_Randomer()
    ex.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()