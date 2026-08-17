class Libro:
    def __init__(self):
        self.titulo = None
        self.autor = None
        self.isbn = None
        self.estaDisponible = True

    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.estaDisponible = True