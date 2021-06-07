# -*- coding: utf-8 -*-
"""
Created on Wed May  5 13:56:33 2021

@author: Ángel
"""

import bcGenerica as cd

class MetodoCoberturaCausal():
    
    """Se realizara el metodo de cobertura casual para la realizacion de la aplicacion de diagnostico"""
    def __init__(self, fallos):
        
        self.fallos = fallos
        self.explicacion = ''
        self.diferencial = []
        self.diagnostico = []
        self.evidencias = []
        self.observables = []
        self.observablesVistos = []
        
    def getDiferencial(self):
        
        #Devuelve la lista con la posibles hipotesis
        return self.diferencial
        
    def getDiagnostico(self):
        
        #Se devuelve el diagnostico
        return self.diagnostico
        
    def getExplicacion(self):
        
        #Se devuelve la explicacion para el diagnostico
        return self.explicacion
        
    def setObservables(self, listaObservables):
        
        #Establece la lista de observables
        self.observables = listaObservables
        
    def execute(self, tr = False):
        
        #Ejecucion del metodo de cobertura causal para la tarea de diagnostico
        cc = Cubrir(self.fallos)
        self.diferencial = cc.execute() #Devuelve una lista con las posibles hipotesis
        
        if len(self.diferencial)<=0:
            print ("No hay hipotesis") #Poner en la vista
        else:
            for i in self.diferencial:
                self.diagnostico.append(i) #Se añade a diagnostico las posibles hipótesis, es decir el conjunto diferencial
            while len(self.diagnostico)>0 and len(self.observables)>0:
                hipotesisSeleccionada = Seleccionar(self.diagnostico).execute() #Seleccionamos una de las posibles hipotesis
            
                if tr: #Este if solo salta si estamos ejecutando para la terminal
                    print (len(self.diagnostico))
                    print (len(self.observables))
                    print (self.diagnostico)
                    print (self.observables)
                    print ("hipotesis seleccionada: ", hipotesisSeleccionada.nombre)
                    print ("======================")
            
                    #Ahora vamos a especificar un observable
                observable = Especificar().execute(self.observables, self.observablesVistos) #Especificamos para obtener el observable
                
                
                if tr:
                    print ("------->"+str(observable))
                    print ("Observable seleccionado: ", observable.nombre)
                    print ("=========================")
            
                #Ahora vamos a obtener un hallazgo de ese observable
                hallazgo = Obtener().execute(observable)
                if hallazgo not in self.evidencias:
                    self.evidencias.append(hallazgo) #añadimos el hallazgo a la lista de evidencias.
                
                if tr:
                    print ("Hallazgo del observable ", observable.nombre, " es: ", hallazgo.valor)
            
                #Ahora vamos a realizar la verificacion
                for i in self.diferencial:
                    if i in self.diagnostico:
                        verifica = Verificar(self.evidencias, i).execute() #aqui el verificar recibe la lista de evidencias u hallazgos y la posible hipótesis de solución
            
                        if verifica[0] is False: #Si la hipotesis no es posible se elimina del conjunto diferencial
                            if tr:
                                print ("Verificacion completada. No puede ser, por lo tanto se borra")
                                self.explicacion += verifica[1]
                                if i in self.diagnostico:
                                    self.diagnostico.remove(i) #vamos eliminando aquellas hipotesis que sean falsas
                        #si verificar es falso para esa hipotesis, esta será eliminada del conjunto diagnostico que contendrá la solucion final(averia) o soluciones
                        else:
                            self.explicacion += verifica[1]
                self.observables.pop(0)           
            
class Inferencia():
    
    def __init__(self):
        
        pass
    
    def execute(self):
        
        pass
        
class Cubrir(Inferencia):
    
    #Se le pasa una lista de fallos y proporciona una lista de posibles hipotesis
    def __init__(self, fallos):
        
        super().__init__(self)
        self.fallos = fallos
        self.listaHipotesis = []
        
    def execute(self):
        
        hipotesis = cd.hipotesis()
        for h in hipotesis:
            for i in h.fallos:
                for f in self.fallos:
                    print (h.nombre)
                    if i.nombre == f:
                        if not h in self.listaHipotesis:
                            self.listaHipotesis.append(h)
        hipotesis = self.listaHipotesis
        return hipotesis
        
