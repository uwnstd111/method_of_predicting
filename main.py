####################################
# IMPORTS
import sys
import os
import sklearn
import numpy as np
import statistics
from scipy.stats import *
import pandas as pd
import colorama
from colorama import Fore


import statsmodels.api as stat_model
import csv, codecs
from PyQt5.QtCore import QFile, QSettings, Qt, QFileInfo, QItemSelectionModel, QDir
from PyQt5.QtWidgets import (QMainWindow, QAction, QWidget, QLineEdit, QMessageBox, QAbstractItemView, QApplication,
                             QTableWidgetItem, QGridLayout, QFileDialog, QMenu, QInputDialog)
from PySide2.QtWidgets import QTableWidget
from PyQt5 import Qt
from PyQt5 import QtCore, QtGui, QtWidgets
import pyqtgraph as pg
from PyQt5.QtWidgets import QApplication, QMainWindow, QSizeGrip, QGraphicsDropShadowEffect, QTableWidget, QCheckBox
from PySide2 import QtCore, QtGui
from PyQt5.QtCore import Qt, QPoint, QPropertyAnimation
from PyQt5.QtGui import QMouseEvent, QDropEvent
from qt_material import *
import bcolors
from functools import partial
from brown import *
from linest import *
from F_test import *
from holt import *
from exponencial import *
from power import *
from logarythmical import *
from polynomial import *
# from Custom_Widgets.Widgets import *
from PySide2.QtGui import QPainter
from PySide2.QtCharts import QtCharts
# from PyQt5.uic import loadUiType

####################################


####################################
# IMPORT GUI

