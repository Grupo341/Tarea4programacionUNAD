# =========================================================
# SISTEMA PRINCIPAL
# Archivo: main.py
# =========================================================

from clientes import Cliente
from servicios import AsesoriaEspecializada, ReservaSala, AlquilerEquipo
from reservas import Reserva
from excepciones import ErrorServicio
import logging

logging.basicConfig(
    filename="logs.txt",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def mostrar_menu():
    print("\n====================================")
    print(" SISTEMA INTEGRAL SOFTWARE FJ ")
    print("====================================")
    print("1. Registrar cliente")
    print("2. Registrar servicio")
    print("3. Crear reserva")
    print("4. Salir")
    print("====================================")


clientes = []
servicios = []
reservas = []


while True:

    mostrar_menu()
    opcion = input("Seleccione una opción: ")

    if opcion == "1":

        try:
            codigo = input("Ingrese codigo del cliente: ")
            nombre = input("Ingrese nombre del cliente: ")
            telefono = input("Ingrese teléfono: ")
            correo = input("Ingrese correo: ")

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

    elif opcion == "2":

        try:
            codigo = input("Ingrese codigo del servicio: ")
            nombre_servicio = input("Ingrese nombre del servicio: ")

            print("Seleccione tipo de servicio:")
            print("1. Asesoría especializada")
            print("2. Reserva de sala")
            print("3. Alquiler de equipo")

            tipo = input("Tipo de servicio: ")
            precio = float(input("Ingrese precio: "))

            if tipo == "1":
                nuevo_servicio = AsesoriaEspecializada(codigo, nombre_servicio, precio)
            elif tipo == "2":
                nuevo_servicio = ReservaSala(codigo, nombre_servicio, precio)
            elif tipo == "3":
                nuevo_servicio = AlquilerEquipo(codigo, nombre_servicio, precio)
            else:
                raise ValueError("Tipo de servicio no válido")

            servicios.append(nuevo_servicio)

        except ValueError as e:
            error = ErrorServicio("Error personalizado: el precio o tipo de servicio es inválido")
            print(error)
            logging.error(error, exc_info=True)

            try:
                raise ErrorServicio("Error encadenado: datos inválidos en servicio") from e
            except ErrorServicio as error_encadenado:
                logging.error(error_encadenado, exc_info=True)

        except Exception as e:
            print("Error inesperado al registrar servicio:", e)
            logging.error("Error inesperado al registrar servicio", exc_info=True)

        else:
            print("Servicio registrado correctamente")
            logging.info("Servicio registrado correctamente")

        finally:
            print("Operación de servicio finalizada")

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

    elif opcion == "4":

        print("Gracias por utilizar el sistema")
        break

    else:

        print("Opción no válida")