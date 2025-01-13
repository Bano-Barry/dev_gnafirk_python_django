# Effectuer un CRUD (Create, Read, Update, Delete) de comptes bancaires
from random import randint
class Account : 
    cpt = 0
    def __init__(self, name, password, phone):
        self.name = name 
        self.password = password
        self.phone = phone
        self.__solde = 0
        self.cpt += 1
        self.count_number = randint(111111, 999999)
    # retourner un objet string pour renommer l'objet
    def __str__(self):
        return f'N°Compte : {self.count_number} , Solde : {self.__solde}'
    # methode depot argent
    def depot(self, amount) : 
        self.__solde += amount
    # methode retrait argent
    def retrait(self, amount) : 
        if amount <= self.__solde : 
            self.__solde -= amount
            return True
        else : 
            print("Montant de retrait est superieur au solde")
            return False
        
              
account1 = Account("Lucien Damey", "Lucien1234", 612320201)
account2 = Account("Mohamed Sine Sangare", "Sine1234", 627530103)
print(f'Avant depot account1 : {account1}')
print(f'Avant depot account2 : {account2}')

account1.depot(5_000_000)
print(f'Apres depot account1 : {account1}')
account1.retrait(1_000_000)
print(f'Apres retrait account1 : {account1}')

def transfert(montant):
  verif = account1.retrait(montant)
  if verif:
      account2.depot(montant)
  else:
      print('transfert impossible')  

transfert(100_000)
print(f'apres le account1 : {account1}')
print(f'apres le account2 : {account2}')
