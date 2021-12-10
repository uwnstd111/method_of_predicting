# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interface2XnRtuP.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from pyqtgraph import PlotWidget
import pyqtgraph as pg
import icons_rc
import design_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(792, 774)
        icon = QIcon()
        icon.addFile(u":/Feather2/Feather2/trending-up.svg", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"*{\n"
"	border: none;\n"
"}")
        self.actionEdit = QAction(MainWindow)
        self.actionEdit.setObjectName(u"actionEdit")
        self.actionNew = QAction(MainWindow)
        self.actionNew.setObjectName(u"actionNew")
        self.actionSave = QAction(MainWindow)
        self.actionSave.setObjectName(u"actionSave")
        self.actionCopy = QAction(MainWindow)
        self.actionCopy.setObjectName(u"actionCopy")
        self.actionPaste = QAction(MainWindow)
        self.actionPaste.setObjectName(u"actionPaste")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMaximumSize(QSize(16666666, 16777215))
        self.centralwidget.setLayoutDirection(Qt.RightToLeft)
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.header_main_frame = QFrame(self.centralwidget)
        self.header_main_frame.setObjectName(u"header_main_frame")
        self.header_main_frame.setStyleSheet(u"background-color: rgb(0, 85, 127);")
        self.header_main_frame.setFrameShape(QFrame.NoFrame)
        self.header_main_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.header_main_frame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.header_right_frame = QFrame(self.header_main_frame)
        self.header_right_frame.setObjectName(u"header_right_frame")
        font = QFont()
        font.setBold(False)
        font.setWeight(50)
        self.header_right_frame.setFont(font)
        self.header_right_frame.setFrameShape(QFrame.StyledPanel)
        self.header_right_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.header_right_frame)
        self.horizontalLayout_2.setSpacing(11)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.close_window_button = QPushButton(self.header_right_frame)
        self.close_window_button.setObjectName(u"close_window_button")
        font1 = QFont()
        font1.setBold(True)
        font1.setWeight(75)
        self.close_window_button.setFont(font1)
        icon1 = QIcon()
        icon1.addFile(u":/Feather/x.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.close_window_button.setIcon(icon1)
        self.close_window_button.setIconSize(QSize(16, 16))

        self.horizontalLayout_2.addWidget(self.close_window_button)

        self.restore_window_button = QPushButton(self.header_right_frame)
        self.restore_window_button.setObjectName(u"restore_window_button")
        self.restore_window_button.setFont(font1)
        icon2 = QIcon()
        icon2.addFile(u":/Feather/maximize.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.restore_window_button.setIcon(icon2)
        self.restore_window_button.setIconSize(QSize(16, 16))

        self.horizontalLayout_2.addWidget(self.restore_window_button)

        self.minimaze_window_button = QPushButton(self.header_right_frame)
        self.minimaze_window_button.setObjectName(u"minimaze_window_button")
        self.minimaze_window_button.setFont(font1)
        icon3 = QIcon()
        icon3.addFile(u":/Feather2/Feather2/minus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.minimaze_window_button.setIcon(icon3)
        self.minimaze_window_button.setIconSize(QSize(16, 16))

        self.horizontalLayout_2.addWidget(self.minimaze_window_button)


        self.horizontalLayout.addWidget(self.header_right_frame, 0, Qt.AlignLeft)

        self.header_center_frame = QFrame(self.header_main_frame)
        self.header_center_frame.setObjectName(u"header_center_frame")
        self.header_center_frame.setFrameShape(QFrame.StyledPanel)
        self.header_center_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.header_center_frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(self.header_center_frame)
        self.label_2.setObjectName(u"label_2")
        font2 = QFont()
        font2.setPointSize(14)
        font2.setBold(True)
        font2.setWeight(75)
        self.label_2.setFont(font2)

        self.horizontalLayout_3.addWidget(self.label_2)

        self.label = QLabel(self.header_center_frame)
        self.label.setObjectName(u"label")
        font3 = QFont()
        font3.setPointSize(14)
        self.label.setFont(font3)
        self.label.setPixmap(QPixmap(u":/Feather2/Feather2/trending-up.svg"))

        self.horizontalLayout_3.addWidget(self.label)


        self.horizontalLayout.addWidget(self.header_center_frame, 0, Qt.AlignHCenter)

        self.header_left_frame = QFrame(self.header_main_frame)
        self.header_left_frame.setObjectName(u"header_left_frame")
        self.header_left_frame.setLayoutDirection(Qt.RightToLeft)
        self.header_left_frame.setFrameShape(QFrame.StyledPanel)
        self.header_left_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.header_left_frame)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pushButton = QPushButton(self.header_left_frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setFont(font1)
        self.pushButton.setLayoutDirection(Qt.LeftToRight)
        icon4 = QIcon()
        icon4.addFile(u":/Production/production/align_left.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon4)
        self.pushButton.setIconSize(QSize(32, 32))

        self.horizontalLayout_4.addWidget(self.pushButton)


        self.horizontalLayout.addWidget(self.header_left_frame, 0, Qt.AlignRight)


        self.verticalLayout.addWidget(self.header_main_frame, 0, Qt.AlignTop)

        self.body_main_frame = QFrame(self.centralwidget)
        self.body_main_frame.setObjectName(u"body_main_frame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.body_main_frame.sizePolicy().hasHeightForWidth())
        self.body_main_frame.setSizePolicy(sizePolicy)
        self.body_main_frame.setFrameShape(QFrame.NoFrame)
        self.body_main_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.body_main_frame)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.right_frame_2 = QFrame(self.body_main_frame)
        self.right_frame_2.setObjectName(u"right_frame_2")
        self.right_frame_2.setStyleSheet(u"background-color: rgb(0, 85, 127);")
        self.right_frame_2.setFrameShape(QFrame.StyledPanel)
        self.right_frame_2.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_8.addWidget(self.right_frame_2)

        self.main_body_contents = QFrame(self.body_main_frame)
        self.main_body_contents.setObjectName(u"main_body_contents")
        self.main_body_contents.setFrameShape(QFrame.StyledPanel)
        self.main_body_contents.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.main_body_contents)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.main_body_contents)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(45, 63, 100, 255), stop:0.159204 rgba(19, 56, 79, 255), stop:0.298507 rgba(29, 43, 71, 255), stop:0.412935 rgba(12, 35, 71, 255), stop:0.552239 rgba(29, 39, 63, 255), stop:0.666667 rgba(36, 28, 70, 255), stop:0.800995 rgba(31, 29, 76, 255), stop:0.970149 rgba(38, 32, 82, 255));")
        self.import_page = QWidget()
        self.import_page.setObjectName(u"import_page")
        self.import_page.setEnabled(False)
        self.verticalLayout_3 = QVBoxLayout(self.import_page)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.import_page)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.pushButton_3 = QPushButton(self.frame)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.verticalLayout_4.addWidget(self.pushButton_3)


        self.verticalLayout_3.addWidget(self.frame, 0, Qt.AlignTop)

        self.frame_2 = QFrame(self.import_page)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setLayoutDirection(Qt.LeftToRight)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frame_2)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.tabWidget = QTabWidget(self.frame_2)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setLayoutDirection(Qt.LeftToRight)
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        font4 = QFont()
        font4.setKerning(True)
        self.tab_3.setFont(font4)
        self.tab_3.setLayoutDirection(Qt.LeftToRight)
        self.verticalLayout_18 = QVBoxLayout(self.tab_3)
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.frame_22 = QFrame(self.tab_3)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_22)
        self.horizontalLayout_19.setSpacing(0)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.frame_22)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMaximumSize(QSize(60, 20))
        self.label_7.setLayoutDirection(Qt.LeftToRight)
        self.label_7.setAutoFillBackground(False)
        self.label_7.setStyleSheet(u"color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(81, 167, 179, 255), stop:0.159204 rgba(29, 101, 119, 255), stop:0.298507 rgba(61, 129, 150, 255), stop:0.412935 rgba(27, 161, 149, 255), stop:0.532338 rgba(85, 184, 146, 255), stop:0.666667 rgba(65, 150, 162, 255), stop:0.800995 rgba(71, 133, 185, 255), stop:0.965174 rgba(50, 96, 128, 255));")
        self.label_7.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_19.addWidget(self.label_7)

        self.spinBox = QSpinBox(self.frame_22)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setMaximumSize(QSize(60, 16777215))
        self.spinBox.setLayoutDirection(Qt.LeftToRight)
        self.spinBox.setAlignment(Qt.AlignCenter)
        self.spinBox.setMaximum(255)

        self.horizontalLayout_19.addWidget(self.spinBox)


        self.verticalLayout_18.addWidget(self.frame_22, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.pushButton_4 = QPushButton(self.tab_3)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(0, 25))
        self.pushButton_4.setMaximumSize(QSize(80, 16777215))
        self.pushButton_4.setLayoutDirection(Qt.LeftToRight)

        self.verticalLayout_18.addWidget(self.pushButton_4)

        self.tableWidget = QTableWidget(self.tab_3)
        self.tableWidget.setObjectName(u"tableWidget")

        self.verticalLayout_18.addWidget(self.tableWidget)

        self.tabWidget.addTab(self.tab_3, "")

        self.verticalLayout_19.addWidget(self.tabWidget)


        self.verticalLayout_3.addWidget(self.frame_2)

        self.stackedWidget.addWidget(self.import_page)
        self.prop_page = QWidget()
        self.prop_page.setObjectName(u"prop_page")
        self.horizontalLayout_10 = QHBoxLayout(self.prop_page)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.prop_page)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.right_option_frame = QFrame(self.frame_4)
        self.right_option_frame.setObjectName(u"right_option_frame")
        self.right_option_frame.setFrameShape(QFrame.StyledPanel)
        self.right_option_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.right_option_frame)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame_6 = QFrame(self.right_option_frame)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setLayoutDirection(Qt.RightToLeft)
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.manual_choose_label = QLabel(self.frame_6)
        self.manual_choose_label.setObjectName(u"manual_choose_label")
        font5 = QFont()
        font5.setPointSize(11)
        font5.setBold(True)
        font5.setWeight(75)
        self.manual_choose_label.setFont(font5)
        self.manual_choose_label.setLayoutDirection(Qt.RightToLeft)
        self.manual_choose_label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.manual_choose_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_12.addWidget(self.manual_choose_label)


        self.verticalLayout_5.addWidget(self.frame_6, 0, Qt.AlignTop)

        self.comboBox_frame = QFrame(self.right_option_frame)
        self.comboBox_frame.setObjectName(u"comboBox_frame")
        self.comboBox_frame.setFrameShape(QFrame.StyledPanel)
        self.comboBox_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.comboBox_frame)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.model_choose_comboBox = QComboBox(self.comboBox_frame)
        self.model_choose_comboBox.addItem("")
        self.model_choose_comboBox.addItem("")
        self.model_choose_comboBox.addItem("")
        self.model_choose_comboBox.addItem("")
        self.model_choose_comboBox.addItem("")
        self.model_choose_comboBox.addItem("")
        self.model_choose_comboBox.addItem("")
        self.model_choose_comboBox.addItem("")
        self.model_choose_comboBox.addItem("")
        self.model_choose_comboBox.setObjectName(u"model_choose_comboBox")
        self.model_choose_comboBox.setEnabled(True)
        font6 = QFont()
        font6.setPointSize(11)
        self.model_choose_comboBox.setFont(font6)
        self.model_choose_comboBox.setLayoutDirection(Qt.LeftToRight)
        self.model_choose_comboBox.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.model_choose_comboBox.setEditable(False)

        self.verticalLayout_6.addWidget(self.model_choose_comboBox)


        self.verticalLayout_5.addWidget(self.comboBox_frame, 0, Qt.AlignTop)


        self.horizontalLayout_11.addWidget(self.right_option_frame, 0, Qt.AlignTop)

        self.left_option_frame = QFrame(self.frame_4)
        self.left_option_frame.setObjectName(u"left_option_frame")
        self.left_option_frame.setFrameShape(QFrame.StyledPanel)
        self.left_option_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.left_option_frame)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_9 = QFrame(self.left_option_frame)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_9)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.auto_choose_label = QLabel(self.frame_9)
        self.auto_choose_label.setObjectName(u"auto_choose_label")
        self.auto_choose_label.setFont(font5)
        self.auto_choose_label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.auto_choose_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.auto_choose_label)


        self.verticalLayout_7.addWidget(self.frame_9, 0, Qt.AlignTop)

        self.auto_choose_frame = QFrame(self.left_option_frame)
        self.auto_choose_frame.setObjectName(u"auto_choose_frame")
        self.auto_choose_frame.setFrameShape(QFrame.StyledPanel)
        self.auto_choose_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.auto_choose_frame)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.auto_choose_button = QPushButton(self.auto_choose_frame)
        self.auto_choose_button.setObjectName(u"auto_choose_button")
        self.auto_choose_button.setFont(font5)
        self.auto_choose_button.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_8.addWidget(self.auto_choose_button)

        self.auto_suggest_label = QFrame(self.auto_choose_frame)
        self.auto_suggest_label.setObjectName(u"auto_suggest_label")
        self.auto_suggest_label.setFrameShape(QFrame.StyledPanel)
        self.auto_suggest_label.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.auto_suggest_label)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.suggested_model_label = QLabel(self.auto_suggest_label)
        self.suggested_model_label.setObjectName(u"suggested_model_label")
        self.suggested_model_label.setFont(font5)
        self.suggested_model_label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.suggested_model_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_13.addWidget(self.suggested_model_label)


        self.verticalLayout_8.addWidget(self.auto_suggest_label, 0, Qt.AlignTop)


        self.verticalLayout_7.addWidget(self.auto_choose_frame, 0, Qt.AlignTop)


        self.horizontalLayout_11.addWidget(self.left_option_frame, 0, Qt.AlignTop)


        self.horizontalLayout_10.addWidget(self.frame_4)

        self.stackedWidget.addWidget(self.prop_page)
        self.score_page = QWidget()
        self.score_page.setObjectName(u"score_page")
        self.horizontalLayout_14 = QHBoxLayout(self.score_page)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.score_page)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.frame_3)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.frame_5)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.frame_18 = QFrame(self.frame_5)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_18)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.graphicsView = PlotWidget(self.frame_18)
        self.graphicsView.setObjectName(u"graphicsView")

        self.gridLayout_2.addWidget(self.graphicsView, 0, 0, 1, 1)


        self.verticalLayout_20.addWidget(self.frame_18)

        self.frame_19 = QFrame(self.frame_5)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setMaximumSize(QSize(100, 16777215))
        self.frame_19.setLayoutDirection(Qt.LeftToRight)
        self.frame_19.setStyleSheet(u"color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(81, 167, 179, 255), stop:0.159204 rgba(29, 101, 119, 255), stop:0.298507 rgba(61, 129, 150, 255), stop:0.412935 rgba(27, 161, 149, 255), stop:0.532338 rgba(85, 184, 146, 255), stop:0.666667 rgba(65, 150, 162, 255), stop:0.800995 rgba(71, 133, 185, 255), stop:0.965174 rgba(50, 96, 128, 255));")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_19)
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.frame_21 = QFrame(self.frame_19)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setMaximumSize(QSize(30, 45))
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.frame_21)
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.label_9 = QLabel(self.frame_21)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font6)
        self.label_9.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_21.addWidget(self.label_9)

        self.label_10 = QLabel(self.frame_21)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font6)

        self.verticalLayout_21.addWidget(self.label_10)


        self.horizontalLayout_18.addWidget(self.frame_21)

        self.frame_20 = QFrame(self.frame_19)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setMaximumSize(QSize(70, 45))
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.frame_20)
        self.verticalLayout_22.setSpacing(0)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.label_12 = QLabel(self.frame_20)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font6)
        self.label_12.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_22.addWidget(self.label_12)

        self.label_11 = QLabel(self.frame_20)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font6)

        self.verticalLayout_22.addWidget(self.label_11)


        self.horizontalLayout_18.addWidget(self.frame_20)


        self.verticalLayout_20.addWidget(self.frame_19)


        self.horizontalLayout_15.addWidget(self.frame_5)

        self.frame_7 = QFrame(self.frame_3)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMaximumSize(QSize(400, 600))
        self.frame_7.setFont(font6)
        self.frame_7.setStyleSheet(u"color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(81, 167, 179, 255), stop:0.159204 rgba(29, 101, 119, 255), stop:0.298507 rgba(61, 129, 150, 255), stop:0.412935 rgba(27, 161, 149, 255), stop:0.532338 rgba(85, 184, 146, 255), stop:0.666667 rgba(65, 150, 162, 255), stop:0.800995 rgba(71, 133, 185, 255), stop:0.965174 rgba(50, 96, 128, 255));")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.frame_11 = QFrame(self.frame_7)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMaximumSize(QSize(85, 16777215))
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_11)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.frame_8 = QFrame(self.frame_11)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFont(font5)
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_8)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.chosen_method_label_value = QLabel(self.frame_8)
        self.chosen_method_label_value.setObjectName(u"chosen_method_label_value")
        self.chosen_method_label_value.setMaximumSize(QSize(16777215, 22))
        self.chosen_method_label_value.setFont(font6)
        self.chosen_method_label_value.setStyleSheet(u"color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(28, 138, 255, 255), stop:1 rgba(20, 100, 250, 137))")
        self.chosen_method_label_value.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.chosen_method_label_value)

        self.corr_label_value = QLabel(self.frame_8)
        self.corr_label_value.setObjectName(u"corr_label_value")
        self.corr_label_value.setMaximumSize(QSize(16777215, 22))
        self.corr_label_value.setFont(font6)
        self.corr_label_value.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.corr_label_value)

        self.r_suared_label_value = QLabel(self.frame_8)
        self.r_suared_label_value.setObjectName(u"r_suared_label_value")
        self.r_suared_label_value.setMaximumSize(QSize(16777215, 22))
        self.r_suared_label_value.setFont(font6)
        self.r_suared_label_value.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.r_suared_label_value)

        self.mean_label_value = QLabel(self.frame_8)
        self.mean_label_value.setObjectName(u"mean_label_value")
        self.mean_label_value.setMaximumSize(QSize(16777215, 22))
        self.mean_label_value.setFont(font6)
        self.mean_label_value.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.mean_label_value)

        self.st_dev_label_value = QLabel(self.frame_8)
        self.st_dev_label_value.setObjectName(u"st_dev_label_value")
        self.st_dev_label_value.setMaximumSize(QSize(16777215, 22))
        self.st_dev_label_value.setFont(font6)
        self.st_dev_label_value.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.st_dev_label_value)

        self.w_coef_label_value = QLabel(self.frame_8)
        self.w_coef_label_value.setObjectName(u"w_coef_label_value")
        self.w_coef_label_value.setMaximumSize(QSize(16777215, 22))
        self.w_coef_label_value.setFont(font6)
        self.w_coef_label_value.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.w_coef_label_value)

        self.point_prognosis_label_value = QLabel(self.frame_8)
        self.point_prognosis_label_value.setObjectName(u"point_prognosis_label_value")
        self.point_prognosis_label_value.setMaximumSize(QSize(16777215, 22))
        self.point_prognosis_label_value.setFont(font6)
        self.point_prognosis_label_value.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.point_prognosis_label_value)

        self.label_15 = QLabel(self.frame_8)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMaximumSize(QSize(16777215, 22))
        self.label_15.setFont(font6)
        self.label_15.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.label_15)

        self.empty_label = QLabel(self.frame_8)
        self.empty_label.setObjectName(u"empty_label")
        self.empty_label.setMaximumSize(QSize(16777215, 38))
        self.empty_label.setFont(font6)

        self.verticalLayout_12.addWidget(self.empty_label)

        self.optimum_alpha_label_value = QLabel(self.frame_8)
        self.optimum_alpha_label_value.setObjectName(u"optimum_alpha_label_value")
        self.optimum_alpha_label_value.setMaximumSize(QSize(16777215, 24))
        self.optimum_alpha_label_value.setFont(font6)
        self.optimum_alpha_label_value.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.optimum_alpha_label_value)

        self.optimum_beta_label_value = QLabel(self.frame_8)
        self.optimum_beta_label_value.setObjectName(u"optimum_beta_label_value")
        self.optimum_beta_label_value.setMaximumSize(QSize(16777215, 24))
        self.optimum_beta_label_value.setFont(font6)
        self.optimum_beta_label_value.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.optimum_beta_label_value)

        self.empty_label_2 = QLabel(self.frame_8)
        self.empty_label_2.setObjectName(u"empty_label_2")
        self.empty_label_2.setStyleSheet(u"color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(81, 167, 179, 255), stop:0.159204 rgba(29, 101, 119, 255), stop:0.298507 rgba(61, 129, 150, 255), stop:0.412935 rgba(27, 161, 149, 255), stop:0.532338 rgba(85, 184, 146, 255), stop:0.666667 rgba(65, 150, 162, 255), stop:0.800995 rgba(71, 133, 185, 255), stop:0.965174 rgba(50, 96, 128, 255));")

        self.verticalLayout_12.addWidget(self.empty_label_2)


        self.verticalLayout_11.addWidget(self.frame_8)


        self.horizontalLayout_16.addWidget(self.frame_11)

        self.frame_10 = QFrame(self.frame_7)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_10)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.chosen_method_label = QLabel(self.frame_10)
        self.chosen_method_label.setObjectName(u"chosen_method_label")
        self.chosen_method_label.setMaximumSize(QSize(16777215, 30))
        self.chosen_method_label.setFont(font6)
        self.chosen_method_label.setStyleSheet(u"color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(28, 138, 255, 255), stop:1 rgba(20, 100, 250, 137))")

        self.verticalLayout_13.addWidget(self.chosen_method_label)

        self.corr_label = QLabel(self.frame_10)
        self.corr_label.setObjectName(u"corr_label")
        self.corr_label.setMaximumSize(QSize(16777215, 30))
        self.corr_label.setFont(font6)

        self.verticalLayout_13.addWidget(self.corr_label)

        self.r_squared_label = QLabel(self.frame_10)
        self.r_squared_label.setObjectName(u"r_squared_label")
        self.r_squared_label.setMaximumSize(QSize(16777215, 30))
        self.r_squared_label.setFont(font6)

        self.verticalLayout_13.addWidget(self.r_squared_label)

        self.mean_label = QLabel(self.frame_10)
        self.mean_label.setObjectName(u"mean_label")
        self.mean_label.setMaximumSize(QSize(16777215, 30))
        self.mean_label.setFont(font6)

        self.verticalLayout_13.addWidget(self.mean_label)

        self.st_dev_label = QLabel(self.frame_10)
        self.st_dev_label.setObjectName(u"st_dev_label")
        self.st_dev_label.setMaximumSize(QSize(16777215, 30))
        self.st_dev_label.setFont(font6)

        self.verticalLayout_13.addWidget(self.st_dev_label)

        self.w_coef_label = QLabel(self.frame_10)
        self.w_coef_label.setObjectName(u"w_coef_label")
        self.w_coef_label.setMaximumSize(QSize(16777215, 30))
        self.w_coef_label.setFont(font6)

        self.verticalLayout_13.addWidget(self.w_coef_label)

        self.point_prognosis_label = QLabel(self.frame_10)
        self.point_prognosis_label.setObjectName(u"point_prognosis_label")
        self.point_prognosis_label.setMaximumSize(QSize(16777215, 30))
        self.point_prognosis_label.setFont(font6)

        self.verticalLayout_13.addWidget(self.point_prognosis_label)

        self.label_21 = QLabel(self.frame_10)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setMaximumSize(QSize(16777215, 30))
        self.label_21.setFont(font6)

        self.verticalLayout_13.addWidget(self.label_21)

        self.frame_13 = QFrame(self.frame_10)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setMaximumSize(QSize(16777215, 60))
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_13)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.label_8 = QLabel(self.frame_13)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font6)

        self.verticalLayout_10.addWidget(self.label_8, 0, Qt.AlignHCenter)

        self.label_14 = QLabel(self.frame_13)
        self.label_14.setObjectName(u"label_14")
        font7 = QFont()
        font7.setBold(True)
        font7.setItalic(False)
        font7.setUnderline(False)
        font7.setWeight(75)
        font7.setStrikeOut(False)
        self.label_14.setFont(font7)

        self.verticalLayout_10.addWidget(self.label_14, 0, Qt.AlignHCenter)


        self.verticalLayout_13.addWidget(self.frame_13)

        self.frame_14 = QFrame(self.frame_10)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setMaximumSize(QSize(16777215, 180))
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_14)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.frame_12 = QFrame(self.frame_14)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.frame_17 = QFrame(self.frame_12)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_17)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.optimum_alpha_label = QLabel(self.frame_17)
        self.optimum_alpha_label.setObjectName(u"optimum_alpha_label")
        self.optimum_alpha_label.setFont(font6)

        self.verticalLayout_16.addWidget(self.optimum_alpha_label)

        self.optimum_beta_label = QLabel(self.frame_17)
        self.optimum_beta_label.setObjectName(u"optimum_beta_label")
        self.optimum_beta_label.setFont(font6)

        self.verticalLayout_16.addWidget(self.optimum_beta_label)


        self.horizontalLayout_17.addWidget(self.frame_17)

        self.frame_16 = QFrame(self.frame_12)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setMaximumSize(QSize(85, 16777215))
        self.frame_16.setFont(font6)
        self.frame_16.setStyleSheet(u"color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(81, 167, 179, 255), stop:0.159204 rgba(29, 101, 119, 255), stop:0.298507 rgba(61, 129, 150, 255), stop:0.412935 rgba(27, 161, 149, 255), stop:0.532338 rgba(85, 184, 146, 255), stop:0.666667 rgba(65, 150, 162, 255), stop:0.800995 rgba(71, 133, 185, 255), stop:0.965174 rgba(50, 96, 128, 255));")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_16)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.alphadoubleSpinBox_2 = QDoubleSpinBox(self.frame_16)
        self.alphadoubleSpinBox_2.setObjectName(u"alphadoubleSpinBox_2")
        self.alphadoubleSpinBox_2.setEnabled(True)
        font8 = QFont()
        font8.setPointSize(11)
        font8.setItalic(False)
        self.alphadoubleSpinBox_2.setFont(font8)
        self.alphadoubleSpinBox_2.setLayoutDirection(Qt.LeftToRight)
        self.alphadoubleSpinBox_2.setAutoFillBackground(False)
        self.alphadoubleSpinBox_2.setStyleSheet(u"color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(28, 138, 255, 255), stop:1 rgba(255, 255, 255, 255));")
        self.alphadoubleSpinBox_2.setAlignment(Qt.AlignCenter)
        self.alphadoubleSpinBox_2.setDecimals(3)
        self.alphadoubleSpinBox_2.setMaximum(1.000000000000000)
        self.alphadoubleSpinBox_2.setSingleStep(0.001000000000000)
        self.alphadoubleSpinBox_2.setValue(0.500000000000000)

        self.verticalLayout_15.addWidget(self.alphadoubleSpinBox_2)

        self.doubleSpinBox_beta3 = QDoubleSpinBox(self.frame_16)
        self.doubleSpinBox_beta3.setObjectName(u"doubleSpinBox_beta3")
        self.doubleSpinBox_beta3.setFont(font6)
        self.doubleSpinBox_beta3.setLayoutDirection(Qt.LeftToRight)
        self.doubleSpinBox_beta3.setAlignment(Qt.AlignCenter)
        self.doubleSpinBox_beta3.setDecimals(3)
        self.doubleSpinBox_beta3.setMaximum(1.000000000000000)
        self.doubleSpinBox_beta3.setSingleStep(0.001000000000000)
        self.doubleSpinBox_beta3.setValue(0.500000000000000)

        self.verticalLayout_15.addWidget(self.doubleSpinBox_beta3)


        self.horizontalLayout_17.addWidget(self.frame_16, 0, Qt.AlignVCenter)


        self.verticalLayout_14.addWidget(self.frame_12, 0, Qt.AlignVCenter)

        self.frame_15 = QFrame(self.frame_14)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_15)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.refresh_stats_button = QPushButton(self.frame_15)
        self.refresh_stats_button.setObjectName(u"refresh_stats_button")
        self.refresh_stats_button.setFont(font6)

        self.verticalLayout_17.addWidget(self.refresh_stats_button)


        self.verticalLayout_14.addWidget(self.frame_15, 0, Qt.AlignVCenter)


        self.verticalLayout_13.addWidget(self.frame_14)


        self.horizontalLayout_16.addWidget(self.frame_10, 0, Qt.AlignVCenter)


        self.horizontalLayout_15.addWidget(self.frame_7, 0, Qt.AlignTop)


        self.horizontalLayout_14.addWidget(self.frame_3)

        self.stackedWidget.addWidget(self.score_page)

        self.verticalLayout_2.addWidget(self.stackedWidget)


        self.horizontalLayout_8.addWidget(self.main_body_contents)

        self.right_frame = QFrame(self.body_main_frame)
        self.right_frame.setObjectName(u"right_frame")
        self.right_frame.setMinimumSize(QSize(40, 0))
        self.right_frame.setMaximumSize(QSize(40, 16777215))
        self.right_frame.setStyleSheet(u"background-color: rgb(0, 85, 127);")
        self.right_frame.setFrameShape(QFrame.StyledPanel)
        self.right_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.right_frame)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.left_menu = QFrame(self.right_frame)
        self.left_menu.setObjectName(u"left_menu")
        self.left_menu.setMinimumSize(QSize(200, 0))
        self.left_menu.setFrameShape(QFrame.StyledPanel)
        self.left_menu.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.left_menu)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.score_button = QPushButton(self.left_menu)
        self.score_button.setObjectName(u"score_button")
        icon5 = QIcon()
        icon5.addFile(u":/Design/tasks.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.score_button.setIcon(icon5)
        self.score_button.setIconSize(QSize(36, 36))

        self.gridLayout.addWidget(self.score_button, 2, 1, 1, 1)

        self.label_6 = QLabel(self.left_menu)
        self.label_6.setObjectName(u"label_6")
        font9 = QFont()
        font9.setPointSize(12)
        font9.setBold(True)
        font9.setWeight(75)
        self.label_6.setFont(font9)

        self.gridLayout.addWidget(self.label_6, 2, 0, 1, 1)

        self.label_4 = QLabel(self.left_menu)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font9)

        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)

        self.label_5 = QLabel(self.left_menu)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font9)

        self.gridLayout.addWidget(self.label_5, 1, 0, 1, 1)

        self.properties_button = QPushButton(self.left_menu)
        self.properties_button.setObjectName(u"properties_button")
        icon6 = QIcon()
        icon6.addFile(u":/Feather2/Feather2/tool.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.properties_button.setIcon(icon6)
        self.properties_button.setIconSize(QSize(36, 36))

        self.gridLayout.addWidget(self.properties_button, 1, 1, 1, 1)

        self.import_button = QPushButton(self.left_menu)
        self.import_button.setObjectName(u"import_button")
        icon7 = QIcon()
        icon7.addFile(u":/Design/opened_folder.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.import_button.setIcon(icon7)
        self.import_button.setIconSize(QSize(36, 36))

        self.gridLayout.addWidget(self.import_button, 0, 1, 1, 1)


        self.horizontalLayout_9.addWidget(self.left_menu, 0, Qt.AlignLeft|Qt.AlignTop)


        self.horizontalLayout_8.addWidget(self.right_frame, 0, Qt.AlignRight)


        self.verticalLayout.addWidget(self.body_main_frame)

        self.footer_main_frame = QFrame(self.centralwidget)
        self.footer_main_frame.setObjectName(u"footer_main_frame")
        self.footer_main_frame.setStyleSheet(u"background-color: rgb(0, 85, 127);")
        self.footer_main_frame.setFrameShape(QFrame.NoFrame)
        self.footer_main_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.footer_main_frame)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.size_grip = QFrame(self.footer_main_frame)
        self.size_grip.setObjectName(u"size_grip")
        self.size_grip.setMinimumSize(QSize(10, 10))
        self.size_grip.setMaximumSize(QSize(10, 10))
        self.size_grip.setFrameShape(QFrame.StyledPanel)
        self.size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.size_grip, 0, Qt.AlignBottom)

        self.footer_right_frame = QFrame(self.footer_main_frame)
        self.footer_right_frame.setObjectName(u"footer_right_frame")
        self.footer_right_frame.setFrameShape(QFrame.StyledPanel)
        self.footer_right_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.footer_right_frame)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.pushButton_2 = QPushButton(self.footer_right_frame)
        self.pushButton_2.setObjectName(u"pushButton_2")
        font10 = QFont()
        font10.setBold(True)
        font10.setUnderline(True)
        font10.setWeight(75)
        self.pushButton_2.setFont(font10)

        self.horizontalLayout_7.addWidget(self.pushButton_2)


        self.horizontalLayout_5.addWidget(self.footer_right_frame, 0, Qt.AlignLeft)

        self.footer_left_frame = QFrame(self.footer_main_frame)
        self.footer_left_frame.setObjectName(u"footer_left_frame")
        self.footer_left_frame.setFrameShape(QFrame.StyledPanel)
        self.footer_left_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.footer_left_frame)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.footer_left_frame)
        self.label_3.setObjectName(u"label_3")
        font11 = QFont()
        font11.setFamily(u"Arial")
        font11.setBold(True)
        font11.setItalic(True)
        font11.setUnderline(False)
        font11.setWeight(75)
        font11.setStrikeOut(False)
        font11.setKerning(True)
        self.label_3.setFont(font11)

        self.horizontalLayout_6.addWidget(self.label_3, 0, Qt.AlignRight)


        self.horizontalLayout_5.addWidget(self.footer_left_frame)


        self.verticalLayout.addWidget(self.footer_main_frame, 0, Qt.AlignBottom)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(2)
        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Students Forecaster", None))
        self.actionEdit.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.actionNew.setText(QCoreApplication.translate("MainWindow", u"New", None))
