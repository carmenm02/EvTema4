import heapq


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

def HuffmanTree(text):
    if len(text) == 0:
        return
    
    frecuencia = {i: text.count(i) for i in set(text)}

    pq = [arbol(k,v) for k, v in frecuencia.items()]
    heapq.heapify(pq)

    