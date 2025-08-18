import math

class Raices:
#Constructor:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

#Método para obtener el valor del discriminante
    def get_discriminante(self):
        discriminante = math.pow(self.b, 2) - (4 * self.a * self.c)
        return discriminante

#Método para indicar si tiene dos posibles soluciones
    def tiene_raices(self):
        if self.get_discriminante() > 0:
            return True
        else:
            return False

#Método para indicar si tiene una única solución
    def tiene_raiz(self):
        if self.get_discriminante() == 0:
            return True
        else:
            return False

#Método para obtener Raíces e imprimir las dos posibles soluciones
    def obtener_raices(self):
        if self.tiene_raices():
            resultado1 = (-self.b + math.sqrt(self.get_discriminante())) / (2 * self.a)
            resultado2 = (-self.b - math.sqrt(self.get_discriminante())) / (2 * self.a)
            print(f'La ecuación de segundo grado tiene dos posibles soluciones: {resultado1:.1f} y {resultado2:.1f}')

#Metodo para obtener Raiz e imprimir la posible solución
    def obtener_raiz(self):
        if self.tiene_raiz():
            resultado = (-self.b + math.sqrt(self.get_discriminante())) / (2 * self.a)
            print(f'La ecuación de segundo grado tiene una posible solución:{resultado:.1f}')

#Método para calcular la ecuación de segundo grado y mostrar posibles soluciones
    def calcular(self):
        if self.tiene_raices():
            self.obtener_raices()
        elif self.tiene_raiz():
            self.obtener_raiz()
        else:
            print('La ecuación de segundo grado no tiene soluciones dentro del conjunto de los números reales')