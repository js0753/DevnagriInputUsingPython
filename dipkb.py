# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\jaina\Desktop\DevnagriInterface\dipkb.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!



import time

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])
try:
    from PyQt5 import QtCore, QtGui, QtWidgets
    import keyboard
    from pynput.mouse import Button,Controller
except ImportError:
    install('pynput')
    install('pyqt5')
    install('keyboard')
    from pynput.mouse import Button,Controller
    from PyQt5 import QtCore, QtGui, QtWidgets
    import keyboard
    
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint )
        MainWindow.setObjectName("MainWindow")
        #MainWindow.setFocusPolicy(QtCore.Qt.NoFocus)
        
        MainWindow.resize(460, 360)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 170, 101, 41))
        self.pushButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(180, 170, 101, 41))
        self.pushButton_2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_2.setObjectName("pushButton_2") 
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 230, 101, 41))
        self.pushButton_3.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(180, 230, 101, 41))
        self.pushButton_4.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(350, 170, 101, 41))
        self.pushButton_5.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(350, 230, 101, 41))
        self.pushButton_6.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_6.setObjectName("pushButton_6")
        #self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        #self.lineEdit.setGeometry(QtCore.QRect(180, 40, 311, 61))
        #self.lineEdit.setFocusPolicy(QtCore.Qt.NoFocus)
        #self.lineEdit.setObjectName("lineEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        arr=[self.pushButton,self.pushButton_2,self.pushButton_3,self.pushButton_4,self.pushButton_5,self.pushButton_6]
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
                 
        self.pushButton.clicked.connect(lambda: self.on_click(self.pushButton))
        self.pushButton_2.clicked.connect(lambda: self.on_click(self.pushButton_2))
        self.pushButton_3.clicked.connect(lambda: self.on_click(self.pushButton_3))
        self.pushButton_4.clicked.connect(lambda: self.on_click(self.pushButton_4))
        self.pushButton_5.clicked.connect(lambda: self.on_click(self.pushButton_5))
        self.pushButton_6.clicked.connect(lambda: self.on_click(self.pushButton_6))
        
        #for button in arr:
            #button.clicked.connect(lambda: self.on_click(button))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "अ"))
        self.pushButton_2.setText(_translate("MainWindow", "आ"))
        self.pushButton_3.setText(_translate("MainWindow", "ई"))
        self.pushButton_4.setText(_translate("MainWindow", "उ"))
        self.pushButton_5.setText(_translate("MainWindow", "इ"))
        self.pushButton_6.setText(_translate("MainWindow", "ऊ"))


    def on_click(self,pushButton):
        time.sleep(0.1)
        print("Clicked ",pushButton.text())
        X=""
        Y=""
        X1=""
        Y1=""
        with open('mouse_log.txt', 'r') as f:
            lines = f.read().splitlines()
            last_line = lines[-2]
            new_line=lines[-1]
        i=0   
        while(last_line[i]!='('):
            i=i+1
        i=i+1
        while(last_line[i]!=','):
            X=X+last_line[i]                
            i=i+1
        i=i+1
           
        while(last_line[i]!=')'):
            Y=Y+last_line[i]
            i=i+1    
        print(X,Y)    
        mouse=Controller()
        mouse.position=(int(X),int(Y))
        mouse.click(Button.left)
        mouse.release(Button.left)
        
        keyboard.write(pushButton.text())
        #mouse.position=(int(X)+1,int(Y))

        #mouse.click(Button.left)
        #mouse.release(Button.left)
        i=0   
        while(new_line[i]!='('):
            i=i+1
        i=i+1
        while(new_line[i]!=','):
            X1=X1+new_line[i]                
            i=i+1
        i=i+1
           
        while(new_line[i]!=')'):
            Y1=Y1+new_line[i]
            i=i+1
        mouse.position=(int(X1),int(Y1))   


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
