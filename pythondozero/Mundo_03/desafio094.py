# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa 
# em um dicionário e todos os dicionários em uma lista. 
# No final, mostre:
# A) Quantas pessoas foram cadastradas 
# B) A média de idade 
# C) Uma lista com as mulheres 
# D) Uma lista de pessoas com idade acima da média

#criando uma lista e um dicionário
pessoas = []
dados = {}

#enquanto verdade, faça 
while True:
    #pede um nome, converte pra str e elimina os espaços da esquerda e da direita com o strip e joga na
    #key 'nome'
    dados['Nome'] = str(input('Digite o seu nome: ')).strip()
    #pede a idade, converte pra int e armazena na key 'idade'
    dados['Idade'] = int(input('Digite sua idade: '))
    #crio um vari´vel chamada 'sexo' que inicia como uma string vazia 
    sexo = ' '
    #enquanto sexo o usuário não digitar F ou M, o while repete 
    while sexo not in 'FM':
        #pede o sexo, converte pra str, joga a letra pra maiúscula e considera só o caractere 0
        sexo = str(input('Digite seu sexo [M/F]: ')).upper()[0]
        #se o usuário não digitar F ou M, vai mostrar um erro
        if (sexo not in 'MF'):
            print("Erro! Digite apenas 'M' para 'Masculino' ou 'F' para 'Feminino'.")
    
    #depois de validar o sexo, adiciona na key sexo no dicionário dados
    dados['Sexo'] = sexo
    #adiciono uma cópia do dicionário na lista 'pessoas' usando o append
    pessoas.append(dados.copy()) 
    #depois uso a função clear para limpar o dicionário 'dados '
    dados.clear()

    #repito o mesmo processo feito no 'sexo' para validar a resposta do usuário 
    resposta = ' '
    #enquanto o usuário não digitar s ou n, o while repete 
    while resposta not in 'SN':
        #pega a resposta, converte pra str, joga pra letra maiúscula e considera só o caractere 0
        resposta = str(input('Deseja adicionar uma nova pessoa ? [S/N]: ')).upper()[0]

        #se a resposta for diferente de s ou n, mostra um erro 
        if (resposta not in 'SN'):
            print("Erro! Digite apenas 'S' para 'Sim' ou 'N' para 'Não'.")
    
    #depois de ter validado a resposta, verifico se a resposta é igual a 'N', se for eu uso o break para 
    #encerrar o laço  
    if (resposta == 'N'):
            break  

#uso o len para pegar o tamanho de pessoas que representa a quantidade de pessoas cadastradas e armazeno em 
#'totalDePessoas'
totalDePessoas = len(pessoas)
#crio um acumulador chamado mediaDeIdade que iniciante valendo 0 e vai sendo incrementado a cada iteração do 
#laço for abaixo 
mediaDeIdade = 0
#crio um lista para armazenar todas as mulheres que foram cadastradas 
mulheresCadastradas = []

#crio um laço for para percorrer cada pessoa dentro da lista pessoas    
for i in pessoas:
    #a cada iteração do laço for, o acumulador mediaDeIdade incrementa com a idade da pessoa 
    mediaDeIdade += i['Idade'] 

    #verifico se o sexo da pessoa é igual a 'F'
    if (i['Sexo'] == 'F'):
        #se for, eu adiciono o nome dessa pessoa na lista 'mulheres cadastradas'
        mulheresCadastradas.append(i['Nome'])
#ao fim do laço for, pego a soma de todas as idade que foi armazenada em 'mediaDeIdade' e divido pelo totalDePessoas
#e armazeno na mesma variável mediaDeIdade
mediaDeIdade = mediaDeIdade/totalDePessoas

#mostro o total de pessoas 
print(f'A-) {totalDePessoas} pessoa(s) foram cadastradas!' )
#mostro a média de idade
print(f"B-) A média de idade é '{mediaDeIdade:.2f}' anos. ")

#verifico se o tamanaho da lista mulheres cadastradas é igual a zero, se for, nenhuma mulher foi cadastrada
if (len(mulheresCadastradas) == 0):
    print('C-) Nenhuma mulher foi cadastrada!')
    #senão, faça
