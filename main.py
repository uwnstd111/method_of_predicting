####################################
# IMPORTS
import sys
import os
import sklearn
import numpy as np
import statistics
from scipy.stats import *
import pandas as pd

import statsmodels.api as stat_model
import csv, codecs
from PyQt5.QtCore import QFile, QSettings, Qt, QFileInfo, QItemSelectionModel, QDir
from PyQt5.QtWidgets import (QMainWindow, QAction, QWidget, QLineEdit, QMessageBox, QAbstractItemView, QApplication,
                             QTableWidgetItem, QGridLayout, QFileDialog, QMenu, QInputDialog)
from PySide2.QtWidgets import QTableWidget
from PyQt5 import Qt
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QSizeGrip, QGraphicsDropShadowEffect, QTableWidget
from PySide2 import QtCore, QtGui
from PyQt5.QtCore import Qt, QPoint, QPropertyAnimation
from PyQt5.QtGui import QMouseEvent, QDropEvent
from qt_material import *
from functools import partial
from brown import *
from linest import *
from F_test import *
# from Custom_Widgets.Widgets import *
from PySide2.QtGui import QPainter
from PySide2.QtCharts import QtCharts
# from PyQt5.uic import loadUiType

####################################


####################################
# IMPORT GUI

#from interface2 import *
from interface1 import *
#from ui_interface2 import *

