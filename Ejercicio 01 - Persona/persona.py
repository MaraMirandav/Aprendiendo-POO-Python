import math
import random

class Persona:
    #Constantes
    ##__SEXO_POR_DEFECTO = "H"
    __SEXOS_VALIDOS = ("H","M")
    __BAJO_PESO = -1
    __PESO_IDEAL = 0
    __SOBREPESO = 1
    __ERROR_PESO = -2

    #Constructor
    def __init__(self,nombre:str, edad:int, extranjero:bool, sexo:str = __SEXOS_VALIDOS[0], peso:float = 0, altura:float = 0):
        self.__nombre = nombre
        self.__edad = edad
        self.__extranjero = extranjero
        self.__dni_nie = self.generar_dni_nie()
        self.__sexo = self.comprobar_sexo(sexo)
        self.__peso = peso
        self.__altura = altura

    #Getter y Setter
    @property
    def nombre(self) -> str:
        return self.__nombre

    @nombre.setter
    def nombre(self,nombre) -> str:
        self.__nombre = nombre

    @property
    def edad(self) -> int:
        return self.__edad

    @edad.setter
    def edad(self,edad) -> int:
        self.__edad = edad

    @property
    def dni_nie(self) -> str:
        return self.__dni_nie

    @property
    def extranjero(self) -> bool:
        return self.__extranjero

    @extranjero.setter
    def extranjero(self,extranjero) -> bool:
        self.__extranjero = extranjero
        self.__dni_nie = self.generar_dni_nie()

    @property
    def sexo(self) -> str:
        return self.__sexo

    @sexo.setter
    def sexo(self,sexo) -> str:
        self.__sexo = sexo

    @property
    def peso(self) -> float:
        return self.__peso

    @peso.setter
    def peso(self,peso) -> float:
        self.__peso = peso

    @property
    def altura(self) -> float:
        return self.__altura

    @altura.setter
    def altura(self,altura) -> float:
        self.__altura = altura

    #Método para calcular IMC
    def calcular_imc(self) -> int:
        if self.altura <= 0:
            return Persona.__ERROR_PESO

        imc = self.peso / (self.altura / 100)**2
        if imc < 20:
            return Persona.__BAJO_PESO
        elif imc <= 25:
            return Persona.__PESO_IDEAL
        else:
            return Persona.__SOBREPESO

    #Método para determinar si es mayor de edad
    def es_mayor_de_edad(self) -> bool:
        return self.edad >= 18

    #Método comprobar el sexo de la persona
    def comprobar_sexo(self,sexo) -> str:
        if sexo not in Persona.__SEXOS_VALIDOS:
            return "H"
        else:
            return sexo

    #Método para generar DNI - NIE aleatorios
    def generar_dni_nie(self) -> str:
        letra = ('T','R','W','A','G','M','Y','F','P','D','X','B','N','J','Z','S','Q','V','H','L','C','K','E')

        if self.extranjero:
            digito_control_nie = random.randint(0,2)
            nie = random.randint(1000000,9999999)
            resto = nie % 23
            verificador = letra[resto]

            match(digito_control_nie):
                case 0:
                    letra_nie = "X"
                    dni_nie = f'{letra_nie}{nie}{verificador}'
                    return dni_nie
                case 1:
                    letra_nie = "Y"
                    dni_nie = f'{letra_nie}{nie}{verificador}'
                    return dni_nie
                case 2:
                    letra_nie = "X"
                    dni_nie = f'{letra_nie}{nie}{verificador}'
                    return dni_nie
        else:
            dni = random.randint(1000000,9999999)
            resto = dni % 23
            verificador = letra[resto]
            dni_nie = f'{dni}{verificador}'
            return dni_nie


    #Método Str:
    def __str__(self) -> str:
        return f'''Persona
    - Nombre : {self.nombre}
    - Edad : {self.edad}
    - ¿Es Extranjero? : {"Sí" if self.extranjero else "No"}
    - DNI / NIE : {self.dni_nie}
    - Sexo : {self.sexo}
    - Peso : {self.peso}
    - Altura : {self.altura}
                '''


if __name__ == "__main__":
    p1 = Persona("Abdul", 29, True)
    print(p1)
