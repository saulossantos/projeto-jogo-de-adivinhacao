'''Classe TV: Faça um programa que simule um televisor criando-o como um objeto. 
O usuário deve ser capaz de informar o número do canal e aumentar ou diminuir o volume. 
Certifique-se de que o número do canal e o nível do volume permanecem dentro de faixas válidas.'''

class Televisão:
    def __init__(self):
        self.canal = 1
        self.volume = 50

    def alterar_canal(self, novo_canal):
        if 1 <= novo_canal <= 100:
            self.canal = novo_canal
            print("Canal alterado para:", novo_canal)
        else:
            print("Canal inválido.")

    def aumentar_volume(self):
        if self.volume < 100:
            self.volume += 1
            print("Volume aumentado para:", self.volume)
        else:
            print("Volume máximo alcançado.")

    def diminuir_volume(self):
        if self.volume > 0:
            self.volume -= 1
            print("Volume diminuído para:", self.volume)
        else:
            print("Volume mínimo alcançado.")


tv = Televisão()

tv.alterar_canal(13)

tv.aumentar_volume()

tv.diminuir_volume()
