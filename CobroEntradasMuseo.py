# Nombre: Hector Martinez Santiago
#Matrícula: AL07289823
#Fecha: Miercoles 19 de Agosto 2026
#Actividad 2: Cobro Entradas Museo
precio_base = 45
precio_menor = 30
precio_bebes = 0
tipo = input("Ingresar tipo de visitante: ")
if tipo == "adulto_mayor":
    descuento = precio_base * 0.88
elif tipo == "estudiante" or "profesor":
    descuento = precio_base * 0.90
elif tipo == "estudiante" and "precio_menor":
    descuento = precio_menor * 0.90
elif tipo == "menor":
    descuento = precio_menor
elif tipo == "bebe":
    descuento = precio_bebes
else: 
    descuento = 0

