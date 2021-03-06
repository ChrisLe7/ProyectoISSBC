# -*- coding: utf-8 -*-
"""
Created on Wed May  5 13:56:33 2021

@author: Ángel Fuentes (i82fuala) Christian Luna (i82luesc)
"""

from importlib import import_module
from bcGenerica import Hallazgo

# Guarda el módulo de la base de conocimientos cargado
bc = None

'''
Clase para el método de cobertura causal
'''
class MetodoCoberturaCausal():
    
    '''
    Se realizara el metodo de cobertura casual para la realizacion de la aplicacion de diagnostico
    '''
    def __init__(self, fallos, observables):
        
        self.fallos = fallos
        self.explicacion = ''
        self.diferencial = []
        self.diagnostico = []
        self.evidencias = []
        self.observables = observables
        self.observablesVistos = []
        
    def execute(self, tr = False):
        
        if bc == None:
            return 'Primero debe de seleccionar un dominio', [], []
        
        if self.fallos == []:
            return 'No se han seleccionado fallos', [], []
        
        # Ejecucion del metodo de cobertura causal para la tarea de diagnostico
        self.explicacion += u'Ejecutando cobertura causal.\n'
        self.diagnosticoEncontrado = []
        # Se obtiene el conjunto diferencial invocando a la inferencia de cobertura causal
        self.diferencial = Cubrir(self.fallos).execute() # Devuelve una lista con las posibles hipotesis
        
        self.explicacion+=u'\nSe obtiene el conjunto diferencial: \n'
        
        for f in self.diferencial: # Va construyendo la explicación
            self.explicacion += "  -  " + str(f.nombre) + '\n' # Se Agregan todas las posibles hipotesis a la explicación
        
        self.explicacion += '\n=====================\n'
        
        if len(self.diferencial) <= 0:
            print ("No hay hipotesis") # Poner en la vista
        else:
            for i in self.diferencial:
                self.diagnostico.append(i) # Se añade a diagnostico las posibles hipótesis, es decir el conjunto diferencial
            
            while len(self.diagnostico) > 0 and len(self.observables) > 0:
                # AUNQUE ES UNA TAREA QUE SE PUEDE HACER SEGÚN LA PLANTILLA DE TEORÍA
                # PARA ESTA FORMA DE IMPLEMENTAR EL ALGORITMO NO ES NECESARIA
                hipotesisSeleccionada = Seleccionar(self.diagnostico).execute() # Seleccionamos una de las posibles hipotesis
            
                if tr: # Para ver el proceso por terminal
                    print ("Observables:", self.observables)
                    print ("=========================")
            
                # Ahora vamos a especificar un observable
                observable = Especificar().execute(self.observables, self.observablesVistos) # Especificamos para obtener el observable

                # Ahora vamos a obtener un hallazgo de ese observable
                hallazgo = Obtener().execute(observable)
                
                if hallazgo not in self.evidencias:
                    self.evidencias.append(hallazgo) # Añadimos el hallazgo a la lista de evidencias.
                
                # Ahora vamos a realizar la verificacion
                for i in self.diferencial:
                    if i in self.diagnostico:
                        self.explicacion += u'\n Probamos la  hipotesis de ' + str(i.nombre) + '\n'
                        
                        verifica = Verificar(self.evidencias, i, self.fallos).execute() # Aqui el verificar recibe la lista de evidencias u hallazgos y la posible hipótesis de solución
            
                        if verifica[0] is False: # Si la hipotesis no es posible se elimina del conjunto diferencial
                            if tr:
                                print ("Verificacion completada. No puede ser, por lo tanto se borra la hipotesis\n")
                                
                            self.explicacion += verifica[1]
                                
                            if self.diagnosticoEncontrado.count(i.nombre) != 0:
                                self.diagnosticoEncontrado.remove(i.nombre)
                            if i in self.diagnostico:
                                self.diagnostico.remove(i) # Vamos eliminando aquellas hipotesis que sean falsas
                        # Si verificar es falso para esa hipotesis, esta será eliminada del conjunto diagnostico que contendrá la solucion final(averia) o soluciones
                        else:
                            if tr:
                                print ("Verificacion completada. Si puede ser, por lo tanto se mantiene la hipotesis\n")
                            
                            if self.diagnosticoEncontrado.count(i.nombre) == 0:
                                self.diagnosticoEncontrado.append(i.nombre)
                                
                            self.explicacion += verifica[1]
                            
                self.observables.pop(0)
                
            return self.explicacion, self.diferencial, self.diagnosticoEncontrado

