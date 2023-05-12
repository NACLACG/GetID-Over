import sys
from PyQt6 import QtGui, QtWidgets
from OWO import Ui_GetID

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_GetID()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
