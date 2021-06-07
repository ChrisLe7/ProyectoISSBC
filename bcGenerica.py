# -*- coding: utf-8 -*-
"""
Created on Wed May  5 12:36:20 2021

@author: Ángel
"""

class Observable(object):
    
    """Definicion generica de una observable"""
    def __init__(self, nombre = None, tipo = None, valoresPermitidos = None, valor = None):
        
        self.nombre = nombre
        self.valor = valor
        self.tipo = tipo
        self.valoresPermitidos = valoresPermitidos

class Hallazgo():
    
    """Definicion generica de un hallazgo"""
    def __init__(self, nombre = None, valor = None):
        
        self.nombre = nombre
        self.valor = valor
        
    def getNombre(self):
        
        return self.nombre
        
    def getValor(self):
        
        return self.valor
    
class Hipotesis():
    
    """Definicion generica de una hipotesis"""
    def __init__(self, nombre):
        
        self.nombre = nombre
        self.ayuda = u''