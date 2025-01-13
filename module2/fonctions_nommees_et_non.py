# def saluer_utilisateur(nom, *, prenom) : 
#     return print(f"bonjour {prenom}-{nom}")

# saluer_utilisateur('douno', prenom='fode')

# def tuplets(*args) :
#     print(args)
    
# tuplets(20, 'bano', 'genie informatique')

def dictionnaire (**kwargs):
    for cle, valeur in kwargs.items():
        print(f"cle = {cle} et valeur = {valeur}")
        
dictionnaire(a=5, b='fode')