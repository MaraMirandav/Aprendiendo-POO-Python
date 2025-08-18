from random import choice, randint
from os import system
from datos import Datos

from estudiante import Estudiante
from profesor import Profesor
from aula import Aula

#Función para generar estudiantes
def generador_de_estudiantes(cantidad:int) -> list[Estudiante]:
    estudiantes:list[Estudiante] = []
    for i in range(cantidad):
        edad = randint(17, 25)
        datos = choice(list(Datos)).value
        estudiantes.append(Estudiante(datos[0], edad, datos[1]))
    return estudiantes

#Función para generar profesores
def generador_de_profesores(cantidad:int) -> list[Profesor]:
    profesores:list[Profesor] = []
    for i in range(cantidad):
        edad = randint(35, 65)
        datos = choice(list(Datos)).value
        profesores.append(Profesor(datos[0], edad, datos[1]))
    return profesores

if __name__ == "__main__":
    system("clear")

    #Creación de listas de estudiantes y profesores
    estudiantes = generador_de_estudiantes(8)
    profesores = generador_de_profesores(2)

    #Instancia de aula 1
    aula1 = Aula(profesores[0],estudiantes)
    print(aula1)

    print()

    #Instancia de aula 2
    aula2 = Aula(profesores[1],estudiantes)
    print(aula2)
