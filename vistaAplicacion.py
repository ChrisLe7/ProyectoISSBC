# -*- coding: utf-8 -*-
"""
Created on Sun May  2 19:53:04 2021

@author: Ángel Fuentes (i82fuala) Christian Luna (i82luesc)
"""

import sys
import controladorAplicacion as ctrl
from os import listdir
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (QApplication, QMainWindow, QTableWidget, QLabel, QListWidget, 
                             QPushButton, QPlainTextEdit, QHBoxLayout, QVBoxLayout, QGridLayout, QWidget, 
                             QDesktopWidget, QAction, QTableWidgetItem, QComboBox)

class ClasificacionDlg(QMainWindow):
    
    def __init__(self):
        
        super().__init__()
        self.initUI()
        
    def initUI(self):
        
        widgetCentral = QWidget()
        
        cabeceraObservables = ['Observable', 'Valores Posibles']
        cabeceraFallos = ['Fallo']
       
        self.labelFallosA = QLabel ("Seleccione los fallos existentes")
        
        #Para el tema de mostrar los fallos y observables utilizaremos el QTableWidget
        self.tablaFallos = QTableWidget(len(ctrl.getFallos()), 1)
        self.tablaFallos.setColumnWidth(0, 250) #Asignan ancho a las columnas
        self.tablaFallos.setHorizontalHeaderLabels(cabeceraFallos) #Asignamos de esta forma la cabecera de la tabla
        
        self.labelObservablesA = QLabel("Seleccione los valores para observables", self)
        
        self.tablaObservables = QTableWidget(len(ctrl.getObservables()), 2) #Crea la tabla de elementos observables de dos columnas
        self.tablaObservables.setColumnWidth(0, 350) #Asignan ancho a las columnas
        self.tablaObservables.setColumnWidth(1, 385) #Asignan ancho a las columnas
        self.tablaObservables.setHorizontalHeaderLabels(cabeceraObservables) #Asignamos de esta forma la cabecera de la tabla
        
        #Listado de las posibles hipotesis que se puedan dar
        self.labelHipotesisL=QLabel("Posibles Hipótesis",self)#Creamos un listwidget para las posibles hipotesis
        self.listWidgetHipotesis = QListWidget()#Lista de hipotesis
        
        #ListWidget para el diagnostico
        self.labelDiagnosticoL=QLabel("Diagnóstico Encontrado",self)
        self.listWidgetDiagnosticos = QListWidget()#Lista de diagnosticos
        
        #Texto de explicación del diagnostico
        self.labelExplicacionL=QLabel("Explicación",self)
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
        layoutSeccionSuperior.addLayout(layoutFallos, 0, 0)
        layoutSeccionSuperior.setColumnStretch(0, 1)
        layoutSeccionSuperior.addLayout(layoutObservables, 0, 1)        
        layoutSeccionSuperior.setColumnStretch(1, 3)
        layoutSeccionSuperior.addLayout(layoutHipotesis, 0, 2)

        #Layout Inferior
        layoutSeccionInferior = QGridLayout() 
        layoutSeccionInferior.addLayout(layoutDiagnosticos, 0, 0)
        layoutSeccionInferior.addLayout(layoutExplicacion, 0, 1)
 
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
        
        #Creamos la barra del menu y añadimos las opciones
        self.menubar = self.menuBar()
        self.eleccionDominio = self.menubar.addMenu('&Dominio')
        
        opcionesDiagnostico = self.menubar.addMenu('&Opciones')
        opcionesDiagnostico.addAction(diagnosticar)
        opcionesDiagnostico.addAction(reiniciarDatos)
        opcionesDiagnostico.addAction(exitAct)
        
        self.getDominios()
                
        self.setCentralWidget(widgetCentral) #Asignar a la ventana la distribucion de los controles
        
        self.setWindowTitle(u'Aplicación para el Diagnostico - Ángel Fuentes y Christian Luna')
        self.setFixedSize(1318, 750)
        self.setWindowIcon(QIcon('imagenes/Logo_UCO.png'))
       
        self.establecerColores()
        self.center()
        self.show()

    '''
    Con esta función realizaremos la asignación de los estilos para los diferentes Widgets del sistema
    '''
    def establecerColores(self):
        
        self.colorFondo = "background-color: #513d47;"
        self.estiloLabel = "font: bold italic 10pt; color: #d3d7d2"
        self.colorEstablecidoBox = """background-color: rgb(159, 168, 180 ); border: 2px solid; border-radius:5px; """
        self.colorEstablecidoBoton = """background-color: rgb(159, 168, 180 ); border: 2px solid; border-radius:5px; padding: 0.5em; """
        
        stlTabla = """
        QHeaderView {
            background-color:rgb(98, 115, 71 );
            font: bold 10pt;
        }
        
        QHeaderView::section{
            background:rgb(98, 115, 71  );
        }
        
        QTableWidget {
            background-color: rgb(168, 182, 148 );
        }
        
        QComboBox {
            background-color: rgb(168, 182, 148 );
        }
     
        """
        stlLista = """
        QListWidget {
            background-color: rgb(168, 182, 148 );
        }
        """
        
        stlTextPlain = """
        QPlainTextEdit {
            background-color: rgb(168, 182, 148 );
        }
        """
        
        self.menubar.setStyleSheet(self.colorEstablecidoBox)
        
        self.tablaFallos.setStyleSheet(stlTabla)
        self.tablaObservables.setStyleSheet(stlTabla)
        self.listWidgetHipotesis.setStyleSheet(stlLista )
        self.listWidgetDiagnosticos.setStyleSheet(stlLista)
        self.PlainTextEditExplicacion.setStyleSheet(stlTextPlain)
        self.setStyleSheet(self.colorFondo)
        
        self.labelFallosA.setStyleSheet(self.estiloLabel)
        self.labelObservablesA.setStyleSheet(self.estiloLabel)
        self.labelHipotesisL.setStyleSheet(self.estiloLabel)
        self.labelDiagnosticoL.setStyleSheet(self.estiloLabel)
        self.labelExplicacionL.setStyleSheet(self.estiloLabel)
        
        self.diagnosticaButton.setStyleSheet(self.colorEstablecidoBoton)

    '''
    Con esta función centraremos la ventana de la aplicación
    '''
    def center(self):
        
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())    

    '''
    Mediante esta función rellenaremos las tablas de observables
    '''
    def rellenarObservables(self):
        
        print("Se rellenan los observables")
        
        observables = ctrl.getObservables()
        self.tablaObservables.setRowCount(len(observables))
        
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
  
    '''
    Mediante esta función rellenaremos las tablas de fallos
    '''    
    def rellenarFallos(self):
        
        print("Se rellenan los fallos")
        
        fallos = ctrl.getFallos()
        self.tablaFallos.setRowCount(len(fallos))
        
        for i in range(len(fallos)):
            item = QTableWidgetItem(fallos[i].nombre)
            item.setCheckState(Qt.Unchecked)
            item.setFlags(Qt.ItemIsUserCheckable | Qt.ItemIsEnabled)
            self.tablaFallos.setItem(i, 0, item)           
         
    '''
    De esta forma podemos obtener los diferentes dominios de forma dinámica, permitiendo sin necesidad de modificar la vista el 
    agregar un nuevo dominio, unicamente deberá de seguir el formato de los dominios que ya se encuentran en dicha carpeta
    '''
    def getDominios(self):

        print("Detectamos los dominios que se pueden cargar")

        dominios = [dominio for dominio in listdir("dominios") if dominio.startswith("bc") and dominio.endswith(".py")]

        for d in dominios:
            dominio = d.replace("bc", "").replace(".py", "")
            act = QAction(dominio, self)
            act.setStatusTip('Cambia el dominio del diagnostico')
            act.triggered.connect(self.cambiarDominio)
            self.eleccionDominio.addAction(act)

    '''
    De esta forma cambiamos el dominio de la aplicación actual, reiniciando los datos de los observables y de los fallos posibles.
    '''
    def cambiarDominio(self):
                
        print("Cambiaremos el dominio al de '" + self.sender().text() + "'")
                
        dominio = "bc" + self.sender().text()
        ctrl.cargarDominio(dominio)
        self.reiniciarDatos()
   
    '''
    Esta función reinicia los datos de las tablas y de las listas visibles en la vista
    '''   
    def reiniciarDatos(self):
        
        print ('Reiniciar los datos')
        
        self.rellenarObservables()
        self.rellenarFallos()
        self.PlainTextEditExplicacion.setPlainText("Se ha reiniciado el Sistema")
        self.listWidgetDiagnosticos.clear()
        self.listWidgetHipotesis.clear()
     
    '''
    Función que desencadenara la tarea de diagnostico del controlador, encargada de recoger los fallos presentados y los observables dados
    '''
    def diagnosticar(self):
        
        print ('Realizar Diagnostico\n')
        
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
        
        self.PlainTextEditExplicacion.setPlainText(explicacion)
            
        self.listWidgetHipotesis.addItems([d.nombre for d in diferencial])
             
        self.listWidgetDiagnosticos.addItems(diagnosticoDetectado)

def main():
    app = QApplication(sys.argv)
    ex = ClasificacionDlg()
    sys.exit(app.exec_())

if __name__=='__main__':
    main()