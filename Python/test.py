from PyQt5 import QtCore, QtGui, QtWidgets

class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        layout = QtWidgets.QGridLayout(self)

        self.label = QtWidgets.QLabel()
        layout.addWidget(self.label)
        self.label.setPixmap(QtGui.QPixmap('myimage.png'))
        self.label.installEventFilter(self)

        self.cursorPos = None
        # I'm using the crosshair cursor as shown at
        # https://doc.qt.io/qt-5/qt.html#CursorShape-enum
        self.cursorPixmap = QtGui.QPixmap('cursor-cross.png')

    def eventFilter(self, source, event):
        if event.type() == QtCore.QEvent.MouseButtonPress:
            # set the current position and schedule a repaint of the label
            self.cursorPos = event.pos()
            self.label.update()
        elif event.type() == QtCore.QEvent.Paint:
            # intercept the paintEvent of the label and call the base
            # implementation to actually draw its contents
            self.label.paintEvent(event)
            if self.cursorPos is not None:
                # if the cursor position has been set, draw it
                qp = QtGui.QPainter(self.label)
                # translate the painter at the cursor position
                qp.translate(self.cursorPos)
                # paint the pixmap at an offset based on its center
                qp.drawPixmap(-self.cursorPixmap.rect().center(), self.cursorPixmap)
            return True
        return super().eventFilter(source, event)


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())