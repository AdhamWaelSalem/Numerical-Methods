from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QTableWidgetItem
import gui

class Ui_outputWindow(object):
    def setupUi(self, outputWindow, data, rows, columns, time, function, root, precision, method):
        outputWindow.resize(800, 600)

        self.centralwidget = QtWidgets.QWidget(outputWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(0, 100, 801, 331))
        self.tableWidget.setObjectName("tableWidget")

        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(10)

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 480, 34, 16))
        self.label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label.setFont(font)

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 510, 61, 16))
        self.label_2.setFont(font)

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 540, 101, 16))
        self.label_3.setFont(font)

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 570, 131, 16))
        self.label_4.setFont(font)

        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(20, 450, 61, 16))
        self.label_10.setFont(font)

        self.func_label = QtWidgets.QLabel(self.centralwidget)
        self.func_label.setGeometry(QtCore.QRect(90, 450, 261, 16))
        self.func_label.setFont(font)
        self.func_label.setText(function)

        self.root_label = QtWidgets.QLabel(self.centralwidget)
        self.root_label.setGeometry(QtCore.QRect(60, 480, 241, 16))
        self.root_label.setFont(font)
        self.root_label.setText(str(root))

        self.precision_label = QtWidgets.QLabel(self.centralwidget)
        self.precision_label.setGeometry(QtCore.QRect(90, 510, 151, 16))
        self.precision_label.setFont(font)
        self.precision_label.setText(str(precision))

        self.time_lable = QtWidgets.QLabel(self.centralwidget)
        self.time_lable.setGeometry(QtCore.QRect(120, 540, 181, 16))
        self.time_lable.setFont(font)
        self.time_lable.setText(str(time))

        self.iterations_label = QtWidgets.QLabel(self.centralwidget)
        self.iterations_label.setGeometry(QtCore.QRect(150, 570, 141, 16))
        self.iterations_label.setFont(font)
        self.iterations_label.setText(str(rows))

        self.done_button = QtWidgets.QPushButton(self.centralwidget)
        self.done_button.setGeometry(QtCore.QRect(640, 540, 131, 31))
        self.done_button.setFont(font)


        font.setPointSize(20)
        self.method_label = QtWidgets.QLabel(self.centralwidget)
        self.method_label.setGeometry(QtCore.QRect(220, 10, 331, 61))
        self.method_label.setFont(font)
        self.method_label.setAlignment(QtCore.Qt.AlignCenter)
        self.method_label.setText(method)

        self.data = data
        self.tableWidget.setRowCount(rows)
        self.tableWidget.setColumnCount(columns)
        self.setDataItems(data)
        outputWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(outputWindow)
        QtCore.QMetaObject.connectSlotsByName(outputWindow)

    def retranslateUi(self, outputWindow):
        _translate = QtCore.QCoreApplication.translate
        outputWindow.setWindowTitle(_translate("outputWindow", "Output"))
        self.label.setText(_translate("outputWindow", "Root ="))
        self.label_2.setText(_translate("outputWindow", "Precision ="))
        self.label_3.setText(_translate("outputWindow", "Execution Time ="))
        self.label_4.setText(_translate("outputWindow", "Number of Iterations = "))
        self.done_button.setText(_translate("outputWindow", "Done"))
        self.label_10.setText(_translate("outputWindow", "Function = "))


    def setDataItems(self, data):
        headers = []
        for n, key in enumerate(self.data.keys()):
            headers.append(key)
            for m, value in enumerate(self.data[key]):
                newitem = QTableWidgetItem(str(value))
                self.tableWidget.setItem(m, n, newitem)
        self.tableWidget.setHorizontalHeaderLabels(headers)
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.resizeRowsToContents()




