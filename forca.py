import random


def jogar_forca():
    apresentacao()
    palavra = sorteia_palavra()
    letras_acertadas = inicializaletrasacertadas(palavra)

    enforcou = False
    acertou = False
    qtd_erros = 0

    print(letras_acertadas)

    # ENQUANTO NÃO ACERTAR E NEM SE ENFORCAR, CONTINUA JOGANDO
    while not enforcou and not acertou:
        print("JOGANDO...")
        chute = chute_jogador()

        # SE O CHUTE EXISTIR NA PALAVRA, ELE SUBSTITUI O VALOR
        if chute in palavra:
            marca_chute_correto(palavra, chute, letras_acertadas)
        else:
            qtd_erros += 1
            print("VOCÊ ERROU, AINDA TEM {} TENTATIVAS PARA ADIVINHAR A PALAVRA".format(7 - qtd_erros))
            desenha_forca(qtd_erros)
        acertou = "_" not in letras_acertadas
        enforcou = qtd_erros == 7

    if (acertou):
        vencedor()
    else:
        perdeu(palavra)


def apresentacao():
    print("*********************************")
    print("Bem vindo ao jogo de forca!")
    print("*********************************")

def sorteia_palavra():
    # IMPORTANDO .TXT PARA O CODIGO
    lista_Palavras = list()
    with open("palavras.txt") as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            lista_Palavras.append(linha)

    # SORTEANDO PALAVRA DO ARQUIVO .TXT
    numero = random.randrange(0, len(lista_Palavras))
    palavra = lista_Palavras[numero].upper()
    return palavra


def inicializaletrasacertadas(palavra):
    return ["_" for letra in palavra]


def chute_jogador():
    chute = input(str('Digite uma letra: '))
    chute = chute.strip().upper()
    return chute


def marca_chute_correto(palavra,chute,letras_acertadas):
    index = 0
    for letra in palavra:
        if chute.upper() == letra.upper():
            letras_acertadas[index] = chute
            print(letras_acertadas)
        index += 1


def vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def perdeu(palavra):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

if __name__ == "___main__":
    jogar_forca()




