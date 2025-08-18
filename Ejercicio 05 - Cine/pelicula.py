from enum_peliculas import datosPeliculas

class Pelicula:
    def __init__(self,datos:datosPeliculas):
        self.__titulo = datos.titulo
        self.__duracion = datos.duracion
        self.__edad_minima = datos.edad_minima
        self.__director = datos.director

    @property
    def titulo(self):
        return self.__titulo

    @property
    def duracion(self):
        return self.__duracion

    @property
    def edad_minima(self):
        return self.__edad_minima

    @property
    def director(self):
        return self.__director


    #Método Str:
    def __str__(self) -> str:
        return f'''
    - Título : {self.titulo}
    - Duración : {self.duracion} horas
    - Edad Mínima : {self.edad_minima} años
    - Director : {self.director}
    '''