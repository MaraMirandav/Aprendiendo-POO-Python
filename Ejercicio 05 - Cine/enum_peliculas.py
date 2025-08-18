from enum import Enum

class datosPeliculas(Enum):
    CASABLANCA = ("Casablanca", 1.82, 12, "Michael Curtiz")
    EL_PADRINO = ("El Padrino", 2.92, 17, "Francis Ford Coppola")
    FIGHT_CLUB = ("Fight Club", 2.31, 18, "David Fincher")
    MATRIX = ("Matrix", 2.25, 16, "Lana y Lilly Wachowski")
    FORREST_GUMP = ("Forrest Gump", 2.22, 12, "Robert Zemeckis")
    EL_SENOR_DE_LOS_ANILLOS = "El Señor de los Anillos: La Comunidad del Anillo", 2.98, 13, "Peter Jackson"
    TITANIC = "Titanic", 3.15, 13, "James Cameron"
    PULP_FICTION = "Pulp Fiction", 2.58, 18, "Quentin Tarantino"
    LA_VIDA_ES_BELLA = "La Vida es Bella", 1.87, 10, "Roberto Benigni"
    HARRY_POTTER_AZKABAN = "Harry Potter y el Prisionero de Azkaban", 2.22, 10, "Alfonso Cuarón"
    TOY_STORY = "Toy Story", 1.33, 6, "John Lasseter"
    MI_VECINO_TOTORO = "Mi Vecino Totoro", 1.28, 6, "Hayao Miyazaki"
    EL_VIAJE_DE_CHIHIRO = "El Viaje de Chihiro", 2.05, 10, "Hayao Miyazaki"

    def __init__(self, titulo:str, duracion:float, edad_minima: int, director:str):
        self.titulo = titulo
        self.duracion = duracion
        self.edad_minima = edad_minima
        self.director = director
