import pyautogui
import sys
#from PyQt5 import QtCore, QtGui, QtWidgets
#from gui.gui import Ui_MainWindow
from app.utility import setupAutoGui, mouse_movements

def main():
    print("Program started")

    #app = QtWidgets.QApplication(sys.argv)
    #MainWindow = QtWidgets.QMainWindow()
    #ui = Ui_MainWindow()
    #ui.setupUi(MainWindow)
    #MainWindow.show()

    #sys.exit(app.exec_())

    #if ui.move_button.click():
    #    print("button pressed")
    #    movements(True)

    return True

if __name__ == "__main__":

    #Gui version
    #main()
    
    screenWidth, screenHeight = pyautogui.size()
    currentMouseX, currentMouseY = pyautogui.position()

    try:
        while 1:
            var = input("enter p to exit:  ")
            if var == 'p':
                break
            else:
                print('test something')
                mouse_movements()

    except KeyboardInterrupt:
            sys.exit()
            raise

    #manual version
    #result = movements(True)