from interface3 import *
#from interface1 import *
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

        ###Top Bar NAVI ###
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

        #MENU BUTTON
        self.ui.pushButton.clicked.connect(lambda: self.slideLeftMenu())

        self.ui.pushButton_3.clicked.connect(self.openFile)
        self.ui.pushButton_4.clicked.connect(self.showData)
        apply_stylesheet(app, theme=list_themes()[1])
        self.ui.label_4.setStyleSheet("border : 4px solid blue")
        #  CHART  detection
        def mouseOnChartMoved(evt):
            p = self.ui.graphicsView.plotItem.vb.mapSceneToView(evt[0])

            mousePoint = p
            self.ui.label_12.setText(str(int(mousePoint.x() + 0.5)))
            self.ui.label_11.setText(str("{:.2f}".format(mousePoint.y())))

        self.proxy = pg.SignalProxy(self.ui.graphicsView.scene().sigMouseMoved, rateLimit=60, slot=mouseOnChartMoved)

        #   CHART   LAYERS
        self.optLinCurve = self.ui.graphicsView_2.plot()
        self.optBrownCurve = self.ui.graphicsView_2.plot()
        self.optHoltCurve = self.ui.graphicsView_2.plot()
        self.optEXPCurve = self.ui.graphicsView_2.plot()
        self.optPowerCurve = self.ui.graphicsView_2.plot()
        self.optLogCurve = self.ui.graphicsView_2.plot()
        self.optPolyCurve = self.ui.graphicsView_2.plot()
        self.optDefaultCurve = self.ui.graphicsView_2.plot()


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
        path = QFileDialog.getOpenFileName(self, "Open CSV", os.getcwd(), "CSV (*.csv)")
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
        self.F_statistic = f.ppf(q=1 - 0.05, dfn=2, dfd=len(self.list) - 3)
        alpha = 0.05
        self.T_student_criticalValue = t.ppf(q=1 - alpha / 2, df=len(self.list) - 2)
        print("F-Statistic: " + str(self.F_statistic))
        print("F-Test: " + str(f_test(self.list, self.time_serial_list)) + "\nT-Student inverse two-tailed: " + str(self.T_student_criticalValue))
        print("Srednia: " + str(self.mean))
        print("Odchylenie standardowe: " + str(self.st_dev))
        print("Suma bledow odchylen: " + str(self.standardError))
        print("Wspolczynnik zmiennosci/wyrazistosci: " + str(self.coef_of_variation))
        print("Lista: " + str(self.list))
        print("Seria czasowa" + str(self.time_serial_list))
        self.optDefaultCurve.setData(self.time_serial_list, self.list, pen=pg.mkPen(color=(255, 255, 255)),
                                     symbol='o')
        self.initializeRunMethods(self.list, self.time_serial_list)

    def initializeRunMethods(self, df, timeSeries):
        print("Wspolczynnik wyrazistosci (Brown): " + str(ret_ex_post_error(df, timeSeries)))
        print("Optymalne alfa (Brown): " + str(retOptimumAlpha(df, timeSeries)))
        print("Wartosc krytyczna T-Student: " + str(retCriticalTValue(df, 0.05, 2)))
        print("Wspolczynnik determinacji R^2: " + str(ret_coef_of_determination(df, timeSeries)))
        print(len(df))
        print(len(timeSeries))
        print(df)
        print(timeSeries)
        # optCurve.setData(timeSeries, df, color=(200, 100, 255), style=QtCore.Qt.DotLine,symbol='o')
        curve1 = self.ui.graphicsView.plot()  #referencje
        # curve2 = self.ui.graphicsView.plot()
        curve1.setData(timeSeries, df, symbol='o')
        # curve2.setData([2013, 2014, 2015], [600, 800, 100], symbol='o')
        # self.ui.label_12.setText(str(np.array(df).astype(np.int32)))
        # self.ui.label_11.setText(str(np.array(timeSeries).astype(np.int32)))

        print("Prognoza liniowa: " + str(ret_model_values(df)))

        #print("Prognoza liniowa: " + bcolors.OKBLUE + str(retPointPrognosis(df)) + bcolors.ENDC)
        #df = df[:-2]

        self.checkBoxLinest = self.ui.checkBox_lin
        self.checkBoxBrown = self.ui.checkBox_brown
        self.checkBoxHolt = self.ui.checkBox_holt
        self.checkBoxExp = self.ui.checkBox_exp
        self.checkBoxPow = self.ui.checkBox_pow
        self.checkBoxLog = self.ui.checkBox_log
        self.checkBoxPoly = self.ui.checkBox_multII
        self.checkBoxDefault = self.ui.checkBox_default
        self.checkBoxLinest.toggled.connect(lambda: self.putLinChartValues(timeSeries, ret_model_values(df),
                                                                           self.checkBoxLinest))
        self.checkBoxBrown.toggled.connect(lambda: self.putBrownChartValues(timeSeries, retBrownProgValues(df, timeSeries),
                                                                            self.checkBoxBrown))
        self.checkBoxHolt.toggled.connect(lambda: self.putHoltChartValues(timeSeries, retHoltValues(df), self.checkBoxHolt))
        self.checkBoxExp.toggled.connect(lambda: self.putEXPChartValues(timeSeries, ret_transfromed_exp_model_to_linear(df), self.checkBoxExp))
        self.checkBoxPow.toggled.connect(lambda: self.putPowerChartValues(timeSeries, ret_power_values(df), self.checkBoxPow))
        self.checkBoxLog.toggled.connect(lambda: self.putLogChartValues(timeSeries, ret_log_values(df), self.checkBoxLog))
        self.checkBoxPoly.toggled.connect(lambda: self.putPolyChartValues(timeSeries, ret_poly_values(df), self.checkBoxPoly))
        self.checkBoxDefault.toggled.connect(lambda: self.putDefaultChartValues(timeSeries, df, self.checkBoxDefault))


    def putLinChartValues(self, times, dataFrame, b):
        # dataFrame = dataFrame[:-2]
        # nowe okno tworzy
        """optCurve = pg.plot(timeS, dataFrame, pen=pg.mkPen(color=(200, 100, 255), style=QtCore.Qt.DotLine),
                           symbol='o')"""
        if b.isChecked():
            self.optLinCurve.setData(times, dataFrame, pen=pg.mkPen(color=(200, 100, 255), style=QtCore.Qt.DotLine))
        else:
            self.optLinCurve.setData([], [], pen=pg.mkPen(color=(0, 0, 0), style=QtCore.Qt.DotLine), alpha=0.0)

    def putBrownChartValues(self, times, dataFrame, b):
        times = times[2:]
        if b.isChecked():
            self.optBrownCurve.setData(times, dataFrame, pen=pg.mkPen(color=(100, 200, 255), style=QtCore.Qt.DotLine))
        else:
            self.optBrownCurve.setData([], [], pen=pg.mkPen(color=(0, 0, 0), style=QtCore.Qt.DotLine), alpha=0.0)

    def putHoltChartValues(self, times, dataFrame, b):
        times = times[1:]
        if b.isChecked():
            self.optHoltCurve.setData(times, dataFrame, pen=pg.mkPen(color=(100, 255, 200), style=QtCore.Qt.DotLine))
        else:
            self.optHoltCurve.setData([], [], pen=pg.mkPen(color=(0, 0, 0), style=QtCore.Qt.DotLine), alpha=0.0)

    def putEXPChartValues(self, times, dataFrame, b):
        if b.isChecked():
            self.optEXPCurve.setData(times, dataFrame, pen=pg.mkPen(color=(200, 255, 100), style=QtCore.Qt.DotLine))
        else:
            self.optEXPCurve.setData([], [], pen=pg.mkPen(color=(0, 0, 0), style=QtCore.Qt.DotLine), alpha=0.0)

    def putPowerChartValues(self, times, dataFrame, b):
        if b.isChecked():
            self.optPowerCurve.setData(times, dataFrame, pen=pg.mkPen(color=(255, 200, 100), style=QtCore.Qt.DotLine))
        else:
            self.optPowerCurve.setData([], [], pen=pg.mkPen(color=(0, 0, 0), style=QtCore.Qt.DotLine), alpha=0.0)

    def putLogChartValues(self, times, dataFrame, b):
        if b.isChecked():
            self.optLogCurve.setData(times, dataFrame, pen=pg.mkPen(color=(255, 100, 200), style=QtCore.Qt.DotLine))
        else:
            self.optLogCurve.setData([], [], pen=pg.mkPen(color=(0, 0, 0), style=QtCore.Qt.DotLine), alpha=0.0)

    def putPolyChartValues(self, times, dataFrame, b):
        if b.isChecked():
            self.optPolyCurve.setData(times, dataFrame, pen=pg.mkPen(color=(0, 100, 200), style=QtCore.Qt.DotLine))
        else:
            self.optPolyCurve.setData([], [], pen=pg.mkPen(color=(0, 0, 0), style=QtCore.Qt.DotLine), alpha=0.0)

    def putDefaultChartValues(self, times, dataFrame, b):
        if b.isChecked():
            self.optDefaultCurve.setData(times, dataFrame, pen=pg.mkPen(color=(255, 255, 255)),
                                      symbol='o')
        else:
            self.optDefaultCurve.setData([], [], pen=pg.mkPen(color=(0, 0, 0)), alpha=0.0)

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
        #print("Menu Slided!")
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
