# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'qt_ui_betarZxwEi.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *

from . import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1051, 762)
        icon = QIcon()
        icon.addFile(u":/images/file_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(880, 600))
        self.drop_shadow_layout = QGridLayout(self.centralwidget)
        self.drop_shadow_layout.setObjectName(u"drop_shadow_layout")
        self.drop_shadow_layout.setContentsMargins(10, 10, 10, 10)
        self.drop_shadow_frame = QFrame(self.centralwidget)
        self.drop_shadow_frame.setObjectName(u"drop_shadow_frame")
        self.drop_shadow_frame.setStyleSheet(u"border-radius: 10px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(123, 180, 180, 255), stop:1 rgba(159, 226, 226, 255));")
        self.drop_shadow_frame.setFrameShape(QFrame.NoFrame)
        self.drop_shadow_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.drop_shadow_frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.title_bar = QFrame(self.drop_shadow_frame)
        self.title_bar.setObjectName(u"title_bar")
        self.title_bar.setMaximumSize(QSize(16777215, 50))
        self.title_bar.setStyleSheet(u"background-color: rgb(123, 177, 177);\n"
"border-radius: 10px;")
        self.title_bar.setFrameShape(QFrame.HLine)
        self.title_bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.title_bar)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_title = QFrame(self.title_bar)
        self.frame_title.setObjectName(u"frame_title")
        font = QFont()
        font.setFamily(u"Tw Cen MT Condensed Extra Bold")
        font.setPointSize(14)
        self.frame_title.setFont(font)
        self.frame_title.setFrameShape(QFrame.StyledPanel)
        self.frame_title.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_title)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(10, 0, 0, 0)
        self.label_title = QLabel(self.frame_title)
        self.label_title.setObjectName(u"label_title")
        self.label_title.setEnabled(True)
        font1 = QFont()
        font1.setFamily(u"Tw Cen MT Condensed Extra Bold")
        font1.setPointSize(14)
        font1.setBold(False)
        font1.setWeight(50)
        self.label_title.setFont(font1)
        self.label_title.setStyleSheet(u"color: rgb(56, 71, 104)")

        self.verticalLayout_2.addWidget(self.label_title)


        self.horizontalLayout.addWidget(self.frame_title)

        self.frame_buttons = QFrame(self.title_bar)
        self.frame_buttons.setObjectName(u"frame_buttons")
        self.frame_buttons.setMaximumSize(QSize(100, 16777215))
        self.frame_buttons.setFrameShape(QFrame.StyledPanel)
        self.frame_buttons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_buttons)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.button_min = QPushButton(self.frame_buttons)
        self.button_min.setObjectName(u"button_min")
        self.button_min.setMinimumSize(QSize(16, 16))
        self.button_min.setMaximumSize(QSize(17, 17))
        self.button_min.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"	\n"
"	background-color: rgb(103, 148, 148);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(164, 247, 111);\n"
"}")

        self.horizontalLayout_4.addWidget(self.button_min)

        self.button_max = QPushButton(self.frame_buttons)
        self.button_max.setObjectName(u"button_max")
        self.button_max.setMinimumSize(QSize(16, 16))
        self.button_max.setMaximumSize(QSize(17, 17))
        self.button_max.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"	background-color: rgb(103, 148, 148);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(255, 188, 80);\n"
"}")

        self.horizontalLayout_4.addWidget(self.button_max)

        self.button_exit = QPushButton(self.frame_buttons)
        self.button_exit.setObjectName(u"button_exit")
        self.button_exit.setMinimumSize(QSize(16, 16))
        self.button_exit.setMaximumSize(QSize(17, 17))
        self.button_exit.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"	\n"
