from random import choice, randint
from os import system

from enum_datos import Datos
from enum_peliculas import datosPeliculas

from espectador import Espectador
from pelicula import Pelicula
from cine import Cine

#Función para generar espectadores
def generador_de_espectadores(cantidad:int) -> list[Espectador]:
    espectador:list[Espectador] = []
    for i in range(cantidad):
        edad = randint(3, 75)
        datos = choice(list(Datos)).value
        espectador.append(Espectador(datos, edad))
    return espectador


if __name__ == "__main__":
    system("clear")

    #Generando instancias de espectadores
    espectadores = generador_de_espectadores(8)
    espectador1 = espectadores[0]
    espectador2 = espectadores[1]
    espectador3 = espectadores[2]
    espectador4 = espectadores[3]
    espectador5 = espectadores[4]
    espectador6 = espectadores[5]
    espectador7 = espectadores[6]
    espectador8 = espectadores[7]

    #Generando instancia de peliculas
    pulp_fiction = datosPeliculas.PULP_FICTION
    matrix = datosPeliculas.MATRIX
    totoro = datosPeliculas.MI_VECINO_TOTORO

    pelicula_elegida = Pelicula(pulp_fiction)

    #Instancia de CINE
    sala_cine1 = Cine(pelicula_elegida,espectadores)

    #1) Sala de cine vacía
    print(sala_cine1)

    #2) Compra de dos asientos de forma aleatoria
    sala_cine1.comprar_asiento_aleatorio(espectador1,pelicula_elegida)
    print(str(espectador1))
    sala_cine1.comprar_asiento_aleatorio(espectador2,pelicula_elegida)
    print(str(espectador2))

    #3) Estado de la sala luego de la primera compra de entradas:
    print(sala_cine1)

    #4) Compra de dos asientos de forma aleatoria
    sala_cine1.comprar_asiento_aleatorio(espectador3,pelicula_elegida)
    print(str(espectador3))
    sala_cine1.comprar_asiento_aleatorio(espectador4,pelicula_elegida)
    print(str(espectador4))

    #5) Estado de la sala luego de la segunda compra de entradas:
    print(sala_cine1)

    #6) Consulta por Asiento disponible y lo compra de forma manual
    sala_cine1.comprobar_asiento_disponible(4,"D")
    sala_cine1.comprar_asiento_disponible(espectador5,pelicula_elegida,4,"D")
    print(str(espectador5))

    #7) Consulta por Asiento disponible y lo compra de forma manual
    sala_cine1.comprobar_asiento_disponible(2,"C")
    sala_cine1.comprar_asiento_disponible(espectador6,pelicula_elegida,2,"C")
    print(str(espectador6))

    #8) Estado de la sala luego de la tercera compra de entradas:
    print(sala_cine1)