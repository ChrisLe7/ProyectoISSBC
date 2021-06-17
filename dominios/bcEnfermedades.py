# -*- coding: utf-8 -*-
"""
Created on Thu May  6 13:52:00 2021

@author: Ángel
"""

from bcGenerica import Observable, Hipotesis

#Observables
class Escalofrios(Observable):
    
    def __init__(self, valor = None):
        
        nombre = 'Tiene escalofrios'
        tipo = 'boleano'
        valoresPermitidos = None
        super().__init__(nombre, tipo, valoresPermitidos, valor)
        self.ayuda = '''El paciente tiene escalofrios'''
        
class DolorCabeza(Observable):
    
    def __init__(self, valor = None):
        
        nombre = 'Tiene dolor de cabeza'
        tipo = 'multiple'
        valoresPermitidos = ['Nada', 'Leve', 'Moderado', 'Severo']
        super().__init__(nombre, tipo, valoresPermitidos, valor)
        self.ayuda = '''El paciente tiene dolor de cabeza'''

class DolorGarganta(Observable):
    
    def __init__(self, valor = None):
        
        nombre = 'Tiene dolor de garganta'
        tipo = 'multiple'
        valoresPermitidos = ['Nada', 'Leve', 'Moderado', 'Severo']
        super().__init__(nombre, tipo, valoresPermitidos, valor)
        self.ayuda = '''El paciente tiene dolor de garganta'''
        
class Fiebre(Observable):
    
    def __init__(self, valor = None):

        nombre = 'Tiene fiebre'
        tipo = 'boleano'
        valoresPermitidos = None
        super().__init__(nombre, tipo, valoresPermitidos, valor)
        self.ayuda = '''El paciente tiene fiebre'''

class Nauseas(Observable):
    
    def __init__(self, valor = None):
        
        nombre = 'Tiene nauseas'
        tipo = 'boleano'
        valoresPermitidos = None
        super().__init__(nombre, tipo, valoresPermitidos, valor)
        self.ayuda = '''El paciente tiene nauseas'''

class DolorAbdominal(Observable): 
    
    def __init__(self, valor = None):
        
        nombre = 'Tiene dolor abdominal'
        tipo = 'boleano'
        valoresPermitidos = None
        super().__init__(nombre, tipo, valoresPermitidos, valor)
        self.ayuda = '''El paciente tiene dolor abdominal'''

def getObservables():
    
    '''
    Devuelve la lista de observables de la BC
    '''
    obs = []
    obs.append(Escalofrios())
    obs.append(DolorCabeza())
    obs.append(DolorGarganta())
    obs.append(Fiebre())
    obs.append(Nauseas())
    obs.append(DolorAbdominal())
    
    return obs

#Fallos
class Estornudos(Observable):
    
    def __init__(self, valor = None):
        
        nombre = 'Estornuda a menudo'
        tipo = 'boleano'
        valoresPermitidos = None
        super().__init__(nombre, tipo, valoresPermitidos, valor)
        self.ayuda = '''El paciente estornuda a menudo'''
        
class CongestionNasal(Observable):
    
    def __init__(self, valor = None):
        
        nombre = 'Tiene congestion nasal'
        tipo = 'boleano'
        valoresPermitidos = None
        super().__init__(nombre, tipo, valoresPermitidos, valor)
        self.ayuda = '''El paciente presenta congestion nasal'''
        
class Tos(Observable):
    
    def __init__(self, valor = None):
        
        nombre = 'Tose'
        tipo = 'boleano'
        valoresPermitidos = None
        super().__init__(nombre, tipo, valoresPermitidos, valor)
        self.ayuda = '''El paciente tiene tos'''
        
class Diarrea(Observable):
    
    def __init__(self, valor = None):
        
        nombre = 'Tiene diarrea'
        tipo = 'boleano'
        valoresPermitidos = None
        super().__init__(nombre, tipo, valoresPermitidos, valor)
        self.ayuda = '''El paciente tiene diarrea'''
        
class Vomitos(Observable): 
    
    def __init__(self, valor = None):
        
        nombre = 'Tiene vomitos'
        tipo = 'boleano'
        valoresPermitidos = None
        super().__init__(nombre, tipo, valoresPermitidos, valor)
        self.ayuda = '''El paciente vomita'''

def getFallos():
    
    '''
    Devuelve la lista de fallos de la BC
    '''
    fallos = []
    fallos.append(Estornudos())
    fallos.append(CongestionNasal())
    fallos.append(Tos())
    fallos.append(Diarrea())
    fallos.append(Vomitos())
    
    return fallos

