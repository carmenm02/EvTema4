import heapq
from multiprocessing.connection import deliver_challenge
from turtle import right
from heapq import heappop,heappush

from sympy import root

def isLeaf(root):
    return root.izquierda is None and root.derecha is None

class arbol:
    def __init__(self,frecuencia,simbolo) :
        self.frecuencia = frecuencia
        self.simbolo = simbolo
        self.derecha = None
        self.izquierda = None
        self.padre = None

def ordenar(lista):
    lista = sorted(lista,key=lambda x: x.simbolo)
    lista = sorted(lista, key=lambda x: x.frecuencia)
    return lista

def insertar(lista,nodo):
    for i in range(len(lista)):
        if lista[i].frecuencia > nodo.frecuencia:
            lista.insert(i,nodo)
            break
        if i == len(lista)-1:
            lista.append(nodo)
            break
    return lista

def HuffmanTree(simbolos,frecuencias):
    nodos = []
    for i in range(len(simbolos)):
        nodos.append(arbol(simbolos[i],frecuencias[i]))
    nodos = ordenar(nodos)
    while len(nodos)>1:
        nodo = arbol('XX', nodos[0].frecuencia + nodos[1].frecuencia)
        nodo.izquierda = nodos[0]
        nodo.izquierda.padre = nodo
        nodo.derecha = nodos[1]
        nodo.derecha.padre = nodo
        nodos = insertar(nodos,nodo)
        nodos.pop(1)
        nodos.pop(0)
    return nodos[0] 

def encode(root, s, huffman_code):
    if root is None:
        return

    if isLeaf(root):
        huffman_code[root.ch] = s if len(s) > o else '1'

    encode(root.izquierda, s + '0', huffman_code)
    encode(root.derecha, s + '1', huffman_code)

def decode(root,index, s):
    if root is None:
        return index
    if isLeaf(root):
        print(root.ch, end='')
        return index

    index = index + 1
    root = root.left if s[index] == '0' else root.right
    return decode(root, index, s)