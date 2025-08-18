from entregable import Entregable

class Series(Entregable):
    #Constantes
    __TEMPORADAS_POR_DEFECTO = 3
    __ENTREGADO_POR_DEFECTO = False


    #Constructor
    def __init__(self, titulo:str, genero:str, creador:str, numero_temporadas:int =  __TEMPORADAS_POR_DEFECTO, entregado:bool  =  __ENTREGADO_POR_DEFECTO):
        super().__init__()
        self.__titulo = titulo
        self.__genero = genero
        self.__creador = creador
        self.__numero_temporadas = numero_temporadas
        self.__entregado = entregado


    #Getter y Setter
    @property
    def titulo(self) -> str:
        return self.__titulo

    @titulo.setter
    def titulo(self, titulo : str) -> None:
        self.__titulo = titulo

    @property
    def numero_temporadas(self) -> int:
        return self.__numero_temporadas

    @numero_temporadas.setter
    def numero_temporadas(self, numero_temporadas : int) -> None:
        self.__numero_temporadas = numero_temporadas

    @property
    def genero(self) -> str:
        return self.__genero

    @genero.setter
    def genero(self, genero : str) -> None:
        self.__genero = genero

    @property
    def creador (self) -> str:
        return self.__creador

    @creador.setter
    def creador (self, creador : str) -> None:
        self.__creador = creador


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
    @staticmethod
    def compare_to(self,other) -> None:
        if isinstance(other,Series):
            if self.numero_temporadas > other.numero_temporadas:
                print(f'La serie {self.titulo} tiene más temporadas que la serie {other.titulo}')
            elif self.numero_temporadas < other.numero_temporadas:
                print(f'La serie {other.titulo} tiene más temporadas que la serie {self.titulo}')
            else:
                print(f'La serie {self.titulo} y la serie {other.titulo} tienen el mismo número de temporadas')


    #Método Str:
    def __str__(self) -> str:
        return f'''Serie {self.titulo}
    - Género : {self.genero}
    - Creador : {self.creador}
    - Número Temporadas : {self.numero_temporadas}
    - Entregado : {"Sí" if self.is_entregado() else "No"}
                '''


if __name__ == "__main__":
    
    ## SERIES
    Friends = Series("Friends","Comedia", "David Crane y Marta Kauffman",10)
    Sherlock = Series("Sherlock","Crimen","Steven Moffat y Mark Gatiss",4)
    TheOffice = Series("The Office", "Comedia", "Greg Daniels",9)
    BreakingBad = Series("Breaking Bad","Drama", "Vince Gilligan",5)
    StrangerThings = Series("Stranger Things","Ciencia Ficción", "The Duffer Brothers",4)
    
    Series.compare_to(TheOffice, Sherlock)