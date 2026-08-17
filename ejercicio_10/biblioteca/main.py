from modelos.libro import Libro
from servicios.prestamo import realizar_devolucion, realizar_prestamo, consultar_disponibilidad

libro1 = Libro("Quijote de la mancha", "Autor anonimo", 1560)

realizar_prestamo(libro1)
consultar_disponibilidad(libro1)
#realizar_prestamo(libro1)
#realizar_devolucion(libro1)
realizar_devolucion(libro1)
consultar_disponibilidad(libro1)