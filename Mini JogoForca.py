secreto = 'academia'
digitadas = []
chances = 3

while True:
    if chances <= 0:
        print ('Você perdeu !!!')
        break
    
    letra = input('Digite uma letra para descobrir qual a palavra secreta: ')

    if letra not in secreto:
        chances -= 1
    print (f'Você ainda tem mais {chances} chances. ')
    print()

    if len(letra) > 1:
        print ('Ahh isso não vale, digite apenas uma letra.')
        continue

    digitadas.append(letra)

    if letra in secreto:
        print(f'UHUUUUULL, você acertou a letra "{letra}". ')
    else:
        print(f'affz, você errou a letra "{letra}" não existe')
        digitadas.pop()
    
    secreto_temporario = ''
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'
    
    if secreto_temporario == secreto:
        print(f'BOOOA, VOCÊ GANHOU !!! a palavra secreta era "{secreto_temporario}". ')
        break
    else:
        print (f'A palavra secreta esta assim: "{secreto_temporario}"')
    
    