"	background-color: rgb(103, 148, 148);\n"
"}\n"
"QPushButton:hover {\n"
"	\n"
"	background-color: rgb(249, 128, 58);\n"
"}")

        self.horizontalLayout_4.addWidget(self.button_exit)


        self.horizontalLayout.addWidget(self.frame_buttons)


        self.verticalLayout.addWidget(self.title_bar)

        self.content = QFrame(self.drop_shadow_frame)
        self.content.setObjectName(u"content")
        self.content.setStyleSheet(u"background-color: none;\n"
"border-radius: 10px;")
        self.content.setFrameShape(QFrame.StyledPanel)
        self.content.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.content)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.frame_pages = QFrame(self.content)
        self.frame_pages.setObjectName(u"frame_pages")
        self.frame_pages.setMinimumSize(QSize(0, 0))
        self.frame_pages.setMaximumSize(QSize(0, 16777215))
        self.frame_pages.setAutoFillBackground(False)
        self.frame_pages.setStyleSheet(u"background-color: rgb(123, 177, 177);")
        self.frame_pages.setFrameShape(QFrame.StyledPanel)
        self.frame_pages.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_pages)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(9, 9, 9, 9)
        self.home_page = QPushButton(self.frame_pages)
        self.home_page.setObjectName(u"home_page")
        self.home_page.setMinimumSize(QSize(0, 50))
        font2 = QFont()
        font2.setFamily(u"Yu Gothic UI Semibold")
        font2.setBold(True)
        font2.setWeight(75)
        self.home_page.setFont(font2)
        self.home_page.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(103, 148, 148);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(154, 222, 222);\n"
"}")

        self.verticalLayout_3.addWidget(self.home_page)

        self.credits_page = QPushButton(self.frame_pages)
        self.credits_page.setObjectName(u"credits_page")
        self.credits_page.setMinimumSize(QSize(0, 50))
        self.credits_page.setFont(font2)
        self.credits_page.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(103, 148, 148);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(154, 222, 222);\n"
"}")

        self.verticalLayout_3.addWidget(self.credits_page)

        self.frame_menu_holder = QFrame(self.frame_pages)
        self.frame_menu_holder.setObjectName(u"frame_menu_holder")
        self.frame_menu_holder.setFrameShape(QFrame.StyledPanel)
        self.frame_menu_holder.setFrameShadow(QFrame.Raised)

        self.verticalLayout_3.addWidget(self.frame_menu_holder)


        self.gridLayout_2.addWidget(self.frame_pages, 1, 0, 1, 1)

        self.stackedWidget = QStackedWidget(self.content)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background-color: none;")
        self.page_home = QWidget()
        self.page_home.setObjectName(u"page_home")
        font3 = QFont()
        font3.setFamily(u"Berlin Sans FB Demi")
        font3.setBold(True)
        font3.setWeight(75)
        self.page_home.setFont(font3)
        self.page_home.setStyleSheet(u"/* VERTICAL SCROLLBAR */\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(7, 174, 177);\n"
"    width: 14px;\n"
"    margin: 15px 0 15px 0;\n"
"	border-radius: 0px;\n"
" }\n"
"\n"
"/*  HANDLE BAR VERTICAL */\n"
"QScrollBar::handle:vertical {	\n"
"	background-color: rgb(12, 109, 136);\n"
"	min-height: 30px;\n"
"	border-radius: 7px;\n"
"}\n"
"QScrollBar::handle:vertical:hover{	\n"
"	background-color: rgb(15, 146, 182);\n"
"}\n"
"QScrollBar::handle:vertical:pressed {	\n"
"	background-color: rgb(9, 158, 148);\n"
"}\n"
"\n"
"/* BTN TOP - SCROLLBAR */\n"
"QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"	background-color: rgb(6, 154, 124);\n"
"	height: 15px;\n"
"	border-top-left-radius: 7px;\n"
"	border-top-right-radius: 7px;\n"
"	subcontrol-position: top;\n"
"	subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical:hover {	\n"
"	background-color: rgb(6, 197, 156);\n"
"}\n"
"QScrollBar::sub-line:vertical:pressed {	\n"
"	background-color: rgb(4, 115, 91);\n"
"}\n"
"\n"
"/* BTN BO"
                        "TTOM - SCROLLBAR */\n"
"QScrollBar::add-line:vertical {\n"
"	border: none;\n"
"	background-color: rgb(6, 154, 124);\n"
"	height: 15px;\n"
"	border-bottom-left-radius: 7px;\n"
"	border-bottom-right-radius: 7px;\n"
"	subcontrol-position: bottom;\n"
"	subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-line:vertical:hover {	\n"
"	background-color: rgb(6, 197, 156);\n"
"}\n"
"QScrollBar::add-line:vertical:pressed {	\n"
"	background-color: rgb(4, 115, 91);\n"
"}\n"
"\n"
"/* RESET ARROW */\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"	background: none;\n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"	background: none;\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.gridLayout = QGridLayout(self.page_home)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(9, 15, -1, -1)
        self.frame_info_ascii = QFrame(self.page_home)
        self.frame_info_ascii.setObjectName(u"frame_info_ascii")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_info_ascii.sizePolicy().hasHeightForWidth())
        self.frame_info_ascii.setSizePolicy(sizePolicy)
        self.frame_info_ascii.setMinimumSize(QSize(100, 50))
        font4 = QFont()
        font4.setFamily(u"Yu Gothic UI")
        font4.setPointSize(12)
        font4.setBold(True)
        font4.setWeight(75)
        self.frame_info_ascii.setFont(font4)
        self.frame_info_ascii.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(96, 165, 172);\n"
