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
    
    # setup auto gui
    setupAutoGui()
    #manual version
    #result = movements(True)
    mouse_movements(True)
