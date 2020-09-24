# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 19:44:47 2020

@author: dkmau
"""
import random

def vetor10():
    vetor = []
    while len(vetor) <= 9:
        number = input("Insira um número: ")
        if number.isnumeric(): vetor.append(number)
        else: print("Você não inseriu um número!")
    print(vetor)
    
def matrix10x10():
    # Aqui criamos a Matriz
    rangeX = 10
    rangeY = 10
    matrix = [[random.randint(0,100) for x in range(rangeX)] for y in range(rangeY)]
    # Matriz criada e preenchida com numeros aleatórios de 0 a 100
    
    print(matrix)
    
def simpleStack():
    stack = []
    while len(stack) <= 9:
        number = input("Insira um numero: ")
        if number.isnumeric() : stack.append(number)
        else: print("Insira somente numeros!") 
    print("Pilha preenchida! removendo itens ... \n")
    while len(stack) > 0:
        print("Removendo: ", stack.pop())
        print("Pilha: ", stack, "\n")
    if len(stack) == 0 : print("Pilha vazia!")
    else: print("Algo deu errado!")
    
def simpleQueue():
    queue = []
    while len(queue) <= 9:
        number = input("Insira um numero: ")
        if number.isnumeric() : queue.insert(0,number)
        else: print("Insira somente numeros!") 
    print("Fila preenchida! removendo itens ... \n")
    while len(queue) > 0:
        print("Removendo: ", queue.pop())
        print("Fila: ", queue, "\n")
    if len(queue) == 0 : print("Fila vazia!")
    else: print("Algo deu errado!")
    
simpleQueue()