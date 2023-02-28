print()
perguntas = {
    'Pergunta 1': {
        'pergunta': 'Quem é o atual campeao do Mr.Olympia? ',
        'respostas': {
            'A':'Had Chopan',
            'B':'Toguro',
            'C':'Xandao',
            'D':'Lee Priest',
        },
        'resposta_certa': 'A',
    },
    'Pergunta 2': {
        'pergunta': 'Qual o maior campeão do Mr.Olympia? ',
        'respostas': {
            'A':'Arnold',
            'B':'Ronnie Coleman',
            'C':'Sergio Oliva',
            'D':'Toguro',
        },
        'resposta_certa': 'B',
    },
}

chances = 2
resposta_certas = 0

for pk, pv in perguntas.items():
    print (f'{pk}: {pv["pergunta"]}')

    for rk, rv in pv["respostas"].items():
        print(f'[{rk}]: {rv}')
        
    resposta_usuario = input('Responda aqui: ')
    print()
    if resposta_usuario.isnumeric() or len(resposta_usuario)>=2:
        print ('Coloque apenas UMA letra das alternativas.')
        print()
        break
                    
    if resposta_usuario.upper() == pv['resposta_certa']:
        resposta_certas += 1
    else:
        chances -=1
        print()
    if chances == 0:
        print ('Você perdeu...')
        break
        
    qtd_perguntas = len(perguntas)
    if qtd_perguntas == resposta_certas:
        print('Booa Monstro')
    elif qtd_perguntas >=1:
        print ('Quase um monstro')




    
    
