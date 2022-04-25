def main():
    Nota__1 = int(input('Digite a nota de sua 1° prova:  '))
    Nota__2 = int(input('Digite a nota de sua 2° prova:  '))

    media = (Nota__1 + Nota__2)/2

    if media >= 6:
        print('Você passou')
    else:
        print('Você não passou')

    print(f'Sua nota foi {media} pontos')
main()