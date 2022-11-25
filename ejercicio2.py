from csv import reader

from ejercicio1 import insertar

class arbol:
    def __init__(self,informacion):
        self.informacion = informacion
        self.derecha = None
        self.izquierda = None
    
    def insertar(raiz,dato):
        if raiz == None:
            raiz = arbol(dato)
        elif dato < raiz.info:
            raiz.izquierda = insertar(raiz.izquierda, dato)
        else:
            raiz.derecha = insertar(raiz.derecha, dato)
        return raiz
    def buscar(self,nodo,busqueda):
        if nodo is None:
            return None
        if nodo.dato == busqueda:
            return nodo
        if busqueda < nodo.dato:
            return self.buscar(nodo.izquierda, busqueda)
        else:
            return self.buscar(nodo.derecha, busqueda)
        
    
    
                