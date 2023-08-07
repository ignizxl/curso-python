# Faça um programa que tenha uma função chamada área(), 
# que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.

#criando a função 'area' que recebe como parametro 'l'(largura) e 'c'(comprimento)
def area(l, c):
    #multiplico o 'l' vezes o 'c' e armazeno o resultado em 'area' 
    area = l * c
    #mostro o resultado com uma casa flutuante
    print(f"A área de um terreno {l:.1f}x{c:.1f} é de {area:.1f}m² ")


#mostra um mensagem
print('Controle de Terrenos')
print('=--=' * 5)
#pedindo a largura e comprimento, convertendo pra float e armazenando nas variáveis correspondentes 
largura = float(input('Comprimento (m): '))
comprimento = float(input('Comprimento (m): '))

#depois, basta chamar a função 'area' passando como parâmetro a largura e o comprimento
area(largura, comprimento)