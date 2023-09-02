from classroom.asignatura import Asignatura

class Grupo:
    grado = None

    def __init__(self, grupo="grupo predeterminado", asignaturas = [], estudiantes = [], grado = "Grado 12"):
        self._grupo = grupo
        self._asignaturas = asignaturas
        self.listadoAlumnos = estudiantes
        self.listadoAlumnos.sort()
        Grupo.grado = grado

    def listadoAsignaturas(self, **kwargs):
        for x in kwargs.values():
            self._asignaturas.append(Asignatura(x))

    def agregarAlumno(self, alumno, lista=None):
        if lista is None:
            lista = []
        lista.append(alumno)
        self.listadoAlumnos = self.listadoAlumnos + lista
        self.listadoAlumnos.sort()
        

    def __str__(self):
         return f"Grupo de estudiantes: {self._grupo}"


    @ classmethod
    def asignarNombre(cls, nombre="Grado 6"):
        cls.grado = nombre
