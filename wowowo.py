import random


def jogo_adivinha():
    # Apresentando o jogo
    print(32 * "*")
    print("Bem vindo ao jogo de adivinhação")
    print(32 * "*")
    # Mostrando ao jogador as opçoes de dificuldade disponiveis
    print("Selecione a dificuldade:")
    print("1-Facil (10 tentativas)")
    print("2-Medio (5 tentativas)")
    print("3-Dificil (3 tentativas)")
    # esperando a resposta do jogador
    resp = int(input(">>>"))
    # caso ele responda algo fora do planejado, entra em uma condição de repetição até escolher uma opção valida
    while resp < 1 or resp > 3:
        resp = int(input("Erro! Digite o número correspondente a dificuldade desejada! \n>>>"))

    tentativas = 0
    acertou = False
    # definindo a quantia de tentativas por dificuldade
    if resp == 1:
        tentativas = 10
    elif resp == 2:
        tentativas = 5
    elif resp == 3:
        tentativas = 3
    # declarando pontos e o numero secreto
    numero_secreto = random.randrange(1, 101)
    pontos = 1000
    # iniciando o jogo por meio de estrutura de repetição
    for x in range(1, tentativas + 1):
        print("Tentativa {} de {}".format(x, tentativas))
        chute = int(input("Digite um numero entre 1 e 100: "))
        while chute < 1 or chute > 100:
            chute = int(input("Numero inválido! Digite um numero entre 1 e 100: "))
        acertou = (chute == numero_secreto)
        maior = (chute > numero_secreto)
        menor = (chute < numero_secreto)

        if acertou:
            print("Voce acertou!")
            break
        elif maior:
            print("Voce errou! O numero secreto é menor")
            pontos = pontos - (abs(chute - numero_secreto))
        elif menor:
            print("Voce errou! O numero secreto é maior")
            pontos = pontos - (abs(chute - numero_secreto))

    # Declarando se o jogador perder todas suas tentativas, fim de jogo e a pontuacao final
    if not acertou:
        pontos = pontos - 600
        print("Sua pontuação foi", pontos, "pontos!")
        print("Suas Tentativas acabaram! Encerrando o jogo")
    else:
        print("Sua pontuação foi", pontos, "pontos!")
        print("Encerrando o jogo!")


if __name__ == "__main__":
    jogo_adivinha()
