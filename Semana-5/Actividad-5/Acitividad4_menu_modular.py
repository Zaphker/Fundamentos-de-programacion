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

def mostrar_tuplas():
    print("Tercer elemento:", numeros[2])

    nuevo1 = int(input("Ingresa un número: "))
    nuevo2 = int(input("Ingresa otro número: "))

    numeros_nuevos = numeros + (nuevo1, nuevo2)
    print("Nueva tupla:", numeros_nuevos)

    lista_numeros = list(numeros_nuevos)
    lista_numeros.sort()
    print("Lista ordenada:", lista_numeros)

    suma = sumar_numeros(numeros)
    print("Suma de los elementos:", suma)

def sumar_numeros(tupla):
    total = 0
    for numero in tupla:
        total += numero
    return total



contactos = {
    "Mario": "66-5535",
    "Carla": "55-3533",
    "Tomas": "44-2494",
    "Ricardo": "44-7571",
    "Fabiola": "44-2409",
    "Antonio": "55-3451"
}

def mostrar_diccionarios():
    nombre_nuevo = input("Ingresa el nombre del nuevo contacto: ")
    telefono_nuevo = input("Ingresa el teléfono del nuevo contacto: ")
    contactos[nombre_nuevo] = telefono_nuevo

    print("Nombres de los contactos:")
    for nombre in contactos:
        print(nombre)

    nombre_buscado = input("Ingresa el nombre a buscar: ")
    telefono = buscar_telefono(contactos, nombre_buscado)
    if telefono is not None:
        print(f"El teléfono de {nombre_buscado} es {telefono}")
    else:
        print("Contacto no encontrado")

def buscar_telefono(diccionario, nombre):
    if nombre in diccionario:
        return diccionario[nombre]
    else:
        return None



def mostrar_excepciones():
    try:
        num1 = int(input("Ingresa el primer número: "))
        num2 = int(input("Ingresa el segundo número: "))
        print("La suma es:", num1 + num2)
        print("La división es:", num1 / num2)
    except ValueError:
        print("Debes ingresar solo números enteros")
    except ZeroDivisionError:
        print("No se puede dividir entre cero")



def mostrar_strings():
    mensaje = input("Ingresa un mensaje: ")

    print("Longitud del mensaje:", len(mensaje))
    print("En mayúsculas:", mensaje.upper())

    mensaje_reemplazado = mensaje.replace("Python", "programación")
    print("Texto reemplazado:", mensaje_reemplazado)

    print("Palabras totales:", contar_palabras(mensaje))

def contar_palabras(texto):
    return len(texto.split())



opcion = 0
while opcion != 5:
    print("\n1. Tuplas")
    print("2. Diccionarios")
    print("3. Excepciones")
    print("4. Strings")
    print("5. Finalizar")

    opcion = int(input("Elige una opción: "))

    if opcion == 1:
        mostrar_tuplas()
    elif opcion == 2:
        mostrar_diccionarios()
    elif opcion == 3:
        mostrar_excepciones()
    elif opcion == 4:
        mostrar_strings()
    elif opcion == 5:
        print("Programa finalizado")
    else:
        print("Opción no válida")