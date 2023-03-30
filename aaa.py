# Bloco de apresentação
print("*" * 10, "Programa de Criptografia", "*" * 10)
print("*" * 40)


# Bloco de funções
def matriz(a):
    b = a.replace(" ", "")
    lmsg = list(b)
    if (len(lmsg) % 8) == 0:
        linha = len(lmsg) // 8
    else:
        linha = 1 + (len(lmsg) // 8)
    k = 0
    cmsg = []
    for m in range(linha):
        cmsg.append([0] * 8)
    for i in range(linha):
        for j in range(8):
            if k < (len(lmsg)):
                cmsg[i][j] = lmsg[k]
            else:
                cmsg[i][j] = "*"
            k = k + 1
    for i in range(linha):
        print(cmsg[i])
    print("")
    return cmsg


def cripto(a):
    linha = len(a)
    c=[]
    for m in range(linha):
        c.append([0] * 8)
    # origi - 0,1,2,3,4,5,6,7
    chave = 1, 0, 2, 7, 3, 6, 4, 5
    for i in range(linha):
        for j in range(8):
            k = chave[j]
            c[i][j] = a[i][k]


    return c


def descripto(a):
    linha = len(a)
    c = []
    for m in range(linha):
        c.append([0] * 8)
    chave = 1, 0, 2, 4, 6, 7, 5, 3
    for i in range(linha):
        for j in range(8):
            k = chave[j]
            c[i][j] = a[i][k]
    for i in range(linha):
        print(c[i])
    print("")
    for i in range(linha):
        for j in range(8):
            print(c[i][j])


# Bloco de entrada

op = 'm'
while op != "e":
    op = input("Escolha uma opção:\nC-Criptografe uma mensagem\nD-Descriptografe uma mensagem\nE-sair\n").lower()
    if op == "c":
        msg = input("digite a mensagem a ser criptografada:\t").lower()
        while len(msg) > 128:
            print("mensagem excedeu 128 caracteres, insira uma mensagem menor.")
            msg = input("digite a mensagem a ser criptografada:\t").lower()

        teste = cripto(matriz(msg))
    elif op == "d":
        print(descripto(teste))
    elif op == "e":
        print("Encerrando o programa...")
    else:
        print("Opção selecionada é invalida, selecione uma das opções abaixo:")
# Bloco de processamento
# Bloco de saida
