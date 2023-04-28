import random
def jogo_forca():
    #anunciando o jogo
    print(32 * "*")
    print("***Bem vindo ao jogo da forca***")
    print(32 * "*")

    #declarando variaveis para o jogo funcionar corretamente
    acertou = False
    enforcado = False
    val = 0

    #gerando algumas possiveis palavras secretas para o jogo
    lista=("amizade","sincero","aventura","felicidade","enigma","paixao","desafio","misterio","liberdade","conquista","chupacabra")

    #escolhendo a palavra da lista que sera usada no jogo
    x=random.randrange(0,11)

    #transformando a palavra secreta em str e gerando a versão da palavra apenas em traços para facilitar para o jogador
    palavra_secreta = str(lista[x])
    segredo = (len(palavra_secreta) * "_")
    print(segredo)
    s = list(segredo)

    #gerando o desenho da forca, que ditara a quantia de vezes que um jogador pode errar e um desenho inicial de traços que sera alterado conforme jogador erra
    enforca = "o-|--<"
    en = (len(enforca) * "_")
    enfo = list(enforca)
    e = list(en)
    print(en)

    #começando o laço principal do jogo
    while not enforcado and not acertou:
        #declaramos index para saber onde substituiremos o traço pela letra quando o jogador acertar, e o contador para saber quando o jogador errar
        index = 0
        cont=0
        chute = input("Chute uma letra: ").lower().strip()

        #laço onde olharemos cada caracter da palavra secreta para ver se a letra que chutamos esta nela
        for i in palavra_secreta:
            if i == chute:
                s[index] = chute
                cont=cont+1
            index = index + 1

        #caso não ache a letra chutada, essa condiçao sera ativada e as tentativas restantes do jogador diminuem
        if cont==0:
            e[val] = enfo[val]
            val = val + 1

        #alteramos as strings com as mudanças que houveram em suas versões de lista
        en = "".join(e)
        segredo = "".join(s)

        print(segredo)
        print(en)

        #por ultimo temos as condiçoes de derrota e vitoria, caso o desenho da forca se complete, o jogador perde, mas caso ele acerte a palavra antes disso, ele ganha
        if en.__eq__(enforca):
            print("Voce perdeu!")
            print("A palavra era:",palavra_secreta)
            enforcado = True
        if segredo.__eq__(palavra_secreta):
            print("Voce Venceu!")
            acertou = True

    print("Fim de jogo")


if __name__ == "__main__":
    jogo_forca()
