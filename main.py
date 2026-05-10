# =========================================================
# SISTEMA PRINCIPAL
# Archivo: main.py
# =========================================================

# Importa los módulos del sistema
from clientes import Cliente
from servicios import AsesoriaEspecializada, ReservaSala, AlquilerEquipo
from reservas import Reserva

import logging

logging.basicConfig(
    filename="logs.txt",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
    )

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

        try:
            codigo = input("Ingrese codigo del cliente: ")
            nombre = input("Ingrese nombre del cliente: ")
            telefono = input("Ingrese teléfono: ")
            correo = input("Ingrese correo:")

            nuevo_cliente = Cliente(codigo, nombre, correo, telefono)
            clientes.append(nuevo_cliente)

        except Exception as e:
            print("Error al registrar cliente:", e)
            logging.error("Error al registrar cliente", exc_info=True)

        else:
            print("Cliente registrado correctamente")
            logging.info("Cliente registrado correctamente")

        finally:
            print("Operación de cliente finalizada")
    # -----------------------------------------------------
    # OPCIÓN 2 - REGISTRAR SERVICIO
    # -----------------------------------------------------

    elif opcion == "2":

        codigo = input("Ingrese codigo del servicio")
        nombre_servicio = input("Ingrese nombre del servicio: ")
        try:            
            precio = float(input("Ingrese precio: "))

            nuevo_servicio = AsesoriaEspecializada(codigo, nombre_servicio, precio)

            servicios.append(nuevo_servicio)

            print("Servicio registrado correctamente")


        except ValueError as e:
            print("Error: debe ingresar un numero valido") 
            logging.error("Precio invalido", exc_info=True)
            

        

    # -----------------------------------------------------
    # OPCIÓN 3 - CREAR RESERVA
    # -----------------------------------------------------

    elif opcion == "3":

        try:
            if len(clientes) == 0 or len(servicios) == 0:
             raise ValueError("Debe registrar clientes y servicios primero")

            cliente = clientes[0]
            servicio = servicios[0]
            duracion = float(input("Ingrese duración de la reserva: "))

            nueva_reserva = Reserva(cliente, servicio, duracion)
            reservas.append(nueva_reserva)

        except ValueError as e:
            print("Error:", e)
            logging.error("Error al crear reserva", exc_info=True)

        except Exception as e:
            print("Error inesperado:", e)
            logging.error("Error inesperado en reserva", exc_info=True)

        else:
            print("Reserva creada correctamente")
            logging.info("Reserva creada correctamente")

        finally:
            print("Operación de reserva finalizada")
            
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