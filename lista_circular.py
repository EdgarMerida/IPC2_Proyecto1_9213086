from nodop import *

class lista_circular():
    def __init__(self):
        self.inicio = None
        self.fin = None

    def vacia(self):
        return self.inicio == None

    def agregar_inicio(self, id, nombre, row, col):
        if self.vacia():
            self.inicio = self.fin = NodoP(id, nombre, row, col)
            self.fin.siguiente = self.inicio
        else:
            aux = NodoP(id, nombre, row, col)
            aux.siguiente = self.inicio
            self.inicio = aux
            self.inicio.siguiente = self.inicio

    def agregar_fin(self, id, nombre, row, col):
        if self.vacia():
            self.inicio = self.fin = NodoP(id, nombre, row, col)
            self.fin.siguiente = self.inicio
        else:
            aux = self.fin
            self.fin = aux.siguiente = NodoP(id, nombre, row, col)
            self.fin.siguiente = self.inicio
    
    def recorrerlc(self):
        aux = self.inicio
        while aux:
            print(aux.id, aux.nombre, aux.row, aux.col)
            aux = aux.siguiente
            if aux == self.inicio:
                break
"""
quitar
        while aux.siguiente != self.inicio:
            print(aux.id, aux.nombre, aux.row, aux.col)
            aux = aux.siguiente
        print(aux.id, aux.nombre, aux.row, aux.col)

sustituir por 


quitar
        while aux.siguiente != self.inicio:
            print(aux.dato)
            aux = aux.siguiente
        print(aux.dato)

sustutuir por 
        while aux:
            print(aux.dato)
            aux = aux.siguiente
            if aux == self.inicio:
                break
"""

