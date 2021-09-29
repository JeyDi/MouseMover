# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(420, 369)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.move_button = QtWidgets.QPushButton(self.centralwidget)
        self.move_button.setGeometry(QtCore.QRect(130, 100, 151, 71))
        self.move_button.setObjectName("move_button")
        self.start_label = QtWidgets.QLabel(self.centralwidget)
        self.start_label.setGeometry(QtCore.QRect(130, 20, 171, 16))
        self.start_label.setObjectName("start_label")
        self.text_display = QtWidgets.QTextBrowser(self.centralwidget)
        self.text_display.setGeometry(QtCore.QRect(120, 190, 171, 111))
        self.text_display.setObjectName("text_display")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.move_button.setText(_translate("MainWindow", "Move!"))
        self.start_label.setText(_translate("MainWindow", "Mouse Movement Program"))

    def pressed(self):
        pass
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
