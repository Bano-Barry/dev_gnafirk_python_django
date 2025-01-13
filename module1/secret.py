import random

secret = random.randint(0,20)
# while not (a == secret) : 
#     a = int(input("Entrez un nombre entre 0 et 20 : "))
    
# if a == secret : 
#     print("Vous avez trouve le nombre")


    
while True:
    a = input("Entrez un nombre entre 0 et 20 : ")
    if a.isdigit():
        a = int(a)
    else :
        print("La valeur saisie n'est pas un nombre")
        
    if secret == a : 
        print("Vous avez trouve le nombre secret ")
        break
    else :
        print("Reessayez !")