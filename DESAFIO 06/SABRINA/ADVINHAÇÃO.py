import random

def jogo_advinhacao():
    print("\n🌝Bem-vindo ao Jogo de Adivinhação!")

    numero_secreto = random.randint(1, 10)
    tentativas = 0
    max_tentativas = 3

    while tentativas < max_tentativas:
        tentativa = int(input("🤯Tente adivinhar o número entre 1 e 10:\n>>>"))

        if tentativa == numero_secreto:
            print("\n😃Parabéns, você acertou!")
            break
        elif tentativa < numero_secreto:
            print("\n🤓Tente um número maior!")
        else:
            print("\n🤓Tente um número menor!")

        tentativas += 1

    if tentativas == max_tentativas:
        print(f"\n🤬Suas chances acabaram. O número secreto era {numero_secreto}!")

if __name__ == "__main__":
    jogo_advinhacao()
