#  Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e
# vai retornar um dicionário com as seguintes informações:
# – Quantidade de notas 
# – A maior nota 
# – A menor nota 
# – A média da turma                                                                                                                                                      – A situação (opcional)


#criando a função calculaNotas que recebe como parâmetro várias notas e um parâmetro opcional
def calculaNotas(xNotas, situacao = False):
    
    #criando um dicionário para armazenar as informações da turma 
    notas = {}

    #criando a docstring da função calculaNotas

    """
    calculaNotas(xNotas, situacao = False)
        -> Função para analisar notas e situações da vários alunos.
        :param xNotas: Um parâmetro para representar xNotas
        :param situacao: Um parâmetro opcional para mostrar ou não a situação da turma
        :return: retorna um dicionário com várias informações sobre a situação da turma 
    """

    #uso o len para descobrir a quantidade de notas 
    total = len(xNotas)
    #uso a função sum para somar todas as notas digitadas
    soma = sum(xNotas)
    #e para calcular a média, basta pegar a soma das notas e dividir pelo total de notas,
    #depois armazeno tudo em media 
    media = soma / total

    #crio a key total e adiciono o 'Total' 
    notas['Total'] = total
    #uso a função max para pegar a maior nota digitada e adiciono na key 'Maior'
    notas['Maior'] = max(xNotas)
    #uso a função min para pegar a menor nota digitada e adiciono na key 'Menor' 
    notas['Menor'] = min(xNotas)
    #crio a key média e adiciono a 'Média'
    notas['Média'] = media
    #se situação for true, faça 
    if (situacao):
        #se a média for menor que 4, 'ruim'
        if (media < 4):
            notas['Situacão'] = 'Ruim'
        #se a média estiver entre 4 e 7. 'razoável'
        elif 4 <= media <=7:
            notas['Situacão'] = 'Razoável'
        #senão, 'boa'
        else:
            notas['Situacão'] = 'Boa'

    #retorna o dicionário 
    return notas


#criando um lista chamada 'n' para armazenar todas as notas digitadas 
n = []
#criando uma variável chamada 'entrada' para o usuário digitar as notas e depois 'fatia' tudo com o split()
entrada = input("Digite as notas dos alunos separadas por espaço. Ex: 10 3.6 7.0: \n").split()
#criando um for, para percorrer cada elemento dentro de entrada
for i in entrada:
    #e a cada iteração, pega o i(elemento da vez) converte pra int e armazena em 'n'
    n.append(int(i))

#pergunta se o usuário quer exibir a situação da turma 
resposta = input('Deseja mostrar a situação da turma? [S/N]: ').upper()[0]

#se a resposta for 'S', resposta = true, senão, resposta = false
if (resposta == 'S'):
    resposta = True
else:
    resposta = False 

#chamo a função digitando os parâmetros acima 
print(calculaNotas(n, resposta))

#mostrando a docstring da função 
print(calculaNotas.__doc__)