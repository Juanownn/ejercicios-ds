from modelos.libro import Libro
from excepciones import MiExcepcion

def realizar_prestamo(libro: Libro):
    if not(libro.estaDisponible):
        raise MiExcepcion("El libro no esta disponible")
    else:
        libro.estaDisponible = False
        print(f"Retira el libro {libro.titulo} de {libro.autor}")
    
def realizar_devolucion(libro: Libro):
    if libro.estaDisponible:
        raise MiExcepcion("No puede devolver un libro que no retiro")
    else:
        libro.estaDisponible = True
        print(f"Devuelve el libro {libro.titulo} de {libro.autor}")

def consultar_disponibilidad(libro: Libro):
    if libro.estaDisponible:
        print(f"Libro: {libro.titulo} esta disponible")
    else:
        print(f"Libro: {libro.titulo} NO esta disponible")