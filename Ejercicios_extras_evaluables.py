#Extra 1: División de cuenta con propina

#Enunciado: Crea un programa que pida el total de la cuenta de un restaurante, el porcentaje de propina a dejar y el número de personas que pagarán. El programa debe calcular el monto de la propina, el total a pagar con propina y cuánto le toca pagar a cada persona (con dos decimales).
#Entrada:
#Total de la cuenta: 250
#Porcentaje de propina: 15
#Número de personas: 4
#Salida:
#Propina: $37.50
#Total con propina: $287.50
#Pago por persona: $71.88

total_cuenta = int(input("Digitar el total de la cuenta: "))
porcentaje_propina = int(input("Porcentaje de propina que desean agregar: "))
numero_de_personas = int(input("Número de personas en las que se dividirá la cuenta: "))
propina = total_cuenta * (porcentaje_propina / 100)
total_con_propina = total_cuenta + propina
pago_individual = total_cuenta / numero_de_personas

print(f"Su cuenta fue de: {total_cuenta} \nPropina dejada: {propina:.2f} \nTotal de la cuenta con propina agregada: {total_con_propina:.2f} \nPago por persona: {pago_individual:.2f}")
 
# Extra 2: Conversor de minutos a días, horas y minutos
# Enunciado: Crea un programa que pida una cantidad total de minutos (entero) y la convierta a días, horas y minutos restantes. Utiliza los operadores de división entera `//` y módulo `%`. (Pista: 1 día = 1440 minutos, 1 hora = 60 minutos.)
# Entrada:
# Total de minuto
# Salida:
# 1500 minutos = 1 día(s), 1 hora(s), 0 minuto(s)

minutos = int(input("Ingresar los minutos que desee convertir: "))
total_dias = minutos // 1440 
total_horas = (minutos - (1440 * total_dias)) // 60
total_minutos = (minutos - 1440) % 60
print(f"{total_dias} dia(s), {total_horas} hora(s), {total_minutos} minuto(s)")

# Extra 3: Calificación 
# Enunciado: Crea un programa que pida las calificaciones de tres parciales (valores de 0 a 10) y calcule la calificación final considerando una ponderación de 30%, 30% y 40% respectivamente. Muestra el resultado con dos decimales.
# Entrada:
# Parcial 1 (30%): 8
# Parcial 2 (30%): 9
# Parcial 3 (40%): 7
# Salida:
# Tu calificación final es: 7.90

parcial_1 = float(input("Ingresar calificación del primer parcial: "))
parcial_2 = float(input("Ingresar calificación del segundo parcial: "))
parcial_3 = float(input("Ingresar calificación del tercer parcial: "))
calificacion_final = ((parcial_1) + (parcial_2) + (parcial_3)) / 3

print(f"Tu calificacion final es: {calificacion_final:.2f}")

# Extra 4: Conversor de moneda (MXN a USD y EUR)
# Enunciado: Crea un programa que pida una cantidad en pesos mexicanos y los tipos de cambio del dólar (USD) y del euro (EUR). Debe calcular y mostrar las equivalencias redondeadas a dos decimales. (Fórmula: `cantidad / tipo\\\_de\\\_cambio`.)
# Entrada:
# Cantidad en MXN: 1000
# Tipo de cambio USD: 18.50
# Tipo de cambio EUR: 21.00
# Salida:
# $1000.00 MXN equivalen a:
# USD: 54.05
# EUR: 47.62

pesos = float(input("Ingresa la cantidad de $MXN que quieras convertir a dolares: "))
usd = pesos / 18.50
eur = pesos / 21.00

print(f"${pesos} MXN equivalen a: \nUSD: {usd:.2f}\nEUR: {eur:.2f}")