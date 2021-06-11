# -*- coding: utf-8 -*-
"""
Created on Sun May  2 19:53:04 2021

@author: Ángel
"""

import sys
from os import listdir
from importlib import import_module
from bcGenerica import Observable
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QLabel, QListWidget, QPushButton, QPlainTextEdit, QHBoxLayout, QVBoxLayout, QGridLayout

class ClasificacionDlg(QMainWindow):
    
    def __init__(self):
        
        super().__init__()
        self.initUI()
        
    def initUI(self):
        
        print(len(Observable.__subclasses__()))
        
        num_observable = len(Observable.__subclasses__())

        cabeceraObservables = ['Observable', 'Valores Posibles']
        #Para el tema de mostrar los fallos y observables utilizaremos el QTableWidget
        labelFallosA = QLabel("Seleccione los valores para observables", self)
        labelFallosB = QLabel("", self)
        
        self.tablaObservables = QTableWidget(num_observable,2) #Crea la tabla de elementos observables de dps columnas
        self.tablaObservables.setColumnWidth(0, 250) #Asignan ancho a las columnas
        self.tablaObservables.setColumnWidth(1, 400) #Asignan ancho a las columnas
        self.tablaObservables.setHorizontalHeaderLabels(cabeceraObservables) #Asignamos de esta forma la cabecera de la tabla
        
        #Listado de las posibles hipotesis que se puedan dar

        labelHipotesisL=QLabel("Posibles Hipotesis A buscar",self)#Creamos un listwidget para las posibles hipotesis
        labelHipotesisR=QLabel("",self)
        self.listWidgetHipotesis = QListWidget()#Lista de hipotesis
        
        #ListWidget para el diagnostico
        labelDiagnosticoL=QLabel("Diagnostico Encontrado",self)
        labelDiagnosticoR=QLabel("",self)
        self.listWidgetDiagnosticos = QListWidget()#Lista de diagnosticos
        
        
        #Texto de explicación del diagnostico
          
        labelExplicacionL=QLabel("Explicacion",self)
        labelExplicacionR=QLabel("     ",self)
        self.PlainTextEditExplicacion = QPlainTextEdit("Todavía no se ha realizado al diagnostico")#Cuadro de texto de la explicacion 
          
        #Botones
        self.diagnosticaButton=QPushButton('Diagnosticar') #Para ejecutar el diagnostico
        
        self.buttonsLayout = QHBoxLayout() #Gestor de diseño horizontal
        self.buttonsLayout.addStretch() 
        self.buttonsLayout.addWidget(self.diagnosticaButton)
        self.buttonsLayout.addStretch()
        
        grid = QGridLayout()
        grid.setSpacing(5)
        
        grid.addWidget(labelFallosA, 0, 4)
        grid.addWidget(labelFallosB, 0, 5)
        grid.addWidget(self.tablaObservables, 2, 2, 1, 8)
        
        grid.addWidget(labelHipotesisL, 0, 10)
        grid.addWidget(labelHipotesisR, 0, 11)
        grid.addWidget(self.listWidgetHipotesis, 2, 10,1,3)
        
        grid.addWidget(labelDiagnosticoL, 4, 0)
        grid.addWidget(labelDiagnosticoR, 4, 1)
        grid.addWidget(self.listWidgetDiagnosticos, 5, 0,1,2)
        grid.addWidget(labelExplicacionL, 4, 2)
        grid.addWidget(labelExplicacionR, 4, 3)
        grid.addWidget(self.PlainTextEditExplicacion, 5, 2,1,11)
        
        #Diseño principal
        mainLayout = QVBoxLayout() #Se crea el diseño principal en forma vertical
        mainLayout.addLayout(grid) #Le añadimos la rejilla de los controles
        mainLayout.addLayout(self.buttonsLayout) #Añadimos la disposicion de controles horizontal
        self.setLayout(mainLayout) #Asignar a la ventana la distribucion de los controles
        
    
        
        self.setWindowTitle('Aplicación para el Diagnostico - Ángel Fuentes y Christian Luna')
        self.resize(400, 400)
        self.show()







def main():
    app = QApplication(sys.argv)
    ex = ClasificacionDlg()
    sys.exit(app.exec_())

if __name__=='__main__':
    main()