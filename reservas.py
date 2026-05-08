# ==========================================================
# RESERVAS
# Archivo: reservas.py
# ==========================================================

# Importa las clases de servicios
from servicios import Servicio

# Importa la clase cliente
from clientes import Cliente


# ==========================================================
# CLASE RESERVA
# ==========================================================

# Clase Reserva
class Reserva:

    # Constructor de la clase
    def __init__(self, cliente, servicio, duracion):

        # Verifica que el cliente sea válido
        if not isinstance(cliente, Cliente):

            # Genera error si no es un cliente válido
            raise ValueError("El cliente asignado no es válido.")

        # Verifica que el servicio sea válido
        if not isinstance(servicio, Servicio):

            # Genera error si el servicio no es válido
            raise ValueError("El servicio asignado no es válido.")

        # Verifica que la duración sea mayor que cero
        if duracion <= 0:

            # Genera error si la duración es incorrecta
            raise ValueError("La duración debe ser mayor que cero.")

        # Guarda el cliente
        self.cliente = cliente

        # Guarda el servicio
        self.servicio = servicio

        # Guarda la duración
        self.duracion = duracion

        # Estado inicial de la reserva
        self.estado = "Pendiente"

    # ======================================================
    # MÉTODO CONFIRMAR RESERVA
    # ======================================================

    # Método para confirmar reserva
    def confirmar(self):

        # Cambia el estado a confirmada
        self.estado = "Confirmada"

        # Mensaje en pantalla
        print("Reserva confirmada correctamente.")

    # ======================================================
    # MÉTODO CANCELAR RESERVA
    # ======================================================

    # Método para cancelar reserva
    def cancelar(self):

        # Cambia el estado a cancelada
        self.estado = "Cancelada"

        # Mensaje en pantalla
        print("Reserva cancelada.")

    # ======================================================
    # MÉTODO PROCESAR RESERVA
    # ======================================================

    # Método para procesar reserva
    def procesar(self):

        try:

            # Confirma la reserva
            self.confirmar()

            # Calcula el costo total
            costo = self.servicio.calcular_costo(
                self.duracion,
                impuesto=0.19,
                descuento=10000
            )

        # Captura errores controlados
        except Exception as error:

            # Muestra mensaje de error
            print(f"[ERROR] {error}")

        # Se ejecuta si no ocurre error
        else:

            # Muestra información de la reserva
            print("\n=== RESERVA PROCESADA ===")

            # Muestra cliente
            print(f"Cliente: {self.cliente.obtener_nombre()}")

            # Muestra servicio
            print(f"Servicio: {self.servicio.describir_servicio()}")

            # Muestra duración
            print(f"Duración: {self.duracion} horas")

            # Muestra costo
            print(f"Costo total: ${costo}")

            # Muestra estado
            print(f"Estado: {self.estado}")

        # Siempre se ejecuta
        finally:

            # Mensaje final
            print("Proceso de reserva finalizado.")