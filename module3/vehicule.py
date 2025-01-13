# concepts heritage

#classe mere
class Vehicule : 
    def __init__(self, marque, couleur, annee, km=0):
        self.marque = marque
        self.couleur = couleur
        self.annee = annee
        self.km = km
# classe fille voiture
class Voiture(Vehicule) : 
    def __init__(self,):
        super().__init__()

# classe fille moto