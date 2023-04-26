#nome="jorge"
#sobre="romero"
#print(nome+sobre)
print(32*"*")
print("Bem vindo ao jogo de adivinhação")
print(32*"*")

x=1
numero_secreto=42
tentativas=3
rodadas=tentativas

while(tentativas>0):
    print("Tentativa ",x," de",rodadas)
    chute=int(input("Digite um numero: "))
    print("Voce digitou", chute)
    acertou = (chute == numero_secreto)
    maior = (chute > numero_secreto)
    menor = (chute < numero_secreto)

    if(acertou):
        print("Voce acertou!")
        break
    elif(maior):
        print("Voce errou! O numero secreto é menor")
    elif (menor):
        print("Voce errou! O numero secreto é maior")
    tentativas=tentativas-1
    x=x+1

if(acertou==False):
    print("Suas Tentativas acabaram! Encerrando o jogo")
else:
    print("Encerrando o jogo!")




