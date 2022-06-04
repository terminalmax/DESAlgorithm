from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QDialog, QApplication
from PyQt5.uic import loadUi



class Application(QMainWindow):
    def __init__(self):
        super(Application, self).__init__()
        loadUi("MainWindow.ui", self)


        self.DecryptButton.clicked.connect(self.decryptfunction)
        self.EncryptButton.clicked.connect(self.encryptfunction)

    
    def encryptfunction(self):
        pass
    
    def decryptfunction(self):
        pass
    