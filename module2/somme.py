# def somme(a,b) : 
#     return a + b
# print(f'somme = {somme(2,24)}')

try : 
    a = int(input('Entrez un premier nombre : '))
    b = int(input('Entrez un second nombre : '))
    print(f'division = {a / b}')
except Exception as e: 
    print(f'type de l\'exception :  {type(e)}')