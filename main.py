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
    f = 'e^x'
    f = f.replace('^', '**')
    xl_list = []
    f_xl_list = []
    xu_list = []
    f_xu_list = []
    xr_list = []
    f_xr_list = []
    print(
        functions.bisection(f, 2, 0,20, xl_list, xu_list, f_xl_list, f_xu_list, xr_list, f_xr_list,0.01))
    print(xr_list)
    sys.exit(app.exec_())
