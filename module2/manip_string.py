password = input("Saisir votre mot de passe : ")
if not len(password) > 6 :
    print('le mot de passe saisi est trop court; minimum saisissez 6 caracteres')
if not any(majuscule.isupper() for majuscule in password):
    print("votre mot de passe doit contenir une majuscule")
if not any(entier.isdigit() for entier in password) : 
    print("Votre mot de passe doit contenir un entier")