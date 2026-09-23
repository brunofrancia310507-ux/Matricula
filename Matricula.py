"""
Sistema de Soporte Académico - Version simple
Guia de Laboratorio Tema 2 (CIIN1205P) - Funciones y control de versiones
"""
# Listas para guardar los datos de cada solicitud (variables del programa principal)
lista_codigos = []
lista_nombres = []
lista_tipos = []
lista_prioridades = []
def main():
    opcion = ""
    while opcion != "3":
        mostrar_menu()  # funcion sin retorno
        opcion = input("Elija una opcion: ")

        if opcion == "1":
            registrar_solicitud()
        elif opcion == "2":
            mostrar_resumen_general()
        elif opcion != "3":
            print("Opcion no valida.")
# Requerimiento 4: funcion SIN retorno
def mostrar_menu():
    print("")
    print("=== Soporte Academico ===")
    print("1. Registrar solicitud")
    print("2. Ver resumen de solicitudes")
    print("3. Salir")
# Registra una solicitud pidiendo los datos y validandolos
def registrar_solicitud():
    codigo = input("Codigo de estudiante: ")
    nombre = input("Nombre: ")
    tipo = input("Tipo de consulta (matricula, pagos, constancia, plataforma, otro): ")
    # Requerimiento 2: validar el codigo
    codigo_valido = validar_texto_obligatorio(codigo, 4)
    if codigo_valido == False:
        print("Error: el codigo debe tener minimo 4 caracteres.")
        return
    # Requerimiento 3: validar el tipo de consulta
    tipo_valido = validar_tipo_consulta(tipo)
    if tipo_valido == False:
        print("Error: tipo de consulta no reconocido.")
        return
    # Requerimiento 5: asignar prioridad (funcion con retorno)
    prioridad = asignar_prioridad(tipo)
    # Guardamos los datos en las listas
    lista_codigos.append(codigo)
    lista_nombres.append(nombre)
    lista_tipos.append(tipo)
    lista_prioridades.append(prioridad)
    mostrar_resumen_solicitud(codigo, nombre, tipo, prioridad)

# Requerimiento 6: funcion CON retorno, recibe parametros y no usa variables globales
def validar_texto_obligatorio(texto, longitud_minima):
    texto_limpio = texto.strip()
    if texto_limpio == "":
        return False
    if len(texto_limpio) < longitud_minima:
        return False
    return True
# Requerimiento 3: funcion con retorno
def validar_tipo_consulta(tipo):
    tipo_limpio = tipo.strip().lower()
    if tipo_limpio == "matricula":
        return True
    elif tipo_limpio == "pagos":
        return True
    elif tipo_limpio == "constancia":
        return True
    elif tipo_limpio == "plataforma":
        return True
    elif tipo_limpio == "otro":
        return True
    else:
        return False
# Requerimiento 5: funcion con retorno
def asignar_prioridad(tipo):
    tipo_limpio = tipo.strip().lower()
    if tipo_limpio == "pagos":
        return "Alta"
    elif tipo_limpio == "plataforma":
        return "Alta"
    elif tipo_limpio == "matricula":
        return "Media"
    else:
        return "Baja"
# Requerimiento 7: funcion sin retorno, muestra los datos de una solicitud
def mostrar_resumen_solicitud(codigo, nombre, tipo, prioridad):
    print("")
    print("--- Solicitud registrada ---")
    print("Codigo:", codigo)
    print("Nombre:", nombre)
    print("Tipo:", tipo)
    print("Prioridad:", prioridad)
# Muestra todas las solicitudes guardadas hasta el momento
def mostrar_resumen_general():
    print("")
    print("Total de solicitudes registradas:", len(lista_codigos))
    i = 0
    while i < len(lista_codigos):
        mostrar_resumen_solicitud(lista_codigos[i], lista_nombres[i], lista_tipos[i], lista_prioridades[i])
        i = i + 1
main()