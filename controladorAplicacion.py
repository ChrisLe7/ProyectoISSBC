# -*- coding: utf-8 -*-
"""
Created on Wed May  5 13:53:31 2021

@author: Ángel
"""

import modeloAplicacion as modelo

"""TEMPORAL PARA PRUEBAS"""
import modelos.bcEnfermedades as bc
    
"""Método utilizado para diagnosticar (llamar al método de cobertura causal)"""    
def eventoDiagnosticar(fallos, observables):
    
    metodo = modelo.MetodoCoberturaCausal(fallos, observables)
    return metodo.execute(True)
    
def getObservables():
    
    return bc.getObservables()

def getFallos():
    
    return bc.getFallos()

def getPosiblesHipotesis():
    
    return bc.getHipotesis()