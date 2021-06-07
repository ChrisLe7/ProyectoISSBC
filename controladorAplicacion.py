# -*- coding: utf-8 -*-
"""
Created on Wed May  5 13:53:31 2021

@author: Ángel
"""

import modeloAplicacion as modelo
    
"""Método utilizado para diagnosticar (llamar al método de cobertura causal)"""    
def eventoDiagnosticar(fallos):
    
    metodo = modelo.MetodoCoberturaCausal(fallos)
    return metodo.execute()