from random import randint

class Espectador:
    #Constructor
    def __init__(self, nombre: str, edad:int):
        self.__nombre = nombre
        self.__edad = edad
        self.__dinero = self.asignar_dinero()

    @property
    def nombre(self):
        return self.__nombre

    @property
    def edad(self):
        return self.__edad

    @property
    def dinero(self):
        return self.__dinero

    @dinero.setter
    def dinero(self,dinero):
        self.__dinero = dinero

    #Método para asignar dinero al espectador
    def asignar_dinero(self) -> float:
        dinero = randint(5,50)
        if self.edad >= 18:
            return dinero
        elif self.edad > 6 and self.edad < 18:
            return dinero / 2.00
        return 0

    #Método Str:
    def __str__(self) -> str:
        dinero_str = f'{self.dinero:.2f} €'
        return f'''Datos del Espectador :
    - Nombre : {self.nombre}
    - Edad : {self.edad} años
    - Dinero : {dinero_str}
    '''