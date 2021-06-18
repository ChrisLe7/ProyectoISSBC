# -*- coding: utf-8 -*-
"""
Created on Wed May  5 13:53:31 2021

@author: Ángel Fuentes (i82fuala) Christian Luna (i82luesc)
"""

import modeloAplicacion as modelo
    
'''
Método utilizado para diagnosticar (llamar al método de cobertura causal)
'''
def eventoDiagnosticar(fallos, observables):
    
    metodo = modelo.MetodoCoberturaCausal(fallos, observables)
    return metodo.execute()
    
'''
Método utilizado para obtener los observables de la base de conocimientos activa
'''
def getObservables():
    
    return modelo.getObservables()

'''
Método utilizado para obtener los fallos de la base de conocimientos activa
'''
def getFallos():
    
    return modelo.getFallos()

'''
Método utilizado para cargar un dominio
'''
def cargarDominio(dominio):
    
    modelo.cargarDominio(dominio)