from PyQt5 import QtCore, QtGui, QtWidgets

import draft
import functions
import table
import time


# Function to Check whether the input is a number or not
def is_number(string):
    try:
        float(string)
        return True
    except ValueError:
        return False


# Function to validate the input function string
def validateSyntax(expression):
    try:
        functions.calc(expression, 2.14)
    except (SyntaxError, NameError, ZeroDivisionError):
        return False
    else:
        return True


class Ui_myWindow(object):
    # Setting up the Components of the Window and their Geometrical Dimensions
    def setupUi(self, myWindow):
        myWindow.resize(631, 481)
        self.centralwidget = QtWidgets.QWidget(myWindow)

        # Setting Fonts Family and font size
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)

        font2 = QtGui.QFont()
        font2.setPointSize(7)

        # Setting the Input (line edits)
        self.func_input = QtWidgets.QLineEdit(self.centralwidget)
        self.func_input.setGeometry(QtCore.QRect(10, 60, 281, 20))

        self.tolerance_input = QtWidgets.QLineEdit(self.centralwidget)
        self.tolerance_input.setGeometry(QtCore.QRect(440, 410, 113, 20))

        self.iterations_input = QtWidgets.QLineEdit(self.centralwidget)
        self.iterations_input.setGeometry(QtCore.QRect(70, 410, 113, 20))

        self.fileName_input = QtWidgets.QLineEdit(self.centralwidget)
        self.fileName_input.setGeometry(QtCore.QRect(340, 59, 271, 21))

        self.range_input1 = QtWidgets.QLineEdit(self.centralwidget)
        self.range_input1.setGeometry(QtCore.QRect(230, 220, 113, 20))

        self.range_input2 = QtWidgets.QLineEdit(self.centralwidget)
        self.range_input2.setGeometry(QtCore.QRect(470, 220, 113, 20))

        # Setting Labels
        self.label3 = QtWidgets.QLabel(self.centralwidget)
        self.label3.setGeometry(QtCore.QRect(400, 379, 191, 21))
        self.label3.setAlignment(QtCore.Qt.AlignCenter)
        self.label3.setFont(font)

        self.label2 = QtWidgets.QLabel(self.centralwidget)
        self.label2.setGeometry(QtCore.QRect(0, 380, 271, 21))
        self.label2.setAlignment(QtCore.Qt.AlignCenter)
        self.label2.setFont(font)

        self.method_name_label = QtWidgets.QLabel(self.centralwidget)
        self.method_name_label.setGeometry(QtCore.QRect(300, 160, 211, 21))
        self.method_name_label.setFont(font)
        self.method_name_label.setAlignment(QtCore.Qt.AlignCenter)  # to set the alignment of the label to be centered

        self.range_label1 = QtWidgets.QLabel(self.centralwidget)
        self.range_label1.setGeometry(QtCore.QRect(220, 200, 131, 20))
        self.range_label1.setFont(font)
        self.range_label1.setAlignment(QtCore.Qt.AlignCenter)  # to set the alignment of the label to be centered

        self.range_label2 = QtWidgets.QLabel(self.centralwidget)
        self.range_label2.setGeometry(QtCore.QRect(470, 200, 111, 20))
        self.range_label2.setFont(font)
        self.range_label2.setAlignment(QtCore.Qt.AlignCenter)  # to set the alignment of the label to be centered

        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(60, 430, 131, 21))
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setFont(font2)

        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(410, 430, 181, 20))
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setFont(font2)

        # Setting Combo Box
        self.method_options = QtWidgets.QComboBox(self.centralwidget)
        self.method_options.setGeometry(QtCore.QRect(30, 220, 111, 22))
        self.method_options.addItem("")
        self.method_options.addItem("")
        self.method_options.addItem("")
        self.method_options.addItem("")
        self.method_options.addItem("")
        self.method_options.addItem("")

        # Setting Push Button
        self.calculate_button = QtWidgets.QPushButton(self.centralwidget)
        self.calculate_button.setGeometry(QtCore.QRect(240, 430, 141, 31))

        # Setting Radio Buttons
        self.function_rbutton = QtWidgets.QRadioButton(self.centralwidget)
        self.function_rbutton.setGeometry(QtCore.QRect(60, 20, 171, 21))
        self.function_rbutton.setFont(font)
        self.function_rbutton.setChecked(True)  # Setting this radio button as being checked by default

        self.file_rbutton = QtWidgets.QRadioButton(self.centralwidget)
        self.file_rbutton.setGeometry(QtCore.QRect(390, 20, 201, 20))
        self.file_rbutton.setFont(font)
        self.fileName_input.setEnabled(False)  # Since the other radio button is checked then disable this input

        font2.setPointSize(9)
        font2.setBold(True)

        # Setting Error Messages
        self.func_error_msg = QtWidgets.QLabel(self.centralwidget)
        self.func_error_msg.setGeometry(QtCore.QRect(10, 90, 281, 31))
        self.func_error_msg.setAlignment(QtCore.Qt.AlignCenter)  # to set the alignment of the label to be centered
        self.func_error_msg.setFont(font2)
        self.func_error_msg.setText('')

        self.file_error_msg = QtWidgets.QLabel(self.centralwidget)
        self.file_error_msg.setGeometry(QtCore.QRect(340, 90, 271, 31))
        self.file_error_msg.setAlignment(QtCore.Qt.AlignCenter)  # to set the alignment of the label to be centered
        self.file_error_msg.setFont(font2)
        self.file_error_msg.setText('')

        self.range1_error_msg = QtWidgets.QLabel(self.centralwidget)
        self.range1_error_msg.setGeometry(QtCore.QRect(170, 250, 231, 31))
        self.range1_error_msg.setAlignment(QtCore.Qt.AlignCenter)  # to set the alignment of the label to be centered
        self.range1_error_msg.setFont(font2)
        self.range1_error_msg.setText('')

        self.range2_error_msg = QtWidgets.QLabel(self.centralwidget)
        self.range2_error_msg.setGeometry(QtCore.QRect(416, 250, 211, 31))
        self.range2_error_msg.setAlignment(QtCore.Qt.AlignCenter)  # to set the alignment of the label to be centered
        self.range2_error_msg.setFont(font2)
        self.range2_error_msg.setText('')

        myWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(myWindow)
        QtCore.QMetaObject.connectSlotsByName(myWindow)

    # Setting the starting values of the GUI Window
    def retranslateUi(self, myWindow):
        _translate = QtCore.QCoreApplication.translate
        myWindow.setWindowTitle(_translate("myWindow", "MainWindow"))

        # Setting Combo box Options
        self.method_options.setItemText(0, _translate("myWindow", "Bisection"))
        self.method_options.setItemText(1, _translate("myWindow", "False-Position"))
        self.method_options.setItemText(2, _translate("myWindow", "Newton-Raphson"))
        self.method_options.setItemText(3, _translate("myWindow", "Secant"))
        self.method_options.setItemText(4, _translate("myWindow", "Fixed Point"))
        self.method_options.setItemText(5, _translate("myWindow", "Modified Secant"))

        # Setting labels,radio buttons and push buttons starting text
        self.calculate_button.setText(_translate("myWindow", "Calculate"))
        self.method_name_label.setText(_translate("myWindow", "Bisection Method"))
        self.range_label1.setText(_translate("myWindow", "Xu"))
        self.range_label2.setText(_translate("myWindow", "Xl"))

        self.function_rbutton.setText(_translate("myWindow", "Function"))
        self.file_rbutton.setText(_translate("myWindow", "File Name"))

        self.iterations_input.setText("50")
        self.tolerance_input.setText("0.00001")

        self.label3.setText(_translate("myWindow", "Tolerance"))
        self.label2.setText(_translate("myWindow", "Maximum Number of Iterations"))
        self.label_5.setText(_translate("myWindow", "default = 50"))
        self.label_6.setText(_translate("myWindow", "default = 0.00001"))

        # Connect the combo box to function activated() when value is changed
        self.method_options.activated.connect(self.activated)

        # Connect radio button to function checked() when toggled
        self.file_rbutton.toggled.connect(self.checked)

        # Connect push button to function clicked() when clicked
        self.calculate_button.clicked.connect(self.clicked)

    # Function Activated when the radio button value is changed/switched
    def checked(self):
        # If function as input is selected then disable the other input
        if self.file_rbutton.isChecked():
            self.func_input.setEnabled(False)
            self.func_input.setText("")
            self.fileName_input.setEnabled(True)
            self.func_error_msg.setText("")
        else:
            self.func_input.setEnabled(True)
            self.fileName_input.setText("")
            self.fileName_input.setEnabled(False)
            self.file_error_msg.setText("")

    # function Activated when the Combo Box Choice is changed
    def activated(self):
        index = self.method_options.currentIndex()

        # Clear all the input and error messages labels
        self.range_input1.setText('')
        self.range_input2.setText('')
        self.range1_error_msg.setText('')
        self.range2_error_msg.setText('')

        # Set the Labels Title According to the method used
        # if the method requires only 1 input then the second input is disabled
        if index == 0:
            self.range_input2.setEnabled(True)
            self.method_name_label.setText("Bisection Method")
            self.range_label1.setText('Xu')
            self.range_label2.setText('Xl')
        elif index == 1:
            self.range_input2.setEnabled(True)
            self.method_name_label.setText("False Position Method")
            self.range_label1.setText('Xu')
            self.range_label2.setText('Xl')
        elif index == 2:
            self.method_name_label.setText("Newton Raphson Method")
            self.range_label2.setText('')
            self.range_label1.setText('Initial Guess')
            self.range_input2.setEnabled(False)
        elif index == 3:
            self.range_input2.setEnabled(True)
            self.method_name_label.setText("Secant Method")
            self.range_label1.setText('Xi-1')
            self.range_label2.setText('Xi')
        elif index == 4:
            self.range_input2.setEnabled(False)
            self.method_name_label.setText("Fixed Point Method")
            self.range_label1.setText('Starting Point')
            self.range_label2.setText('')
        else:
            self.range_input2.setEnabled(True)
            self.range_input2.setText('0.01')
            self.range_label1.setText("Xi")
            self.range_label2.setText("Delta")
            self.method_name_label.setText("Modified Secant Method")

    # Function activated when the "Calculate" Button is clicked
    def clicked(self):
        index = self.method_options.currentIndex()

        # Clear all error messages
        self.func_error_msg.setText('')
        self.file_error_msg.setText('')
        self.range1_error_msg.setText('')
        self.range2_error_msg.setText('')

        # if function as input is selected and the input is empty display error message
        if self.func_input.text().strip() == '' and self.func_input.isEnabled():
            self.func_error_msg.setText('Please Insert a Function!')
            return

        # if file as input is selected and the input is empty display error message
        if self.fileName_input.text().strip() == '' and self.fileName_input.isEnabled():
            self.file_error_msg.setText('Please Insert File Name!')
            return

        # if the first required input is empty display error message
        if self.range_input1.text().strip() == '':
            self.range1_error_msg.setText('This Field Can\'t be Empty')
            return

        # if the first input is not a number display error message
        if not is_number(self.range_input1.text()):
            self.range1_error_msg.setText('Enter a Number!')
            return

        # if the second required input is empty display error message
        if (index != 2 and index != 4 and index != 5) and self.range_input2.text().strip() == '':
            self.range2_error_msg.setText('This Field Can\'t be Empty')
            return

        # if the second input is not a number display error message
        if (index != 2 and index != 4 and index != 5) and not is_number(self.range_input2.text()):
            self.range2_error_msg.setText('Enter a Number')
            return

        # if iterations input is empty select the default value (50), else store the input
        if self.iterations_input.text().strip() == "":
            maxIterations = 50
        else:
            maxIterations = self.iterations_input.text()

        # if tolerance input is empty select the default value (0.00001), else store the input
        if self.tolerance_input.text().strip() == "":
            tolerance = 0.00001
        else:
            tolerance = self.tolerance_input.text()

        # Check which radio button is checked
        # if function as input is checked get the input
        # if file as input is checked then open file and read the function from the file
        if self.function_rbutton.isChecked():
            function = self.func_input.text()
        else:
            file_name = self.fileName_input.text() + ".txt"
            with open(file_name, 'r') as f:
                function = f.read()
                f.close()

        function_temp = function
        function = function.replace('^', '**')

        # check if the function is valid or not
        if self.function_rbutton.isChecked() and not validateSyntax(function):
            self.func_error_msg.setText("Please Enter a Valid Function!")
            return

        # depending on the index chosen from the Combo Box the method is selected
        # Number of columns used in the output table is defined depending on the method
        # Get inputs required for the calculation of the root for the method
        # Call the method to get the root
        # Calculate Execution time of the selected method
        if index == 0:
            method = "Bisection"
            columns = 7
            xu = self.range_input1.text()
            xl = self.range_input2.text()
            startTime = time.time()
            data, rows, root, precision, message = functions.bisection(function, float(xu), float(xl), int(maxIterations),
                                                              float(tolerance))
            runTime = time.time() - startTime
        elif index == 1:
            method = "False Position"
            columns = 7
            xu = self.range_input1.text()
            xl = self.range_input2.text()
            startTime = time.time()
            data, rows, root, precision, message = draft.falsePosition(function, float(xl), float(xu), float(tolerance),
                                                              int(maxIterations))
            runTime = time.time() - startTime
        elif index == 2:
            method = "Newton Raphson"
            columns = 3
            xi = self.range_input1.text()
            startTime = time.time()
            data, rows, root, precision, message = functions.newton_raphson(function, float(xi), int(maxIterations),
                                                                   float(tolerance))
            runTime = time.time() - startTime
        elif index == 3:
            method = "Secant"
            columns = 6
            x = self.range_input1.text()
            xi = self.range_input2.text()
            startTime = time.time()
            data, rows, root, precision, message = draft.Secant(function, float(x), float(xi), float(tolerance),
                                                       int(maxIterations))
            runTime = time.time() - startTime
        elif index == 4:
            method = "Fixed Point"
            columns = 3
            x = self.range_input1.text()
            startTime = time.time()
            data, rows, root, precision, message = draft.fixedPoint(function, float(x), float(tolerance), int(maxIterations))
            runTime = time.time() - startTime
        else:
            method = "Modified Secant"
            columns = 4
            if self.range_input2.text().strip() == "":
                delta = 0.01
            else:
                delta = self.range_input2.text()
            x = self.range_input1.text()
            startTime = time.time()
            data, rows, root, precision, message = draft.ModefiedSecant(function, float(x), float(delta), float(tolerance),
                                                               int(maxIterations))
            runTime = time.time() - startTime

        # Passing the data to the output window to display the output
        self.outputWindow = QtWidgets.QMainWindow()
        self.ui2 = table.Ui_outputWindow()
        self.ui2.setupUi(self.outputWindow, data, rows, columns, runTime, function_temp, root, precision, method, message)
        self.outputWindow.show()
