class voiture : 
    cpt = 0
    def __init__(self, marque, couleur, annee, km=0):
        self.marque = marque
        self.couleur = couleur
        self.annee = annee
        self.km = km
        self.cpt += 1
        self.__prix = 160000 # attribut private
    # getter ou accesseur , pour recuper le contenu d'un attribut
    def getPrix(self) : 
        return self.__prix
    # setter ou modificateur, pour modifier le contenu d'un attribut
    def setPrix(self, prix) : 
        self.__prix = prix

v1 = voiture('Tesla', 'Verte', 2020)
print(f'Marque : {v1.marque}')
print(f'Couleure : {v1.couleur}')
# avant modification du prix
print(f'Avant modification, Prix : {v1.getPrix()}')
# modification du prix avec le setter
v1.setPrix(900900)
# apres modification du prix
print(f'Apres modification, Prix : {v1.getPrix()}')