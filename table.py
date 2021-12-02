from functools import partial

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
import functions


# Function to check for the occurrence of an error
def checkError(message):
    if message == '':
        return 0
    return 1


# Function to plot the Graph of the Function
def clicked(function, root):
    function = function.replace('^', '**')
    functions.graph(function, root[-1])


class Ui_outputWindow(object):
    # Setting up the Components of the Window and their Geometrical Dimensions
    def setupUi(self, outputWindow, data, rows, columns, time, function, root, precision, method, message):
        outputWindow.resize(800, 600)

        self.centralwidget = QtWidgets.QWidget(outputWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Setting the Table Widget
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(0, 100, 801, 331))
        self.tableWidget.setObjectName("tableWidget")

        # Setting Fonts Family and font size
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(10)
        font2 = QtGui.QFont()
        font2.setPointSize(9)
        font2.setBold(True)

        # Setting Labels
        self.func_label = QtWidgets.QLabel(self.centralwidget)
        self.func_label.setGeometry(QtCore.QRect(10, 450, 341, 20))
        self.func_label.setFont(font)
        self.func_label.setText("Function= "+function)

        self.root_label = QtWidgets.QLabel(self.centralwidget)
        self.root_label.setGeometry(QtCore.QRect(10, 480, 341, 20))
        self.root_label.setFont(font)

        self.precision_label = QtWidgets.QLabel(self.centralwidget)
        self.precision_label.setGeometry(QtCore.QRect(10, 510, 341, 20))
        self.precision_label.setFont(font)

        self.time_lable = QtWidgets.QLabel(self.centralwidget)
        self.time_lable.setGeometry(QtCore.QRect(10, 540, 341, 20))
        self.time_lable.setFont(font)

        self.iterations_label = QtWidgets.QLabel(self.centralwidget)
        self.iterations_label.setGeometry(QtCore.QRect(10, 570, 341, 20))
        self.iterations_label.setFont(font)

        font.setPointSize(20)
        self.method_label = QtWidgets.QLabel(self.centralwidget)
        self.method_label.setGeometry(QtCore.QRect(220, 10, 331, 61))
        self.method_label.setFont(font)
        self.method_label.setAlignment(QtCore.Qt.AlignCenter)
        self.method_label.setText(method)

        #Setting Push Button
        self.graph = QtWidgets.QPushButton(self.centralwidget)
        self.graph.setGeometry(QtCore.QRect(374, 560, 91, 31))

        # Error Message Information
        self.error_msg = QtWidgets.QLabel(self.centralwidget)
        self.error_msg.setGeometry(QtCore.QRect(486, 442, 291, 141))
        self.error_msg.setFont(font2)
        self.error_msg.setAlignment(QtCore.Qt.AlignCenter)

        self.message = message

        # Checking if there is an error message
        # if the error message is empty then the function executes successfully and the data is showed
        # if the error message not empty then the function diverges --> show the error message
        if checkError(message) == 0:
            self.data = data
            self.tableWidget.setRowCount(rows)
            self.tableWidget.setColumnCount(columns)
            self.setDataItems(data)
            self.iterations_label.setText("Number of Iterations = "+str(rows))
            self.time_lable.setText("Execution Time = "+str(time))
            self.precision_label.setText("Precision = "+str(precision[-1]))
            self.root_label.setText("Root = "+str(root[-1]))
        else:
            self.error_msg.setText(message)
            self.graph.setEnabled(False)

        self.graph.clicked.connect(partial(clicked, function, root))
        outputWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(outputWindow, message)
        QtCore.QMetaObject.connectSlotsByName(outputWindow)

    # Setting the starting values of the GUI Window
    def retranslateUi(self, outputWindow, message):
        _translate = QtCore.QCoreApplication.translate
        outputWindow.setWindowTitle(_translate("outputWindow", "Output"))
        self.graph.setText(_translate("MainWindow", "Graph"))

    # Function to Set the data into the output table
    def setDataItems(self, data):
        # headers list used to store the headers of the Table
        headers = []

        # first loop to iterate over the keys and the second loop to iterate over the values
        # Insert each element into its place in the table using dimensions n and m
        for n, key in enumerate(self.data.keys()):
            headers.append(key)
            for m, value in enumerate(self.data[key]):
                newitem = QTableWidgetItem(str(value))
                self.tableWidget.setItem(m, n, newitem)

        # Set the headers into the table
        self.tableWidget.setHorizontalHeaderLabels(headers)

        # Disable Edit Triggers to prevent the user from editing the output
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

        # Adjust Size Policy of both rows and columns to adjust to content
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.resizeRowsToContents()




