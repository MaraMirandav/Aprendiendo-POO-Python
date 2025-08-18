from os import system
from series import Series
from videojuego import Videojuego
from entregable import Entregable

#Método para indicar cuantas Series fueron entregadas
def cuantas_series_entregadas(lista : list):
    contador_series = 0
    for object in lista:
        if isinstance(object,Series):
            if object.is_entregado():
                contador_series += 1
    if contador_series > 0:
        print(f'Hay {contador_series} series entregadas\n')
    else:
        print("No hay series entregadas\n")

#Método para indicar cuantas Videojuegos fueron entregados
def cuantas_videojuegos_entregados(lista : list):
    contador_videojuegos = 0
    for object in lista:
        if isinstance(object,Videojuego):
            if object.is_entregado():
                contador_videojuegos += 1
    if contador_videojuegos > 0:
        print(f'Hay {contador_videojuegos} videojuegos entregados\n')
    else:
        print("No hay videojuegos entregados\n")

#Método para indicar la serie con mayor número de temporadas
def mayor_numero_temporadas(lista : list):
    serie_max = lista[0]
    for serie in lista[1:]:
        if serie.numero_temporadas > serie_max.numero_temporadas:
            serie_max = serie
    print(f"La serie con mayor número de temporadas es {serie_max.titulo} con {serie_max.numero_temporadas} temporadas\n")
    print(serie_max)
    print()

#Método para indicar el videojuego con mayor número de horas estimadas
def mayor_horas_estimadas(lista : list):
    videojuego_max = lista[0]
    for videojuego in lista[1:]:
        if videojuego.horas_estimadas > videojuego_max.horas_estimadas:
            videojuego_max = videojuego
    print(f"El videojuego con más horas estimadas es {videojuego_max.titulo} con {videojuego_max.horas_estimadas} horas estimadas\n")
    print(videojuego_max)
    print()


#Método compare to (desde el Método abstracto)
def compare_to(objeto1, objeto2):
    if isinstance(objeto1, Videojuego) and isinstance(objeto2, Videojuego):
        if objeto1.horas_estimadas > objeto2.horas_estimadas:
            print(f'El videojuego {objeto1.titulo} tiene horas estimadas que el videojuego {objeto2.titulo}')
        elif objeto1.horas_estimadas < objeto2.horas_estimadas:
            print(f'El videojuego {objeto2.titulo} tiene más horas estimadas que el videojuego {objeto1.titulo}')
        else:
            print(f'El videojuego {objeto1.titulo} y el videojuego {objeto2.titulo} tienen la misma cantidad de horas estimadas')

    if isinstance(objeto1, Series) and isinstance(objeto2, Series):
        if objeto1.numero_temporadas > objeto2.numero_temporadas:
            print(f'La serie {objeto1.titulo} tiene más temporadas que la serie {objeto2.titulo}')
        elif objeto1.numero_temporadas < objeto2.numero_temporadas:
            print(f'La serie {objeto2.titulo} tiene más temporadas que la serie {objeto1.titulo}')
        else:
            print(f'La serie {objeto1.titulo} y la serie {objeto2.titulo} tienen el mismo número de temporadas')

    if isinstance(objeto1, Series) and isinstance(objeto2,Videojuego):
        if objeto1.numero_temporadas > objeto2.horas_estimadas:
            print(f'La serie {objeto1.titulo} tiene más temporadas que el video juego {objeto2.titulo}')
        elif objeto1.numero_temporadas < objeto2.horas_estimadas:
            print(f'El videojuego {objeto2.titulo} tiene más horas estimadas que la serie {objeto1.titulo}')
        else:
            print(f'La serie {objeto1.titulo} y el videojuego {objeto2.titulo} tienen la misma cantidad de temporadas y horas estimadas más horas estimadas')

def comparito_to(*args: Entregable): # *(3,4,5,6,4)
    maximo = 0
    objeto :Entregable = None
    for i in args:
        if isinstance(i, Series):
            if i.numero_temporadas > maximo:
                maximo = i.numero_temporadas
                objeto = i
        elif isinstance(i, Videojuego):
            if i.horas_estimadas > maximo:
                maximo = i.horas_estimadas
                objeto = i
    if isinstance(objeto, Videojuego): print(f"El video juego con más horas es: {objeto.titulo} con {objeto.horas_estimadas}")
    if isinstance(objeto, Series): print(f"La serie con más temporadas es: {objeto.titulo} con {objeto.numero_temporadas}")

if __name__ == '__main__':
    system("clear")

    #INSTANCIAS DE SERIES
    Friends = Series("Friends","Comedia", "David Crane y Marta Kauffman",10)
    Sherlock = Series("Sherlock","Crimen","Steven Moffat y Mark Gatiss",4)
    TheOffice = Series("The Office", "Comedia", "Greg Daniels",9)
    BreakingBad = Series("Breaking Bad","Drama", "Vince Gilligan",5)
    StrangerThings = Series("Stranger Things","Ciencia Ficción", "The Duffer Brothers",4)

    #Lista de Series vacia
    series = []

    #Agregando "series" en la lista series
    series.append(Friends)
    series.append(Sherlock)
    series.append(TheOffice)
    series.append(BreakingBad)
    series.append(StrangerThings)

    #Series entregadas
    Friends.entregar()
    Sherlock.entregar()

    print("---------------------------- Series ----------------------------")
    cuantas_series_entregadas(series)
    mayor_numero_temporadas(series)


    #INSTANCIAS DE VIDEOJUEGOS
    TheLastOfUs = Videojuego("The Last of Us", "Acción", "Naughty Dog",20)
    SuperMario64 = Videojuego("Super Mario 64", "Plataformas", "Nintendo",15)
    MetalGearSolid = Videojuego("Metal Gear Solid", "Sigilo", "Konami",20)
    Minecraft = Videojuego("Minecraft", "Aventura", "Mojang",100)
    StardewValley = Videojuego("Stardew Valley", "Simulación", "ConcernedApe",70)

    #Lista de Videojuegos vacia
    videojuegos = []

    #Agregando "videojuegos" en la lista videojuegos
    videojuegos.append(TheLastOfUs)
    videojuegos.append(SuperMario64)
    videojuegos.append(MetalGearSolid)
    videojuegos.append(Minecraft)
    videojuegos.append(StardewValley)

    #Videojuegos entregadas
    StardewValley.entregar()
    TheLastOfUs.entregar()
    Minecraft.entregar()

    print("------------------------- Videojuegos -------------------------")
    cuantas_videojuegos_entregados(videojuegos)
    mayor_horas_estimadas(videojuegos)


    #Comparación entre videojuegos y series
    print("------------------------- COMPARACIÓN -------------------------")
    compare_to(TheOffice, Sherlock)
    compare_to(TheLastOfUs,StardewValley)
    compare_to(StrangerThings,MetalGearSolid)
    print()
