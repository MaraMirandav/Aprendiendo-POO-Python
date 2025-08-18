from enum import Enum

class Materia(Enum):
    M1 = "Matemáticas"
    M2 = "Física"
    M3 = "Filosofía"

if __name__ == "__main__":
    for i in Materia:
        print(i.value)
