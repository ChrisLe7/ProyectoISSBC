# -*- coding: utf-8 -*-
"""
Created on Sun May  2 19:53:04 2021

@author: Ángel
"""

import sys
from PyQt5.QtCore import Qt
import controladorAplicacion as ctrl
from PyQt5.QtWidgets import (QApplication, QMainWindow, QTableWidget, QLabel, QListWidget, 
                             QPushButton, QPlainTextEdit, QHBoxLayout, QVBoxLayout, QGridLayout, QWidget, 
                             QDesktopWidget, QAction, QTableWidgetItem, QComboBox)
from PyQt5.QtGui import QIcon

class ClasificacionDlg(QMainWindow):
    
    def __init__(self):
        
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.colorEstablecidoBox = "background-color: rgb(218, 232, 236);"
        #117, 220, 75 : 188, 240, 166 
        
        self.colorFondo = "background-color: rgb(188, 240, 166);"
        self.estiloLabel = "font: bold italic 10pt; "
        widgetCentral = QWidget()
        
        cabeceraObservables = ['Observable', 'Valores Posibles']
        cabeceraFallos = ['Fallo']
        #Para el tema de mostrar los fallos y observables utilizaremos el QTableWidget
       
        self.labelFallosA = QLabel ("Seleccione los fallos existentes")
        
        self.tablaFallos = QTableWidget(len(ctrl.getFallos()), 1)
        self.tablaFallos.setColumnWidth(0, 250) #Asignan ancho a las columnas
        self.tablaFallos.setHorizontalHeaderLabels(cabeceraFallos) #Asignamos de esta forma la cabecera de la tabla
        self.rellenarFallos()
        
        self.labelObservablesA = QLabel("Seleccione los valores para observables", self)
        
        self.tablaObservables = QTableWidget(len(ctrl.getObservables()), 2) #Crea la tabla de elementos observables de dos columnas
        self.tablaObservables.setColumnWidth(0, 350) #Asignan ancho a las columnas
        self.tablaObservables.setColumnWidth(1, 385) #Asignan ancho a las columnas
        self.tablaObservables.setHorizontalHeaderLabels(cabeceraObservables) #Asignamos de esta forma la cabecera de la tabla
        self.rellenarObservables()
        
        #Listado de las posibles hipotesis que se puedan dar

        self.labelHipotesisL=QLabel("Posibles Hipotesis",self)#Creamos un listwidget para las posibles hipotesis
        self.listWidgetHipotesis = QListWidget()#Lista de hipotesis
        #self.rellenarPosiblesHipotesis()
        
        #ListWidget para el diagnostico
        self.labelDiagnosticoL=QLabel("Diagnostico Encontrado",self)
        self.listWidgetDiagnosticos = QListWidget()#Lista de diagnosticos
        
        
        #Texto de explicación del diagnostico
          
        self.labelExplicacionL=QLabel("Explicacion",self)
        self.PlainTextEditExplicacion = QPlainTextEdit("Todavía no se ha realizado al diagnostico")#Cuadro de texto de la explicacion 
          
        #Botones
        self.diagnosticaButton=QPushButton('Diagnosticar') #Para ejecutar el diagnostico
        self.diagnosticaButton.clicked.connect(self.diagnosticar)
        self.buttonsLayout = QHBoxLayout() #Gestor de diseño horizontal
        self.buttonsLayout.addStretch() 
        self.buttonsLayout.addWidget(self.diagnosticaButton)
        self.buttonsLayout.addStretch()
        
        
        #Ahora agruparemos los widgets en sus respectivos layouts
       
        layoutFallos = QVBoxLayout()
        layoutFallos.addWidget(self.labelFallosA)
        layoutFallos.addWidget(self.tablaFallos)
        
        layoutObservables = QVBoxLayout()
        layoutObservables.addWidget(self.labelObservablesA)
        layoutObservables.addWidget(self.tablaObservables)

        layoutHipotesis = QVBoxLayout()
        layoutHipotesis.addWidget(self.labelHipotesisL)
        layoutHipotesis.addWidget(self.listWidgetHipotesis)

        layoutDiagnosticos = QVBoxLayout()
        layoutDiagnosticos.addWidget(self.labelDiagnosticoL)
        layoutDiagnosticos.addWidget(self.listWidgetDiagnosticos)

        layoutExplicacion = QVBoxLayout()
        layoutExplicacion.addWidget(self.labelExplicacionL)
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
        menubar.setStyleSheet(self.colorEstablecidoBox)
        self.setCentralWidget(widgetCentral) #Asignar a la ventana la distribucion de los controles
        
        self.setWindowTitle(u'Aplicación para el Diagnostico - Ángel Fuentes y Christian Luna')
        self.setFixedSize(1318, 750)
        self.setWindowIcon(QIcon('imagenes/Logo_UCO.png'))
       
        stlButton = """QPushButton {
        background-color: palegoldenrod;
        border-width: 2px;
        border-color: darkkhaki;
        border-style: solid;
        border-radius: 5;
        padding: 3px;
        min-width: 9ex;
        min-height: 2.5ex;
        }"""
        QApplication.instance().setStyleSheet(stlButton)
        
        self.establecerColores()
        self.center()
        self.show()

    def establecerColores(self):
        self.tablaFallos.setStyleSheet(self.colorEstablecidoBox)
        self.tablaObservables.setStyleSheet(self.colorEstablecidoBox )
        self.listWidgetHipotesis.setStyleSheet(self.colorEstablecidoBox )
        self.listWidgetDiagnosticos.setStyleSheet(self.colorEstablecidoBox )
        self.PlainTextEditExplicacion.setStyleSheet(self.colorEstablecidoBox )
        self.setStyleSheet(self.colorFondo)
        
        self.labelFallosA.setStyleSheet(self.estiloLabel)
        self.labelObservablesA.setStyleSheet(self.estiloLabel)
        self.labelHipotesisL.setStyleSheet(self.estiloLabel)
        self.labelDiagnosticoL.setStyleSheet(self.estiloLabel)
        self.labelExplicacionL.setStyleSheet(self.estiloLabel)

    def center(self):
        
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())    

    def rellenarObservables(self):
        
        print("Se rellenan los observables")
        
        observables = ctrl.getObservables()
        
        for i in range(len(observables)):
            item = QTableWidgetItem(observables[i].nombre)
            item.setFlags(Qt.ItemIsUserCheckable | Qt.ItemIsEnabled)
            opciones = QComboBox()
            
            if (observables[i].tipo == 'multiple'):
                for j in observables[i].valoresPermitidos:
                    opciones.addItem(j)
            else:
                opciones.addItem('False')
                opciones.addItem('True')
                
            self.tablaObservables.setItem(i, 0, item)
            self.tablaObservables.setCellWidget(i, 1, opciones)
        
    def rellenarFallos(self):
        
        print("Se rellenan los fallos")
        
        fallos = ctrl.getFallos()
        
        for i in range(len(fallos)):
            item = QTableWidgetItem(fallos[i].nombre)
            item.setCheckState(Qt.Unchecked)
            item.setFlags(Qt.ItemIsUserCheckable | Qt.ItemIsEnabled)
            self.tablaFallos.setItem(i, 0, item)
    
    def rellenarPosiblesHipotesis(self):
        
        print("Se rellenan las posibles hipotesis")
        
        posiblesHipotesis = ctrl.getPosiblesHipotesis()
        
        for i in range(len(posiblesHipotesis)):
            self.listWidgetHipotesis.addItem(posiblesHipotesis[i].nombre)            
            
    def cambiarDominioEnfermedades(self):
        print("Cambiaremos el dominio al Medico")

    def cambiarDominioSegundo(self):
        print("Cambiaremos el dominio")
        
    def reiniciarDatos(self):
        print ('Reiniciar los datos')
        self.rellenarObservables()
        self.rellenarFallos()
        self.PlainTextEditExplicacion.setPlainText("Se ha reiniciado el Sistema")
        self.listWidgetDiagnosticos.clear()
        self.listWidgetHipotesis.clear()
        
    def diagnosticar(self):
        print ('Realizar Diagnostico')
        
        self.PlainTextEditExplicacion.setPlainText("")
        self.listWidgetDiagnosticos.clear()
        self.listWidgetHipotesis.clear()
        
        fallos = []
        
        for i in range(self.tablaFallos.rowCount()):
            item = self.tablaFallos.item(i, 0)
            
            if (item.checkState() == Qt.Checked):
                fallos.append(item.text())
        
        observables = []
        
        for i in range(self.tablaObservables.rowCount()):
            item1=self.tablaObservables.item(i,0)
            item2=self.tablaObservables.cellWidget(i, 1)
            observables.append((item1.text() , item2.currentText()))
        
        explicacion, diferencial, diagnosticoDetectado = ctrl.eventoDiagnosticar(fallos, observables)
        
        """TEMPORAL"""
        self.PlainTextEditExplicacion.setPlainText(explicacion)
        print(diagnosticoDetectado)
        
        for h in diferencial:
            self.listWidgetHipotesis.addItem(h.nombre)
                
        for d in diagnosticoDetectado:
             self.listWidgetDiagnosticos.addItem(d)

def main():
    app = QApplication(sys.argv)
    ex = ClasificacionDlg()
    sys.exit(app.exec_())

if __name__=='__main__':
    main()