'''
Clase base para las inferencias
'''
class Inferencia():
    
    def __init__(self):
        
        pass
    
    def execute(self, tr = False):
        
        pass

'''
Clase para la inferencia de cubrir
'''
class Cubrir(Inferencia):
    
    # Se le pasa una lista de fallos y proporciona una lista de posibles hipotesis
    def __init__(self, fallos):
        
        super().__init__()
        self.fallos = fallos
        self.listaHipotesis = []
        
    def execute(self, tr = False):
        
        hipotesis = bc.getHipotesis()
        
        for h in hipotesis:
            for i in h.fallos:
                for f in self.fallos:
                    if i.nombre == f:
                        if not h in self.listaHipotesis:
                            self.listaHipotesis.append(h)
      
        # Para ver el proceso por terminal
        if tr:
            print ("Hipotesis posibles:", [h.nombre for h in self.listaHipotesis])
            print ("=========================")
        
        hipotesis = self.listaHipotesis
        return hipotesis

'''
Clase para la inferencia de seleccionar
'''        
class Seleccionar(Inferencia):
    
    # Selecciona una hipotesis del conjunto diferencial
    def __init__(self, conjuntoDiferencial):
        
        super().__init__()
        self.conjuntoDiferencial = conjuntoDiferencial
        
    def execute(self, tr = False):
        
        hipotesis = None
        
        if len(self.conjuntoDiferencial) > 0:
            hipotesis = self.conjuntoDiferencial[0]
            
            # Para ver el proceso por terminal
            if tr:
                print ("Hipotesis seleccionada:", hipotesis.nombre)
                print ("=========================")
        
        return hipotesis
 
'''
Clase para la inferencia de especificar
'''           
class Especificar(Inferencia):
    
    # Crea el observable
    def __init__(self):
        
        super().__init__()        
        
    def execute(self, listaObservables, listaObservablesVistos, tr = False):  
                
        observable = bc.creaObservable(listaObservables[0]) # lObservables es la lista actual de observables con los valores que tienen marcados por el usuario
        listaObservablesVistos.append(listaObservables[0])
        
        # Para ver el proceso por terminal
        if tr:
            print ("Observable seleccionado:", observable.nombre)
            print ("=========================")
        
        return observable

'''
Clase para la inferencia de obtener
'''    
class Obtener(Inferencia):
    
    # Se le pasa un observable y se obtiene un hallazgo (el valor de ese observable) 
    def __init__(self):
        
        super().__init__()
        
    def execute(self, observable, tr = False):
        
        hallazgo = Hallazgo(observable.nombre, observable.valor)
        
        # Para ver el proceso por terminal
        if tr:
            print ("Hallazgo:", observable.nombre, observable.valor)
            print ("=========================")
        
        return hallazgo

