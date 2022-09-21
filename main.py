# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import ctypes
from os import walk

filenames = next(walk("images"), (None, None, []))[2] 
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.i = 0
        self.i_last = len(filenames)-1
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.background = QtWidgets.QLabel(self.centralwidget)
        self.background.setGeometry(QtCore.QRect(0, 0, 800, 600))
        self.background.setText("")
        self.background.setPixmap(QtGui.QPixmap("images/"+filenames[self.i]))
        self.background.setScaledContents(True)
        self.background.setObjectName("background")
        self.next_button = QtWidgets.QPushButton(self.centralwidget)
        self.next_button.setGeometry(QtCore.QRect(680, 100, 75, 400))
        font = QtGui.QFont()
        font.setPointSize(41)
        self.next_button.setFont(font)
        self.next_button.setStyleSheet("background-color: rgba(0, 0, 0,0);\n"
"color: rgb(255, 255, 255);")
        self.next_button.setIconSize(QtCore.QSize(50, 500))
        self.next_button.setObjectName("next_button")
        self.next_button.clicked.connect(self.next_image)
        
        self.back_button = QtWidgets.QPushButton(self.centralwidget)
        self.back_button.setGeometry(QtCore.QRect(60, 100, 75, 400))
        font = QtGui.QFont()
        font.setPointSize(41)
        self.back_button.setFont(font)
        self.back_button.setStyleSheet("background-color: rgba(0, 0, 0,0);\n"
"color: rgb(255, 255, 255);")
        self.back_button.setIconSize(QtCore.QSize(50, 500))
        self.back_button.setObjectName("back_button")
        self.back_button.clicked.connect(self.back_image)
        if self.i ==0:
                self.back_button.hide()
        self.set_background_button = QtWidgets.QPushButton(self.centralwidget)
        self.set_background_button.setGeometry(QtCore.QRect(300, 470, 201, 61))
        self.set_background_button.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:15px;")
        self.set_background_button.setObjectName("set_background_button")
        self.set_background_button.clicked.connect(self.set_as_background)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def next_image(self):
        print('next')
        self.i = self.i+1
        self.background.setPixmap(QtGui.QPixmap("images/"+filenames[self.i]))
        self.back_button.show()
        if self.i == self.i_last:
                print(self.i_last)
                self.next_button.hide()
    def back_image(self):
        print("back")
        print(self.i)
        if self.i==1:
                self.back_button.hide()
        self.i = self.i-1
        self.background.setPixmap(QtGui.QPixmap("images/"+filenames[self.i]))
        if self.i < self.i_last:
                print(self.i_last)
                self.next_button.show()
    def set_as_background(self):
        print(filenames[self.i])
        path_integrate = r'C:\Users\dogea\OneDrive\Documents\python projects\10hours\background_1.1\images'
        ctypes.windll.user32.SystemParametersInfoW(20,0,path_integrate+"/"+filenames[self.i],0)
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.next_button.setText(_translate("MainWindow", ">"))
        self.back_button.setText(_translate("MainWindow", "<"))
       
        self.set_background_button.setText(_translate("MainWindow", "SET AS BACKGROUND"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