#if QT_CONFIG(statustip)
        self.actionNew.setStatusTip(QCoreApplication.translate("MainWindow", u"Create a new file", None))
#endif // QT_CONFIG(statustip)
        self.actionSave.setText(QCoreApplication.translate("MainWindow", u"Save", None))
#if QT_CONFIG(statustip)
        self.actionSave.setStatusTip(QCoreApplication.translate("MainWindow", u"Save a file", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(shortcut)
        self.actionSave.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.actionCopy.setText(QCoreApplication.translate("MainWindow", u"Copy", None))
#if QT_CONFIG(statustip)
        self.actionCopy.setStatusTip(QCoreApplication.translate("MainWindow", u"Copy a file", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(shortcut)
        self.actionCopy.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+C", None))
#endif // QT_CONFIG(shortcut)
        self.actionPaste.setText(QCoreApplication.translate("MainWindow", u"Paste", None))
#if QT_CONFIG(statustip)
        self.actionPaste.setStatusTip(QCoreApplication.translate("MainWindow", u"Paste a file", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(shortcut)
        self.actionPaste.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+V", None))
#endif // QT_CONFIG(shortcut)
        self.close_window_button.setText("")
        self.restore_window_button.setText("")
        self.minimaze_window_button.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Students Forecaster", None))
        self.label.setText("")
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Menu", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Otw\u00f3rz plik .csv", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Wiersze:", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Poka\u017c", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Tab 1", None))
        self.manual_choose_label.setText(QCoreApplication.translate("MainWindow", u"Wyb\u00f3r r\u0119czny", None))
        self.model_choose_comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Liniowy", None))
        self.model_choose_comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Wyk\u0142adniczy", None))
        self.model_choose_comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Pot\u0119gowy", None))
        self.model_choose_comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Logarytmiczny", None))
        self.model_choose_comboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Wielomianowy II stopnia", None))
        self.model_choose_comboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"Browna", None))
        self.model_choose_comboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"Holta", None))
        self.model_choose_comboBox.setItemText(7, QCoreApplication.translate("MainWindow", u"Regresja wieloraka", None))
        self.model_choose_comboBox.setItemText(8, "")

        self.model_choose_comboBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"--- wyb\u00f3r strategii ---", None))
        self.auto_choose_label.setText(QCoreApplication.translate("MainWindow", u"Automatyczny wyb\u00f3r", None))
        self.auto_choose_button.setText(QCoreApplication.translate("MainWindow", u"Nie", None))
        self.suggested_model_label.setText(QCoreApplication.translate("MainWindow", u"<Proponowany model>", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"X = ", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Y = ", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"[]", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"[]", None))
        self.chosen_method_label_value.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.corr_label_value.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.r_suared_label_value.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.mean_label_value.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.st_dev_label_value.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.w_coef_label_value.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.point_prognosis_label_value.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.empty_label.setText("")
        self.optimum_alpha_label_value.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.optimum_beta_label_value.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.empty_label_2.setText("")
        self.chosen_method_label.setText(QCoreApplication.translate("MainWindow", u"Wybrana metoda: ", None))
        self.corr_label.setText(QCoreApplication.translate("MainWindow", u"Wsp\u00f3\u0142czynnik korelacji:", None))
        self.r_squared_label.setText(QCoreApplication.translate("MainWindow", u"Wsp\u00f3\u0142czynnik determinacji:", None))
        self.mean_label.setText(QCoreApplication.translate("MainWindow", u"\u015arednia:", None))
        self.st_dev_label.setText(QCoreApplication.translate("MainWindow", u"Odchylenie standardowe:", None))
        self.w_coef_label.setText(QCoreApplication.translate("MainWindow", u"Wsp\u00f3\u0142czynnik zmienno\u015bci:", None))
        self.point_prognosis_label.setText(QCoreApplication.translate("MainWindow", u"Prognoza punktowa:", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Dodatkowe opcje", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"[Brown/Holt]", None))
        self.optimum_alpha_label.setText(QCoreApplication.translate("MainWindow", u"Optymalne alfa:", None))
        self.optimum_beta_label.setText(QCoreApplication.translate("MainWindow", u"Optymalne beta:", None))
        self.refresh_stats_button.setText(QCoreApplication.translate("MainWindow", u"Od\u015bwie\u017c", None))
        self.score_button.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Wyniki", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Importuj plik", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Opcje prognozy", None))
        self.properties_button.setText("")
        self.import_button.setText("")
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Pomoc", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Wersja 1.0 | Miko\u0142aj Abramczyk | Wojskowa Akademia Techniczna ", None))
    # retranslateUi