"	border: 1px solid rgb(121, 248, 229);\n"
"	border-radius: 20px;\n"
"}\n"
"")
        self.frame_info_ascii.setFrameShape(QFrame.StyledPanel)
        self.frame_info_ascii.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_info_ascii)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_ascii = QLabel(self.frame_info_ascii)
        self.label_ascii.setObjectName(u"label_ascii")
        self.label_ascii.setMinimumSize(QSize(100, 25))
        font5 = QFont()
        font5.setFamily(u"Yu Gothic UI")
        font5.setPointSize(14)
        font5.setBold(True)
        font5.setWeight(75)
        self.label_ascii.setFont(font5)
        self.label_ascii.setStyleSheet(u"QLabel{\n"
"	border: none;\n"
"}")
        self.label_ascii.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.label_ascii)


        self.gridLayout.addWidget(self.frame_info_ascii, 1, 3, 1, 1)

        self.frame_info_binary = QFrame(self.page_home)
        self.frame_info_binary.setObjectName(u"frame_info_binary")
        sizePolicy.setHeightForWidth(self.frame_info_binary.sizePolicy().hasHeightForWidth())
        self.frame_info_binary.setSizePolicy(sizePolicy)
        self.frame_info_binary.setMinimumSize(QSize(200, 50))
        self.frame_info_binary.setFont(font4)
        self.frame_info_binary.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(96, 165, 172);\n"
