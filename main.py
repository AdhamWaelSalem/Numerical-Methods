from PyQt5 import QtCore, QtGui, QtWidgets
import gui
import functions

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    myWindow = QtWidgets.QMainWindow()
    ui = gui.Ui_func_input()
    ui.setupUi(myWindow)
    myWindow.show()
    x = 60
    print(functions.calc('cos(x)', 60))
    sys.exit(app.exec_())
