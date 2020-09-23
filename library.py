# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 19:44:47 2020

@author: dkmau
"""

def vetor10():
    vetor = []
    while len(vetor) <= 9:
        number = input("Insira um número: ")
        if number.isnumeric(): vetor.append(number)
        else: print("Você não inseriu um número!")
    print(vetor)
    
    