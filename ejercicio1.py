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
