a = int(input("Veillez saisir le nombre souhaite : "))
fact = 1
compt = 1

while compt <= a :
    fact *= compt
    compt += 1
    
print(f"la factorielle de {a} est {fact}")
