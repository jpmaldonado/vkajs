from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QApplication

class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__() # Pulling all default properties/methods from the base class
        uic.loadUi("app.ui", self) # Loading our layout into the constructor of MyWindow

if __name__ == '__main__':
    app = QtWidgets.QApplication([])            
    mainWindow = MyWindow()
    mainWindow.show()
    app.exec_()