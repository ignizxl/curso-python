#Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final mostre os 10 primeiros termos dessa progressão.

#vou começar decorando o meu programa escrevendo 30 sinais de '=' e escrevendo '10 termos de uma pa' em 30 espaços entre sinais de '='
print("=" * 30)
print("{:=^30}".format("10 termos de uma PA"))
print("=" * 30)

#vou pedir ao usuário o primeiro termo e armazenar o resultado em 'ptermo'
ptermo = int(input("Primeiro termo: "))

#vou pedir a razao e armazenar o resultado em 'razao' 
razao = int(input("Razão: "))

#para calcular o decimo termo de uma pa, basta usar essa regra
# primiero termor + ('como eu quero o decimo termo eu coloco' 10 - 1) * razao
# nesse caso ficaria = ptermo + (10 - 1) * razao  
decimo =  ptermo + (10 - 1) * razao

#agora vou criar um laço de repetição que vai começar no intervalo de ptermo(valor armazenado em ptermo) até o decimo(valor armazenado em decimo)
# termo + a razao(valor armazenado em razao) pulando de razao(valor armazenado em razao)
# é preciso colocar decimo + razao porque se eu não colocar vai faltar termos.  
for i in range(ptermo, decimo + razao, razao):
#vou mostrar na tela a minha pa seguido de uma '-->'
#esse end = '-->' significa que vai continuar na mesma linha com uma --> 
    print(" {} ".format(i), end = " --> ")
print("ACABOU")
    