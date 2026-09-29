import time
import os
import re
import datetime
import threading
import queue


# Los archivos .txt están en la misma carpeta que este script
DIRECTORIO_RAIZ = os.path.dirname(os.path.abspath(__file__))


def obtener_ruta(nombre_archivo):
    # Arma la ruta absoluta de un archivo dentro de la carpeta del proyecto
    return os.path.join(DIRECTORIO_RAIZ, nombre_archivo)

ARCHIVOS_SISTEMA = [
    obtener_ruta("usuarios.txt"),
    obtener_ruta("menu.txt"),
    obtener_ruta("pedidos.txt"),
    obtener_ruta("bitacora.txt"),
]

TIEMPO_MAXIMO_INACTIVIDAD = 10  # 10 minutos en segundos
_cola_entrada = queue.Queue()
hilo_lector = None
def leer_linea():
    _cola_entrada.put(input())

def leer_texto(prompt, segundos= None):
    global hilo_lector
    print(prompt, end="", flush=True)
    if hilo_lector is None or not hilo_lector.is_alive():
        hilo_lector = threading.Thread(target=leer_linea, daemon=True)
        hilo_lector.start()
        try: 
            return _cola_entrada.get(timeout=segundos)
        except queue.Empty:
            print()
            return None

def inicializar_archivos_txt():
    # Crea los 4 archivos base si no existen, con datos por defecto
    ruta_usuarios, ruta_menu, ruta_pedidos, ruta_bitacora = ARCHIVOS_SISTEMA
    try:
        if not os.path.exists(ruta_usuarios):
            with open(ruta_usuarios, "w", encoding="utf-8") as f:
                f.write("cajero,tecmilenio2026\n")

        if not os.path.exists(ruta_menu):
            with open(ruta_menu, "w", encoding="utf-8") as f:
                f.write("Coctel de fruta,65,False,desayunos\n")
                f.write("Waffle Belga,85,False,desayunos\n")
                f.write("Refresco,20,True,bebida\n")
                f.write("Hamburguesa sencilla,75,False,hamburguesa\n")

        if not os.path.exists(ruta_pedidos):
            with open(ruta_pedidos, "w", encoding="utf-8") as f:
                f.write("=== HISTORIAL DE PEDIDOS Y TICKETS ===\n")

        if not os.path.exists(ruta_bitacora):
            with open(ruta_bitacora, "w", encoding="utf-8") as f:
                f.write("=== BITÁCORA GENERAL DEL SISTEMA ===\n")

    except FileNotFoundError as e:
        print(f"No se encontró la ruta del archivo inicial: {e}")
    except PermissionError as e:
        print(f"Error de permisos al crear los archivos: {e}")
    except Exception as e:
        print(f"Error inesperado al inicializar archivos: {e}")


inicializar_archivos_txt()  # Se ejecuta al arrancar el programa


# ==========================================
# PANTALLA DE CARGA Y LOGIN
# ==========================================

def pantalla_carga():
    # Simula una carga de 5 segundos al iniciar el sistema
    print("\n[CARGANDO SISTEMA DE CAFETERÍA]")
    for segundo in range(1, 6):
        time.sleep(1)
        print(f"Cargando sistema... {segundo} segundos")
    print("Carga del Sistema completado\n")


def cargar_usuarios_validos():
    # Lee usuarios.txt y regresa un diccionario {usuario: contraseña}
    usuarios_validos = {}
    try:
        with open(obtener_ruta("usuarios.txt"), "r", encoding="utf-8") as f:
            for linea in f:
                linea = linea.strip()
                if linea and "," in linea:
                    usuario, contrasena = linea.split(",", 1)
                    usuarios_validos[usuario.strip()] = contrasena.strip()
    except FileNotFoundError:
        print("[Error]: No se encontró el archivo 'usuarios.txt'.")
    except Exception as e:
        print(f"[Error] al leer usuarios.txt: {e}")
    return usuarios_validos


def iniciar_sesion():
    # Pide usuario/contraseña hasta que el login sea correcto
    usuarios_validos = cargar_usuarios_validos()
    while True:
        print("\n--- INICIO DE SESIÓN - CAFETERÍA TECMILENIO ---")
        usuario = input("Usuario: ")
        contrasena = input("Contraseña: ")

        if usuarios_validos.get(usuario) == contrasena:
            print(f"Bienvenido, {usuario}.\n")
            return time.time()
        print("Usuario o contraseña incorrectos. Intenta de nuevo.\n")


# ==========================================
# CARGA Y GESTIÓN DE MENÚ
# ==========================================

