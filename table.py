from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QAction, QTableWidget, QTableWidgetItem, QVBoxLayout, \
    QHeaderView
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
import sys
import functions

data, rows = functions.bisection('x**4-2*x**3-4*x**2-4*x+4', 2, 0, 20, 0.01)


class TableView(QTableWidget):
    def __init__(self, data, *args):
        QTableWidget.__init__(self, *args)
        self.data = data
        self.setData()
        self.resizeColumnsToContents()
        self.resizeRowsToContents()

    def setData(self):
        horHeaders = []
        for n, key in enumerate(self.data.keys()):
            horHeaders.append(key)
            for m, item in enumerate(self.data[key]):
                newitem = QTableWidgetItem(str(item))
                self.setItem(m, n, newitem)
        self.setHorizontalHeaderLabels(horHeaders)


def main(args):
    app = QApplication(args)
    table = TableView(data, rows, 6)
    table.show()
    print(data)
    sys.exit(app.exec_())


if __name__ == "__main__":
    main(sys.argv)
