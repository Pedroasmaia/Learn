def main():
    numero = 13
    chute = int(input('Pronto já escolhi meu número. Qual número eu escolhi:'))

    if chute == numero:
        print('Você acertou, parabens')
    elif chute > numero:
        print('Você chutou alto demais')
    else:
        print('Tente mais baixo')
main()