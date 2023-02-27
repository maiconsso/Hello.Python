# criar variaveis para o nome (str), idade (int),
# altura (float) e peso (float) de uma pessoa
# criar variável com o ano atural (int)
# obter ano de nascimento da pessoa  (baseado na idade e no ano atual)
# obter o imc da pessoa com 2 casas decimais (peso e na altura da pessoa )
# exibir um texto com todos os valores na tela usando f- strings ( com as chaves )

from datetime import date

nome = str('John')
idade = int(32) 
altura = float(1.65)
peso = float(75.0)
data = (date.today())
ano_atual = int(data.year)
ano_nasc = int(ano_atual-idade)
imc = float(peso/altura**2)

print (f'{nome} tem {idade} anos, {altura}cm de altura e pesa {peso}kg.')
print (f'O seu IMC é {imc:.2f}.')
print (f'{nome} nasceu em {ano_nasc}.')