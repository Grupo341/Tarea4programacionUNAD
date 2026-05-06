# =========================================================
# Tarea4 Sistema Integral de Gestion de Clientes, servicios y reservas.
# Empresa: Software FJ
# =========================================================

# Importa herramientas para crear clases abstractas
from abc import ABC, abstractmethod


# ==========================================================
# CLASE ABSTRACTA GENERAL
# ==========================================================

# Clase abstracta base del sistema
class EntidadSistema(ABC):

    # Constructor de la clase
    def __init__(self, codigo):

        # Verifica que el código no esté vacío
        if not codigo:

            # Genera un error si el código está vacío
            raise ValueError("El código no puede estar vacío.")

        # Guarda el código en un atributo protegido
        self._codigo = codigo

    # Método abstracto obligatorio para clases hijas
    @abstractmethod
    def mostrar_informacion(self):

        # Método vacío que será sobrescrito
        pass


# ==========================================================
# CLASE CLIENTE
# ==========================================================

# Clase Cliente que hereda de EntidadSistema
class Cliente(EntidadSistema):

    # Constructor de la clase Cliente
    def __init__(self, codigo, nombre, correo, telefono):

        # Llama al constructor de la clase padre
        super().__init__(codigo)

        # ==================================================
        # VALIDACIÓN DEL NOMBRE
        # ==================================================

        # Verifica que el nombre no esté vacío
        if not nombre.strip():

            # Genera error si el nombre está vacío
            raise ValueError("El nombre del cliente no puede estar vacío.")

        # ==================================================
        # VALIDACIÓN DEL CORREO
        # ==================================================

        # Verifica que el correo tenga @ y .
        if "@" not in correo or "." not in correo:

            # Genera error si el correo no es válido
            raise ValueError("El correo electrónico no es válido.")

        # ==================================================
        # VALIDACIÓN DEL TELÉFONO
        # ==================================================

        # Verifica que el teléfono solo tenga números
        if not telefono.isdigit():

            # Genera error si contiene letras o símbolos
            raise ValueError("El teléfono solo debe contener números.")

        # ==================================================
        # ENCAPSULACIÓN DE DATOS
        # ==================================================

        # Guarda el nombre como atributo privado
        self.__nombre = nombre

        # Guarda el correo como atributo privado
        self.__correo = correo

        # Guarda el teléfono como atributo privado
        self.__telefono = telefono  

    # ======================================================
    # MÉTODO PARA MOSTRAR INFORMACIÓN DEL CLIENTE
    # ======================================================

    # Método sobrescrito de la clase abstracta
    def mostrar_informacion(self):

        # Retorna los datos del cliente en formato texto
        return (
            f"Cliente: {self.__nombre} | "
            f"Correo: {self.__correo} | "
            f"Teléfono: {self.__telefono}"
        )

    # ======================================================
    # MÉTODOS GET
    # ======================================================

    # Método para obtener el nombre
    def obtener_nombre(self):

        # Retorna el nombre del cliente
        return self.__nombre

    # Método para obtener el correo
    def obtener_correo(self):

        # Retorna el correo del cliente
        return self.__correo

    # Método para obtener el teléfono
    def obtener_telefono(self):

        # Retorna el teléfono del cliente
        return self.__telefono
