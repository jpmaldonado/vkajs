from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QApplication
import pandas as pd
from utils import PandasModel
import logging

logging.basicConfig(filename="debug.log", level=logging.DEBUG, format='%(asctime)s %(message)s')

class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__() # Pulling all default properties/methods from the base class
        uic.loadUi("app.ui", self) # Loading our layout into the constructor of MyWindow


        # Bind signal (user presses a button) with a slot (the code that is executed as a consequence of the action)
        self.loadButton.pressed.connect(self.read_csv)

    def read_csv(self):
        # Here goes the code to read the file...
        file_path = self.fileUpload.path
        df = pd.read_csv(file_path)

        # Create a data model for passing to the TableView widget
        data_model = PandasModel(df)
        self.dataTable.setModel(data_model)



if __name__ == '__main__':
    app = QtWidgets.QApplication([])            
    mainWindow = MyWindow()
    mainWindow.show()
    app.exec_()