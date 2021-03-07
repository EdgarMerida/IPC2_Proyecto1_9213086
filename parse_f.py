import xml.etree.ElementTree as ET
from lista_circular import lista_circular
from Lista import lista


lc = lista_circular()
l = lista()
ind = 0
error = 0
tree = ET.parse('Ejemplo1.xml')
root = tree.getroot()
print(root.tag, root.attrib, root.text)
print('')
"""
x = n = row,  y = m = col

"""
for mat in root:
    atributo = mat.attrib
    x_f = int(atributo['n'])
    y_c = int(atributo['m'])
    cardinal = x_f*y_c
    if cardinal != len(mat):
        error += 1
        print(f"la matriz '{atributo['nombre']}' es de cardinalidad incorrecta, el(los) errore(s) encontrado(s) número {error}")
    else:
        lc.agregar_fin(ind, atributo['nombre'], atributo['n'], atributo['m'])
        for row in mat:
            atributoM = row.attrib            
            l.insertar(ind, int(atributoM['x']), int(atributoM['y']), int(row.text))
    for i in range(x_f):
        for j in range(y_c):
            l.ordenar(i,j)


#lc.recorrerlc()
l.recorrer()
#l.buscar(3,1)

#l.recorrer()
