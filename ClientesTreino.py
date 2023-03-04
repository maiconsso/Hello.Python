""" print(f"{'Exercicio':^30} | {'Séries':^6} | {'Repetições':^15}")


for pessoa in treino:
    d = treino[pessoa]
    print(f"{d['exercicio']:<30} | {d['series']:^6} | {d['repeticoes']:>15}") """


treino_h = {
    '0': {'exercicio': '          Treino A', 'series': '-', 'repeticoes': '-'},
    '1': {'exercicio': 'Supino Inclinado com Halteres', 'series': '4', 'repeticoes': '10-12'},
    '2': {'exercicio': 'Crucifixo na Máquina', 'series': '3', 'repeticoes': '15'},
    '3': {'exercicio': 'Supino fechado', 'series': '2', 'repeticoes': '8-10'},
    '4': {'exercicio': 'Remada Alta com Halteres', 'series': '2', 'repeticoes': '8-10'},
    '5': {'exercicio': 'Tríceps Testa', 'series': '4', 'repeticoes': '8-10'},
    '6': {'exercicio': '           Treino B', 'series': '-', 'repeticoes': '-'},
    '7': {'exercicio': 'Pulley Frente', 'series': '4', 'repeticoes': '10-12'},
    '8': {'exercicio': 'Remada Baixa', 'series': '4', 'repeticoes': '10'},
    '9': {'exercicio': 'Remada Articulada', 'series': '3', 'repeticoes': '8-10'},
    '10': {'exercicio': 'Elevação Posterior', 'series': '4', 'repeticoes': '8-10'},
    '11': {'exercicio': 'Rosca 21', 'series': '5', 'repeticoes':'21'},
    '12': {'exercicio': 'Encolhimento com barra', 'series': '4','repeticoes':'10'},
    '13': {'exercicio': '         Treino C', 'series': '-', 'repeticoes': '-'},
    '14': {'exercicio': 'Passada', 'series': '4', 'repeticoes': '10-12'},
    '15': {'exercicio': 'Stiff', 'series': '4', 'repeticoes': '10-12'},
    '16': {'exercicio': 'Leg Press', 'series': '4', 'repeticoes': '10-12'},
    '17': {'exercicio': 'Mesa Flexora Sentado', 'series': '3', 'repeticoes': '10-12'},
    '18': {'exercicio': 'Gêmeos em Pé', 'series': '5', 'repeticoes': '10-12'},
    '19': {'exercicio': 'Elevação de Pernas', 'series': '4', 'repeticoes': '10-12'},

}         
treino_m = {
    '0': {'exercicio': '          Treino A', 'series': '-', 'repeticoes': '-'},
    '1': {'exercicio': 'Supino Inclinado com Halteres', 'series': '4', 'repeticoes': '10-12'},
    '2': {'exercicio': 'Crucifixo na Máquina', 'series': '3', 'repeticoes': '15'},
    '3': {'exercicio': 'Supino fechado', 'series': '2', 'repeticoes': '8-10'},
    '4': {'exercicio': 'Remada Alta com Halteres', 'series': '2', 'repeticoes': '8-10'},
    '5': {'exercicio': 'Tríceps Testa', 'series': '4', 'repeticoes': '8-10'},
    '6': {'exercicio': '           Treino B', 'series': '-', 'repeticoes': '-'},
    '7': {'exercicio': 'Pulley Frente', 'series': '4', 'repeticoes': '10-12'},
    '8': {'exercicio': 'Remada Baixa', 'series': '4', 'repeticoes': '10'},
    '9': {'exercicio': 'Remada Articulada', 'series': '3', 'repeticoes': '8-10'},
    '10': {'exercicio': 'Elevação Posterior', 'series': '4', 'repeticoes': '8-10'},
    '11': {'exercicio': 'Rosca 21', 'series': '5', 'repeticoes':'21'},
    '12': {'exercicio': 'Encolhimento com barra', 'series': '4','repeticoes':'10'},
    '13': {'exercicio': '         Treino C', 'series': '-', 'repeticoes': '-'},
    '14': {'exercicio': 'Passada', 'series': '4', 'repeticoes': '10-12'},
    '15': {'exercicio': 'Stiff', 'series': '4', 'repeticoes': '10-12'},
    '16': {'exercicio': 'Leg Press', 'series': '4', 'repeticoes': '10-12'},
    '17': {'exercicio': 'Mesa Flexora Sentado', 'series': '3', 'repeticoes': '10-12'},
    '18': {'exercicio': 'Gêmeos em Pé', 'series': '5', 'repeticoes': '10-12'},
    '19': {'exercicio': 'Elevação de Pernas', 'series': '4', 'repeticoes': '10-12'},

}             

Alunos = {
    'nome':'Maicon',
    'genero':0,
    'treino':treino_h,
}


def CadastrarAlunos():
    dados = {
        'nome': str (input('Nome completo: ')),
        'genero':int(input('Masculino = 0, Feminino = 1: ')),
    }
    nome = dados.get('nome')
    genero = dados.get('genero')
    list_nome = [cliente.get('login') for cliente in Alunos]    
    if nome in list_nome:
        return False
    else:
        Alunos.update(dados)
        if genero == 0:
            Alunos:nome['treino'] = treino_h   
        else:
            Alunos:nome['treino'] = treino_m
        return True

def AlunosCadastrados():
    genero = Alunos.get('genero')
    list_genero = [cliente.get('genero') for cliente in Alunos]
    nome = str(input('Nome completo: '))
    
    
    if list_genero in Alunos and genero == 0:
        print(f'ola {nome}')
        
  



while True:
    print('[2] Já sou cadastrado')
    print('[1] Cadastrar cliente')
    print('[0] Sair')
    

    opcao = int(input('Opção: '))

    if opcao == 0:
        break

    elif opcao == 1:
        cadastro = CadastrarAlunos()
        genero = Alunos('genero')
        if cadastro is True:
            print("Cliente Cadastrado com sucesso!!")
        else:
            print("Cliente já cadastrado!!")
    elif opcao == 2:
        AlunosCadastrados()
    else:
        print("Opção incorreta")
