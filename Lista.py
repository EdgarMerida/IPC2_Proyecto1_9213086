from Nodo import *

class lista:
    def __init__(self):
        self.inicio = None
        self.fin = None

    def insertar(self, id, row, col, dato):
        if self.inicio == None:
            self.inicio = NodoD(id, row, col, dato)
            self.fin = self.inicio
        else:
            nuevo = NodoD(id, row, col, dato)
            self.fin.setSiguiente(nuevo)
            self.fin = nuevo

    def recorrer(self):
        if self.inicio != None:
            aux = self.inicio
            while aux != None:
                print(int(aux.getId()), int(aux.getRow()), int(aux.getCol()),int(aux.dato))
                aux = aux.getSiguiente()
    
    def modificar(self, id, nombre):
        if self.inicio != None:
            aux = self.inicio
            while aux != None:
                if aux.getId() == id:
                    aux.setNombre(nombre)
                    break
                aux = aux.getSiguiente()

    def eliminar(self, id):
        if self.inicio != None:
            if self.inicio.getId() == id and self.inicio.getSiguiente() == None:
                self.inicio = None
                self.fin = None
            elif self.inicio.getId() == id:
                self.inicio = self.inicio.getSiguiente()
            else:
                aux = self.inicio
                aux2 = None
                while aux != None:
                    if aux.getId() == id and aux != self.fin:
                        aux2.setSiguiente(aux.getSiguiente)
                    elif aux.getId() == id:
                        aux2.setSiguiente(None)
                        self.fin = aux2
                    aux2 = aux
                    aux = aux.getSiguiente()

