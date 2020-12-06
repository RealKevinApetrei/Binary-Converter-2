# ///////////////////////////////////////////////////////////////////// #
# MADE BY KEVIN APETREI # MADE BY KEVIN APETREI # MADE BY KEVIN APETREI #
# ///////////////////////////////////////////////////////////////////// #

# pylint: disable=E1101

import sys

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *

from files.ui_main import Ui_MainWindow


GLOBAL_STATE = 0


class MainWindow(QMainWindow): # Main Window
    def __init__(self): # Main initialisation
        super(MainWindow, self).__init__() # Call superclass

        # UI Setup
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self) 

        # Move Window
        def move_window(event):
            # Restore Window (before movement)
            if UIFunctions.return_status(self) == 1: # If maximized
                UIFunctions.maximize_restore(self)
                # QCursor.setPos(self.previous_cursor_pos)

            if event.buttons() == Qt.LeftButton: # If Left Click (move window)
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        # Set Title Bar
        self.ui.title_bar.mouseMoveEvent = move_window

        # Set UI Definitions
        UIFunctions.ui_definitions(self)

        self.show() # Show main window

    def mousePressEvent(self, event): # Mouse Press Event
        self.dragPos = event.globalPos()


class UIFunctions(MainWindow):
    def maximize_restore(self): # Restore Maximize
        global GLOBAL_STATE
        status = GLOBAL_STATE

        if status == 0: # If maximized
            GLOBAL_STATE = 1

            # self.previous_cursor_pos = QCursor.pos()
            # print(self.previous_cursor_pos)
            self.showMaximized()

            # Remove Margins and Border Radius
            self.ui.drop_shadow_layout.setContentsMargins(0, 0, 0, 0)
            self.ui.drop_shadow_frame.setStyleSheet("border-radius: 0px; background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(123, 180, 180, 255), stop:1 rgba(159, 226, 226, 255));")
            
            self.ui.button_max.setToolTip("Restore")
        
        else: # If not maximised
            GLOBAL_STATE = 0
            
            self.showNormal()
            
            # Add Margins and Border Radius
            self.resize(self.width() + 1, self.height() + 1)
            self.ui.drop_shadow_layout.setContentsMargins(10, 10, 10, 10)
            self.ui.drop_shadow_frame.setStyleSheet("border-radius: 10px; background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(123, 180, 180, 255), stop:1 rgba(159, 226, 226, 255));")
            
            self.ui.button_max.setToolTip("Maximize")

    def convert_binary_to_text(self): # Convert Binary to Text
        contents = self.ui.text_edit_binary.toPlainText().split() # Current Entry Data
        text_string = "" # Initialise Text String (Output)

        self.ui.text_edit_text.textChanged.disconnect()

        try:
            for value in contents:
                text_string += chr(int(value, 2)) # Find Chr value of each binary value and add to output string
        except:
            text_string = "INVALID"
        finally:
            try:
                self.ui.text_edit_text.setPlainText(text_string) # Set converted data
            except:
                self.ui.text_edit_text.setPlainText("INVALID")
            finally:
                self.ui.text_edit_text.textChanged.connect(lambda: UIFunctions.convert_text_to_binary(self))


    def convert_text_to_binary(self): # Conver Text to Binary
        contents = self.ui.text_edit_text.toPlainText() # Current Entry Data
        
        self.ui.text_edit_binary.textChanged.disconnect()

        if not contents == "INVALID":
            try:
                binary_list = [f"{ord(i):08b}" for i in contents] # Binary List (Output)
            except:
                binary_list = ["INVALID"]
            finally:
                self.ui.text_edit_binary.setPlainText(" ".join(binary_list)) # Set converted data
                self.ui.text_edit_binary.textChanged.connect(lambda: UIFunctions.convert_binary_to_text(self))

    def return_status(self): # Return window status (if maximized or restarted)
        return GLOBAL_STATE

    def ui_definitions(self): # UI Definitions
        # Remove Title Bar
        self.setWindowFlag(Qt.FramelessWindowHint) 
        self.setAttribute(Qt.WA_TranslucentBackground)

        # Set Dropshadow Window
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 100))
        
        # Apply Dropshadow to Frame
        self.ui.drop_shadow_frame.setGraphicsEffect(self.shadow)

        # Maximize / Restore
        self.ui.button_max.clicked.connect(lambda: UIFunctions.maximize_restore(self))

        # Minimize
        self.ui.button_min.clicked.connect(lambda: self.showMinimized())

        # Close
        self.ui.button_exit.clicked.connect(lambda: self.close())

        # Detect change in Binary
        self.ui.text_edit_binary.textChanged.connect(lambda: UIFunctions.convert_binary_to_text(self))

        # Detect change in Text
        self.ui.text_edit_text.textChanged.connect(lambda: UIFunctions.convert_text_to_binary(self))

        # Create size grip to resize window
        self.sizegrip = QSizeGrip(self.ui.frame_grip)
        self.sizegrip.setStyleSheet("QSizeGrip { width: 10px; height: 10px; margin: 5px; } QSizeGrip:hover { background-color: rgb(117, 170, 170); }")
        self.sizegrip.setToolTip("Resize Window")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()

    sys.exit(app.exec_())

# ///////////////////////////////////////////////////////////////////// #
# MADE BY KEVIN APETREI # MADE BY KEVIN APETREI # MADE BY KEVIN APETREI #
# ///////////////////////////////////////////////////////////////////// #
