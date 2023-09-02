from classroom.asignatura import Asignatura

class Grupo:
    grado = None

    def __init__(self, grupo="grupo predeterminado", asignaturas = None, estudiantes = None, grado = "Grado 12"):
        self._grupo = grupo
        self._asignaturas = asignaturas
        if self._asignaturas is None:
            self._asignaturas = []
        self.listadoAlumnos = estudiantes
        if self.listadoAlumnos is None:
            self.listadoAlumnos = []
        Grupo.grado = grado

    def listadoAsignaturas(self, **kwargs):
        for x in kwargs.values():
            self._asignaturas.append(Asignatura(x))

    def agregarAlumno(self, alumno, lista=None):
        if lista is None:
            lista = []
        lista.append(alumno)
        lista.sort()
        self.listadoAlumnos = self.listadoAlumnos + lista
        
        

    def __str__(self):
         return f"Grupo de estudiantes: {self._grupo}"


    @ classmethod
    def asignarNombre(cls, nombre="Grado 6"):
        cls.grado = nombre
