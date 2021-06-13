# -*- coding: utf-8 -*-
"""
Created on Sun May  2 19:53:04 2021

@author: Ángel
"""

import sys
from os import listdir
from importlib import import_module
from bcGenerica import Observable
from PyQt5.QtWidgets import (QApplication, QMainWindow, QTableWidget, QLabel, QListWidget, 
                             QPushButton, QPlainTextEdit, QHBoxLayout, QVBoxLayout, QGridLayout, QWidget, 
                             QDesktopWidget, QAction)

class ClasificacionDlg(QMainWindow):
    
    def __init__(self):
        
        super().__init__()
        self.initUI()
        
    def initUI(self):
                
        widgetCentral = QWidget()
        
        num_observable = len(Observable.__subclasses__())

        cabeceraObservables = ['Observable', 'Valores Posibles']
        cabeceraFallos = ['Fallo']
        #Para el tema de mostrar los fallos y observables utilizaremos el QTableWidget
       
        labelFallosA = QLabel ("Seleccione los fallos existentes")
        self.tablaFallos = QTableWidget(num_observable,1)
        self.tablaFallos.setColumnWidth(0, 250) #Asignan ancho a las columnas
        self.tablaFallos.setHorizontalHeaderLabels(cabeceraFallos) #Asignamos de esta forma la cabecera de la tabla
        
        
        labelObservablesA = QLabel("Seleccione los valores para observables", self)
        labelFallosB = QLabel("", self)
        
        self.tablaObservables = QTableWidget(num_observable,2) #Crea la tabla de elementos observables de dos columnas
        self.tablaObservables.setColumnWidth(0, 350) #Asignan ancho a las columnas
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
        
        
        #Ahora agruparemos los widgets en sus respectivos layouts
       
        layoutFallos = QVBoxLayout()
        layoutFallos.addWidget(labelFallosA)
        layoutFallos.addWidget(self.tablaFallos)
        
        
        layoutObservables = QVBoxLayout()
        layoutObservables.addWidget(labelObservablesA)
        layoutObservables.addWidget(self.tablaObservables)
        
        layoutHipotesis = QVBoxLayout()
        layoutHipotesis.addWidget(labelHipotesisL)
        layoutHipotesis.addWidget(self.listWidgetHipotesis)
        
        layoutDiagnosticos = QVBoxLayout()
        layoutDiagnosticos.addWidget(labelDiagnosticoL)
        layoutDiagnosticos.addWidget(self.listWidgetDiagnosticos)
 
        layoutExplicacion = QVBoxLayout()
        layoutExplicacion.addWidget(labelExplicacionL)
        layoutExplicacion.addWidget(self.PlainTextEditExplicacion)       

        #Layout Superior
        
        layoutSeccionSuperior = QGridLayout() 
        
        layoutSeccionSuperior.addLayout(layoutFallos,0,0)
        layoutSeccionSuperior.setColumnStretch (0,1)
        layoutSeccionSuperior.addLayout(layoutObservables,0,1)        
        layoutSeccionSuperior.setColumnStretch (1,3)    

        
        layoutSeccionSuperior.addLayout(layoutHipotesis,0,2)

        #Layout Inferior
        layoutSeccionInferior = QGridLayout() 
        layoutSeccionInferior.addLayout(layoutDiagnosticos,0,0)

        layoutSeccionInferior.addLayout(layoutExplicacion,0,1)

 
        #Diseño principal
        mainLayout = QVBoxLayout() #Se crea el diseño principal en forma vertical
        mainLayout.addLayout(layoutSeccionSuperior) 
        mainLayout.addLayout(layoutSeccionInferior) 
        mainLayout.addLayout(self.buttonsLayout) #Añadimos la disposicion de controles horizontal
        
        widgetCentral.setLayout(mainLayout)
        
        #Ahora crearemos la barra de menu 
        #Creamos las acciones 
        exitAct = QAction('Exit', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('Exit application')
        exitAct.triggered.connect(self.close)
        
        reiniciarDatos = QAction('Reiniciar', self)
        reiniciarDatos.setShortcut('Ctrl+R')
        reiniciarDatos.setStatusTip('Reiniciar Datos Diagnosticos')
        reiniciarDatos.triggered.connect(self.reiniciarDatos)
        
        diagnosticar = QAction('Diagnosticar', self)
        diagnosticar.setShortcut('Ctrl+D')
        diagnosticar.setStatusTip('Iniciar el Diagnostico')
        diagnosticar.triggered.connect(self.diagnosticar)
        
        
        
        dominioEnfermedades = QAction('Enfermedades', self)
        dominioEnfermedades.setShortcut('Ctrl+E')
        dominioEnfermedades.setStatusTip('Cambiaremos el dominio del diagnostico')
        dominioEnfermedades.triggered.connect(self.cambiarDominioEnfermedades)
        
        dominioSegundo = QAction('SegundoDominio', self)
        dominioSegundo.setShortcut('Ctrl+X')
        dominioSegundo.setStatusTip('Cambiaremos el dominio del diagnostico')
        dominioSegundo.triggered.connect(self.cambiarDominioSegundo)
        
        #Creamos la barra del menu y añadimos las opciones
        menubar = self.menuBar()
        eleccionDominio = menubar.addMenu('&Dominio')
        eleccionDominio.addAction(dominioEnfermedades)
        eleccionDominio.addAction(dominioSegundo)
        
        opcionesDiagnostico = menubar.addMenu('&Opciones')
        opcionesDiagnostico.addAction(diagnosticar)
        opcionesDiagnostico.addAction(reiniciarDatos)
        opcionesDiagnostico.addAction(exitAct)
        
        self.setCentralWidget(widgetCentral)  #Asignar a la ventana la distribucion de los controles
        
        self.setWindowTitle(u'Aplicación para el Diagnostico - Ángel Fuentes y Christian Luna')
        self.resize(1300, 750)
        self.center()
        self.show()

    def center(self):
        
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())    

    def rellenarObservables(self):
        
        print("Se rellenan los observables")
    
    def cambiarDominioEnfermedades(self):
        print("Cambiaremos el dominio al Medico")

    def cambiarDominioSegundo(self):
        print("Cambiaremos el dominio")
        
    def reiniciarDatos(self):
        print ('Reiniciar los datos')
        
    def diagnosticar(self):
        print ('Realizar Diagnostico')

def main():
    app = QApplication(sys.argv)
    ex = ClasificacionDlg()
    sys.exit(app.exec_())

if __name__=='__main__':
    main()