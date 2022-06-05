import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QDialog, QApplication, QFileDialog
from PyQt5.uic import loadUi



class ApplicationWindow(QMainWindow):
    def __init__(self):
        super(ApplicationWindow, self).__init__()
        loadUi("MainWindow.ui", self)

        self.LoadPlaintextButton.clicked.connect(self.loadplaintext)
        self.LoadCiphertextButton.clicked.connect(self.loadciphertext)

        self.SavePlaintextButton.clicked.connect(self.saveplaintext)
        self.SaveCiphertextButton.clicked.connect(self.saveciphertext)

        self.DecryptButton.clicked.connect(self.decryptfunction)
        self.EncryptButton.clicked.connect(self.encryptfunction)

    def loadplaintext(self):
        fname = QFileDialog.getOpenFileName(self, 'Choose Plain Text', directory='', filter='Text files (*.txt)')
        
    
    def loadciphertext(self):
        pass
    
    def saveplaintext(self):
        pass

    def saveciphertext(self):
        pass

    def encryptfunction(self):
        pass
    
    def decryptfunction(self):
        pass



app = QApplication(sys.argv)
mainwindow = ApplicationWindow()

widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)

widget.setFixedWidth(1200)
widget.setFixedHeight(800)

widget.show()

app.exec_()