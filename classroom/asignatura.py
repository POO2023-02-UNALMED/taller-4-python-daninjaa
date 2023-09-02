class Asignatura:

    def __init__(self, nombre, salon = None):
        self._nombre = nombre
        self._salon = salon

    
    def __str__(self):
        return f"{self._nombre} remoto"
