import adivinhação
import forca
def escolhe_jogo():
    print("*********************************")
    print("********Escolha seu jogo!********")
    print("*********************************")

    print('(1)Forca (2)Adivinhação')
    jogo = int(input('Qual jogo você quer jogar?'))

    if(jogo == 1):
        print('Jogando forca')
        forca.jogar_forca()
    elif(jogo == 2):
        print('Jogando adivinhação')
        adivinhação.jogar_adivinhacao()

if(__name__ == "__main__"):
    escolhe_jogo()

escolhe_jogo()