else:
    #crio um for para percorrer cadas mulher cadastrada na lista 'mulheresCadastradas '
    for i in mulheresCadastradas:
        #se é a primeira iteração do laço for para imprimir de maneira diferente 
        if (mulheresCadastradas.index(i) == 0):
            # mostra uma mensagem, imprime o nome da mulher e continua na mesma linha 
            print(f"C-) Mulher(es) cadastrada(s) no sistema: {i}", end = '')
        else:
            #e depois só continua na mesma linha 
            print(f', {i}', end = '')
    print('.')

print('D-) Lista das pessoas acima da média:')
#crio um laço for para percorrer cada pessoa dentro da lista pessoas 
for i in pessoas:
    #e a cada iteração, verifico se a idade da pessoa passou da 'mediaDeIdade'
    if (i['Idade'] > mediaDeIdade):
        #se passar da média, eu mostro todas as informações da pessoa 
        print(f" >= Nome : {i['Nome']} ; Idade = {i['Idade']} ; Sexo = {i['Sexo']}; ")

print('<< Encerrando! >>')

#segunda forma de fazer 

print('=-=- Segunda forma =-=-')

#criando um lista e um dicionário 
galera = []
pessoa = {}

#criando u lista para acumular o soma das idades e uma para média, ambas iniciam valendo 0 
somaDasIdades = mediaDasIdades = 0

#enquanto verdade, faça 
while True:
    
    #repetindo o mesmo processo feito na solução anterior 
    pessoa['Nome'] = str(input('Nome: '))
    pessoa['Idade'] = int(input('Idade: '))
    somaDasIdades += pessoa['Idade']

    #fazendo a validação do sexo
    while True:
        #pede o sexo, converte pra str, joga a letra pra maiúscula e considera apenas a primeira letra 
        pessoa['Sexo'] = str(input('Sexo: [M/F]: ')).upper()[0]

        #verifica se o usuário digitou M ou F, se digitou M ou F, encerra o laço 
        if (pessoa['Sexo'] in 'MF'):
            break
        #se não atendeu a condição acima, mostra um erro 
        print('Erro! Por favor, digite apenas M ou F.')
    
    #depois de validar o sexo, uso o append para enviar uma cópia de 'pessoa' para a lista 'galera'
    galera.append(pessoa.copy())
    #e depois, uso o clear para limpar o dicionário 'pessoa'
    pessoa.clear()

    #e repito o mesmo processo para validar a resposta do usuário 
    while True:
        resp = str(input('Quer continuar? [S/N]: ')).upper()[0]

        if (resp in 'SN'):
            break
        print('Erro! Responda apenas S ou N.')
    
    #depois de ter validado a resposta, verifico se a respotas é igual a 'N', se for, uso o break para encerrar
    #o laço 
    if (resp == 'N'):
        break

#imprimindo resultados 
print('=-=' * 20)

#mostrando a quantidade de pessoas cadastradas 
print(f'A-) Ao todo temos {len(galera)} pessoas cadastradas.')

#calculando a média das idades e armazenado em 'mediaDasIdades'
mediaDasIdades = somaDasIdades / len(galera)
#mostrando a média das idades em 5 caracteres com duas casas flutuantes
print(f'B-) A média de idade é de {mediaDasIdades:5.2f} anos')
print(f'C-) As mulheres cadastradas foram ', end = '')
#para mostrar as mulheres cadastradas o processo é o mesmo da solução anterior 
#crio um laço for para percorrer cada pessoa dentro de galera 
for pessoa in galera:
    #e a cada iteração, verifica se o sexo é igual a 'F'
    if (pessoa['Sexo'] == 'F'):
        #se for, mostra o nome da pessoa e continua na mesma linha 
        print(f'{pessoa["Nome"]} ', end = "")
print()

print(f'D-) A lista das pessoas que estão acima da média: ')
#mesmo processo para verificar as pessoas acima da média 
#crio um laço for para percorrer cada pessoa dentro de galera 
for pessoa in galera:
    #e a cada iteração verifica se a idade da pessoa é maior que a média de idade 
    if (pessoa['Idade'] > mediaDasIdades):
        print('     ', end = "")
        #se for, eu crio um laço for e uso a função .items() para me retornar a key e o value da pessoa 
        for key, value in pessoa.items():
            #e a cada iteração eu mostro a key e value correspondente 
            print(f' => {key} = {value}; ', end = "")
        print()
print('< Encerrando >')