import random


def imprime_mensagem_abertura():
    # anunciando o jogo
    print(32 * "*")
    print("***Bem vindo ao jogo da forca***")
    print(32 * "*")


def palavra_segredo():
    # pegando as possiveis palavras secretas de um arquivo
    lista = []
    arquivo = open("palavras.txt", "r")
    for linha in arquivo:
        linha = linha.strip()
        lista.append(linha)
    arquivo.close()
    # escolhendo a palavra da lista que sera usada no jogo
    x = random.randrange(0, 11)

    # transformando a palavra secreta em str e gerando a versão da palavra apenas em traços
    palavra_secreta = str(lista[x])

    return palavra_secreta


def cerne_do_jogo(palavra_secreta, e, enfo, s, enforca):
    # declarando variaveis para o jogo funcionar corretamente
    acertou = False
    enforcado = False
    val = 0

    # começando o laço principal do jogo
    while not enforcado and not acertou:
        # declaramos index para substituir o traço pela letra nas posicoes certas, e contador para quando o jogador erra
        index = 0
        cont = 0
        chute = input("Chute uma letra: ").lower().strip()

        # laço onde olharemos cada caracter da palavra secreta para ver se a letra que chutamos esta nela
        for i in palavra_secreta:
            if i == chute:
                s[index] = chute
                cont = cont + 1
            index = index + 1

        # caso não ache a letra chutada, essa condiçao sera ativada e as tentativas restantes do jogador diminuem
        if cont == 0:
            e[val] = enfo[val]
            val = val + 1

        # alteramos as strings com as mudanças que houveram em suas versões de lista
        en = "".join(e)
        segredo = "".join(s)

        print(segredo)
        print(en)

        # condiçoes de derrota e vitoria, caso o desenho se complete, o jogador perde, caso ele acerte antes, ele ganha
        if en.__eq__(enforca):
            print("Voce perdeu!")
            print("A palavra era:", palavra_secreta)
            enforcado = True
        if segredo.__eq__(palavra_secreta):
            print("Voce Venceu!")
            acertou = True


def jogo_forca():
    # Imprimindo o nome do jogo
    imprime_mensagem_abertura()

    # Criando a lista de palavra secreta e dando dica para o jogador de quantia de letras
    palavra_secreta = palavra_segredo()
    segredo = (len(palavra_secreta) * "_")
    print(segredo)
    s = list(segredo)

    # gerando o desenho da forca, que ditara a quantia de vezes que um jogador pode errar
    enforca = "o-|--<"
    en = (len(enforca) * "_")
    enfo = list(enforca)
    e = list(en)
    print(en)

    cerne_do_jogo(palavra_secreta, e, enfo, s, enforca)

    print("Fim de jogo")


if __name__ == "__main__":
    jogo_forca()
