import sys
import time
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from datetime import datetime
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from themes import Theme

mainWindow, _ = loadUiType('front/Main page.ui')



class MainApp(QMainWindow, mainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.Handel_Buttons()
        self.setWindowTitle("Python App")
        self.setWindowIcon(QIcon('icon/python.png'))
        # self.calasic_theme()


    # def Handel_UI_Changes(self):
    #     self.tabWidget.tabBar().setVisible(False)

    def Handel_Buttons(self):

        self.ClasicTheme.clicked.connect(self.calasic_theme)
        self.darktheme.clicked.connect(self.dark_theme)


    def dark_theme(self):

        baseColor = '#0C2233' #222831 
        color_B = '#0C2233' #555555
        toolBoxhover = '#0E918C'
        color_D = 'rgb(34, 40, 49)'
        textColor = '#EEEDEB'
        border = '#0E918C'
        groupBoxtitle = '#0E918C'
        lineEdit = '#34857F'
        lineEditFocus = '#007acc'

        Theme.setting_page_theme(self, baseColor, color_B, toolBoxhover, color_D,
                                textColor, groupBoxtitle, lineEdit, 
                                lineEditFocus, border)

    def calasic_theme(self):

        baseColor = '#EEEDEB'
        color_B = '#f0f0f0'
        toolBoxhover = '#007acc'
        color_D = 'rgb(238, 238, 238)'
        textColor = '#333333'
        border = '#cccccc'
        groupBoxtitle = '#EBD9B4'
        lineEdit = '#F2EFE5'
        lineEditFocus = '#007acc'

        Theme.setting_page_theme(self, baseColor, color_B, toolBoxhover, color_D,
                                textColor, groupBoxtitle, lineEdit, 
                                lineEditFocus, border)





if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainApp()
    window.setFixedSize(965, 610)
    window.show()
    app.exec_()