####################################
####################################
# MAIN WINDOW CLASS
####################################
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.path = ''
        self.ui.pushButton_4.setEnabled(False)
        self.list = []
        self.time_serial_list = []
        # creating a QGraphicsDropShadowEffect object
        shadowEffect = QGraphicsDropShadowEffect()
        # setting blur radius
        shadowEffect.setBlurRadius(15)

        print(list_themes())
        QSizeGrip(self.ui.size_grip)
        # QSizeGrip(self.ui.input_table)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(50)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QtGui.QColor(0, 92, 157, 550))
        self.ui.centralwidget.setGraphicsEffect(self.shadow)
        self.setWindowIcon(QtGui.QIcon(":/Feather2/Feather2/trending-up.svg"))
        self.setWindowTitle("Students Forecaster")
        self.ui.minimaze_window_button.clicked.connect(lambda:
                                                       self.showMinimized())
        self.ui.restore_window_button.clicked.connect(lambda:
                                                      self.restore_or_maximize_window())
        self.ui.close_window_button.clicked.connect(lambda:
                                                    self.close())

        ###NAVIGATION###

        self.ui.import_button.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.import_page))
        self.ui.import_button.clicked.connect(lambda: self.glowImportLabel(shadowEffect))

        self.ui.properties_button.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.prop_page))
        self.ui.properties_button.clicked.connect(lambda: self.glowPropLabel(shadowEffect))

        self.ui.score_button.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.score_page))
        self.ui.score_button.clicked.connect(lambda: self.glowScoreLabel(shadowEffect))

        def moveEvent(event):
            if self.isMaximized() == False:
                if event.buttons() == QtCore.Qt.LeftButton:
                    self.move(self.pos() + event.globalPos() - self.oldPosition)
                    self.oldPosition = event.globalPos()
                # delta = QPoint(event.globalPos() - self.oldPosition)
                # self.move(self.x() + delta.x(), self.y() + delta.y())
                # self.oldPosition = event.globalPos()

        self.ui.header_main_frame.mouseMoveEvent = moveEvent

        self.ui.pushButton.clicked.connect(lambda: self.slideLeftMenu())

        self.ui.pushButton_3.clicked.connect(self.openFile)
        self.ui.pushButton_4.clicked.connect(self.showData)
        apply_stylesheet(app, theme=list_themes()[1])
        self.ui.label_4.setStyleSheet("border : 4px solid blue")

        self.show()

    def glowImportLabel(self, shadowEffect):
        # adding shadow to the label
        self.ui.label_4.setGraphicsEffect(shadowEffect)
        self.ui.label_4.setStyleSheet("border : 4px solid blue")
        self.ui.label_5.setStyleSheet("border : 0px solid blue")
        self.ui.label_6.setStyleSheet("border : 0px solid blue")

    def glowPropLabel(self, shadowEffect):
        self.ui.label_5.setGraphicsEffect(shadowEffect)
        self.ui.label_4.setStyleSheet("border : 0px solid blue")
        self.ui.label_5.setStyleSheet("border : 4px solid blue")
        self.ui.label_6.setStyleSheet("border : 0px solid blue")

    def glowScoreLabel(self, shadowEffect):
        self.ui.label_6.setGraphicsEffect(shadowEffect)
        self.ui.label_4.setStyleSheet("border : 0px solid blue")
        self.ui.label_5.setStyleSheet("border : 0px solid blue")
        self.ui.label_6.setStyleSheet("border : 4px solid blue")

    def openFile(self):
        path = QFileDialog.getOpenFileName(self, "Open CSV", os.getcwd(), "CSV (*.csv *.tsv *.txt)")
        if path != ('', ''):
            self.all_data = pd.read_csv(path[0], sep=':', error_bad_lines=False, index_col=False, dtype='unicode')
            self.ui.pushButton_4.setEnabled(True)

    # dashboard_df = pd.read_csv(p_file, sep=',', error_bad_lines=False, index_col=False, dtype='unicode')
    def showData(self):
        numColumn = self.ui.spinBox.value()
        self.globalColumnNumber = numColumn
        if numColumn == 0 or numColumn > len(self.all_data.index):
            numRows = len(self.all_data.index)
            self.globalRowNumber = numRows
        else:
            numRows = numColumn
            self.globalRowNumber = numRows
        self.ui.tableWidget.setColumnCount(len(self.all_data.columns))
        self.ui.tableWidget.setRowCount(numRows)
        self.ui.tableWidget.setHorizontalHeaderLabels(self.all_data.columns)

        for i in range(numRows):
            for j in range(len(self.all_data.columns)):
                self.ui.tableWidget.setItem(i, j, QTableWidgetItem(str(self.all_data.iat[i, j])))
                #print(str(self.all_data.iat[i, j]))

        self.ui.tableWidget.resizeColumnsToContents()
        # print(self.all_data)
        #for column in self.all_data:
           # print(self.all_data[column])


        for index, row in self.all_data.iterrows():
            self.list.append(float(row[1]))
            self.time_serial_list.append(int(row[0]))
        self.mean = statistics.mean(self.list)
        self.st_dev = statistics.stdev(self.list)
        self.standardError = sem(self.list)
        self.coef_of_variation = "{:.3%}".format(self.standardError / self.mean)
        self.F_statistic = f.ppf(q = 1 - 0.05, dfn = 2, dfd = len(self.list) - 3)
        alpha = 0.05
        #TODO
        """dorobic spinBox do Alphy"""

        self.T_student_criticalValue = t.ppf(q = 1 - alpha / 2, df = len(self.list) - 2)
        print("F-Statistic: " + str(self.F_statistic))
        print("F-Test: " + str(f_test(self.list, self.time_serial_list)) + "\nT-Student inverse two-tailed: " + str(self.T_student_criticalValue))
        print("Srednia: " + str(self.mean))
        print("Odchylenie standardowe: " + str(self.st_dev))
        print("Suma bledow odchylen: " + str(self.standardError))
        print("Wspolczynnik zmiennosci/wyrazistosci: " + str(self.coef_of_variation))
        print("Lista: " + str(self.list))
        print("Seria czasowa" + str(self.time_serial_list))
        self.initializeRunMethods(self.list, self.time_serial_list)




    def initializeRunMethods(self, df, timeSeries):


        print("Wspolczynnik wyrazistosci (Brown): " + str(ret_ex_post_error(df, timeSeries)))
        print("Optymalne alfa (Brown):")
        print(retOptimumAlpha(df, timeSeries))

        print("Wartosc krytyczna T-Student:")
        print(retCriticalTValue(df, 0.05))
        print("Wspolczynnik determinacji R^2:")
        print(ret_coef_of_determination(df, timeSeries))


    def calculatedStatisticsBasedOnChosenMethod(self):
        self.methodName = ''
        self.personCorrelValue = "N/A"
        self.coef_of_determination = 0
        self.mean = 1
        self.standardError = 0
        self.st_dev = 0
        self.coef_of_variation = self.st_dev / self.mean
        self.F_statistic = "N/A"
        self.T_student_criticalValue = "N/A"
        self.prognosisValue = 0
        self.relativeForecastError = 0
        for column in self.all_data:
            print(self.all_data[column])

    def slideLeftMenu(self):
        width = self.ui.right_frame.width()

        if width == 0:
            newWidth = 220
        else:
            newWidth = 0

        self.animation = QPropertyAnimation(self.ui.right_frame, b"minimumWidth")
        self.animation.setDuration(300)
        self.animation.setStartValue(width)
        self.animation.setEndValue(newWidth)
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()

    def mousePressEvent(self, event):
        if self.isMaximized() == False:
            self.oldPosition = event.globalPos()

        #
        #

    def restore_or_maximize_window(self):
        if self.isMaximized():
            self.showNormal()
            self.ui.restore_window_button.setIcon(QtGui.QIcon(u":/Feather2/Feather2/maximize-2.svg"))
        else:
            self.showMaximized()
            self.ui.restore_window_button.setIcon(QtGui.QIcon(u":/Feather2/Feather2/minimize-2.svg"))


####################################
# APP EXECUTION
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
####################################