"	border: 1px solid rgb(121, 248, 229);\n"
"	border-radius: 20px;\n"
"}\n"
"")
        self.frame_info_binary.setFrameShape(QFrame.StyledPanel)
        self.frame_info_binary.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_info_binary)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_binary = QLabel(self.frame_info_binary)
        self.label_binary.setObjectName(u"label_binary")
        self.label_binary.setFont(font5)
        self.label_binary.setStyleSheet(u"QLabel{\n"
"	border: none;\n"
"}")
        self.label_binary.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.label_binary)


        self.gridLayout.addWidget(self.frame_info_binary, 1, 1, 1, 1)

        self.text_edit_text = QTextEdit(self.page_home)
        self.text_edit_text.setObjectName(u"text_edit_text")
        font6 = QFont()
        font6.setFamily(u"Berlin Sans FB")
        font6.setPointSize(14)
        font6.setBold(False)
        font6.setWeight(50)
        self.text_edit_text.setFont(font6)
        self.text_edit_text.viewport().setProperty("cursor", QCursor(Qt.IBeamCursor))
        self.text_edit_text.setStyleSheet(u"QTextEdit{\n"
"	background-color: rgb(99, 143, 143);\n"
"}\n"
"QTextEdit:hover{\n"
"	background-color: rgb(115, 166, 166)\n"
"}\n"
"\n"
"QScrollBar{\n"
"	background-color: rgb(134, 193, 193);\n"
"}")
        self.text_edit_text.setTabChangesFocus(False)
        self.text_edit_text.setReadOnly(False)

        self.gridLayout.addWidget(self.text_edit_text, 0, 3, 1, 1)

        self.text_edit_binary = QTextEdit(self.page_home)
        self.text_edit_binary.setObjectName(u"text_edit_binary")
        self.text_edit_binary.setFont(font6)
        self.text_edit_binary.viewport().setProperty("cursor", QCursor(Qt.IBeamCursor))
        self.text_edit_binary.setStyleSheet(u"QTextEdit{\n"
"	background-color: rgb(99, 143, 143);\n"
"}\n"
"QTextEdit:hover{\n"
"	background-color: rgb(115, 166, 166)\n"
"}\n"
"\n"
"QScrollBar{\n"
"	background-color: rgb(134, 193, 193);\n"
"}")
        self.text_edit_binary.setTabChangesFocus(False)
        self.text_edit_binary.setReadOnly(False)

        self.gridLayout.addWidget(self.text_edit_binary, 0, 1, 1, 1)

        self.stackedWidget.addWidget(self.page_home)
        self.page_credits = QWidget()
        self.page_credits.setObjectName(u"page_credits")
        self.page_credits.setStyleSheet(u"background-color: none;")
        self.verticalLayout_5 = QVBoxLayout(self.page_credits)
        self.verticalLayout_5.setSpacing(6)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(9, 15, 9, 9)
        self.frame_content_credits = QFrame(self.page_credits)
        self.frame_content_credits.setObjectName(u"frame_content_credits")
        self.frame_content_credits.setStyleSheet(u"background-color: none;")
        self.frame_content_credits.setFrameShape(QFrame.StyledPanel)
        self.frame_content_credits.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_content_credits)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.circle_frame = QFrame(self.frame_content_credits)
        self.circle_frame.setObjectName(u"circle_frame")
        self.circle_frame.setEnabled(True)
        self.circle_frame.setMinimumSize(QSize(250, 250))
        self.circle_frame.setMaximumSize(QSize(250, 250))
        self.circle_frame.setStyleSheet(u"QFrame{\n"
"	border: 5px solid rgb(101, 216, 147);\n"
"	border-radius: 125px;\n"
"	background-color: rgb(172, 255, 243);\n"
"}\n"
"QFrame:hover{\n"
"	background-color: rgb(152, 225, 214)\n"
"}\n"
"")
        self.circle_frame.setFrameShape(QFrame.StyledPanel)
        self.circle_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.circle_frame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.credits_label = QLabel(self.circle_frame)
        self.credits_label.setObjectName(u"credits_label")
        self.credits_label.setMinimumSize(QSize(100, 0))
        font7 = QFont()
        font7.setFamily(u"Rockwell Extra Bold")
        font7.setPointSize(14)
        font7.setBold(True)
        font7.setWeight(75)
        self.credits_label.setFont(font7)
        self.credits_label.setStyleSheet(u"background-color: none; border: none;")
        self.credits_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.credits_label)


        self.horizontalLayout_5.addWidget(self.circle_frame)


        self.verticalLayout_5.addWidget(self.frame_content_credits)

        self.stackedWidget.addWidget(self.page_credits)

        self.gridLayout_2.addWidget(self.stackedWidget, 1, 1, 1, 1)

        self.frame_top = QFrame(self.content)
        self.frame_top.setObjectName(u"frame_top")
        self.frame_top.setMinimumSize(QSize(0, 30))
        self.frame_top.setFrameShape(QFrame.StyledPanel)
        self.frame_top.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_top)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.frame_menu_toggle = QFrame(self.frame_top)
        self.frame_menu_toggle.setObjectName(u"frame_menu_toggle")
        self.frame_menu_toggle.setMaximumSize(QSize(115, 16777215))
        self.frame_menu_toggle.setFrameShape(QFrame.StyledPanel)
        self.frame_menu_toggle.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_menu_toggle)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.button_menu_toggle = QPushButton(self.frame_menu_toggle)
        self.button_menu_toggle.setObjectName(u"button_menu_toggle")
        self.button_menu_toggle.setMinimumSize(QSize(50, 0))
        self.button_menu_toggle.setMaximumSize(QSize(40, 16777215))
        self.button_menu_toggle.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(96, 139, 139);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(143, 207, 207);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/images/menu_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_menu_toggle.setIcon(icon1)
        self.button_menu_toggle.setIconSize(QSize(32, 32))

        self.horizontalLayout_9.addWidget(self.button_menu_toggle)


        self.horizontalLayout_8.addWidget(self.frame_menu_toggle, 0, Qt.AlignLeft)

        self.frame_holder = QFrame(self.frame_top)
        self.frame_holder.setObjectName(u"frame_holder")
        self.frame_holder.setFrameShape(QFrame.StyledPanel)
        self.frame_holder.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_8.addWidget(self.frame_holder)


        self.gridLayout_2.addWidget(self.frame_top, 0, 0, 1, 2)


        self.verticalLayout.addWidget(self.content)

        self.credits_bar = QFrame(self.drop_shadow_frame)
        self.credits_bar.setObjectName(u"credits_bar")
        self.credits_bar.setMaximumSize(QSize(16777215, 30))
        self.credits_bar.setStyleSheet(u"background-color: rgb(123, 177, 177);\n"
"border-radius: 10px;")
        self.credits_bar.setFrameShape(QFrame.StyledPanel)
        self.credits_bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.credits_bar)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_credits = QFrame(self.credits_bar)
        self.frame_credits.setObjectName(u"frame_credits")
        self.frame_credits.setFrameShape(QFrame.StyledPanel)
        self.frame_credits.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_credits)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(10, 0, 0, 0)
        self.label_credits = QLabel(self.frame_credits)
        self.label_credits.setObjectName(u"label_credits")
        font8 = QFont()
        font8.setBold(True)
        font8.setItalic(True)
        font8.setWeight(75)
        self.label_credits.setFont(font8)
        self.label_credits.setStyleSheet(u"color: rgb(53, 77, 108);")

        self.horizontalLayout_3.addWidget(self.label_credits)


        self.horizontalLayout_2.addWidget(self.frame_credits)

        self.frame_grip = QFrame(self.credits_bar)
        self.frame_grip.setObjectName(u"frame_grip")
        self.frame_grip.setMinimumSize(QSize(30, 30))
        self.frame_grip.setMaximumSize(QSize(30, 30))
        self.frame_grip.setStyleSheet(u"padding: 5px;")
        self.frame_grip.setFrameShape(QFrame.StyledPanel)
        self.frame_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_2.addWidget(self.frame_grip)


        self.verticalLayout.addWidget(self.credits_bar)


        self.drop_shadow_layout.addWidget(self.drop_shadow_frame, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Binary Converter", None))
        self.label_title.setText(QCoreApplication.translate("MainWindow", u"Binary Converter", None))
#if QT_CONFIG(tooltip)
        self.button_min.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.button_min.setText("")
#if QT_CONFIG(tooltip)
        self.button_max.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.button_max.setText("")
#if QT_CONFIG(tooltip)
        self.button_exit.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.button_exit.setText("")
#if QT_CONFIG(whatsthis)
        self.content.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>QFrame{</p><p>    border: 5px rgb(150, 216, 216);</p><p>}</p><p><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.home_page.setText(QCoreApplication.translate("MainWindow", u"Home Page", None))
        self.credits_page.setText(QCoreApplication.translate("MainWindow", u"Credits Page", None))
        self.label_ascii.setText(QCoreApplication.translate("MainWindow", u"Text", None))
        self.label_binary.setText(QCoreApplication.translate("MainWindow", u"Binary", None))
        self.text_edit_text.setDocumentTitle("")
        self.text_edit_binary.setDocumentTitle("")
        self.credits_label.setText(QCoreApplication.translate("MainWindow", u"By Kevin Apetrei", None))
        self.button_menu_toggle.setText("")
        self.label_credits.setText(QCoreApplication.translate("MainWindow", u"Made by Kevin Apetrei | v.0.96-beta1", None))
    # retranslateUi

