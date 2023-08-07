# Faça um programa que tenha uma função chamada escreva(), que receba 
# um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.  

#crio a função 'escreva' que recebe como parâmetro um texto qualquer 
def escreva(texto):

    #uso o len para pegar o tamanho do texto, somo + 4 e armazeno em 'espacos' 
    # (o +4 é para deixar 2 espaços na direita e na esquerda)
    espacos = len(texto) + 4

    #multiplico o sinal que eu quero exibir vezes a quantidade de 'espacos'
    print('-' * espacos)
    #mostro o texto centralizado em x 'espacos'
    print(f'{texto:^{espacos}}')
    print('-' * espacos)

#chamo a função e escrevo algumas frases 
escreva('Curso em Vídeo')
escreva('Python é muito bom!')
escreva('DEV')
escreva(input('Escreva algo... :'))