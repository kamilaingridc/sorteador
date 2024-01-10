import os
import random
import time
import threading

vidas = 100
chances = 3


def killer():
    pid = os.getpid()
    os.kill(pid, 0)


def tempo(numero_sorteado):
    time.sleep(10)
    print(f"Seu tempo acabou. Você perdeu. O número sorteado foi {numero_sorteado}.")
    killer()


eprimo = False
while not eprimo:
    numero_sorteado = random.randint(0, 101)
    if numero_sorteado % 2 != 0 and numero_sorteado % 3 != 0 and numero_sorteado % 5 != 0:
        eprimo = True

print("-------------------------------------------------------")
print("Olá, seja bem-vindo ao nosso jogo sorteador de números!")
print("-------------------------------------------------------")
print("Aqui você vai ter 100 vidas e 3 chances e 10 segundos para adivinhar! \n")

while chances > 0 and vidas > 0:
    chances -= 1
    n = int(input("Adivinhe o número: "))
    print(f"Você escolheu o número: {n}")
    threading.Thread(target=tempo, args=(numero_sorteado,)).start()
    print("-------------------------------------------------------")
    if n == numero_sorteado:
        print("Você acertou!! Parabéns.")
    else:
        vidas -= abs(n - numero_sorteado)
        print("Você errou, tente novamente :(")
        print("-------------------------------------------------------")
        print("Vidas restantes:", vidas)
        print(f"Chances restantes: {chances} ")
        print("-------------------------------------------------------")

if chances <= 0 or vidas <= 0:
    print('Você perdeu! O número sorteado foi:', numero_sorteado)
    killer()
