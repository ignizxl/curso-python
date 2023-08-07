#crie um programa que tenha uma tupla com várias palavras (não usar acentos).
#Depois disso, você deve mostrar, para cada palavra, quias são as suas vogais.

#cria um tupla e armazena várias palavras 
palavras = ('aprender', 'programar','linguagem','python',
            'curso','gratis', 'estudar','praticar','trabalhar',
            'mercado','programador' ,'futuro')
#para cada palavra dentro da tupla palavras, faça
for palavra in palavras:
    #imprime  a palavra em letras maiúsculas e continua na mesma linha
    print(f'Na palavras {palavra.upper()} temos: ', end='')
    
    #analiza cada letra dentro da palavra
    for letras in palavra:
        #joga todas as letras para minúscula e se as letras forem a,e,i,o,u, mostre na tela a letra
        if letras.lower() in 'aeiou':
            #mostre a letra e continue na mesma linha
            print(f'{letras}', end=' ')
    #no fim do laço eu vou fazer um print() vazio para a saída sair bonita 
    print()

print()
#armazeno alguns nomes dentro da tupla herois 
herois = ('axe', 'juggernaut', 'bristleback', 'bloodseeker', 'doctor', 'void' , 'legion', 'antimage', 'timbersaw')

#para cada elemento(cada nome de heroi) dentro da tupla herois, faça
for heroi in herois:
    #mostre o nome do heroi em letra maiúscula e continue na mesma linha
    print(f'No nome do hero {heroi.upper()} existem: ', end=' ')
    #para cada letra dentro do nome do heroi, faça
    for letras in heroi:
        #joga a letra pra minúscula e verifica se tem alguma vogal(a,e,i,o,u) dentro de letra, se tiver, faça
        if letras.lower() in 'aeiou':
            #mostre na tela a letra e continue na mesma linha
            print(letras, end=' ')
    #print nada pra saida ficar bonita
    print() 