def cargar_menu():
    # Carga el menú desde menu.txt
    menu_cargado = []
    try:
        with open(obtener_ruta("menu.txt"), "r", encoding="utf-8") as f:
            for linea in f:
                partes = linea.strip().split(",")
                if len(partes) == 4:
                    articulo, precio, preparado_str, categoria = partes
                    menu_cargado.append({
                        "articulo": articulo,
                        "precio_articulo": float(precio),
                        "preparado": preparado_str.lower() == "true",
                        "categoria": categoria,
                    })
    except FileNotFoundError:
        print("Aviso: menu.txt no existe, cargando menú vacío.")
    except Exception as e:
        print(f"Error al leer el menú: {e}")
    return menu_cargado


menu = cargar_menu()


def guardar_menu_en_archivo(menu_actual):
    # Guarda el menú actual en el archivo y registra el cambio en bitácora
    hoy = datetime.date.today()
    fecha = (hoy.day, hoy.month, hoy.year)

    try:
        with open(obtener_ruta("menu.txt"), "w", encoding="utf-8") as f:
            for item in menu_actual:
                f.write(f"{item['articulo']},{item['precio_articulo']},{item['preparado']},{item['categoria']}\n")

        with open(obtener_ruta("bitacora.txt"), "a", encoding="utf-8") as bitacora:
            bitacora.write(f"Menú actualizado. Fecha={fecha}\n")
    except Exception as e:
        print(f"Error al guardar el menú: {e}")


def mostrar_menu(menu_local):
    # Imprime todo el menú numerado
    print("\n--- MENÚ CAFETERÍA TECMILENIO ---")
    for numero, item in enumerate(menu_local, start=1):
        estado = "Disponible" if item["preparado"] else "Requiere preparación y tiempo de espera"
        print(f"{numero}. {item['articulo']} - ${item['precio_articulo']} ({estado})")
    print("----------------------------------")


def agregar_articulo_menu(menu_local):
    # Agrega un artículo nuevo al menú y lo guarda
    try:
        nombre_nuevo = input("Nombre del nuevo artículo: ")
        precio_nuevo = float(input("Precio del artículo: "))
        disponible = input("¿Servir sin espera? (s/n): ").lower() == "s"

        print("Categorías existentes:", ", ".join(obtener_categorias(menu_local)))
        categoria_nueva = input("Categoría del artículo (o 'varios' si no aplica): ").lower()

        menu_local.append({
            "articulo": nombre_nuevo,
            "precio_articulo": precio_nuevo,
            "preparado": disponible,
            "categoria": categoria_nueva,
        })
        guardar_menu_en_archivo(menu_local)
        print(f"'{nombre_nuevo}' fue agregado.\n")
    except ValueError:
        print("Error: Número no válido. Intente nuevamente.")


def eliminar_articulo_menu(menu_local):
    # Elimina un artículo del menú por número y guarda el cambio
    mostrar_menu(menu_local)
    try:
        opcion = int(input("Número del artículo a eliminar: "))
        if 1 <= opcion <= len(menu_local):
            eliminado = menu_local.pop(opcion - 1)
            guardar_menu_en_archivo(menu_local)
            print(f"Se eliminó '{eliminado['articulo']}' del sistema.\n")
        else:
            print("Número no existe.\n")
    except ValueError:
        print("Error: Ingresar un número entero válido.")


# ==========================================
# CATEGORÍAS
# ==========================================

def obtener_categorias(menu_local):
    # Regresa las categorías únicas del menú, ordenadas
    return sorted({item["categoria"] for item in menu_local})


def mostrar_categorias(menu_local):
    # Imprime las categorías numeradas y las regresa
    categorias = obtener_categorias(menu_local)
    print("\n--- CATEGORÍAS ---")
    for numero, categoria in enumerate(categorias, start=1):
        print(f"{numero}. {categoria.capitalize()}")
    print("--------------------------------")
    return categorias


def mostrar_menu_categoria(menu_local, categoria):
    # Imprime y regresa solo los artículos de una categoría
    articulos_categoria = [item for item in menu_local if item["categoria"] == categoria]
    print(f"\n--- {categoria.upper()} ---")
    for numero, item in enumerate(articulos_categoria, start=1):
        estado = "Disponible" if item["preparado"] else "Requiere preparación"
        print(f"{numero}. {item['articulo']} - ${item['precio_articulo']} ({estado})")
    print("----------------------------------")
    return articulos_categoria


# ==========================================
# TOMA DE PEDIDO Y PERSISTENCIA
# ==========================================

