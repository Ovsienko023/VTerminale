import sys  # sys нужен для передачи argv в QApplication
from PyQt5 import QtWidgets
import login_in


class Login(QtWidgets.QMainWindow, login_in.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.LoginInPushButton.clicked.connect(self.log_in)
        
    def log_in(self):
        print('Button Login in')
        login = self.LoginLineEdit.text()
        password = self.passwordLineEdit.text()
        print(login, password)
        self.close()
        




def main_widget():
    app = QtWidgets.QApplication(sys.argv)
    window = Login()
    window.show()
    app.exec_()



main_widget()
