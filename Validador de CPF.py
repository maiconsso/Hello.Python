# cpf = 16899535009

while True:
    cpf = input('Digite o CPF: ')
    novo_cpf = cpf[:-2]
    reverso = 10
    total = 0
    cpf_valido = len(cpf)

    if not novo_cpf.isnumeric() or not cpf_valido ==(11):
        print('O CPF deve conter 11 números apenas.')      
        break

    for index in range(19):
        if index > 8:
            index -=9

        total += int(novo_cpf[index]) * reverso
        
        reverso -=1
        if reverso < 2:
            reverso = 11
            d = 11 - (total % 11)
            
            if d > 9:
                d = 0
            total = 0
            novo_cpf += str(d)

    sequencia = novo_cpf == str(novo_cpf[0]) * len(cpf)

    if cpf == novo_cpf and not sequencia:
        print ('CPF Válido')

    else:
        print ('CPF Invalido')

    sair = input('Deseja pesquisar outro CPF ? [S]im ou [N]ão: ')

    if sair.lower() == 's': 
        break
