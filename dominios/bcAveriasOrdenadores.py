# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 16:23:37 2021

@author: ChrisLe
"""

from bcGenerica import Observable, Hipotesis

#Observables
class PitidosLargos(Observable):
    
    def __init__(self, valor = None):
        
        nombre = 'Número de Pitidos Largos'
        tipo = 'multiple'
        valoresPermitidos = ['1', '2', '3']
        super().__init__(nombre, tipo, valoresPermitidos, valor)
        self.ayuda = '''El ordenador realiza x número de pitidos largos'''
        
        
class PitidosCortos(Observable):
    
    def __init__(self, valor = None):
        
        nombre = 'Número de Pitidos Cortos'
        tipo = 'multiple'
        valoresPermitidos = ['1', '2', '3', '4', '5','6','7','8', '9', '10', '11' , '12']
        super().__init__(nombre, tipo, valoresPermitidos, valor)
        self.ayuda = '''El ordenador realiza x número de pitidos cortos'''

class PitidosConstantes(Observable):
    
    def __init__(self, valor = None):

        nombre = 'Realiza pitidos constantes'
        tipo = 'boleano'
        valoresPermitidos = None
        super().__init__(nombre, tipo, valoresPermitidos, valor)
        self.ayuda = '''El ordenador realiza pitidos constantemente'''
        
        
def getObservables():
    
    '''
    Devuelve la lista de observables de la BC
    '''
    obs = []
    obs.append(PitidosLargos())
    obs.append(PitidosCortos())
    obs.append(PitidosConstantes())
    
    return obs

#Fallos

        
        
def getFallos():
    
    '''
    Devuelve la lista de fallos de la BC
    '''
    fallos = []

    return fallos


#Hipotesis

def getHipotesis():
    
    '''
    Devuelve la lista de hipotesis de la BC
    '''
    hipotesis = []
    
    
    return hipotesis