#Hipotesis
class Resfriado(Hipotesis):
    
    def __init__(self):
        
        super().__init__(nombre = 'Esta resfriado')
        #Creamos instancias de observables
        
        f1=CongestionNasal(True)
        f2=Estornudos(True)
        
        o1=DolorCabeza(['Leve', 'Moderado'])
        o3=DolorGarganta(['Moderado'])

        self.fallos = [f1, f2]
        self.debePresentar = [o1]
        self.noPuedePresentar = [o3]
        self.ayuda = u'Esta resfriado'

class Gripe(Hipotesis):
    
    def __init__(self):
        
        super().__init__(nombre = 'Tiene gripe')
        #Creamos instancias de observables
        
        f1=Tos(True)             
        
        o1=Escalofrios(True)
        o2=Fiebre(True)

        o7=Vomitos(True)
        o8=Diarrea(True)        
        
        self.fallos = [f1]
        self.debePresentar = [o1, o2]
        self.noPuedePresentar = [o7, o8]
        self.ayuda = u'Tiene gripe'

class Gastroenteritis(Hipotesis):
    
    def __init__(self):
        
        super().__init__(nombre = 'Tiene gastroenteritis')
        #Creamos instancias de observables
        
        f1=Vomitos(True)
        f2=Diarrea(True)
        
        o1=Nauseas(True)
        o2=DolorAbdominal(True)
        o3=Estornudos(True)

        self.fallos = [f1, f2]
        self.debePresentar = [o1, o2]
        self.noPuedePresentar = [o3]
        self.ayuda = u'Tiene gastroenteritis'
        
def getHipotesis():
    
    '''
    Devuelve la lista de hipotesis de la BC
    '''
    hipotesis = []
    
    hipotesis.append(Resfriado())
    hipotesis.append(Gripe())
    hipotesis.append(Gastroenteritis())
    
    return hipotesis

def creaObservable(tp):
    
    '''Crea una instancia de un observable si la tupla coincide con la base de conocimiento. 
    Si el observable es correcto devuelve una instancia del observable. Iremos comprobando los observables
    de la lista de observables con sus valores actualizados, y cuando coincida el observable con su
    correspondiente se creará ese observable'''
    
    if tp[0] == 'Tiene estornudos':
        ob = Estornudos(tp[1])
        if tp[1] == 'True':
            ob.valor = True
        else:
            ob.valor = False
        return ob
    
    elif tp[0] == 'Tiene congestion nasal':
        ob = CongestionNasal(tp[1])
        if tp[1] == 'True':
            ob.valor = True
        else:
            ob.valor = False
        return ob

    elif tp[0] == 'Tiene tos':
        ob = Tos(tp[1])
        if tp[1] == 'True':
            ob.valor = True
        else:
            ob.valor = False
        return ob
        
    elif tp[0] == 'Tiene escalofrios':
        ob = Escalofrios(tp[1])
        if tp[1] == 'True':
            ob.valor = True
        else:
            ob.valor = False
        return ob

    elif tp[0] == 'Tiene dolor de cabeza':
        ob = DolorCabeza(tp[1])
        if tp[1] in ob.valoresPermitidos:
            ob.valor = tp[1]
            return ob
        else:
            print ('no esta presente')
        
    elif tp[0] == 'Tiene dolor de garganta':
        ob = DolorGarganta(tp[1])
        if tp[1] in ob.valoresPermitidos:
            ob.valor = tp[1]
            return ob
        else:
            print ('no esta presente')
                
    elif tp[0] == 'Tiene fiebre':
        ob = Fiebre(tp[1])
        if tp[1] == 'True':
            ob.valor = True
        else:
            ob.valor = False
        return ob
            
    elif tp[0] == 'Tiene diarrea':
        ob = Diarrea(tp[1])
        if tp[1] == 'True':
            ob.valor = True
        else:
            ob.valor = False
        return ob
        
    elif tp[0] == 'Tiene nauseas':
        ob = Nauseas(tp[1])
        if tp[1] == 'True':
            ob.valor = True
        else:
            ob.valor = False
        return ob
        
    elif tp[0] == 'Tiene dolor abdominal':
        ob = DolorAbdominal(tp[1])
        if tp[1] == 'True':
            ob.valor = True
        else:
            ob.valor = False
        return ob

    elif tp[0] == 'Tiene vomitos':
        ob = Vomitos(tp[1])
        if tp[1] == 'True':
            ob.valor = True
        else:
            ob.valor = False
        return ob           
    
    return None