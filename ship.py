x: int
y: int

class Ship:
    name: str
    components: {(x, y): bool} #Coordonnées à entrer
    vitality: int #Nombre de composants intacts (non touché ni coulé)
    fleet:str #Catégorie de navir


    def __init__(self, name, components, fleet):
        self.name:name
        self.components:components
        self.fleet: fleet

    def __str__(self):
        pass

    def is_hit(self, shot_coord):
        pass

    def is_sunk(self):
        pass

    def analyze_shot(self, shot_coord):
        pass
