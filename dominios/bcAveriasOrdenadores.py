# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 16:23:37 2021

@author: ChrisLe
"""

from bcGenerica import Observable, Hipotesis

#Observables
class PitidosLargos(Observable):
    
    def __init__(self, valor = None):
        
        nombre = 'Pitidos Largos'
        tipo = 'multiple'
        valoresPermitidos = ['0', '1', '2', '3']
        super().__init__(nombre, tipo, valoresPermitidos, valor)
        self.ayuda = '''El ordenador realiza x número de pitidos largos'''
        
        
class PitidosCortos(Observable):
    
    def __init__(self, valor = None):
        
        nombre = 'Pitidos Cortos'
        tipo = 'multiple'
        valoresPermitidos = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
        super().__init__(nombre, tipo, valoresPermitidos, valor)
        self.ayuda = '''El ordenador realiza x número de pitidos cortos'''

class PitidosConstantes(Observable):
    
    def __init__(self, valor = None):

        nombre = 'Pitidos Constantes'
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
class NoEnciende(Observable):
    
    def __init__(self, valor = None):
        
        nombre = 'No enciende'
        tipo = 'boleano'
        valoresPermitidos = None
        super().__init__(nombre, tipo, valoresPermitidos, valor)
        self.ayuda = '''El ordenador no se enciende'''
    
class NoDaVideo(Observable):
    
    def __init__(self, valor = None):
        
        nombre = 'No da vídeo'
        tipo = 'boleano'
        valoresPermitidos = None
        super().__init__(nombre, tipo, valoresPermitidos, valor)
        self.ayuda = '''El ordenador no da vídeo'''
        
class SeApaga(Observable):
    
    def __init__(self, valor = None):
        
        nombre = 'Se apaga'
        tipo = 'boleano'
        valoresPermitidos = None
        super().__init__(nombre, tipo, valoresPermitidos, valor)
        self.ayuda = '''El ordenador se apaga'''
        
class NoFuncionaTeclado(Observable):
    
    def __init__(self, valor = None):
        
        nombre = 'No funciona teclado'
        tipo = 'boleano'
        valoresPermitidos = None
        super().__init__(nombre, tipo, valoresPermitidos, valor)
        self.ayuda = '''El teclado del ordenador no funciona'''
        
class NoDaAudio(Observable):
    
    def __init__(self, valor = None):
        
        nombre = 'No da audio'
        tipo = 'boleano'
        valoresPermitidos = None
        super().__init__(nombre, tipo, valoresPermitidos, valor)
        self.ayuda = '''El ordenador da audio'''

class SeSobrecalienta(Observable):
    
    def __init__(self, valor = None):
        
        nombre = 'Se sobrecalienta'
        tipo = 'boleano'
        valoresPermitidos = None
        super().__init__(nombre, tipo, valoresPermitidos, valor)
        self.ayuda = '''El procesador se sobrecalienta'''        

def getFallos():
    
    '''
    Devuelve la lista de fallos de la BC
    '''
    fallos = []
    fallos.append(NoEnciende())
    fallos.append(NoDaVideo())
    fallos.append(SeApaga())
    fallos.append(NoFuncionaTeclado())
    fallos.append(NoDaAudio())
    fallos.append(SeSobrecalienta())

    return fallos


#Hipotesis
class FalloRAM(Hipotesis):
    
    def __init__(self):
        
        super().__init__(nombre = 'Falla la RAM')
        #Creamos instancias de observables
        
        f1 = NoEnciende(True)

        o1 = PitidosCortos(['1', '2', '4'])
        o2 = PitidosLargos(['0'])
        
        o3 = PitidosCortos(['3', '5', '6', '7', '8', '9', '10', '11', '12'])
        o4 = PitidosLargos(['1', '2', '3'])
        o5 = PitidosConstantes(True)
        
        self.fallos = [f1]
        self.debePresentar = [o1, o2]
        self.noPuedePresentar = [o3, o4, o5]
        self.ayuda = u'Falla la RAM'
        
class Fallo64KbRAM(Hipotesis):
    
    def __init__(self):
        
        super().__init__(nombre = 'Fallan los primeros 64Kb RAM')
        #Creamos instancias de observables
        
        f1 = NoEnciende(True)

        o1 = PitidosCortos(['3'])
        o2 = PitidosLargos(['0', '1'])
        
        o3 = PitidosCortos(['0', '1', '2', '4', '5', '6', '7', '8', '9', '10', '11', '12'])
        o4 = PitidosLargos(['2', '3'])
        o5 = PitidosConstantes(True)
        
        self.fallos = [f1]
        self.debePresentar = [o1, o2]
        self.noPuedePresentar = [o3, o4, o5]
        self.ayuda = u'Fallan los primeros 64Kb RAM'

def getHipotesis():
    
    '''
    Devuelve la lista de hipotesis de la BC
    '''
    hipotesis = []
    hipotesis.append(FalloRAM())
    hipotesis.append(Fallo64KbRAM())
    
    return hipotesis

def creaObservable(tp):
    
    '''Crea una instancia de un observable si la tupla coincide con la base de conocimiento. 
    Si el observable es correcto devuelve una instancia del observable. Iremos comprobando los observables
    de la lista de observables con sus valores actualizados, y cuando coincida el observable con su
    correspondiente se creará ese observable'''
        
    if tp[0] == 'Pitidos Cortos':
        ob = PitidosCortos(tp[1])
        if tp[1] in ob.valoresPermitidos:
            ob.valor = tp[1]
            return ob
        else:
            print ('no esta presente')
    
    elif tp[0] == 'Pitidos Largos':
        ob = PitidosLargos(tp[1])
        if tp[1] in ob.valoresPermitidos:
            ob.valor = tp[1]
            return ob
        else:
            print ('no esta presente')

    elif tp[0] == 'Pitidos Constantes':
        ob = PitidosConstantes(tp[1])
        if tp[1] == 'True':
            ob.valor = True
        else:
            ob.valor = False
        return ob
    
    return None