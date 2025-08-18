from random import random, uniform, choice
from enum_Materias import Materia

from persona import Persona

class Profesor(Persona):
    #Constructor
    def __init__(self,nombre:str, edad: int, sexo:str):
        self.__nombre = nombre
        self.__edad = edad
        self.__sexo = sexo
        self.__materia = self.asignar_materia()
        self.__asistencia = self.comprobar_asistencia()

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
    def materia(self) -> str:
        return self.__materia

    @property
    def asistencia(self):
        return self.__asistencia

    #Método para asignar al profesor una materia de forma aleatoria
    def asignar_materia(self) -> str:
        materia_aleatoria = choice(list(Materia)).value
        return materia_aleatoria

    #Método para comprobar asistencia de profesores (Polimorfismo)
    def comprobar_asistencia(self) -> bool:
        return (random() > 0.2)

    #Método Str:
    def __str__(self) -> str:
        return f'''Profesor {self.nombre}
    - Materia : {self.materia}
    - Asistencia : {"Presente" if self.asistencia else "Ausente"}
                '''
