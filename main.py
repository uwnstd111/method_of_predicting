from PyQt5.QtWidgets import (QTableWidgetItem, QFileDialog)

import pyqtgraph as pg
from PyQt5.QtWidgets import QApplication, QMainWindow, QSizeGrip, QGraphicsDropShadowEffect
from PySide2 import QtCore, QtGui
from PyQt5.QtCore import QPropertyAnimation
from qt_material import *
import re
from brown import *
from linest import *
from holt import *
from exponencial import *
from power import *
from logarythmical import *
from polynomial import *
from multi_regression import *
from PyQt5.QtWidgets import QMessageBox

# IMPORT GUI

from interface3 import *

####################################
# MAIN WINDOW CLASS
####################################

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.path = ''
        self.all_data = None
        self.glob_w_coef = 1
        self.ui.pushButton_4.setEnabled(False)
        self.ui.spinBox.setVisible(False)
        self.ui.label_7.setVisible(False)
        self.list = []
        self.time_serial_list = []
        self.depending_variables_list = []
        self.final_list_for_mult_reg = []
        shadowEffect = QGraphicsDropShadowEffect()
        shadowEffect.setBlurRadius(15)
        QSizeGrip(self.ui.size_grip)
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

        # Top Bar NAVI #

        self.ui.minimaze_window_button.clicked.connect(lambda:
                                                       self.showMinimized())
        self.ui.restore_window_button.clicked.connect(lambda:
                                                      self.restore_or_maximize_window())
        self.ui.close_window_button.clicked.connect(lambda:
                                                    self.close())
        # NAVIGATION #

        self.ui.import_button.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.import_page))
        self.ui.import_button.clicked.connect(lambda: self.glowImportLabel(shadowEffect))

        self.ui.properties_button.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.prop_page))
        self.ui.properties_button.clicked.connect(lambda: self.glowPropLabel(shadowEffect))

        self.ui.score_button.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.score_page))
        self.ui.score_button.clicked.connect(lambda: self.glowScoreLabel(shadowEffect))

        def moveEvent(event):
            if not self.isMaximized():
                if event.buttons() == QtCore.Qt.LeftButton:
                    self.move(self.pos() + event.globalPos() - self.oldPosition)
                    self.oldPosition = event.globalPos()
                # delta = QPoint(event.globalPos() - self.oldPosition)
                # self.move(self.x() + delta.x(), self.y() + delta.y())
                # self.oldPosition = event.globalPos()

        self.ui.header_main_frame.mouseMoveEvent = moveEvent

        # MENU BUTTON
        self.ui.pushButton.clicked.connect(lambda: self.slideLeftMenu())

        self.ui.pushButton_3.clicked.connect(self.openFile)
        self.ui.pushButton_4.clicked.connect(self.showData)

        self.ui.pushButton_2.clicked.connect(lambda: self.show_pop_up_info("Wyświetlanie okna pomocy dostępne będzie w następnej wersji programu!"))

        apply_stylesheet(app, theme=list_themes()[1])
        self.ui.label_4.setStyleSheet("border : 4px solid blue")
        # CHART  detection

        def mouseOnChartMoved(evt):
            p = self.ui.graphicsView.plotItem.vb.mapSceneToView(evt[0])

            mousePoint = p
            self.ui.label_12.setText(str(int(mousePoint.x() + 0.5)))
            self.ui.label_11.setText(str("{:.2f}".format(mousePoint.y())))

        self.proxy = pg.SignalProxy(self.ui.graphicsView.scene().sigMouseMoved, rateLimit=60, slot=mouseOnChartMoved)

        #   CHART   LAYERS
        self.ui.graphicsView_2.addLegend()
        #self.ui.graphicsView.addLegend()
        self.curve2 = self.ui.graphicsView.plot(pen=pg.mkPen(color=(0, 0, 0), style=QtCore.Qt.DotLine))
        self.optLinCurve = self.ui.graphicsView_2.plot(pen=pg.mkPen(color=(0, 0, 0), style=QtCore.Qt.DotLine), name="Liniowy")
        self.optBrownCurve = self.ui.graphicsView_2.plot(pen=pg.mkPen(color=(0, 0, 0), style=QtCore.Qt.DotLine), name="Brown")
        self.optHoltCurve = self.ui.graphicsView_2.plot(pen=pg.mkPen(color=(0, 0, 0), style=QtCore.Qt.DotLine), name="Holt")
        self.optEXPCurve = self.ui.graphicsView_2.plot(pen=pg.mkPen(color=(0, 0, 0), style=QtCore.Qt.DotLine), name="Wykładniczy")
        self.optPowerCurve = self.ui.graphicsView_2.plot(pen=pg.mkPen(color=(0, 0, 0), style=QtCore.Qt.DotLine), name="Potęgowy")
        self.optLogCurve = self.ui.graphicsView_2.plot(pen=pg.mkPen(color=(0, 0, 0), style=QtCore.Qt.DotLine), name="Logarytmiczny")
        self.optPolyCurve = self.ui.graphicsView_2.plot(pen=pg.mkPen(color=(0, 0, 0), style=QtCore.Qt.DotLine), name="Wielomianowy II")
        self.optMultRegCurve = self.ui.graphicsView_2.plot(pen=pg.mkPen(color=(0, 0, 0), style=QtCore.Qt.DotLine), name="Regresja wieloraka")
        self.optDefaultCurve = self.ui.graphicsView_2.plot(pen=pg.mkPen(color=(0, 0, 0)), name="Oryginalny zbiór danych")

        #   MODEL ERRORS
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
        path = QFileDialog.getOpenFileName(self, "Wybierz plik z danymi", os.getcwd(), "CSV (*.csv);;Excel (*.xls, *.xlsx)")
        result = re.split('[/]', path[0])
        r = result[len(result) - 1]
        controlRegex = re.findall('.csv|.xlsx|.xls', r)
        r = re.split('.csv|.xlsx|.xls', r)
        self.click = 1
        print(controlRegex[0])
        if sys.getsizeof(self.all_data) > 16:
            self.all_data = None
            self.list = []
            self.time_serial_list = []
        print(sys.getsizeof(self.all_data))
        if path != ('', ''):
            if controlRegex[0] == '.csv':
                self.all_data = pd.read_csv(path[0], sep=':|;|\t', error_bad_lines=False, index_col=False, dtype='unicode',
                                            engine='python')
                if not self.all_data.empty:
                    self.ui.pushButton_4.setEnabled(True)
                else:
                    self.ui.pushButton_4.setEnabled(False)
                    self.show_pop_up_error("Zbiór danych jest pusty!")
            else:
                self.all_data = pd.read_excel(path[0], engine='openpyxl')
                if not self.all_data.empty:
                    self.ui.pushButton_4.setEnabled(True)
                else:
                    self.ui.pushButton_4.setEnabled(False)

        self.ui.tabWidget.setTabText(self.ui.tabWidget.indexOf(self.ui.tab_3), r[0])

    # dashboard_df = pd.read_csv(p_file, sep=',', error_bad_lines=False, index_col=False, dtype='unicode')

    def show_pop_up_error(self, text):
        msg1 = QMessageBox()
        msg1.setWindowTitle("Błąd importu")
        msg1.setText(text) # "Niepoprawny format pliku lub liczby kolumn"
        msg1.setIcon(QMessageBox.Critical)
        msg1.exec_()

    def show_pop_up_info(self, text):
        msg1 = QMessageBox()
        msg1.setWindowTitle("Pomoc")
        msg1.setText(text)  # "Niepoprawny format pliku lub liczby kolumn"
        msg1.setIcon(QMessageBox.Information)
        msg1.exec_()

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

        self.ui.tableWidget.resizeColumnsToContents()

        for index, row in self.all_data.iterrows():
            tmplist = row[2:]
            if len(row) <= 1:
                self.show_pop_up_error("Zbiór danych nie może zawierać mniej niż '2' kolumny!")
                return None

            if len(row) == 2:
                self.time_serial_list.append(int(row[0]))
                self.list.append(float(row[1]))
                self.ui.checkBox_regmult.setDisabled(True)
            if len(row) >= 3:
                self.time_serial_list.append(int(row[0]))
                self.list.append(float(row[1]))
                self.depending_variables_list.append(tmplist)
                self.ui.checkBox_regmult.setDisabled(False)

        for i in range(len(self.all_data.columns) - 2):
            tmplist = []
            for j in range(len(self.list)):
                tmplist.append(self.depending_variables_list[j][i])
                print(self.depending_variables_list[j][i])
            self.final_list_for_mult_reg.append(tmplist)

        """self.F_statistic = f.ppf(q=1 - 0.05, dfn=2, dfd=len(self.list) - 3)
        alpha = 0.05
        self.T_student_criticalValue = t.ppf(q=1 - alpha / 2, df=len(self.list) - 2)
        print("Wartosc krytyczna T-Student: " + str(retCriticalTValue(df, 0.05, 2)))
        """
        self.optDefaultCurve.setData(self.time_serial_list, self.list, pen=pg.mkPen(color=(255, 255, 255)),
                                     symbol='o')
        self.ui.pushButton_3.setDisabled(False)
        self.initializeRunMethods(self.list, self.time_serial_list, self.final_list_for_mult_reg)

    def initializeRunMethods(self, df, timeSeries, list_of_depend_var):
        if len(df) > len(timeSeries):
            df = df[:-2]

        curve1 = self.ui.graphicsView.plot(name="Brak")  #referencje
        curve1.setData(timeSeries, df, symbol='o')

        self.checkBoxLinest = self.ui.checkBox_lin
        self.checkBoxBrown = self.ui.checkBox_brown
        self.checkBoxHolt = self.ui.checkBox_holt
        self.checkBoxExp = self.ui.checkBox_exp
        self.checkBoxPow = self.ui.checkBox_pow
        self.checkBoxLog = self.ui.checkBox_log
        self.checkBoxPoly = self.ui.checkBox_multII
        self.checkBoxMultReg = self.ui.checkBox_regmult
        self.checkBoxDefault = self.ui.checkBox_default
        self.checkBoxLinest.toggled.connect(lambda: self.putLinChartValues(timeSeries, ret_model_values(df, timeSeries),
                                                                           self.checkBoxLinest))
        self.checkBoxBrown.toggled.connect(lambda: self.putBrownChartValues(timeSeries, retBrownProgValues(df, timeSeries),
                                                                            self.checkBoxBrown))
        self.checkBoxHolt.toggled.connect(lambda: self.putHoltChartValues(timeSeries, retHoltValues(df), self.checkBoxHolt))
        self.checkBoxExp.toggled.connect(lambda: self.putEXPChartValues(timeSeries, ret_transfromed_exp_model_to_linear(df), self.checkBoxExp))
        self.checkBoxPow.toggled.connect(lambda: self.putPowerChartValues(timeSeries, ret_power_values(df), self.checkBoxPow))
        self.checkBoxLog.toggled.connect(lambda: self.putLogChartValues(timeSeries, ret_log_values(df), self.checkBoxLog))
        self.checkBoxPoly.toggled.connect(lambda: self.putPolyChartValues(timeSeries, ret_poly_values(df), self.checkBoxPoly))
        self.checkBoxMultReg.toggled.connect(lambda: self.putMultRegChartValues(timeSeries, ret_multreg_values(df, timeSeries, list_of_depend_var)[0], self.checkBoxMultReg))
        self.checkBoxDefault.toggled.connect(lambda: self.putDefaultChartValues(timeSeries, df, self.checkBoxDefault))

        self.ui.auto_choose_button.clicked.connect(lambda: self.autoModelChoose(df, timeSeries, list_of_depend_var))
        self.ui.model_choose_comboBox.activated.connect(lambda: self.chosenModel(df, timeSeries, list_of_depend_var))


    def putLinChartValues(self, times, dataFrame, b):
        if b.isChecked():
            self.optLinCurve.setData(times, dataFrame, pen=pg.mkPen(color=(200, 100, 255), style=QtCore.Qt.DotLine))
        else:
            self.optLinCurve.setData([], [], pen=pg.mkPen(color=(0, 0, 0), style=QtCore.Qt.DotLine), alpha=0.0)

    def putBrownChartValues(self, times, dataFrame, b):
        times = times[2:]
        if len(dataFrame) > len(times):
            dataFrame = dataFrame[:-2]
        if b.isChecked():
            self.optBrownCurve.setData(times, dataFrame, pen=pg.mkPen(color=(100, 200, 255), style=QtCore.Qt.DotLine))
        else:
            self.optBrownCurve.setData([], [], pen=pg.mkPen(color=(0, 0, 0), style=QtCore.Qt.DotLine), alpha=0.0)

    def putHoltChartValues(self, times, dataFrame, b):
        times = times[1:]
        if len(dataFrame) > len(times):
            dataFrame = dataFrame[:-2]
        if b.isChecked():
            self.optHoltCurve.setData(times, dataFrame, pen=pg.mkPen(color=(100, 255, 200), style=QtCore.Qt.DotLine))
        else:
            self.optHoltCurve.setData([], [], pen=pg.mkPen(color=(0, 0, 0), style=QtCore.Qt.DotLine), alpha=0.0)

    def putEXPChartValues(self, times, dataFrame, b):
        if len(dataFrame) > len(times):
            dataFrame = dataFrame[:-2]
        if b.isChecked():
            self.optEXPCurve.setData(times, dataFrame, pen=pg.mkPen(color=(200, 255, 100), style=QtCore.Qt.DotLine))
        else:
            self.optEXPCurve.setData([], [], pen=pg.mkPen(color=(0, 0, 0), style=QtCore.Qt.DotLine), alpha=0.0)

    def putPowerChartValues(self, times, dataFrame, b):
        if len(dataFrame) > len(times):
            dataFrame = dataFrame[:-2]
        if b.isChecked():
            self.optPowerCurve.setData(times, dataFrame, pen=pg.mkPen(color=(255, 200, 100), style=QtCore.Qt.DotLine))
        else:
            self.optPowerCurve.setData([], [], pen=pg.mkPen(color=(0, 0, 0), style=QtCore.Qt.DotLine), alpha=0.0)

    def putLogChartValues(self, times, dataFrame, b):
        if len(dataFrame) > len(times):
            dataFrame = dataFrame[:-2]
        if b.isChecked():
            self.optLogCurve.setData(times, dataFrame, pen=pg.mkPen(color=(255, 100, 200), style=QtCore.Qt.DotLine))
        else:
            self.optLogCurve.setData([], [], pen=pg.mkPen(color=(0, 0, 0), style=QtCore.Qt.DotLine), alpha=0.0)

    def putPolyChartValues(self, times, dataFrame, b):
        if len(dataFrame) > len(times):
            dataFrame = dataFrame[:-2]
        if b.isChecked():
            self.optPolyCurve.setData(times, dataFrame, pen=pg.mkPen(color=(0, 100, 200), style=QtCore.Qt.DotLine))
        else:
            self.optPolyCurve.setData([], [], pen=pg.mkPen(color=(0, 0, 0), style=QtCore.Qt.DotLine), alpha=0.0)

    def putMultRegChartValues(self, times, dataFrame, b):
        if len(dataFrame) > len(times):
            dataFrame = dataFrame[:-2]
        if b.isChecked():
            self.optMultRegCurve.setData(times, dataFrame, pen=pg.mkPen(color=(0, 200, 100), style=QtCore.Qt.DotLine))
        else:
            self.optMultRegCurve.setData([], [], pen=pg.mkPen(color=(0, 0, 0), style=QtCore.Qt.DotLine), alpha=0.0)

    def putDefaultChartValues(self, times, dataFrame, b):
        if len(dataFrame) > len(times):
            dataFrame = dataFrame[:-2]
        if b.isChecked():
            self.optDefaultCurve.setData(times, dataFrame, pen=pg.mkPen(color=(255, 255, 255)),
                                      symbol='o')
        else:
            self.optDefaultCurve.setData([], [], pen=pg.mkPen(color=(0, 0, 0)), alpha=0.0)

    def autoModelChoose(self, df, timeSeries, df_mult):
        corr = 0
        if len(df) > len(timeSeries):
            df = df[:-2]
        best_list = []
        keys_to_dict = ['Liniowy', 'Browna', 'Holta', 'Wykładniczy', 'Potęgowy', 'Logarytmiczny',
                        'Wielomianowy II stopnia', 'Regresja wieloraka']
        self.setErrorDefaults()
        if self.ui.auto_choose_button.text() == "Nie":
            self.linest_error = float(ret_coef_of_variation_linest(df, timeSeries).strip('%')) / 100
            self.brown_error = float(ret_ex_post_error_brown(df, timeSeries).strip('%')) / 100
            self.holt_error = float(ret_ex_post_error_holt(df).strip('%')) / 100
            self.exp_error = float(ret_coef_of_variation_exp(df).strip('%')) / 100
            self.power_error = float(ret_coef_of_variation_power(df).strip('%')) / 100
            self.log_error = float(ret_coef_of_variation_log(df).strip('%')) / 100
            self.poly_error = float(ret_coef_of_variation_poly(df).strip('%')) / 100

            if not len(df_mult) == 0:
                self.mult_reg_error = float(ret_coef_of_variation_mult_reg(df, timeSeries, df_mult).strip('%')) / 100
                corr = calculate_correlation(df, df_mult, self.all_data.columns)
            else:
                self.mult_reg_error = 1

            best_list.append(self.linest_error)
            best_list.append(self.brown_error)
            best_list.append(self.holt_error)
            best_list.append(self.exp_error)
            best_list.append(self.power_error)
            best_list.append(self.log_error)
            best_list.append(self.poly_error)
            best_list.append(self.mult_reg_error)
            X = dict(zip(keys_to_dict, best_list))
            sorted_dict = sorted(X.items(), key=lambda x: x[1])

            self.ui.suggested_model_label.setText(str(sorted_dict[0][0]))
            self.ui.chosen_method_label_value.setText(str(sorted_dict[0][0]))

            w_coef = "{:.3%}".format(float(sorted_dict[0][1]))
            self.glob_w_coef = float(sorted_dict[0][1])
            self.ui.w_coef_label_value.setText(w_coef)

            if sorted_dict[0][0] == 'Regresja wieloraka':
                self.fillMultRegStats(corr, df, df_mult, timeSeries, self.glob_w_coef)
            else:
                if sorted_dict[0][0] == 'Wykładniczy':
                    self.fillExpStats(df, timeSeries, self.glob_w_coef)
                else:
                    if sorted_dict[0][0] == 'Liniowy':
                        self.fillLinStats(df, timeSeries, self.glob_w_coef)
                    else:
                        if sorted_dict[0][0] == 'Browna':
                            self.fillBrownStats(df, timeSeries, self.glob_w_coef)
                        else:
                            if sorted_dict[0][0] == 'Holta':
                                self.fillHoltStats(df, timeSeries, self.glob_w_coef)
                            else:
                                if sorted_dict[0][0] == 'Potęgowy':
                                    self.fillPowerStats(df, timeSeries, self.glob_w_coef)
                                else:
                                    if sorted_dict[0][0] == 'Logarytmiczny':
                                        self.fillLogStats(df, timeSeries, self.glob_w_coef)
                                    else:
                                        if sorted_dict[0][0] == 'Wielomianowy II stopnia':
                                            self.fillPolyStats(df, timeSeries, self.glob_w_coef)
                                        else:
                                            self.fill_default_stats()

            self.ui.auto_choose_button.setText("Tak")
            self.ui.model_choose_comboBox.setDisabled(True)
        else:
            self.ui.auto_choose_button.setText("Nie")
            print(self.click)
            self.ui.suggested_model_label.setText("<Proponowany model>")
            self.ui.model_choose_comboBox.setDisabled(False)

    def setErrorDefaults(self):
        self.linest_error = 1
        self.brown_error = 1
        self.holt_error = 1
        self.exp_error = 1
        self.power_error = 1
        self.log_error = 1
        self.poly_error = 1
        self.mult_reg_error = 1


    def chosenModel(self, df, timeSeries, df_mult):
        corr = 0
        if len(df) > len(timeSeries):
            df = df[:-2]
        if not len(df_mult) == 0:
            error = float(ret_coef_of_variation_mult_reg(df, timeSeries, df_mult).strip('%')) / 100
            corr = calculate_correlation(df, df_mult, self.all_data.columns)
        else:
            error = 1
        cb_str = self.ui.model_choose_comboBox.currentText()

        cb_index = self.ui.model_choose_comboBox.currentIndex()
        self.ui.chosen_method_label_value.setText(cb_str)
        if cb_str == 'Regresja wieloraka':
            self.fillMultRegStats(corr, df, df_mult, timeSeries, error)
        else:
            if cb_str == 'Wykładniczy':
                error = float(ret_coef_of_variation_exp(df).strip('%')) / 100
                self.fillExpStats(df, timeSeries, error)
            else:
                if cb_str == 'Liniowy':
                    error = float(ret_coef_of_variation_linest(df, timeSeries).strip('%')) / 100
                    self.fillLinStats(df, timeSeries, error)
                else:
                    if cb_str == 'Browna':
                        error = float(ret_ex_post_error_brown(df, timeSeries).strip('%')) / 100
                        self.fillBrownStats(df, timeSeries, error)
                    else:
                        if cb_str == 'Holta':
                            error = float(ret_ex_post_error_holt(df).strip('%')) / 100
                            self.fillHoltStats(df, timeSeries, error)
                        else:
                            if cb_str == 'Potęgowy':
                                error = float(ret_coef_of_variation_power(df).strip('%')) / 100
                                self.fillPowerStats(df, timeSeries, error)
                            else:
                                if cb_str == 'Logarytmiczny':
                                    error = float(ret_coef_of_variation_log(df).strip('%')) / 100
                                    self.fillLogStats(df, timeSeries, error)
                                else:
                                    if cb_str == 'Wielomianowy II stopnia':
                                        error = float(ret_coef_of_variation_poly(df).strip('%')) / 100
                                        self.fillPolyStats(df, timeSeries, error)
                                    else:
                                        self.fill_default_stats()
                                        error = 1

        w_coef = "{:.3%}".format(float(error))
        self.ui.w_coef_label_value.setText(w_coef)

        if self.ui.model_choose_comboBox.currentIndex() > 0:
            self.ui.auto_choose_button.setDisabled(True)
        else:
            self.ui.auto_choose_button.setDisabled(False)

    def fill_default_stats(self):
        self.ui.chosen_method_label_value.setText("N/A")
        self.ui.corr_label_value.setText("N/A")
        self.ui.r_suared_label_value.setText("N/A")
        self.ui.mean_label_value.setText("N/A")
        self.ui.st_dev_label_value.setText("N/A")
        self.ui.w_coef_label_value.setText("N/A")
        self.ui.point_prognosis_label_value.setText("N/A")
        self.ui.optimum_alpha_label_value.setText("N/A")
        self.ui.optimum_beta_label_value.setText("N/A")
        self.curve2.setData([], [],
                            pen=pg.mkPen(color=(0, 0, 0), style=QtCore.Qt.DotLine))

    def fillLinStats(self, df, timeSeries, w):
        self.ui.corr_label_value.setText("Brak")
        self.ui.optimum_alpha_label_value.setText("Brak")
        self.ui.optimum_beta_label_value.setText("Brak")
        self.ui.r_suared_label_value.setText(str(ret_coef_of_determination(df, timeSeries)))
        self.ui.mean_label_value.setText(str(format(statistics.mean(df), '.3f')))
        self.ui.st_dev_label_value.setText(str(format((w * statistics.mean(df))**2, '.3f')))
        text = retPointPrognosis(df)
        res = []
        for item in text:
            text = format(item, '.3f')
            print(text)
            res.append(text)
        res = str(res).replace('\'', '')
        self.ui.point_prognosis_label_value.setText(str(res))
        curve2 = self.ui.graphicsView.plot()  # referencje

        t = list(timeSeries)
        r = t[len(t) - 1] - t[len(t) - 2]
        t.append(t[len(t) - 1] + r)
        t.append(t[len(t) - 1] + r)
        d = list(ret_model_values(df, timeSeries))
        points = list(retPointPrognosis(ret_model_values(df, timeSeries)))
        d.append(points[0])
        d.append(points[1])

        self.curve2.setData(t, d,
                            pen=pg.mkPen(color=(200, 100, 255), style=QtCore.Qt.DotLine),
                            symbol='o')

    def fillBrownStats(self, df, timeSeries, w):
        self.ui.corr_label_value.setText("Brak")
        self.ui.r_suared_label_value.setText("Nieistotne")
        self.ui.mean_label_value.setText(str(format(statistics.mean(df), '.3f')))
        self.ui.st_dev_label_value.setText(str(format((w * statistics.mean(df))**2, '.3f')))
        self.ui.optimum_alpha_label_value.setText(str(format(retOptimumAlpha(df, timeSeries), '.3f')))
        self.ui.optimum_beta_label_value.setText("Brak")

        text = retPointPrognosis_Brown(df, timeSeries)
        res = []
        for item in text:
            text = format(item, '.3f')
            res.append(text)
        res = str(res).replace('\'', '')
        self.ui.point_prognosis_label_value.setText(str(res))

        t = list(timeSeries)
        r = t[len(t) - 1] - t[len(t) - 2]
        t.append(t[len(t) - 1] + r)
        t.append(t[len(t) - 1] + r)
        d = list(retBrownProgValues(df, timeSeries))
        points = list(retPointPrognosis_Brown(df, timeSeries))
        d.append(points[0])
        d.append(points[1])
        self.curve2.setData(t[2:], d,
                            pen=pg.mkPen(color=(100, 200, 255), style=QtCore.Qt.DotLine),
                            symbol='o')

    def fillHoltStats(self, df, timeSeries, w):
        self.ui.corr_label_value.setText("Brak")
        self.ui.r_suared_label_value.setText("Nieistotne")
        self.ui.mean_label_value.setText(str(format(statistics.mean(df), '.3f')))
        self.ui.st_dev_label_value.setText(str(format((w * statistics.mean(df))**2, '.3f')))
        a, b = ret_opt_alpha_Holt(df)
        self.ui.optimum_alpha_label_value.setText(str(format(a, '.3f')))
        self.ui.optimum_beta_label_value.setText(str(format(b, '.3f')))

        text = retPointPrognosis_Holt(df)
        res = []
        for item in text:
            text = format(item, '.3f')
            res.append(text)
        res = str(res).replace('\'', '')
        self.ui.point_prognosis_label_value.setText(str(res))

        t = list(timeSeries)
        r = t[len(t) - 1] - t[len(t) - 2]
        t.append(t[len(t) - 1] + r)
        t.append(t[len(t) - 1] + r)
        d = list(retHoltValues(df))
        points = list(retPointPrognosis_Holt(df))
        d.append(points[0])
        d.append(points[1])
        self.curve2.setData(t[1:], d,
                            pen=pg.mkPen(color=(100, 255, 200), style=QtCore.Qt.DotLine),
                            symbol='o')

    def fillExpStats(self, df, timeSeries, w):
        self.ui.corr_label_value.setText("Brak")
        self.ui.optimum_alpha_label_value.setText("Brak")
        self.ui.optimum_beta_label_value.setText("Brak")
        self.ui.r_suared_label_value.setText(str(ret_coef_of_determination_exp(df, timeSeries)))
        self.ui.mean_label_value.setText(str(format(statistics.mean(np.log(df)), '.3f')))
        self.ui.st_dev_label_value.setText(str(format((w * statistics.mean(np.log(df)))**2, '.3f')))
        text = str(retPointPrognosis_EXP(df))
        text.strip('[]')
        text = text.replace('\'', '')
        text.strip('[]')
        self.ui.point_prognosis_label_value.setText(text)

        t = list(timeSeries)
        r = t[len(t) - 1] - t[len(t) - 2]
        t.append(t[len(t) - 1] + r)
        t.append(t[len(t) - 1] + r)
        d = list(ret_transfromed_exp_model_to_linear(df))
        points = list(retPointPrognosis_EXP(df))
        d.append(float(points[0]))
        d.append(float(points[1]))
        self.curve2.setData(t, d,
                            pen=pg.mkPen(color=(200, 255, 100), style=QtCore.Qt.DotLine),
                            symbol='o')

    def fillPowerStats(self, df, timeSeries, w):
        self.ui.corr_label_value.setText("Brak")
        self.ui.optimum_alpha_label_value.setText("Brak")
        self.ui.optimum_beta_label_value.setText("Brak")
        self.ui.mean_label_value.setText(str(format(statistics.mean(np.log(df)), '.3f')))
        self.ui.st_dev_label_value.setText(str(format((w * statistics.mean(np.log(df)))**2, '.3f')))
        self.ui.r_suared_label_value.setText(str(ret_coef_of_determination_power(df, timeSeries)))

        text = str(retPointPrognosis_Power(df))
        text.strip('[]')
        text = text.replace('\'', '')
        self.ui.point_prognosis_label_value.setText(text)

        t = list(timeSeries)
        r = t[len(t) - 1] - t[len(t) - 2]
        t.append(t[len(t) - 1] + r)
        t.append(t[len(t) - 1] + r)
        d = list(ret_power_values(df))
        points = list(retPointPrognosis_Power(df))
        d.append(float(points[0]))
        d.append(float(points[1]))
        self.curve2.setData(t, d,
                            pen=pg.mkPen(color=(255, 200, 100), style=QtCore.Qt.DotLine),
                            symbol='o')

    def fillLogStats(self, df, timeSeries, w):
        self.ui.corr_label_value.setText("Brak")
        self.ui.optimum_alpha_label_value.setText("Brak")
        self.ui.optimum_beta_label_value.setText("Brak")
        self.ui.mean_label_value.setText(str(format(statistics.mean(df), '.3f')))
        self.ui.st_dev_label_value.setText(str(format((w * statistics.mean(df))**2, '.3f')))
        self.ui.r_suared_label_value.setText(str(ret_coef_of_determination_log(df)))

        text = str(ret_log_points(df))
        text.strip('[]')
        text = text.replace('\'', '')
        self.ui.point_prognosis_label_value.setText(text)

        t = list(timeSeries)
        r = t[len(t) - 1] - t[len(t) - 2]
        t.append(t[len(t) - 1] + r)
        t.append(t[len(t) - 1] + r)
        d = list(ret_log_values(df))
        points = list(ret_log_points(df))
        d.append(float(points[0]))
        d.append(float(points[1]))
        self.curve2.setData(t, d,
                            pen=pg.mkPen(color=(255, 100, 200), style=QtCore.Qt.DotLine),
                            symbol='o')

    def fillPolyStats(self, df, timeSeries, w):
        self.ui.corr_label_value.setText("Brak")
        self.ui.optimum_alpha_label_value.setText("Brak")
        self.ui.optimum_beta_label_value.setText("Brak")
        self.ui.mean_label_value.setText(str(format(statistics.mean(df), '.3f')))
        self.ui.st_dev_label_value.setText(str(format((w * statistics.mean(df))**2, '.3f')))
        self.ui.r_suared_label_value.setText(str(ret_coef_of_determination_poly(df)))

        text = str(ret_poly_points(df))
        text.strip('[]')
        text = text.replace('\'', '')
        self.ui.point_prognosis_label_value.setText(text)

        t = list(timeSeries)
        r = t[len(t) - 1] - t[len(t) - 2]
        t.append(t[len(t) - 1] + r)
        t.append(t[len(t) - 1] + r)
        d = list(ret_poly_values(df))
        points = list(ret_poly_points(df))
        d.append(float(points[0]))
        d.append(float(points[1]))
        self.curve2.setData(t, d,
                            pen=pg.mkPen(color=(0, 100, 200), style=QtCore.Qt.DotLine),
                            symbol='o')

    def fillMultRegStats(self, corr, df, list_of_dep_var, timeSeries, w):
        self.ui.optimum_alpha_label_value.setText("Brak")
        self.ui.optimum_beta_label_value.setText("Brak")
        self.ui.corr_label_value.setText(str(corr))
        self.ui.mean_label_value.setText(str(format(statistics.mean(df), '.3f')))
        self.ui.st_dev_label_value.setText(str(format((w * statistics.mean(df))**2, '.3f')))
        self.ui.r_suared_label_value.setText(str(ret_coef_of_determination_mult_reg(df, timeSeries, list_of_dep_var)))

        text = ret_multreg_values(df, timeSeries, list_of_dep_var)[1]
        res = []
        for item in text:
            text = format(item, '.3f')
            res.append(text)
        res = str(res).replace('\'', '')
        self.ui.point_prognosis_label_value.setText(str(res))

        t = list(timeSeries)
        r = t[len(t) - 1] - t[len(t) - 2]
        t.append(t[len(t) - 1] + r)
        t.append(t[len(t) - 1] + r)
        d = list(ret_multreg_values(df, timeSeries, list_of_dep_var)[0])

        print(ret_multreg_values(df, timeSeries, list_of_dep_var)[1])

        points = list(ret_multreg_values(df, timeSeries, list_of_dep_var)[1])
        d.append(float(points[0]))
        d.append(float(points[1]))
        self.curve2.setData(t, d,
                            pen=pg.mkPen(color=(0, 200, 100), style=QtCore.Qt.DotLine),
                            symbol='o')

    def calculatedStatisticsBasedOnChosenMethod(self):
        self.coef_of_determination = 0
        self.mean = 1
        self.standardError = 0
        self.F_statistic = "N/A"
        self.T_student_criticalValue = "N/A"
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
        if not self.isMaximized():
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
