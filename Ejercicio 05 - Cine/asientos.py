from numpy import zeros
from random import randint

class Asientos:
    #Constantes:
    __letras = ["A","B","C","D","E","F","G","H","I"]
    __FILAS = 8
    __COLUMNAS = 9
    __DISPONIBILIDAD = True

    #Constructor
    def __init__(self, filas:int = __FILAS, columnas:int = __COLUMNAS, disponible:bool = __DISPONIBILIDAD):
        self.__filas = filas
        self.__columnas = columnas
        self.__disponible = disponible
        self.__espacios = zeros([filas,columnas],dtype=int)

    #Getter
    @property
    def filas(self) -> int:
        return self.__filas

    @property
    def columnas(self) -> int:
        return self.__columnas

    @property
    def disponible(self) -> bool:
        return self.__disponible

    @property
    def espacios(self) -> list[list[int]]:
        return self.__espacios

    #Método para determinar si un asiento está disponible (0)
    def esta_disponible(self, fila:int, columna:int) -> bool:
        return self.espacios[fila][columna] == 0

    #Método para ocupar un asiento (1)
    def ocupar_asiento(self, numero:int, letra:str) -> None:
        fila = numero - 1
        columna = Asientos.__letras.index(letra)

        if self.esta_disponible(fila,columna):
            self.espacios[fila,columna] = 1

    #Método para encontrar un asiento libre aleatorio
    def buscar_asiento_libre_aleatorio(self) -> tuple[int]:
        asiento_encontrado = (0,0)
        encontrado = False

        while(not encontrado):
            fila = randint(0,self.filas-1)
            columna = randint(0,self.columnas-1)

            if(self.esta_disponible(fila,columna)):
                encontrado = True
                asiento_encontrado = (fila,columna)
                return asiento_encontrado
        return None

    #Método para reservar asiento libre aleatorio
    def reservar_asiento_aleatorio(self) -> None:
        asiento_encontrado = self.buscar_asiento_libre_aleatorio()
        columna = asiento_encontrado[1]
        fila = asiento_encontrado[0]

        if asiento_encontrado is not None:
            self.ocupar_asiento(fila+1,Asientos.__letras[columna])

    #Método para buscar asiento libre con numero y letra
    def buscar_asiento_libre(self, numero:int, letra:str) -> tuple[int]:
        asiento_encontrado = (0,0)
        fila = numero - 1
        columna = Asientos.__letras.index(letra)

        if self.esta_disponible(fila,columna):
            asiento_encontrado = (fila,columna)
            return asiento_encontrado
        return None

    #Método para reservar un asiento libre manualmente
    def reservar_asiento_libre(self, numero: int, letra:str) -> None:
        asiento_encontrado = self.buscar_asiento_libre(numero,letra)

        if asiento_encontrado is not None:
            fila,columna = asiento_encontrado
            posicion_columna = Asientos.__letras[columna]
            self.ocupar_asiento(fila+1,posicion_columna)
            print("-------------------------------------------------")
            print(f"¡Felicidades! Has reservado el asiento [{fila+1}-{posicion_columna}]")
            print("-------------------------------------------------")

    #Método para imprimir los asientos de la sala de cine
    def imprimir_asientos(self) -> str:
        asientos = ''
        for i in range(self.filas-1,-1,-1):
            for j in range(self.columnas):
                if self.espacios[i][j] == 0:
                    asientos += f'[{i+1}-{Asientos.__letras[j]}]'
                else:
                    asientos += '[ X ]'
            asientos += "\n"
        return asientos

    #Método Str:
    def __str__(self) -> str:
        asientos = self.imprimir_asientos()
        return f'\nRevisa los asientos del cine: \n\n{asientos}\n'

if __name__ == "__main__":
    asiento = Asientos()
    asiento.reservar_asiento_aleatorio()
    asiento.reservar_asiento_libre(7,"H")
    print(asiento)
