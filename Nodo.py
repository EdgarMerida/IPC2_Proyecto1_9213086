class NodoD:
    def __init__(self, id, row, col, dato):
        self.id = id
        self.row = row
        self.col = col
        self.dato = dato
        self.siguiente = None

    def getId(self):
        return self.id

    def setId(self, id):
        self.id = id

    def getRow(self):
        return self.row

    def setRow(self, row):
        self.row = row

    def getCol(self):
        return self.col

    def setCol(self, col):
        self.col = col

    def getDato(self):
        return self.dato

    def setDato(self, dato):
        self.dato = dato

    def getSiguiente(self):
        return self.siguiente

    def setSiguiente(self, siguiente):
        self.siguiente = siguiente