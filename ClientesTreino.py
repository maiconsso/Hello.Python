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
    '1': {'exercicio': 'Agachamento livre', 'series': '3', 'repeticoes': '8'},
    '2': {'exercicio': 'Leg Press', 'series': '3', 'repeticoes': '8'},
    '3': {'exercicio': 'Afundo', 'series': '3', 'repeticoes': '8-10'},
    '4': {'exercicio': 'Cadeira extensora', 'series': '3', 'repeticoes': '8-10'},
    '5': {'exercicio': 'Cadeira adutora', 'series': '4', 'repeticoes': '8-10'},
    '6': {'exercicio': '           Treino B', 'series': '-', 'repeticoes': '-'},
    '7': {'exercicio': 'Pulley Frente', 'series': '3', 'repeticoes': '10-12'},
    '8': {'exercicio': 'Remada na polia', 'series': '3', 'repeticoes': '10'},
    '9': {'exercicio': 'Supino reto', 'series': '3', 'repeticoes': '8-10'},
    '10': {'exercicio': 'Voador peitoral', 'series': '3', 'repeticoes': '8-10'},
    '11': {'exercicio': 'Desenvolvimento', 'series': '3', 'repeticoes':'21'},
    '12': {'exercicio': 'Elevação lateral', 'series': '3','repeticoes':'10'},
    '13': {'exercicio': '         Treino C', 'series': '-', 'repeticoes': '-'},
    '14': {'exercicio': 'Mesa flexora', 'series': '3', 'repeticoes': '10-12'},
    '15': {'exercicio': 'Stiff', 'series': '3', 'repeticoes': '10-12'},
    '16': {'exercicio': 'Cadeira flexora', 'series': '4', 'repeticoes': '10-12'},
    '17': {'exercicio': 'Elevação pélvica', 'series': '3', 'repeticoes': '10-12'},
    '18': {'exercicio': 'Prancha', 'series': '5', 'repeticoes': '30'},
    '19': {'exercicio': 'Abdominal reto solo', 'series': '4', 'repeticoes': '10-12'},

}             
Alunos =[{'Nome': 'Maicon', 'Genero': 0}]

def CadastrarAlunos():
    dados = {
        'Nome': str(input('Nome completo: ')),
    }
    nome = dados.get('Nome')
    list_nome = [cliente.get('Nome') for cliente in Alunos]      
    if nome in list_nome:
        return False
    else:
        Alunos.append(dados)
        return True
        
def See_Training ():
    treino_Aluno = int (input('Selecione o seu treino:\n0 = Treino Masculino \n1 = Treino Feminino \nNumero :  '))
    if treino_Aluno == 0:
        print()
        print(f"{'Exercicio':^30} | {'Séries':^6} | {'Repetições':^15}")
                
        for treino in treino_h:
            work = treino_h[treino]
            print(f"{work['exercicio']:<30} | {work['series']:^6} | {work['repeticoes']:>15}")
    else:
        print()
        print(f"{'Exercicio':^30} | {'Séries':^6} | {'Repetições':^15}");
        for treino in treino_m:
            work = treino_m[treino]
            print(f"{work['exercicio']:<30} | {work['series']:^6} | {work['repeticoes']:>15}")    
    
while True:    
    print('[1] Cadastrar cliente')
    print('[0] Sair')
    
    opcao = int(input('Opção: '))

    if opcao == 0:
        break

    elif opcao == 1:
        cadastro = CadastrarAlunos()        
        if cadastro is True:
            print("Cliente Cadastrado com sucesso!!")
            See_Training()
            break             
        else:
            print("Cliente já cadastrado!!")            
    else:
        print("Opção incorreta")
