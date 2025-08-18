from pelicula import Pelicula
from asientos import Asientos
from espectador import Espectador

class Cine:
    #Constantes
    PRECIO_ENTRADA = 5.50
    LETRAS_ASIENTOS = ["A","B","C","D","E","F","G","H","I"]

    def __init__(self, pelicula:Pelicula, espectador: list[Espectador], precio_entrada = PRECIO_ENTRADA):
        self.__pelicula = pelicula
        self.__asientos = Asientos()
        self.__espectador = espectador
        self.__precio_entrada = precio_entrada

    #Getter
    @property
    def pelicula(self):
        return self.__pelicula

    @property
    def precio_entrada(self):
        return self.__precio_entrada

    @property
    def asientos(self):
        return self.__asientos

    @property
    def espectador(self):
        return self.__espectador

    #Método para determinar si el espectador cumple con la edad minima
    def tiene_edad_minima(self,espectador:Espectador,pelicula:Pelicula ) -> bool:
        return espectador.edad >= pelicula.edad_minima

    #Método para determinar si el espectador cuenta con el dinero suficiente
    def tiene_dinero_suficiente(self, espectador:Espectador) -> bool:
        return espectador.dinero >= self.precio_entrada

    #Método para pagar la entrada del cine
    def pagar_entrada(self, espectador:Espectador) -> None:
        saldo = espectador.dinero - self.precio_entrada
        espectador.dinero = saldo

    #Método para comprar entradas de manera Aleatoria, validando las condiciones
    def comprar_asiento_aleatorio(self, espectador:Espectador, pelicula:Pelicula) -> None:
        edad_minima = self.tiene_edad_minima(espectador,pelicula)
        dinero_suficiente = self.tiene_dinero_suficiente(espectador)
        asiento_disponible = (self.asientos.buscar_asiento_libre_aleatorio() is not None)

        if edad_minima and dinero_suficiente and asiento_disponible:
            self.asientos.reservar_asiento_aleatorio()
            self.pagar_entrada(espectador)
            print(f'-------------------------------------------------')
            print(f'Película : {pelicula.titulo}\n')
            print(f'- Precio entrada : {self.precio_entrada:.2f} €\n')
            print(f'- Entrada de {espectador.nombre} comprada con éxito\n')
            print(f'-------------------------------------------------')

        elif not edad_minima and not dinero_suficiente:
            print(f'-------------------------------------------------')
            print(f'Lo siento, {espectador.nombre}, no puedes comprar entradas porque:\n')
            print(f'- No tienes la edad mínima para ver la película\n')
            print(f'- No tienes dinero suficiente para pagar la entrada\n')
            print(f'-------------------------------------------------')

        elif not edad_minima:
            print(f'-------------------------------------------------')
            print(f'"Lo siento, {espectador.nombre}, no tienes la edad mínima para ver la película\n')
            print(f'-------------------------------------------------')

        elif not dinero_suficiente:
            print(f'-------------------------------------------------')
            print(f'Lo siento, {espectador.nombre}, no tienes dinero suficiente para pagar la entrada\n')
            print(f'-------------------------------------------------')

        elif not asiento_disponible:
            print(f'-------------------------------------------------')
            print(f'Lo siento, {espectador.nombre}, no hay asientos disponibles\n')
            print(f'-------------------------------------------------')
        else:
            print(f'-------------------------------------------------')
            print(f'Lo siento, {espectador.nombre}, no puedes comprar entradas porque:\n')
            print(f'- No tienes la edad mínima para ver la película\n')
            print(f'- No tienes dinero suficiente para pagar la entrada\n')
            print(f'- No hay asientos disponibles\n')
            print(f'-------------------------------------------------')

    #Método para comprobar si el asiento se encuentra disponible para comprarlo de manera manual
    def comprobar_asiento_disponible(self, numero:int, letra:str) -> None:
        fila = numero -1
        columna = Cine.LETRAS_ASIENTOS.index(letra)
        posicion_columna = Cine.LETRAS_ASIENTOS[columna]

        if self.asientos.esta_disponible(fila,columna):
            print(f'-------------------------------------------------')
            print(f'El espacio [{fila+1}-{posicion_columna}] está disponible\n')
            print(f'-------------------------------------------------')
        else:
            print(f'-------------------------------------------------')
            print(f'El espacio [{fila+1}-{posicion_columna}] no está disponible\n')
            print(f'-------------------------------------------------')

    #Método para comprar entradas de manera manual y escogiendo asiento, validando las condiciones
    def comprar_asiento_disponible(self, espectador:Espectador, pelicula:Pelicula, fila:int, columna:str) -> None:
        edad_minima = self.tiene_edad_minima(espectador,pelicula)
        dinero_suficiente = self.tiene_dinero_suficiente(espectador)
        asiento_disponible = (self.asientos.buscar_asiento_libre(fila,columna) is not None)

        if edad_minima and dinero_suficiente and asiento_disponible:
            self.asientos.reservar_asiento_libre(fila,columna)
            self.pagar_entrada(espectador)
            print(f'Película : {pelicula.titulo}')
            print(f'- Precio entrada : {self.precio_entrada:.2f} €')
            print(f'- Entrada de {espectador.nombre} comprada con éxito')
            print(f'-------------------------------------------------')

        elif not edad_minima and not dinero_suficiente:
            print(f'-------------------------------------------------')
            print(f'Lo siento, {espectador.nombre}, no puedes comprar entradas porque:')
            print(f'- No tienes la edad mínima para ver la película')
            print(f'- No tienes dinero suficiente para pagar la entrada')
            print(f'-------------------------------------------------')

        elif not edad_minima:
            print(f'-------------------------------------------------')
            print(f'"Lo siento, {espectador.nombre}, no tienes la edad mínima para ver la película\n')
            print(f'-------------------------------------------------')

        elif not dinero_suficiente:
            print(f'-------------------------------------------------')
            print(f'Lo siento, {espectador.nombre}, no tienes dinero suficiente para pagar la entrada\n')
            print(f'-------------------------------------------------')

        elif not asiento_disponible:
            print(f'-------------------------------------------------')
            print(f'Lo siento, {espectador.nombre}, no hay asientos disponibles\n')
            print(f'-------------------------------------------------')
        else:
            print(f'-------------------------------------------------')
            print(f'Lo siento, {espectador.nombre}, no puedes comprar entradas porque:\n')
            print(f'- No tienes la edad mínima para ver la película\n')
            print(f'- No tienes dinero suficiente para pagar la entrada\n')
            print(f'- No hay asientos disponibles\n')
            print(f'-------------------------------------------------')

    #Método Str:
    def __str__(self) -> str:

        return f'''
-------------------------------------------------------------------------------------
Información sobre la función:''' + str(self.pelicula) + f'''
- Precio Entrada : {self.precio_entrada:.2f} €\n''' + str(self.asientos)