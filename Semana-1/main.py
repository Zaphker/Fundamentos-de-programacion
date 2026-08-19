#Actividad Evaluable 1 - Calculadora de Tiempo Digital

# Restaurar color normal
RESET = "\033[0m"
# Colores ANSI básicos
NEGRO   = "\033[30m"
ROJO    = "\033[31m"
VERDE   = "\033[32m"
AMARILLO = "\033[33m"
AZUL    = "\033[34m"
MAGENTA = "\033[35m"
CIAN    = "\033[36m"
BLANCO  = "\033[37m"
#Colores Brillantes
ROJO_CLARO     = "\033[91m"
VERDE_CLARO    = "\033[92m"
AMARILLO_CLARO = "\033[93m"
AZUL_CLARO     = "\033[94m"
MAGENTA_CLARO  = "\033[95m"
CIAN_CLARO     = "\033[96m"
BLANCO_CLARO   = "\033[97m"


nombre_usuario = input("Ingrese su nombre de usuario: ")
tiempo_redes_sociales = float(input("Ingresa el tiempo diario dedicado Redes Sociales en horas aproximadas: "))
tiempo_streaming = float(input("Ingresa el tiempo diario dedicado Streaming en horas aproximadas: "))
tiempo_videojuegos = float(input("Ingresa el tiempo diario dedicado Videojuegos en horas aproximadas: "))
tiempo_estudio_en_linea = float(input("Ingresa el tiempo diario dedicado Estudio en horas aproximadas: "))
tiempo_compras_en_linea = float(input("Ingresa el tiempo diario dedicado Compras en línea en horas aproximadas: "))
tiempo_total = tiempo_redes_sociales + tiempo_streaming + tiempo_videojuegos + tiempo_estudio_en_linea + tiempo_compras_en_linea
porcentaje = (tiempo_total / 24) * 100

print(f"-" * 30)
print("Gestor de Tiempo Digital")
print(f"-" * 30)
print(f" Nombre de Usuario: {nombre_usuario} \n Tiempo Total Acumulado: {tiempo_total} \n Porcentaje Calculado: {porcentaje} ")
print("-" * 30)