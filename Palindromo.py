""" 
DESAFIO PALINDROMO SEM DEF

palavra = input('Digite uma palavra: ')
palavra_inv = palavra[::-1]

if palavra == palavra_inv:
    print(f'{palavra} é um palindromo. ')
else:
    print(f'{palavra} não é um palindromo')
 """

"""DESAFIO PALINDROMO COM DEF"""

def quiz(palavra):
    return palavra == palavra[::-1]

palavra = input('Digite uma palavra: ')

if quiz(palavra):
     print (f'{palavra} é um palindromo')
else:
     print (f'{palavra} não é um palindromo')
