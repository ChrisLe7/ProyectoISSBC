# -*- coding: utf-8 -*-
"""
Created on Sun May  2 19:53:04 2021

@author: Ángel
"""

import sys
from os import listdir
from importlib import import_module
from bcGenerica import Observable
from PyQt5.QtWidgets import QApplication, QMainWindow

class ClasificacionDlg(QMainWindow):
    
    def __init__(self):
        
        super().__init__()
        self.initUI()
        
    def initUI(self):
        
        print(len(Observable.__subclasses__()))
        
        self.setWindowTitle('test')
        self.resize(400, 400)
        self.show()

def main():
    app = QApplication(sys.argv)
    ex = ClasificacionDlg()
    sys.exit(app.exec_())

if __name__=='__main__':
    main()