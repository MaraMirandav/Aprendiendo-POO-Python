from os import system
from raices import Raices

if __name__ == '__main__':
    system("clear")

    #Instancia ecuación 1:
    print("-------------------------- Primera Ecuación --------------------------")
    ecuacion1 = Raices(-1,7,-10)
    print(f"Discriminante = {ecuacion1.get_discriminante()}")
    ecuacion1.calcular()
    print("\n")

    #Instancia ecuación 2:
    print("-------------------------- Segunda Ecuación --------------------------")
    ecuacion2 = Raices(1,-4,4)
    print(f"Discriminante = {ecuacion2.get_discriminante()}")
    ecuacion2.calcular()
    print("\n")

    #Instancia ecuación 3:
    print("-------------------------- Tercera Ecuación --------------------------")
    ecuacion3 = Raices(1,0,6)
    print(f"Discriminante = {ecuacion3.get_discriminante()}")
    ecuacion3.calcular()
    print("\n")