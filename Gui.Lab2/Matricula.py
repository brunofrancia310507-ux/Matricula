# listas para guardar los datos de cada solicitud 
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
# funcion SIN retorno
def mostrar_menu():
    print("")
    print("=== Soporte Academico ===")
    print("1. Registrar solicitud")
    print("2. Ver resumen de solicitudes")
    print("3. Salir")
# registra una solicitud pidiendo los datos y validandolos
def registrar_solicitud():
    codigo = input("Codigo de estudiante: ")
    nombre = input("Nombre: ")
    tipo = input("Tipo de consulta (matricula, pagos, constancia, plataforma, otro): ")
    # validar el codigo
    codigo_valido = validar_texto_obligatorio(codigo, 4)
    if codigo_valido == False:
        print("Error: el codigo debe tener minimo 4 caracteres.")
        return
    # validar el tipo de consulta
    tipo_valido = validar_tipo_consulta(tipo)
    if tipo_valido == False:
        print("Error: tipo de consulta no reconocido.")
        return
    # asignar prioridad, funcion con retorno
    prioridad = asignar_prioridad(tipo)
    # Guardamos los datos en las listas
    lista_codigos.append(codigo)
    lista_nombres.append(nombre)
    lista_tipos.append(tipo)
    lista_prioridades.append(prioridad)
    mostrar_resumen_solicitud(codigo, nombre, tipo, prioridad)