def tomar_pedido(menu_local):
    # Captura el pedido de un estudiante navegando por categorías (máx. 10 artículos, máx. 10 piezas por artículo)
    nombre_estudiante = input("\nNombre del estudiante: ")
    pedido = []
    LIMITE_ARTICULOS = 10
    LIMITE_CANTIDAD = 10
 
    while True:
        if len(pedido) >= LIMITE_ARTICULOS:
            print(f"\n Se alcanzó el límite de {LIMITE_ARTICULOS} artículos por pedido para prevenir saturación.")
            print("Si se requiere hacer un pedido mayor, favor de avisar con un día de antelación.")
            print("El pedido se cierra automáticamente.\n")
            break
 
        categorias = mostrar_categorias(menu_local)
        try:
            num_categoria = int(input("Número de categoría (0 para terminar): "))
            if num_categoria == 0:
                break
            if not (1 <= num_categoria <= len(categorias)):
                print("Categoría inválida.")
                continue
 
            categoria_elegida = categorias[num_categoria - 1]
            articulos_categoria = mostrar_menu_categoria(menu_local, categoria_elegida)
 
            opcion = int(input("Número de artículo (0 para cancelar): "))
            if opcion == 0:
                continue
            if not (1 <= opcion <= len(articulos_categoria)):
                print("Articulo inválido.")
                continue
 
            cantidad = int(input("Cantidad: "))
            if cantidad <= 0:
                print("La cantidad tiene que ser mayor a 0, no se aceptan cantidades negativas.")
                continue
            if cantidad > LIMITE_CANTIDAD:
                print(f"Solo se pueden pedir hasta {LIMITE_CANTIDAD} piezas de un mismo artículo, para no saturar la cocina.")
                print("Si se requiere hacer un pedido mayor, favor de avisar con un día de antelación.")
                continue
 
            item_menu = articulos_categoria[opcion - 1]
            pedido.append({
                "articulo": item_menu["articulo"],
                "precio_articulo": item_menu["precio_articulo"],
                "cantidad": cantidad,
                "preparado": item_menu["preparado"],
            })
            print(f"Agregado: {cantidad} x {item_menu['articulo']} ({len(pedido)}/{LIMITE_ARTICULOS})")
        except ValueError as error:
            print(f"Eso no es válido ({error}), intenta de nuevo.\n")
        except Exception as error:
            print(f"Algo salió mal ({error}).\n")
 
    return nombre_estudiante, pedido

def calcular_total(pedido):
    # Suma el subtotal de cada artículo del pedido
    return sum(item["precio_articulo"] * item["cantidad"] for item in pedido)


def hay_tiempo_de_espera(pedido):
    # True si algún artículo del pedido requiere preparación
    return any(not item["preparado"] for item in pedido)


def imprimir_pedido_cocina(nombre_cliente, pedido, total_pedido):
    # Imprime el ticket en consola y lo guarda en pedidos.txt
    hoy = datetime.date.today()
    fecha = (hoy.day, hoy.month, hoy.year)

    ticket_texto = f"\n===== TICKET PARA COCINA =====\nFecha={fecha}\nCliente: {nombre_cliente}\nArtículos:\n"
    for item in pedido:
        estado = "Disponible" if item["preparado"] else "EN PREPARACIÓN"
        ticket_texto += f"  - {item['cantidad']} x {item['articulo']} ({estado})\n"

    ticket_texto += f"TOTAL A PAGAR: ${total_pedido}\n"
    if hay_tiempo_de_espera(pedido) or total_pedido == 0:
        ticket_texto += "Este pedido requiere tiempo de preparación.\n"
    else:
        ticket_texto += "Pedido listo para entregar de inmediato.\n"

    print(ticket_texto)
    print("================================\n")

    try:
        with open(obtener_ruta("pedidos.txt"), "a", encoding="utf-8") as f:
            f.write(ticket_texto + "\n" + "-" * 40 + "\n")
    except Exception as e:
        print(f"No se pudo guardar el pedido en el archivo: {e}")

# ==========================================
# VENTAS TOTALES DEL DÍA 
# ==========================================

def mostrar_resumen_ventas():
    # Lee pedidos.txt y muestra cuántos pedidos hay y el total vendido
    ruta_pedidos = obtener_ruta("pedidos.txt")
    try:
        with open(ruta_pedidos, "r", encoding="utf-8") as f:
            contenido = f.read()

        totales = [float(valor) for valor in re.findall(r"TOTAL A PAGAR: \$(\d+(?:\.\d+)?)", contenido)]

        print("\n--- RESUMEN DE VENTAS ---")
        print(f"Pedidos registrados: {len(totales)}")
        print(f"Total vendido: ${sum(totales):.2f}")
        print("--------------------------\n")
    except FileNotFoundError:
        print("Aún no hay pedidos registrados.")
    except Exception as e:
        print(f"Error al calcular el resumen: {e}")

# ==========================================
# GESTIÓN DE ARCHIVOS .TXT ADICIONALES
# ==========================================

