from abc import ABC,abstractmethod

class Persona(ABC):
    #Constructor
    def __init__(self,nombre:str, edad:int, sexo:str):
        self.__nombre = nombre
        self.__edad = edad
        self.__sexo = sexo

    @property
    def nombre(self):
        return self.__nombre

    @property
    def edad(self):
        return self.__edad

    @property
    def sexo(self):
        return self.__sexo

    def comprobar_asistencia(self) -> bool:
        pass

