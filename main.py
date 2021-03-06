from PyQt5 import QtWidgets
import gui
import functions
import pandas as pd
import sympy

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    myWindow = QtWidgets.QMainWindow()
    ui = gui.Ui_myWindow()
    ui.setupUi(myWindow)
    myWindow.show()
    sys.exit(app.exec_())
