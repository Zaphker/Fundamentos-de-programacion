# Nombre: Hector Martinez Santiago
#Matrícula: AL07289823
#Fecha: Miercoles 19 de Agosto 2026
#Actividad 2: Cobro Entradas Museo
import pdb
precio = 45
precio_menor_de_edad = 30
precio_niños_menores = 0

descuento_estudiante = .10
descuento_adulto_mayor = .12
descuento_profesor = .10
cantidad_visitantes = int(input("Ingresar cuántos visitantes entrarán: "))
total_final = 0
i = 1





while (i <= cantidad_visitantes):
    pdb.set_trace()

    edad = int(input(f"Ingresar edad del visitante {i}: "))  
    if (edad == -1):
        print("Número inválido para continuar con los visitantes, favor de ingresar nuevamente.")
        break
    if (edad >= 18):
        entrada = precio
    elif (3 < edad <= 17):
        entrada = precio_menor_de_edad
    elif (0 <= edad <= 3): 
        entrada = precio_niños_menores
    else: 
        print("Valor ingresado no es válido\nFavor de intentarlo otra vez.")
        continue

    tipo = input("Ingresar que tipo de visitante eres: (Adulto mayor, Estudiante, Profesor): ")

    if tipo == "Adulto mayor":
        descuento = precio * descuento_adulto_mayor
    elif tipo == "Estudiante":
        descuento = precio * descuento_estudiante
    elif tipo == "Profesor":
        descuento = precio * descuento_profesor
    else: 
        descuento = 0
    i += 1
    precio_individual = entrada - descuento
    descuentoTotal = precio - descuento 
    total_final = total_final + descuentoTotal
    print("-" * 30)
    print("-" * 30)
    print(f"Precio original sin descuento: {entrada}\nDescuento aplicado:{descuento:.2f}\nPrecio del boleto del visitante {i} con descuento incluído: {precio_individual:.2f}")
    print("-" * 30)
    print("-" * 30)
    

print("-" * 30)
print("Tabla Desgloze ")
print("-" * 30)
print(f"Total de visitantes: {cantidad_visitantes}\nPrecio por cada entrada dependiendo el visitante: \nPersona Normal: ${precio}\nPersona menor de 17 años: ${precio_menor_de_edad}\nPrecio menor de 3 años: ${precio_niños_menores} \nTotal a pagar por todos los boletos: ${total_final}")
print("-" * 30)
print("-" * 30)