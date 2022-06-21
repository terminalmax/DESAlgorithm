
import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QDialog, QApplication, QFileDialog, QMessageBox
from PyQt5.uic import loadUi

import DES

class ApplicationWindow(QMainWindow):
    
    def __init__(self):
        super(ApplicationWindow, self).__init__()
        loadUi("MainWindow.ui", self)

        self.running = 0
        self.plaintext = ""
        self.ciphertext = ""
        self.keytext = ""

        #Connecting buttons to functions
        self.LoadPlaintextButton.clicked.connect(self.loadplaintext)
        self.LoadCiphertextButton.clicked.connect(self.loadciphertext)

        self.SavePlaintextButton.clicked.connect(self.saveplaintext)
        self.SaveCiphertextButton.clicked.connect(self.saveciphertext)

        self.DecryptButton.clicked.connect(self.decryptfunction)
        self.EncryptButton.clicked.connect(self.encryptfunction)

        self.ClearPlaintextButton.clicked.connect(self.clearPlaintextInput)
        self.ClearCiphertextButton.clicked.connect(self.clearCiphertextInput)

        #Placeholder Text
        self.KeyInput.setPlaceholderText("AAAAAAAAAAAAAA")
        self.KeyInput.setMaxLength(14)
        

    #Abstracting error dialog
    def showErrorDialog(self, title : str, content : str):
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

        fname = QFileDialog.getOpenFileName(self, caption='Choose Plain Text', directory='', filter='Text files (*.txt)')
        
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
    
    def loadkey(self):
        pass
    
    def clearPlaintextInput(self):
        self.PlaintextInput.clear()
    def clearCiphertextInput(self):
        self.CiphertextInput.clear()

    #Saving functions
    def saveplaintext(self):

        self.plaintext = self.PlaintextInput.toPlainText()

        if self.plaintext == '' or self.plaintext is None:
            self.showErrorDialog('Plain Text Error', 'Plaintext is empty')
            return

        fname = QFileDialog.getSaveFileName(self,caption="Save File",directory='./',filter='Text File (*.txt)')
        print(fname)
        if fname[0] == '':
            return

        try:
            with open(fname[0], 'w') as fp:
                fp.write(self.plaintext)
        except:
            print("File write error")
            return

    def saveciphertext(self):
        self.ciphertext = self.CiphertextInput.toPlainText()

        if self.ciphertext == '' or self.plaintext is None:
            self.showErrorDialog('Cipher Text Error', 'Ciphertext is Empty')
            return
        
        fname = QFileDialog.getSaveFileName(self,caption="Save File",directory='./',filter='Text File (*.txt)')
        print(fname)
        if fname[0] == '':
            return
        
        try:
            with open(fname[0], 'w') as fp:
                fp.write(self.ciphertext)
        except:
            print("File write error")
            return
    
    #Checking Conditions
    
    # Checks all conditions for encryption - True is Valid, False if Invalid
    def checkEncryptionConditions(self):
        try:
            DES.checkKey(self.keytext)
        except DES.InvalidDESKeyLengthException as e:
            self.showErrorDialog('Key Error', 'Invalid Key Length')
            return False
        except DES.InvalidDESKeyException as e:
            self.showErrorDialog('Key Error', 'Invalid Key Character')
            return False

        if self.plaintext == '' or self.plaintext is None:
            self.showErrorDialog('Plain Text Error', 'Empty Plain Text')
            return False

        return True

    #Checks all conditions for decryption
    def checkDecryptionConditions(self):
        try:
            DES.checkKey(self.keytext)
        except DES.InvalidDESKeyLengthException as e:
            self.showErrorDialog('Key Error', 'Invalid Key Length')
            return False
        except DES.InvalidDESKeyException as e:
            self.showErrorDialog('Key Error', 'Invalid Key Character')
            return False

        if self.ciphertext == '' or self.ciphertext is None:
            self.showErrorDialog('Cipher Text Error', 'Empty Cipher Text')
            return False

        return True

    def encryptfunction(self):
        if self.running == 1:
            print("Already Running! Returning")
            return
        self.running = 1
        print("Running Encryption...")


        # Fetch Plaintext and Key
        self.plaintext = self.PlaintextInput.toPlainText()
        print(f'Plaintext set to : {self.plaintext}')
        self.keytext = self.KeyInput.text()
        print(f'Keytext is set to: {self.keytext}')

        # Check all conditions for encryption
        if not self.checkEncryptionConditions():
            print("Do not meet conditions.")
            self.running = 0
            return

        # Encrypt
        self.ciphertext = DES.encryption(self.plaintext, self.keytext)
        
        print("Setting new ciphertext")
        self.CiphertextInput.setPlainText(self.ciphertext)

        self.running = 0
        print("Encryption Done...")
    
    def decryptfunction(self):
        if self.running == 1:
            print("Already Running! Returning")
            return

        self.running = 1
        print("Running Decryption...")

        # Fetch Ciphertext and Key
        self.ciphertext = self.CiphertextInput.toPlainText()
        print(f'Ciphertext set to : {self.ciphertext}')
        self.keytext = self.KeyInput.text()
        print(f'Keytext is set to: {self.keytext}')

        # Check all conditions for decryption
        if not self.checkDecryptionConditions():
            print("Do not meet conditions.")
            self.running = 0
            return

        # Decrypt
        self.plaintext = DES.decryption(self.ciphertext, self.keytext)

        print("Set new plaintext")
        self.PlaintextInput.setPlainText(self.plaintext)

        self.running = 0
        print("Decryption Done...")


app = QApplication(sys.argv)
mainwindow = ApplicationWindow()

widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)

widget.setFixedWidth(800)
widget.setFixedHeight(700)

widget.show()

app.exec_()