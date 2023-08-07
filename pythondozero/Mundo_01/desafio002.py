#crie um script Python que leia o dia, o mês e o ano de nascimento de uma pessoa e mostre uma mensagem com a data formatada.

# o input pergunta qual é o nome do usuário e depois armazena o resultado na variável  'nome' 
nome = input('Digite o seu nome: ')

#(como o resultado desse input vai ser um número inteiro é preciso converte-lo para int) o resultado do input tá sendo convertido para um valor inteiro e depois armazenado na variável  'dia' 
dia = int(input('Digite o dia do seu nascimento:'))

#(o input já converte para str, por isso que não é necessário fazer a conversão) o input pergunta qual é o mês do nascimento do usuário e depois armazena o resultado na variável  'mes'
mes = input('Digite o mês de seu nascimento: ')

#(como o resultado desse input vai ser um número inteiro é preciso converte-lo para int) o resultado do input tá sendo convertido para um valor inteiro e depois armazenado na variável  'ano'
ano = int(input('Digite o ano de seu nascimento: '))

#escreve na tela uma mensagem de boas-vindas para o que foi armazenado na variável nome
#print(f'Olá ,{nome}. Você nasceu no dia {dia} de {mes} no ano de {ano}. Correto?')
print('Olá, {}. Você nasceu no dia {} de {} no ano de {}. Correto?'.format(nome, dia, mes, ano))