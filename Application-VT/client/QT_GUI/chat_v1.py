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
        self.verticalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "VTerminale"))
        self.pushButton.setText(_translate("MainWindow", "Send"))
        self.label.setText(_translate("MainWindow", "Enter Message:"))
        self.label_2.setText(_translate("MainWindow", "Whom:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Tab_1), _translate("MainWindow", "Tab 1"))
        self.pushButton_2.setText(_translate("MainWindow", "Check Message"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
