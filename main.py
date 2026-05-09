# =========================================================
# SISTEMA PRINCIPAL
# Archivo: main.py
# =========================================================

# Importa los módulos del sistema
from clientes import Cliente
from servicios import Servicio
from reservas import Reserva

# =========================================================
# MENÚ PRINCIPAL
# =========================================================

def mostrar_menu():
    print("\n====================================")
    print(" SISTEMA INTEGRAL SOFTWARE FJ ")
    print("====================================")
    print("1. Registrar cliente")
    print("2. Registrar servicio")
    print("3. Crear reserva")
    print("4. Salir")
    print("====================================")


# =========================================================
# LISTAS PARA ALMACENAR DATOS
# =========================================================

clientes = []
servicios = []
reservas = []


# =========================================================
# PROGRAMA PRINCIPAL
# =========================================================

while True:

    mostrar_menu()

    opcion = input("Seleccione una opción: ")

    # -----------------------------------------------------
    # OPCIÓN 1 - REGISTRAR CLIENTE
    # -----------------------------------------------------

    if opcion == "1":

        nombre = input("Ingrese nombre del cliente: ")
        telefono = input("Ingrese teléfono: ")

        nuevo_cliente = Cliente(nombre, telefono)

        clientes.append(nuevo_cliente)

        print("Cliente registrado correctamente")

    # -----------------------------------------------------
    # OPCIÓN 2 - REGISTRAR SERVICIO
    # -----------------------------------------------------

    elif opcion == "2":

        nombre_servicio = input("Ingrese nombre del servicio: ")
        precio = input("Ingrese precio: ")

        nuevo_servicio = Servicio(nombre_servicio, precio)

        servicios.append(nuevo_servicio)

        print("Servicio registrado correctamente")

    # -----------------------------------------------------
    # OPCIÓN 3 - CREAR RESERVA
    # -----------------------------------------------------

    elif opcion == "3":

        if len(clientes) == 0 or len(servicios) == 0:
            print("Debe registrar clientes y servicios primero")

        else:

            cliente = clientes[0]
            servicio = servicios[0]

            nueva_reserva = Reserva(cliente, servicio)

            reservas.append(nueva_reserva)

            print("Reserva creada correctamente")

    # -----------------------------------------------------
    # OPCIÓN 4 - SALIR
    # -----------------------------------------------------

    elif opcion == "4":

        print("Gracias por utilizar el sistema")
        break

    # -----------------------------------------------------
    # OPCIÓN INVÁLIDA
    # -----------------------------------------------------

    else:

        print("Opción no válida")