from random import random, uniform, choice
from enum_Materias import Materia

from persona import Persona

class Estudiante(Persona):
    #Constructor

    def __init__(self,nombre, edad, sexo):
        self.__nombre = nombre
        self.__edad = edad
        self.__sexo = sexo
        self.__asistencia = self.comprobar_asistencia()
        self.__calificacion = self.calificacion_aleatoria()
        self.__aprobado = self.es_aprobado()

#Getter y Setter
    @property
    def nombre(self) -> str:
        return self.__nombre
    @property
    def edad(self) -> int:
        return self.__edad

    @property
    def sexo(self) -> str:
        return self.__sexo

    @property
    def asistencia(self) -> bool:
        return self.__asistencia

    @property
    def calificacion(self) -> float:
        return self.__calificacion

    @property
    def aprobado(self):
        return self.__aprobado

    #Método para generar calificaciones aleatorias a los estudiantes
    def calificacion_aleatoria(self) -> int:
        calificacion = round(uniform(0,10), 1)
        return calificacion

    #Método para comprobar asistencia de estudiantes (Polimorfismo)
    def comprobar_asistencia(self) -> bool:
            return (random() > 0.5)

    #Método para comprobar el estudiante ha aprobado
    def es_aprobado(self) -> bool:
        return self.calificacion >= 5.0

    #Método Str:
    def __str__(self) -> str:
        return f'''
    - Nombre : {self.nombre}
        Asistencia : {"Presente" if self.asistencia else "Ausente"}
        Calificación : {self.calificacion}
        Aprobado : {"Aprobado" if self.aprobado else "Reprobado"}'''