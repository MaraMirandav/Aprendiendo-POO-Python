from persona import Persona
from os import system

#Función IMC para mostrar el mensaje por pantalla del resultado
def resultado_imc(persona:Persona) -> None:
    imc = persona.calcular_imc()
    match(imc):
        case -1:
            resultado = "Bajo Peso"
            print(f"El resultado del IMC de {persona.nombre} indica: {resultado}\n")
        case 0:
            resultado = "Peso Ideal"
            print(f"El resultado del IMC de {persona.nombre} indica: {resultado}\n")
        case 1:
            resultado = "Sobrepeso"
            print(f"El resultado del IMC de {persona.nombre} indica: {resultado}\n")
        case _:
            resultado = "ERROR"
            print(f"El resultado del IMC de {persona.nombre} indica: {resultado} \n")

#Función para imprimir si una persona es mayor de edad por pantalla
def mayor_de_edad(persona:Persona) -> None:
    es_mayor_de_edad = persona.es_mayor_de_edad()
    print(f"¿{persona.nombre} es mayor de edad? = {es_mayor_de_edad}\n")

def ingresar_datos() -> Persona:
    nombre = input("Ingresa tu nombre: ")
    edad = int(input("Ingresa tu edad: "))
    extranjero = True if input("¿Eres extranjero? (S / N)").lower() == 's' else False
    sexo = input("Sexo : ")
    peso = float(input("Peso :"))
    altura = float(input("Altura : "))

    persona1 = Persona(nombre,edad,extranjero,sexo,peso,altura)
    persona2 = Persona(nombre=nombre,edad=edad,extranjero=extranjero,sexo=sexo)
    return persona1, persona2


if __name__ == "__main__":
    system("clear")

    #Instancia Persona 1 y Persona 2:
    persona1, persona2 = ingresar_datos()

    #Instancia Persona 3: Se asignan valores de Persona 1 y se cambian los atributos metodos set
    persona3 = Persona(persona1.nombre,persona1.edad,persona1.extranjero, persona1.sexo)
    persona3.nombre = "María"
    persona3.edad = 16
    persona3.extranjero = True
    persona3.sexo = "M"
    persona3.peso = 60
    persona3.altura = 158


    print("---------------------------- Persona 1 ----------------------------")
    print(persona1)
    mayor_de_edad(persona1)
    resultado_imc(persona1)
    print()
    print("---------------------------- Persona 2 ----------------------------")
    print(persona2)
    mayor_de_edad(persona2)
    resultado_imc(persona2)
    print()
    print("---------------------------- Persona 3 ----------------------------")
    print(persona3)
    mayor_de_edad(persona3)
    resultado_imc(persona3)
    print()