while True:
    print ()
    num_1 = input('Digite um número: ')
    num_2 = input('Digite outro número: ')
    operador = input('Digite um operador: ')
    

    if not num_1.isnumeric() or not num_2.isnumeric():
        print('Error, apenas números.')
        continue

    num_1 = int(num_1)
    num_2 = int(num_2)

    # + - / *
    if operador == '+':
        print ('O resultado é: ',num_1 + num_2)
    elif operador == '-':
        print ('O resultado é: ',num_1 - num_2)
    elif operador == '/':
        print ('O resultado é: ',num_1 / num_2)
    elif operador == '*':
        print ('O resultado é: ',num_1 * num_2)
    else:
        print('Operador Invalido')

    sair = input('Deseja efetuar outro calculo ? [S]im ou [N]ão: ')
    if sair.lower() == 's':
        break
