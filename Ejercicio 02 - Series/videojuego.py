from entregable import Entregable

class Videojuego(Entregable):
    #Constantes
    __HORAS_ESTIMADAS_POR_DEFECTO = 10
    __ENTREGADO_POR_DEFECTO = False

    #Constructor
    def __init__(self, titulo:str, genero:str, creador:str, horas_estimadas:int = __HORAS_ESTIMADAS_POR_DEFECTO, entregado:bool = __ENTREGADO_POR_DEFECTO):
        super().__init__()
        self.__titulo = titulo
        self.__genero = genero
        self.__creador = creador
        self.__horas_estimadas = horas_estimadas
        self.__entregado = entregado

    #Getter y Setter
    @property
    def titulo(self) -> str:
        return self.__titulo

    @titulo.setter
    def titulo(self, titulo : str) -> None:
        self.__titulo = titulo

    @property
    def genero(self) -> str:
        return self.__genero

    @genero.setter
    def genero(self, genero : str) -> None:
        self.__genero = genero

    @property
    def creador(self) -> str:
        return self.__creador

    @creador.setter
    def creador(self, creador : str) -> None:
        self.__creador =creador

    @property
    def horas_estimadas(self) -> str:
        return self.__horas_estimadas

    @horas_estimadas.setter
    def horas_estimadas(self, horas_estimadas : str) -> None:
        self.__horas_estimadas = horas_estimadas


    #Método Entregar (desde el Método abstracto)
    def entregar(self):
        self.__entregado = True

    #Método Devolver (desde el Método abstracto)
    def devolver(self):
        self.__entregado = False

    #Método isEntregado (desde el Método abstracto)
    def is_entregado(self) -> bool:
        return self.__entregado


    #Método compare to (desde el Método abstracto)
    def compare_to(self, other) -> None:
        if isinstance(other, Videojuego):
            if self.horas_estimadas > other.horas_estimadas:
                print(f'El videojuego {self.titulo} tiene más horas estimadas que el videojuego {other.titulo}')
            elif self.horas_estimadas < other.horas_estimadas:
                print(f'El videojuego {other.titulo} tiene más horas estimadas que el videojuego {self.titulo}')
            else:
                print(f'El videojuego {self.titulo} y el videojuego {other.titulo} tienen la misma cantidad de horas estimadas')

    #Método Str:
    def __str__(self) -> str:
        return f'''Videojuego {self.titulo}
    - Género : {self.genero}
    - Creador : {self.creador}
    - Horas Estimadas de juego : {self.horas_estimadas}
    - Entregado : {("Sí" if self.is_entregado() else "No")}
    '''

if __name__ == "__main__":
    pass