def gestionar_archivos_texto():
    # Muestra los 4 archivos del sistema y permite ver/anexar contenido
    print("\n--- GESTIÓN DE ARCHIVOS DE TEXTO (.TXT) ---")
    print("Archivos disponibles en el sistema:")
    for idx, archivo in enumerate(ARCHIVOS_SISTEMA, start=1):
        print(f"{idx}. {archivo}")

    try:
        opcion = int(input("Selecciona el número de archivo a consultar (0 para regresar): "))
        if opcion == 0:
            return
        if not (1 <= opcion <= len(ARCHIVOS_SISTEMA)):
            print("Número de archivo fuera de rango.")
            return

        archivo_elegido = ARCHIVOS_SISTEMA[opcion - 1]
        print(f"\n--- Contenido actual de {archivo_elegido} ---")
        with open(archivo_elegido, "r", encoding="utf-8") as f:
            contenido = f.read()
            print(contenido if contenido else "[Archivo vacío]")

        if input("¿Deseas agregar un registro/nota a este archivo? (si/no): ").strip().lower() == "si":
            texto_nuevo = input("Escribe el contenido a anexar: ")
            hoy = datetime.date.today()
            fecha = (hoy.day, hoy.month, hoy.year)
            with open(archivo_elegido, "a", encoding="utf-8") as f:
                f.write(f"Nota: {texto_nuevo} | Fecha={fecha}\n")
            print("Información guardada")

    except FileNotFoundError:
        print("El archivo seleccionado no se encuentra en el disco.")
    except PermissionError:
        print("Error: No cuentas con los permisos para acceder al archivo.")
    except ValueError:
        print("Error: Entrada inválida. Digita un número.")
    except Exception as e:
        print(f"Error inesperado al gestionar archivos: {e}")


# ==========================================
# CONTROL DE INACTIVIDAD
# ==========================================

def verificar_inactividad_con_for(ultima_actividad):
    # Si pasaron 10 min sin actividad, pregunta (máx 3 intentos) si continuar
    if time.time() - ultima_actividad < TIEMPO_MAXIMO_INACTIVIDAD:
        return ultima_actividad

    print("\nAlerta: Se han detectado 10 minutos de inactividad.")
    for intento in range(1, 4):
        respuesta = input("¿Deseas continuar en la sesión? Escribe \"si\" o \"no\": ").strip().lower()
        if respuesta == "si":
            print("Reanudando sesión...")
            return time.time()
        if respuesta == "no":
            print("Regresando al inicio de sesión...")
            return "reiniciar"
        print(f"Intento {intento}/3. Respuesta no válida. Debe escribir \"si\" o \"no\".")

    print("Demasiados intentos fallidos. Cerrando sesión.")
    return "reiniciar"


# ==========================================
# PROGRAMA PRINCIPAL
# ==========================================

def main():
    # Controla el flujo del sistema: login, menú principal y todas las opciones
    pantalla_carga()
    ultima_actividad = iniciar_sesion()
    atendiendo = True
 
    while atendiendo:
        print("\n+---------------------------------------------------+")
        print("|              CAFETERÍA - MENÚ PRINCIPAL           |")
        print("+---------------------------------------------------+")
        print("| 1. Tomar pedido             | 2. Agregar artículo |")
        print("| 3. Eliminar artículo        | 4. Ver archivos     |")
        print("| 5. Resumen de ventas        | 6. Salir            |")
        print("+---------------------------------------------------+")
 
        opcion = leer_texto("Elige una opción: ", TIEMPO_MAXIMO_INACTIVIDAD)
 
        # Si se acabó el tiempo sin que escribieran nada, se pregunta si siguen ahí
        if opcion is None:
            resultado_inactividad = verificar_inactividad_con_for(ultima_actividad)
            if resultado_inactividad == "reiniciar":
                ultima_actividad = iniciar_sesion()
            else:
                ultima_actividad = resultado_inactividad
            continue
 
        opcion = opcion.strip()
 
        if opcion == "1":
            nombre_estudiante, pedido = tomar_pedido(menu)
            if pedido:
                total_pedido = calcular_total(pedido)
                imprimir_pedido_cocina(nombre_estudiante, pedido, total_pedido)
        elif opcion == "2":
            agregar_articulo_menu(menu)
        elif opcion == "3":
            eliminar_articulo_menu(menu)
        elif opcion == "4":
            gestionar_archivos_texto()
        elif opcion == "5":
            mostrar_resumen_ventas()
        elif opcion == "6":
            atendiendo = False
            print("Cerrando el sistema de la cafetería")
        else:
            print("Opción no válida, intenta de nuevo.")

        ultima_actividad = time.time()

if __name__ == "__main__":
    main()