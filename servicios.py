# Importa clases abstractas
from abc import ABC, abstractmethod


# ==========================================================
# CLASE ABSTRACTA SERVICIO
# ==========================================================

# Clase abstracta Servicio
class Servicio(ABC):

    # Constructor de la clase
    def __init__(self, codigo, nombre, precio_base, disponible=True):

        # Verifica que el precio sea mayor que cero
        if precio_base <= 0:

            # Genera error si el precio es inválido
            raise ValueError("El precio base debe ser mayor que cero.")

        # Guarda el código del servicio
        self._codigo = codigo

        # Guarda el nombre del servicio
        self._nombre = nombre

        # Guarda el precio base
        self._precio_base = precio_base

        # Guarda disponibilidad
        self._disponible = disponible

    # Método abstracto para calcular costos
    @abstractmethod
    def calcular_costo(self, duracion, impuesto=0, descuento=0):
        pass

    # Método abstracto para describir el servicio
    @abstractmethod
    def describir_servicio(self):
        pass

    # Método para validar disponibilidad
    def validar_disponibilidad(self):

        # Verifica si el servicio está disponible
        if not self._disponible:

            # Genera error si no está disponible
            raise ValueError(f"El servicio {self._nombre} no está disponible.")


# ==========================================================
# CLASE RESERVA DE SALA
# ==========================================================

# Clase que hereda de Servicio
class ReservaSala(Servicio):

    # Método para calcular costo
    def calcular_costo(self, duracion, impuesto=0, descuento=0):

        # Verifica duración válida
        if duracion <= 0:

            # Genera error si la duración es inválida
            raise ValueError("La duración debe ser mayor que cero.")

        # Calcula subtotal
        subtotal = self._precio_base * duracion

        # Calcula total con impuesto y descuento
        total = subtotal + (subtotal * impuesto) - descuento

        # Retorna el valor total
        return max(total, 0)

    # Método para describir el servicio
    def describir_servicio(self):

        # Retorna descripción
        return (
            f"Reserva de sala: {self._nombre} | "
            f"Precio por hora: ${self._precio_base}"
        )


# ==========================================================
# CLASE ALQUILER DE EQUIPOS
# ==========================================================

# Clase que hereda de Servicio
class AlquilerEquipo(Servicio):

    # Método para calcular costo
    def calcular_costo(self, duracion, impuesto=0, descuento=0):

        # Verifica duración válida
        if duracion <= 0:

            # Genera error si duración inválida
            raise ValueError("La duración del alquiler debe ser válida.")

        # Calcula subtotal
        subtotal = self._precio_base * duracion

        # Agrega seguro adicional
        seguro = 15000

        # Calcula total
        total = subtotal + seguro + (subtotal * impuesto) - descuento

        # Retorna valor total
        return max(total, 0)

    # Método para describir servicio
    def describir_servicio(self):

        # Retorna descripción
        return (
            f"Alquiler de equipo: {self._nombre} | "
            f"Precio por hora: ${self._precio_base}"
        )


# ==========================================================
# CLASE ASESORÍA ESPECIALIZADA
# ==========================================================

# Clase que hereda de Servicio
class AsesoriaEspecializada(Servicio):

    # Método para calcular costo
    def calcular_costo(self, duracion, impuesto=0, descuento=0):

        # Verifica duración válida
        if duracion <= 0:

            # Genera error si duración inválida
            raise ValueError("La duración de la asesoría debe ser mayor que cero.")

        # Calcula subtotal
        subtotal = self._precio_base * duracion

        # Agrega recargo profesional
        recargo_profesional = 30000

        # Calcula total
        total = subtotal + recargo_profesional + (subtotal * impuesto) - descuento

        # Retorna total
        return max(total, 0)

    # Método para describir servicio
    def describir_servicio(self):

        # Retorna descripción
        return (
            f"Asesoría especializada: {self._nombre} | "
            f"Precio por hora: ${self._precio_base}"
        )