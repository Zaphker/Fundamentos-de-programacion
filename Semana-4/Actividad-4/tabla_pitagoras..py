# Nombre: Héctor Martínez Santiago
# Matricula: AL07289823
# Proposito: La intención final del programa es imprimir una tabla de pitogaras fija imprimiendo solamente los valores sin comas ni corchetes
#            Hacer posible el imprimir deseado al accedes a la fila y columna de la tabla para la multiplicación total de los valores ingresados





tabla = []

for r in range(1, 11): # r por renglón
    fila = []
    for c in range(1, 11): #c por columna
        valor = 0 
        for s in range(c): #s por suma dentro del rango columna
            valor += r # el valor controlado por el renglon para delimitar la tabla 
        fila.append(valor)
    tabla.append(fila)

def imprimir_tabla(tabla):
    for fila in tabla: # recorre la tabla definiada anteriormente 
        for elemento in fila: # recorre los valores dentro de la tabla 
            print(elemento, end="\t") #estructura para imprimir los valores
        print() # Da espacio para repetir el ciclo, para la siguiente fila de valores

def consultar_producto(tabla, renglon, columna):
    return tabla[renglon -1][columna -1]

imprimir_tabla(tabla)

renglon = int(input("Ingresa el renglón a escoger: "))
columna = int(input("Ingresa la columna a escoger: "))
total = consultar_producto(tabla, renglon, columna)

print(f"El producto de {renglon} x {columna} es de: {total}")