'''
Clase para la inferencia de verificar
'''    
class Verificar(Inferencia):
    
    # Verifica si una hipotesis de averia es compatible con un conjuto de hallazgos y fallos
    def __init__(self, lHallazgos, hipotesis, fallos):
        
        super().__init__()
        self.hallazgos = lHallazgos
        self.hipotesis = hipotesis
        self.fallos = fallos
        self.explicacion = ''
        
    def execute(self, tr = False):
        
        resultado = True
        
        # Para ver el proceso por terminal
        if tr:
            print ("Verificando la hipotesis:", self.hipotesis.nombre)
            print ("=========================")
            
        for f in self.hipotesis.fallos:
            if tr:
                print ("Debe presentar:", f.nombre, f.valor)
                
            if f.nombre in self.fallos:
                self.explicacion += u'    (+) Puede ser [' + str(self.hipotesis.nombre)
                self.explicacion += '] porque presenta el fallo ['
                self.explicacion += str(f.nombre) + '] con valor ' + str(f.valor) + '.\n'
            else:
                self.explicacion += u'    (-) No puede ser ['
                self.explicacion += str(self.hipotesis.nombre)
                self.explicacion += u'] porque deberia presentar el fallo ['
                self.explicacion += str(f.nombre) + '] con valor apropiado.\n'
                resultado = False
            
            if resultado == False:
                return (False, self.explicacion)

        for fh in self.hipotesis.debePresentar:
            if tr:
                print ("Debe presentar:", fh.nombre, fh.valor, "=>", [(f.nombre, f.valor) for f in self.hallazgos])
                
            if not (fh.nombre in [f.nombre for f in self.hallazgos]):
                pass
            else:
             # El nombre del fallo de la hipótesis está. Comprobamos que los valores de dicho fallo coincidan
                falla = False # Flag
                 
                for e in self.hallazgos:
                    if e.nombre == fh.nombre: # Comprueba que coincide en valores
                        if isinstance(fh.valor, list): # Si el valor del fallo de la hipótesis es de tipo lista
                            if not e.valor in fh.valor: # Comprueba que el valor del fallo presentado está en esa lista
                                falla = True # El valor del fallo presentado no está en la lista
                                break
                        else: # El valor del fallo de la hipótesis no es de tipo lista
                            if not e.valor == fh.valor: # Si no coincide los valores falla
                                falla = True # El valor del fallo presentado no está en la lista
                                break
                        
                if falla: # Si falla quiere decir que el valor no coincide
                    self.explicacion += u'    (-) No puede ser ['
                    self.explicacion += str(self.hipotesis.nombre)
                    self.explicacion += u'] porque deberia presentar el observable ['
                    self.explicacion += str(fh.nombre) + '] con valor apropiado.\n'
                    resultado = False
                     
            if resultado == False: # Si ha resultado fallida la verificación salimos de la verificación.
                return (False, self.explicacion)
            else:
                self.explicacion += u'    (+) Puede ser [' + str(self.hipotesis.nombre)
                self.explicacion += '] porque presenta el observable ['
                self.explicacion += str(fh.nombre) + '] con valor ' + str(fh.valor) + '.\n'
                 
        # Eliminar aquellas hipotesis que tenga algun fallo en no debe tener
        for f in self.hipotesis.noPuedePresentar:
            falla = False # Flag
            
            for e in self.hallazgos:
                if e.nombre == f.nombre: # Comprueba que coincide en valores
                    if isinstance(f.valor, list): # Si el valor del fallo de la hipótesis es de tipo lista
                        if e.valor in f.valor: # Comprueba que el valor del fallo presentado está en esa lista
                            falla = True # El valor del fallo presentado no está en la lista
                            break
                    else: # El valor del fallo de la hipótesis no es de tipo lista
                        if e.valor == f.valor: # Si no coincide los valores falla
                            falla = True # El valor del fallo presentado no está en la lista
                            break
                        
            if falla: #Si falla quiere decir que el valor no coincide
                self.explicacion += u'    (-) No puede ser ['
                self.explicacion += str(self.hipotesis.nombre)
                self.explicacion += u'] porque no puede presentar el observable ['
                self.explicacion += f.nombre + '] con valor '
                self.explicacion += str(f.valor) + '\n'
                resultado = False
            else:
                self.explicacion += u'    (+) Puede ser ['
                self.explicacion += str(self.hipotesis.nombre)
                self.explicacion += u'] porque no presenta el observable ['
                self.explicacion += f.nombre + '] con valor '
                self.explicacion += str(f.valor) + '\n'
                
            if resultado == False:
                return (False, self.explicacion)
            
        return (True, self.explicacion)

'''
Método utilizado para obtener los observables de la base de conocimientos activa
'''
def getObservables():
    
    if bc == None:
        return []
    
    return bc.getObservables()

'''
Método utilizado para obtener los fallos de la base de conocimientos activa
'''
def getFallos():
    
    if bc == None:
        return []
    
    return bc.getFallos()

'''
Método utilizado para cargar un dominio
'''
def cargarDominio(dominio):
    
    global bc
    # Permite importar un módulo dinámicamente durante tiempo de ejecución
    bc = import_module("dominios." + dominio)