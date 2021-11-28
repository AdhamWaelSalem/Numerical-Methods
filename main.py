from PyQt5 import QtCore, QtGui, QtWidgets
import gui
import functions
import pandas as pd

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    myWindow = QtWidgets.QMainWindow()
    ui = gui.Ui_func_input()
    ui.setupUi(myWindow)
    myWindow.show()
    x = 60
    f = 'x^4-2*x^3-4*x^2-4*x+4'
    f = f.replace('^', '**')
    xl_list = []
    f_xl_list = []
    xu_list = []
    f_xu_list = []
    xr_list = []
    f_xr_list = []

    functions.bisection(f, 2, 0, 20, xl_list, xu_list, f_xl_list, f_xu_list, xr_list, f_xr_list, 0.01)

    data = {}
    df = pd.DataFrame(data)

    df['Xu'] = xu_list
    df['Xl'] = xl_list
    df['f(Xu)'] = f_xu_list
    df['f(Xl)'] = f_xl_list
    df['f(root)'] = f_xr_list
    df['roots'] = xr_list

    print(df)

    #xi_list = []
    #xinew_list = []
    #functions.newton_raphson(f, -20, 20, 0.001, xi_list, xinew_list)

    sys.exit(app.exec_())
