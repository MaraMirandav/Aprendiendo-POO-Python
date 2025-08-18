# Aprendiendo POO en Python

Proyecto realizado durante el segundo trimestre del **primer curso del Grado Superior en Desarrollo de Aplicaciones Multiplatadorma (DAM)**, como parte del módulo optativo de **Programación en Python**.  
Contiene ejercicios entregados por el profesor para practicar y reforzar los fundamentos de la **Programación Orientada a Objetos (POO)**.

## Objetivo
El propósito de estos ejercicios es aplicar los conceptos clave de la Programación Orientada a Objetos en Python:  
- Definición y uso de clases y objetos  
- Manejo de atributos, métodos y constructores  
- Práctica de encapsulamiento, herencia y polimorfismo  
- Uso de enumeraciones (enum) y métodos estáticos 
- Resolución de problemas con enfoque **orientado a objetos**  

## Estructura del repositorio

El repositorio incluye los siguientes ejercicios principales:

- **Ejercicio 1: Persona**  
  - Clase `Persona` con atributos: nombre, edad, sexo, peso y altura.  
  - Métodos para calcular el IMC, verificar si es mayor de edad y mostrar información.   

- **Ejercicio 2: Series**  
  - Clases `Serie` y `Videojuego` con atributos como título, género, entregado, y creador.  
  - Interfaz abstracta `Entregable` con métodos: entregar, devolver, is_entregado, compare_to.  
  - Comparación de objetos según temporadas u horas estimadas.

- **Ejercicio 3: Raíces**  
  - Clase `Raices` que resuelve una **ecuación de segundo grado**.  
  - Métodos: `getDiscriminante()`, `tieneRaices()`, `tieneRaiz()`, `obtenerRaices()` y `obtenerRaiz()`.  
  - Validaciones matemáticas y control de casos según el discriminante.  

- **Ejercicio 4: Aula**  
  - Clase base `Persona` y herencias `Estudiante` y `Profesor`.  
  - Clase `Aula` que gestiona alumnos, profesores y materias (usando `Enum`).  
  - Métodos para controlar **asistencia, notas y disponibilidad de clases**.  
  - `Main` ejecuta la simulación del aula.

- ** Ejercicio 5: Cine**  
  - Clase `Asientos`: gestiona asientos con `numpy` y `random`.  
  - Clase `Espectador`: representa a un espectador con nombre, edad y dinero.  
  - Clase `Pelicula`: contiene título, duración, edad mínima y director.  
  - Clase `Cine`: valida edad y dinero, gestiona pago y reserva de asientos (manual o aleatoria).  
  - Enum `Datos`: nombres de espectadores.  
  - Enum `datosPeliculas`: datos de películas.  
  - `Main` ejecuta la simulación completa de compra y reserva de entradas.

## Requisitos
- **Python 3.12.6**  
- Editor de código como **VSCode**, **PyCharm** o similar  

## Nota
- Estos ejercicios fueron realizados, según las indicaciones entregadas por el profesor del módulo. - Este repositorio tiene fines **educativos** y refleja mi progreso en el aprendizaje de Python durante el primer curso de DAM. 

## Reflexión sobre el aprendizaje adquirido

Estos ejercicios me permitieron comprender y aplicar correctamente los conceptos fundamentales de la Programación Orientada a Objetos en Python. Gracias a ello, aprendí lo siguiente:

- Estructurar y representar datos correctamente mediante la implementación de clases y objetos relacionados con entidades de la vida cotidiana. 
- Usar getters, setters y validaciones para proteger y manejar correctamente los datos.
- Usar herencia y polimorfismo: Reutilicé metodos y extendí clases para manejar objetos distintos tipos de objetos.  
- Uso de Enumeraciones (Enum) como herramienta, evitando errores y datos erróneos.  
- Trabajar con colecciones de objetos, como listas de estudiantes, espectadores del cine o asientos. 
- Resolución de problemas y lógica de programación, ya que ejercicios como `Cine` reforzaron la capacidad de descomponer problemas complejos de manera modular y paso a paso, aplicando las reglas de la Programación Orientada a Objetos.  
- Separar clases en archivos y usar un `Main` central
- Progreso personal, ya que superé dificultades iniciales con la lógica de programación y adquirí confianza para desarrollar proyectos más complejos, programando con mayor fluidez.
