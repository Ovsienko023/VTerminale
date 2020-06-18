# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\login_in.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(350, 300)
        Form.setMinimumSize(QtCore.QSize(350, 300))
        Form.setMaximumSize(QtCore.QSize(350, 300))
        Form.setSizeIncrement(QtCore.QSize(400, 300))
        Form.setBaseSize(QtCore.QSize(400, 300))
        self.LoginLineEdit = QtWidgets.QLineEdit(Form)
        self.LoginLineEdit.setGeometry(QtCore.QRect(100, 80, 171, 20))
        self.LoginLineEdit.setObjectName("LoginLineEdit")
        self.passwordLineEdit = QtWidgets.QLineEdit(Form)
        self.passwordLineEdit.setGeometry(QtCore.QRect(100, 120, 171, 20))
        self.passwordLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordLineEdit.setObjectName("passwordLineEdit")
        self.LoginInPushButton = QtWidgets.QPushButton(Form)
        self.LoginInPushButton.setGeometry(QtCore.QRect(150, 150, 75, 23))
        self.LoginInPushButton.setObjectName("LoginInPushButton")
        self.RegistrCommandLinkButton = QtWidgets.QCommandLinkButton(Form)
        self.RegistrCommandLinkButton.setGeometry(QtCore.QRect(80, 250, 231, 41))
        self.RegistrCommandLinkButton.setObjectName("RegistrCommandLinkButton")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(60, 80, 31, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(40, 120, 51, 16))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Login IN"))
        self.LoginInPushButton.setText(_translate("Form", "login in"))
        self.RegistrCommandLinkButton.setText(_translate("Form", "Forgot your password?"))
        self.label.setText(_translate("Form", "Login:"))
        self.label_2.setText(_translate("Form", "Password:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
