# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\chat_v1.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(545, 332)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.Tab_1 = QtWidgets.QWidget()
        self.Tab_1.setObjectName("Tab_1")
        self.pushButton = QtWidgets.QPushButton(self.Tab_1)
        self.pushButton.setGeometry(QtCore.QRect(10, 190, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.writeMessage = QtWidgets.QTextEdit(self.Tab_1)
        self.writeMessage.setGeometry(QtCore.QRect(10, 110, 461, 71))
        self.writeMessage.setObjectName("writeMessage")
        self.label = QtWidgets.QLabel(self.Tab_1)
        self.label.setGeometry(QtCore.QRect(10, 90, 91, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.Tab_1)
        self.label_2.setGeometry(QtCore.QRect(10, 20, 91, 16))
        self.label_2.setObjectName("label_2")
        self.comboBox = QtWidgets.QComboBox(self.Tab_1)
        self.comboBox.setGeometry(QtCore.QRect(10, 40, 221, 31))
        self.comboBox.setAcceptDrops(False)
        self.comboBox.setObjectName("comboBox")
        self.tabWidget.addTab(self.Tab_1, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.viewMessage = QtWidgets.QTextBrowser(self.tab_2)
        self.viewMessage.setGeometry(QtCore.QRect(10, 10, 271, 231))
        self.viewMessage.setObjectName("viewMessage")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_2.setGeometry(QtCore.QRect(350, 90, 91, 71))
        self.pushButton_2.setObjectName("pushButton_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.pushButton_3 = QtWidgets.QPushButton(self.tab)
        self.pushButton_3.setGeometry(QtCore.QRect(30, 90, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.textBrowser = QtWidgets.QTextBrowser(self.tab)
        self.textBrowser.setGeometry(QtCore.QRect(30, 180, 441, 31))
        self.textBrowser.setObjectName("textBrowser")
        self.lineEdit = QtWidgets.QLineEdit(self.tab)
        self.lineEdit.setGeometry(QtCore.QRect(30, 50, 141, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(30, 30, 61, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(30, 160, 47, 13))
        self.label_4.setObjectName("label_4")
        self.line = QtWidgets.QFrame(self.tab)
        self.line.setGeometry(QtCore.QRect(0, 119, 521, 41))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.pushButton_4 = QtWidgets.QPushButton(self.tab)
        self.pushButton_4.setGeometry(QtCore.QRect(30, 230, 75, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.tabWidget.addTab(self.tab, "")
        self.verticalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "VTerminale"))
        self.pushButton.setText(_translate("MainWindow", "Send"))
        self.label.setText(_translate("MainWindow", "Enter Message:"))
        self.label_2.setText(_translate("MainWindow", "Whom:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Tab_1), _translate("MainWindow", "Send message"))
        self.pushButton_2.setText(_translate("MainWindow", "Check Message"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Check message"))
        self.pushButton_3.setText(_translate("MainWindow", "Find"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "Enter login:"))
        self.label_4.setText(_translate("MainWindow", "Status:"))
        self.pushButton_4.setText(_translate("MainWindow", "Add friend"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Find friends"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
