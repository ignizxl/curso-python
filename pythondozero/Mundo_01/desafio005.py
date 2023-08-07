#faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.

#escreva na tela 'antecessor e sucessor' entre sinais de '=' de forma centralizada 
menu = 'Antecessor e Sucessor'
print('{:=^30}'.format(menu))

#peça um número ao usuário e armazene o resultado em 'n'
n = int(input('Digite um número: '))

#O antecessor = o valor armazenado em 'n' - 1 e O sucessor = o valor armazenado em 'n' + 1  
ant = n - 1
suc = n + 1

#print(f'O antecessor do número {n} é {ant}. \n O sucessor número {n} é {suc}.')
#essa saida formatada acima é bem simples de entender.
#coloque um 'f' antes das aspas e depois você vai preencher as chaves{} com os nomes das variáveis que você queira mostrar na tela 





#mostre na tela o sucessor e antecessor do valor armazenado em 'n'
#\n é uma quebra de linha 
print('O antecessor do número {0} é {1}. \n O sucessor do {0} é {2}'.format(n, ant, suc))

#dica: utilize os números dentro das chaves{} para indicar a saida formatada quando utilizar o .format .. nesse exemplo: 

# 'n' está na posição '0'
# 'ant' está na posição '1'
# 'suc' está na posição '2'
# agora é só numerar as chaves {} de forma correta

#print('O antecessor do número {0} é {1}. \n O sucessor do {0} é {2}'.format(n, ant, suc))
# ou eu posso fazer assim também

#print('O antecessor do número {} é {}. \n O sucessor do {} é {}'.format(n, ant, n, suc))
#só que dessa forma eu tenho que fazer a ordem correta dentro do .format como está ai acima
# 1ª chave{n} 
# 2ª chave{ant} 
# 3ª chave{n} 
# 4ª chave{suc}
