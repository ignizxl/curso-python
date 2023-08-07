#faça um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.

#posso fazer de várias formas. aqui vão algumas:
#vou começar fazendo um laço de repetição para contar entre o intervalo de 1 a 51 porque o ultimo termo é ignorado, então vai de 1 a 50 
for i in range(1, 51):
#e se o resultado do resto da divisão de i por 2 for igual a 0, ele é par
    if i % 2 == 0:
#mostre os números pares 
        print(i)

#aqui, um laço de repetição para contar entre o intervalo de 2 a 51 pulando de 2 em 2
#a contagem começou do número 2 porque o número 1 vai ser ignorado de toda forma por que ele é impar e aqui eu só quero os pares.
#então começar do números 1 ou do 0, o programa iria fazer algumas repetições que são desnecessárias.
#pra o programa não fazer as repetições desnecessárias, eu já vou iniciar o intervalo entre 2 até 51, porque eu sei que o 0 e o 1 vão ser ignorados
#e se eu começar do 2 até 51 pulando de 2 em 2, o programa já vai direto pegando só os pares e sem fazer repetições que não são 'necessárias' por assim dizer

for i in range(2, 51, 2):
    print(i)
    print('.')


for i in range(2, 51, 2):
    print(i)
    print('.')

