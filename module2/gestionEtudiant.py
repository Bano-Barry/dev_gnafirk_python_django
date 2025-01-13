"""
Exercice 1 : Gestion des étudiants

Crée un dictionnaire pour stocker les informations d'un étudiant (nom, âge, niveau d'études, et moyenne).

1. Affiche toutes les informations de l'étudiant.
2. Modifie la moyenne de l'étudiant.
3. Ajoute une nouvelle clé mention avec la valeur "Bien" si la moyenne est supérieure ou égale à 7, sinon "Passable".
4. Affiche le dictionnaire mis à jour.
"""

etudiant = {
    'nom' : 'aminata diallo',
    'age' : 27, 
    'niveau' : 'L4', 
    'moyenne' : 8.5
}
# 1
print(etudiant)
# 2
etudiant['moyenne'] = 5
# 3
if etudiant['moyenne'] >= 7 :
    etudiant['mention'] = 'Bien'
else :
    etudiant['mention'] = 'Passable'
    
# 4
print(etudiant)