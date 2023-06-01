#jogo de adivinhação de números

from random import randint

pc = randint(0, 100)
print("você quer jogar?")
print("tente adivinhar o número que tô pensando, entre 0 e 100..")
acertou = False
tentativas = 0
while not acertou:
    jogador = int(input("Qual o seu palpite? "))
    tentativas += 1
    if jogador == pc:
        acertou = True
    else: 
        if jogador < pc:
            print("você jogou muito baixo.. tente outra vez.")
        elif jogador > pc:
            print("você jogou muito alto.. tente outra vez.")
print("boa! você acertou! {} tentativas".format(tentativas))
