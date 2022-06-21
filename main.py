from re import L
import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QDialog, QApplication, QFileDialog, QMessageBox
from PyQt5.uic import loadUi


class ApplicationWindow(QMainWindow):
    
    def __init__(self):
        super(ApplicationWindow, self).__init__()
        loadUi("MainWindow.ui", self)

        self.running = 0
        self.plaintext = ""
        self.ciphertext = ""

        #Connecting buttons to functions
        self.LoadPlaintextButton.clicked.connect(self.loadplaintext)
        self.LoadCiphertextButton.clicked.connect(self.loadciphertext)

        self.SavePlaintextButton.clicked.connect(self.saveplaintext)
        self.SaveCiphertextButton.clicked.connect(self.saveciphertext)

        self.DecryptButton.clicked.connect(self.decryptfunction)
        self.EncryptButton.clicked.connect(self.encryptfunction)

        self.KeyInput.setPlaceholderText("AAAAAAAAAAAAAA")

    #Abstracting error dialog
    def showErrorDialog(self, title, content):
        dlg = QMessageBox(self)
        dlg.setWindowTitle(title)
        dlg.setText(content)

        dlg.exec()

    #Loading functions
    def loadplaintext(self):
        
        fname = QFileDialog.getOpenFileName(self, 'Choose Plain Text', directory='', filter='Text files (*.txt)')
        
        if fname[0] == '':
            return

        try:
            with open(fname[0], 'r') as fp:
                self.plaintext = fp.read()
        except FileNotFoundError:
            self.showErrorDialog("File Error", "File not found or invalid path!")
            print("File not found error!")
            return
        except:
            self.showErrorDialog("File Error", "Unexpected File error has occured!")
            print("Error: Could not load file")
            return

        #Setting plain text in text box
        print(self.plaintext)
        self.PlaintextInput.setPlainText(self.plaintext)
    
    def loadciphertext(self):

        fname = QFileDialog.getOpenFileName(self, 'Choose Plain Text', directory='', filter='Text files (*.txt)')
        
        if fname[0] == '':
            return

        try:
            with open(fname[0], 'r') as fp:
                self.ciphertext = fp.read()
        except FileNotFoundError:
            self.showErrorDialog("File Error", "File not found or invalid path!")
            print("File not found error!")
            return
        except:
            self.showErrorDialog("File Error", "Unexpected File error has occured!")
            print("Error: Could not load file")
            return
            
        print(self.ciphertext)
        self.CiphertextInput.setPlainText(self.ciphertext)
    
    #Saving functions
    def saveplaintext(self):
        pass

    def saveciphertext(self):
        pass
    
    def encryptfunction(self):
        if self.running == 1:
            return
        
        self.running = 1

        

        self.running = 0
    
    def decryptfunction(self):
        self.running = 1
        self.running = 0




app = QApplication(sys.argv)
mainwindow = ApplicationWindow()

widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)

widget.setFixedWidth(1200)
widget.setFixedHeight(800)

widget.show()

app.exec_()