import wowowo
import forca

print(32 * "*")
print(8 * "*", "Escolha o jogo", 8 * "*")
print(32 * "*")

jogo = int(input("1-Jogo da forca\n2-Jogo de adivinhação\n>>>"))

if jogo == 1:
    forca.jogo_forca()
else:
    wowowo.jogo_adivinha()
