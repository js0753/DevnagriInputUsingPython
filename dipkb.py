# -*- coding: utf-8 -*-
import time
import sys
import threading
import subprocess
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])
try:
    
    from PyQt5.QtCore import Qt
    from PyQt5.QtWidgets import QMainWindow,QApplication,QGridLayout,QLineEdit,QPushButton,QVBoxLayout,QWidget
except ImportError:
    install('pyqt5')
    from PyQt5.QtCore import Qt
    from PyQt5.QtWidgets import QMainWindow,QApplication,QGridLayout,QLineEdit,QPushButton,QVBoxLayout,QWidget
try:    
    import pyautogui
except ImportError:
    install('pyautogui')
    import pyautogui
try:    
    import keyboard
except ImportError:
    install('keyboard')

try:
    from pynput.mouse import Listener
except ImportError:
    install('pynput')
    from pynput.mouse import Listener
    
 
    

import logging

#logging.basicConfig(filename="mouse_log.txt",level=logging.DEBUG, format="%(asctime)s: %(message)s")
#def mouse_clicklogger():
logging.basicConfig(filename="mouse_log.txt",level=logging.DEBUG, format="%(asctime)s: %(message)s")

def mouse_click(x,y,button,pressed):
    if pressed:
        print("({0},{1})".format(x,y))
        logging.info("({0},{1})".format(x,y))

def click_logger():
    with Listener(on_click=mouse_click) as listener:
           listener.join()
    

from functools import partial





class DipUi(QMainWindow):
    

    def __init__(self):
        
        super().__init__()
        self.setWindowFlags(Qt.WindowStaysOnTopHint )
        # Set some main window's properties
        self.setWindowTitle("Dip Keyboard")
        self.setFixedSize(350, 450)
        # Set the central widget and the general layout
        self.generalLayout = QVBoxLayout()
        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)
        self._centralWidget.setLayout(self.generalLayout)
        # Create the display and the buttons
        #self._createDisplay()
        self._createButtons()

    #def _createDisplay(self):
        
        # Create the display widget
        #self.display = QLineEdit()
        # Set some display's properties
        #self.display.setFixedHeight(35)
        #self.display.setAlignment(Qt.AlignRight)
        #self.display.setReadOnly(True)
        # Add the display to the general layout
        #self.generalLayout.addWidget(self.display)

    def _createButtons(self):
        
        self.buttons1 = {}
        buttonsLayout = QGridLayout()
       
        buttons1 = [
            "अ","आ","इ","ई","उ","ऊ","ए","ऎ","ओ","औ",
            
            "क","ख","ग","घ","च","छ","ज","झ","ञ","ट","ठ","ण","ळ","त","थ","द","ध","न","प","फ","ब","भ","म","य","र","ल","व","श","ष","स","ह",

            "ँ","ं","ः","ा","ि","ी","ु","ू","े","ै","ो","ौ","्","<-","space"
        ]
        #print(buttons1[0])
        self.buttons={}
        i=0
        j=0
        for button in buttons1:
            #print(button,i,j)
            if(button=="क" or button=="ँ" or button=="<-"):
                i=i+1
                j=0
           
            self.buttons[button] = (i,j)
            if(j<6):
                j=j+1
            else:
                j=0
                i=i+1
            
            
            
            
        # Create the buttons and add them to the grid layout
        for btnText, pos in self.buttons.items():
            self.buttons[btnText] = QPushButton(btnText)
            self.buttons[btnText].setFixedSize(40, 40)
            buttonsLayout.addWidget(self.buttons[btnText], pos[0], pos[1])
        # Add buttonsLayout to the general layout
        self.generalLayout.addLayout(buttonsLayout)
"""
    def setDisplayText(self, text):
        
        self.display.setText(text)
        self.display.setFocus()

    def displayText(self):
        
        return self.display.text()

    def clearDisplay(self):
       
        self.setDisplayText("")

    def backDisplay(self):
        s=self.display.text()[:-1]
        self.setDisplayText(s)
"""   


        

class SetupConnection:
    

    def __init__(self, view):
       
        self._view = view
        # Connect signals and slots
        for btnText, btn in self._view.buttons.items():
            #if btnText not in {"<-", "clear"}:
            btn.clicked.connect(partial(self.button_press, btnText))
        #self._view.buttons["clear"].clicked.connect(self._view.clearDisplay)
        #self._view.buttons["<-"].clicked.connect(self._view.backDisplay)

 
    def button_press(self, sub_exp):
        """
        if sub_exp not in {"<-", "clear"}:
            expression = self._view.displayText() + sub_exp
            self._view.setDisplayText(expression)
        """
       

        print("Clicked ",sub_exp)
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
      
        pyautogui.click(int(X),int(Y))
        if sub_exp not in {"<-", "clear","space"}:
            keyboard.write(sub_exp)
        elif sub_exp=="<-":
            keyboard.press_and_release('backspace')
        elif sub_exp=="space":
            keyboard.press_and_release('space')
        pyautogui.click(int(X)+10,int(Y))
   
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
        pyautogui.moveTo(int(X1),int(Y1))
        



def main():
    t1 = threading.Thread(target=click_logger)
    t1.start()
    #Listener(on_click=mouse_click)
    
   
        
    app = QApplication(sys.argv)
 
    view = DipUi()
    view.show()
 
    SetupConnection( view=view)
    if(app.exec_()):
        #pynput.mouse.Listner.stop()
        
        sys.exit()
       
       


if __name__ == "__main__" :
    main()
