from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem


class Ui_outputWindow(object):
    def setupUi(self, outputWindow, data, rows, columns):
        outputWindow.setObjectName("outputWindow")
        outputWindow.resize(800, 600)

        self.centralwidget = QtWidgets.QWidget(outputWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(95, 111, 570, 300))
        self.tableWidget.setObjectName("tableWidget")
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



