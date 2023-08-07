# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade)
# em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de 
# contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

#importando a função date da biblioteca datetime
from datetime import datetime

#utilizando a função datetime.now().year para pegar a data atual 
dataAtual = datetime.now().year
#criando um dicionário chamado 'dados'
dados = {}
#armazenando os dados capturados pelo input na key 'nome'
dados['Nome'] = str(input('Nome: ')).strip()
#subtraindo os dados capturados pelo input pela 'dataAtual' e armazenando o resultado na key 'idade' 
dados['Idade'] = dataAtual - int(input('Ano de Nascimento: '))
#armazenando os dados capturados pelo input na key 'ctps'
dados['CTPS'] = int(input('Carteira de Trabalho (0 não tem!): '))
#vefirica se o value da key 'ctps' é diferente de 0, se for, faça
if (dados['CTPS'] != 0):
    #repete o mesmo processo, pega a entrada de dados e armazena nas keys contratação e salário
    dados['Contratação'] = int(input('Ano de Contratação: '))
    dados['Salário'] = float(input('Salário: R$'))
    #para calcular a idade que o indivíduo irá se aponsentar é preciso pegar o ano de contratação e somar mais 
    #a quantidade de contribuição necessária, depôs, subtrai pela dataAtual e, por fim, soma tudo isso com 
    #a idade do indivíduo
    aposentadoria = ((dados['Contratação'] + 15) - dataAtual) + dados['Idade']
    dados['Aposentadoria'] = aposentadoria

print('=-=' * 10)
#e para exibir na tela, crio um laço for utilizando a função .items() para me retornar as keys e os values
for key, value in dados.items():
    #e a cada iteração do laço for, imprime a key seguida de seu value correspondente
    print(f'- {key} tem o valor {value}')