# Nombre: Héctor Martínez Santiago
# Matricula: AL07289823
# Fecha: 09/09/2026
# Carrera: Desarrollo de Software



numeros = (
    596,
    930,
    777,
    123,
    949
)
numero_adicional = int(input("Ingresar un número adicional:"))
numero_adicional1 = int(input("Ingresar un número adicional:"))
numeros1 = numeros + (numero_adicional, numero_adicional1)

lista = list(numeros1)
lista.sort()

print(numeros1[2])
print(lista)

def numero_total(lista):
    total = 0
    for n in lista: 
        total += n 
    return total 

print(f"Total de la suma de los números en la lista: {numero_total(lista)}")

contactos = {
    "Mario": "66-5535",
    "Carla": "55-3533",
    "Tomas": "44-2494",
    "Ricardo": "44-7571",
    "Fabiola": "44-2409",
    "Antonio": "55-3451"
}

cantidad_contactos = int(input("¿Cuántos contactos quieres agregar? "))
lista_contactos = list(contactos)
for c in range(cantidad_contactos):
    nuevo_contacto = input("Ingresar el nombre del contacto a agregar: ").capitalize()
    lista_contactos += [nuevo_contacto]

print(lista_contactos)