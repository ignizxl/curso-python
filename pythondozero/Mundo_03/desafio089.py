# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. 
# No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas 
# de cada aluno individualmente.

#crio 3 listas que iniciam vazias, uma chamada alunos, outra lista temporária dados e uma lista chamada cadastrados 
alunos = []
dados = []
cadastrados = []
#enquanto verdade 
while True:
    #pede o nome do aluno e já adiciona na lista temporária 'dados' 
    dados.append(str(input('Aluno(a): ')))
    #pede também a primeira e segunda nota e já adiciono dentro da lista temporária dados
    dados.append(float(input('1º Nota: ')))
    dados.append(float(input('2º Nota: ')))
    #adiciono uma cópia da lista temporária dados na minha lista principal chamada alunos
    alunos.append(dados[:])
    #depois limpo a lista temporária dados usando a função clear()
    #eu preciso limpar a lista dados a cada iteração do while pra ela receber novos dados e enviar os novos dados
    #pra lista principal, se eu não limpar a lista ela vai começar a acumular os dados e eu vou ter problemas 
    dados.clear()
    #crio uma variável chamada resposta que inicia como uma string vazia 
    resposta = ' '
    #enquanto o que foi armazenado dentro de resposta não for um S ou um N, faça
    while resposta not in 'SN':
        #pede uma resposta, elimina os espaços, joga a letra pra maiúscula e considera só a primeira letra
        resposta = str(input('Deseja cadastra um novo aluno? [S/N]: ')).strip().upper()[0]
    #se a minha resposta for igual a N, eu encerro o laço com o break
    if resposta == 'N':
        break
print('-=-' * 15)
#mostro uma mensagem na tela com os textos centralizados 
print('{:^2} {:<10} {:^4}'.format('Nº.', 'NOME', 'MÉDIA'))
print('-=-'* 15)
#crio um contador chamado n 
n = 0
#crio uma laço for para varrer todos os elementos (sublistas dentro da lista alunos)
#toda vez que eu adicionava uma cópia da lista temporária dados na lista aluno, na verdade eu estava adicionando
#um sublista dentro de uma lista principal(lista alunos)
for aluno in alunos:
    #aluno representa a sublista, aluno[0] representa o nome do aluno, aluno[1] representa a primeira nota e o aluno[2]
    #representa a segunda nota 
    #então pra calcular a média, eu pego aluno na posição 1 e aluno na posição, somo e depois divido por 2
    media = (aluno[1] + aluno[2]) / 2
    #depois mostro na tela os resultados de forma centralizada com o número do aluno(é como se fosse o id do aluno)
    #o nome do aluno e o resultado de sua média 
    print('{:^2} {:<10} {:^5}'.format(n, alunos[n][0], media))
    #depois adiciono o valor armazenado em n na lista cadastrados, ou seja, eu adiciono o id do aluno na lista cadastrados
    cadastrados.append(n)
    #e incremento o contador n porque o id é único e cada aluno tem o seu
    n += 1 
print('-=-'* 15)
#enquanto verdade faça
while True:
    #pergunto se o usuário quer ver as notas de um aluno cadastrado, e para isso ele só precisa digitar o id do aluno(n°)
    flag = int(input('Quer ver as notas de qual aluno(a): (999 interrompe): '))
    #se o número digitado pelo usuário for igual a 999, eu uso o break pra encerrar o laço 
    if flag == 999:
        print('Programa encerrado. Volte sempre!')
        break
    #verifico se o id que usuário digitou acima não existe na lista, se o id não existir dentro da lista cadastrados,
    #eu mostro uma mensagem dizendo que o id não foi encontrado
    if flag not in cadastrados:
        print(f'Esse aluno não foi encontrado! Os números dos alunos cadastrados foram {cadastrados}')
    #senão, eu mostro o nome do aluno na posição flag(representa o número da sublista que o aluno foi cadastrado) e mostro o nome do aluno que é 
    #posição [0], depois mostro as suas duas notas que estão nas posições alunos[flag][1] e aluno[flag][2]
    else:
        print('----'* 15)
        print(f'As notas de {alunos[flag][0]} são:\n 1º Nota: {alunos[flag][1]} \n 2º Nota: {alunos[flag][2]}')
        print('----'* 15)


#outra forma de fazer 

#crio uma lista principal chamada ficha
ficha = list()
#enquanto verdade, faça
while True:
    #pede o nome do aluno e armazena em nome 
    nome = str(input('Nome: '))
    #pede a primeira e segunda nota e armazena em suas respectivas variáveis 
    nota1 = float(input('1º nota: '))
    nota2 = float(input('2º nota: '))
    #somo a primeira mais a segunda nota e divido por 2, e depois armazeno tudo em media final
    media_final = (nota1 + nota2) / 2
    #depois adiciono tudo isso em forma de lista dentro da minha lista principal(ficha)
    #a média vai dentro de uma sublista porque depois eu vou precisar delas separadamente 
    ficha.append([nome, [nota1, nota2], media_final])
    #pergunto se o usuário quer continuar, jogo a letra pra maiúsculo, elimino os espaços e considero só a primeira letra
    # e depois armazeno tudo isso em continuar  
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    #se o que foi armazenado em continuar for igual a N, eu encerro o laço com o break
    if continuar in 'N':
        break

print('-=' * 30)
#mostro o Nº alinhado a esquerda em 4 espaços, nome alinhado a esquerda em 10 espaços e média alinhado a direita em 8 espaços 
print(f'{"Nº":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 30)
#uso a função enumerate para enumerar todos os elemento de ficha
#crio uma variável chamada indice que representa a posição, crio uma variável chamada alunos_cadastrados que irá representar os elementos da lista 
for indice, alunos_cadastrados in enumerate(ficha):
    #alunos cadastrados na posição 0 representa o nome, alunos cadastrados na posição 2 representa a média final
    # alunos_cadastrados:>8.1f significa que vai aparecer centralizado a direita em 8 espaços contando com uma casa flutuante  
    print(f'{indice:<4}{alunos_cadastrados[0]:<10}{alunos_cadastrados[2]:>8.1f}')
#enquanto verdade, faça
while True:
    print('-' * 30)
    #pede pra o usuário digitar o número de um aluno cadastrado, se o usuário digitar 999 o  programa encerra o laço com o break
    opcao = int(input('Mostrar notas de qual aluno? (999 - encerra o programa) '))
    if opcao == 999:
        print('Finalizando...')
        break
        #se o que foi armazenado dentro de opção for menor ou igual o comprimento da lista ficha, significa que o número digitado existe dentro da lista ficha
    if opcao <= len(ficha) -1:
        #então eu mostro na tela o nome do aluno que é ficha na posição opção(que é o aluno cadastrado) na posição [0] que representa o nome do aluno cadastrado
        #e mostro também ficha na posição [opção] e na posição[1](que representa as duas notas que foram armazenadas lá em cima dentro de uma lista(ficha) em uma sublista )
        print(f'Notas de {ficha[opcao][0]} são {ficha[opcao][1]}')
print('Volte sempre!')