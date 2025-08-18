from random import random, uniform, choice, randint
from enum_Materias import Materia

from estudiante import Estudiante
from profesor import Profesor

class Aula:
    CONTADOR_AULA = 0
    CAPACIDAD_MAXIMA_AULA = 10

#Constructor
    def __init__(self, profesor:Profesor, estudiantes:list[Estudiante]):
        self.id_aula = self.asignar_id()
        self.capacidad_maxima_aula = self.CAPACIDAD_MAXIMA_AULA
        self.materia_impartida = self.asignatura_aleatoria()
        self.profesor_encargado = profesor
        self.estudiantes = estudiantes

    #Método para asignar id
    def asignar_id(self) -> int:
        Aula.CONTADOR_AULA += 1
        return Aula.CONTADOR_AULA

    #Método para asignatura aleatoria
    def asignatura_aleatoria(self) -> str:
        materia_aleatoria = choice(list(Materia)).value
        return materia_aleatoria

    #Método para saber si el profesor enseña la materia
    def profesor_enseña_materia(self) -> bool:
        return self.profesor_encargado.materia == self.materia_impartida

    #Método para comprobar la asistencia de los estudiantes a clases
    def comprobar_asistencia_clase(self) -> bool:
        contador_presentes = 0
        contador_ausentes = 0

        for estudiantes in self.estudiantes:
            if estudiantes.comprobar_asistencia():
                contador_presentes += 1
            else:
                contador_ausentes += 1

        if contador_presentes > contador_ausentes:
            return True
        return False

    #Método que devuelve un str con la asistencia de los estudiantes
    def asistencia_final_estudiantes(self) -> str:
        contador_presentes = 0
        contador_ausentes = 0

        for estudiante in self.estudiantes:
            if estudiante.asistencia:
                contador_presentes += 1
            else:
                contador_ausentes += 1

        datos_asistencia = f"\n    Datos asistencia:\n"
        datos_asistencia += f"     - Presentes: {contador_presentes}\n"
        datos_asistencia += f"     - Ausentes : {contador_ausentes}\n"

        return datos_asistencia

    #Método que devuelve un str indicando aprobados y si se realizará clases
    def realizacion_clases(self) -> str:
        #Condiciones a evaluar
        profesor_correcto = self.profesor_enseña_materia()
        asistencia_suficiente = self.comprobar_asistencia_clase()
        clase_se_realiza = profesor_correcto and asistencia_suficiente
        clase_se_realiza_str = "Si" if clase_se_realiza else "No"
        #Contador mujeres / hombres
        mujeres_aprobadas = 0
        hombres_aprobados = 0

        for estudiante in self.estudiantes:
            if estudiante.sexo == "F" and estudiante.aprobado:
                mujeres_aprobadas += 1
            elif estudiante.sexo == "H" and estudiante.aprobado:
                hombres_aprobados += 1

        realizacion = f"¿Se realizará la clase? : {clase_se_realiza_str}\n"

        if clase_se_realiza:
            realizacion += f"\n    Estudiantes aprobados:\n"
            realizacion += f"      - Mujeres: {mujeres_aprobadas}\n"
            realizacion += f"      - Hombres : {hombres_aprobados}\n"
        else:
            realizacion += f"\n    Motivos\n"
            if profesor_correcto == False:
                realizacion += f"      - El profesor no enseña la materia\n"

            if asistencia_suficiente == False:
                realizacion += f"      - Demasiados estudiantes ausentes\n"
        return realizacion

    #Método Str:
    def __str__(self) -> str:
        #Para determinar si hay profesor para realizar la clase
        profe = self.profesor_encargado
        profesor_str = profe.nombre if profe else "No hay profesor disponible"
        profesor_materia_str = profe.materia if profe else "No hay profesor disponible"

        #Para imprimir el listado de estudiantes
        estudiantes_str = ""
        for estudiante in self.estudiantes:
            estudiantes_str += str(estudiante) +"\n"

        #En caso de que no hay estudiantes
        if not len(self.estudiantes):
            estudiantes_str += "No hay estudiantes inscritos"

        return f'''
    ------------------------------------------------------
    AULA {self.id_aula}
    - Capacidad Máxima : {self.capacidad_maxima_aula}
    - Materia Impartida : {self.materia_impartida}
    - Profesor Encargado : {profesor_str}
    - El profesor enseña : {profesor_materia_str}
    ------------------------------------------------------
    ESTUDIANTES:
    {estudiantes_str}
    ------------------------------------------------------
    INFORMACIÓN DE LA CLASE
    {self.asistencia_final_estudiantes() if self.estudiantes else ''}
    {self.realizacion_clases() if self.estudiantes else ''}
    '''