class Seleccionar(Inferencia):
    
    #Selecciona una hipotesis del conjunto diferencial
    def __init__(self, conjuntoDiferencial):
        
        super().__init__(self)
        self.conjuntoDiferencial = conjuntoDiferencial
        
    def execute(self):
        
        if len(self.conjuntoDiferencial)>0:
            return self.conjuntoDiferencial[0]
        else:
            return None
            
class Especificar(Inferencia):
    
    #Crea el observable
    def __init__(self):
        
        super().__init__(self)        
        
    def execute(self, listaObservables, listaObservablesVistos):  
        
        observable = cd.creaObservable(listaObservables[0]) #lObservables es la lista actual de observables con los valores que tienen marcados por el usuario
        listaObservablesVistos.append(listaObservables[0])
        return observable
    
class Obtener(Inferencia):
    
    #Se le pasa un observable y se obtiene un hallazgo (el valor de ese observable) 
    def __init__(self):
        
        super().__init__(self)
        
    def execute(self, observable):
        
        return cd.Hallazgo(observable.nombre, observable.valor)
    
class Verificar(Inferencia):
    
    #Verifica si una hipotesis de averia es compatible con un conjuto de hallazgos
    def __init__(self, lhallazgos, hipotesis):
        
        super().__init__(self)
        self.hallazgos = lhallazgos
        self.hipotesis = hipotesis
        self.resultado = None
        self.justificacion = ''
        
    def execute(self, tr=True):
        resultado = True
        if tr:
            print ("Verificando la hipotesis:", self.hipotesis.nombre, self.hipotesis)
            print

        for h in self.hipotesis.debePresentar:
            if tr:
                print ("Debe presentar:", h, h.nombre, h.valor, "=>", self.hallazgos)
                print ("Debe presentar:", h.nombre, h.valor, "=>", [(f.nombre, f.valor) for f in self.hallazgos])
                print
                
            if not (h.nombre in [f.nombre for f in self.hallazgos]):
                pass
            else: #El nombre del hallazgo de la hipotesis esta pero debe de coincidir los valores
                falla = False #bandera
                for e in self.hallazgos:
                    if e.nombre == h.nombre: #Comprueba que coinciden los valores
                        if isinstance(h.valor, list): #Si el valor del hallazgo de la hipotesis es de tipo lista
                            if not e.valor in h.valor: #Comprueba que el valor del hallazgo presentado esta en esa lista
                                falla = True #El valor del hallazgo presentado no esta en la lista
                                break
                        else: #El valor del hallazgo de la hipotesis no es de tipo lista
                            if not e.valor == h.valor: #Si no coinciden los valores falla
                                falla = True
                                break
                if falla: #Si se ha fallado se anade a la justificacion. Mejorar
                    self.justificacion += "No puede ser " + self.hipotesis.nombre + " porque deberia presentar el hallazgo " + h.nombre + " con valor apropiado." + '\n'
                    print (self.justificacion)
                    resultado = False
            if resultado == False: #Si ha resultado fallida la verificacion salimos de ella
                self.resultado = False
                return (False, self.justificacion)
            else:
                self.justificacion += "De momento puede ser " + self.hipotesis.nombre + '\n'
                
        for f in self.hipotesis.noPuedePresentar:
            if (f.nombre in [x.nombre for x in self.hallazgos]):
                falla = False #Bandera
                for e in self.hallazgos:
                    if e.nombre == f.nombre: 
                        if isinstance(f.valor, list):
                            if e.valor in f.valor:
                                falla = True
                                break
                        else:
                            if e.valor == f.valor:
                                falla = True
                                break
                if falla:
                    self.justificacion += "No puede ser " + self.hipotesis.nombre + " porque no deberia presentar el hallazgo " + f.nombre + " con el valor que lo presenta " + '\n'
                    resultado = False
            if resultado == False:
                self.resultado = False
                return (False, self.justificacion)
            else:
                self.justificacion += "De momento puede ser " + self.hipotesis.nombre + '\n'
            self.resultado=True
            return (True, self.justificacion)