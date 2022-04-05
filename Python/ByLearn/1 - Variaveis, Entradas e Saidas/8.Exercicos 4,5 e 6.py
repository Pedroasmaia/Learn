#Exercicio 4 | Fazer um função que multiplique 2 números entrados pelo usuario
def multi():
    a = int(input('Insira o 1° número a ser multiplicado: '))
    b = int(input('Insira o 2° número a ser multiplicado: '))
    resultado = a*b
    print(f'O resultado da multiplicação de {a} por {b} é {resultado}')

multi()
#Exercicio 5 | Fazer uma funlçao que divida 2 números entrados pelo usuario
def div():
    a = int(input('Insira o número a ser divido: '))
    b = int(input('Insira o número de partes: '))
    resultado = a/b
    print(f'O resultado de {a} divido por {b} divisão é {resultado}')

div()

#Exercicio 6 | Fazer uma funlçao que subtraia 4 números entrados pelo usuario
def sub():
    a = int(input('Insira o 1° a subtrair: '))
    b = int(input('Insira o 2° a subtrair: '))
    c = int(input('Insira o 3° a subtrair: '))
    d = int(input('Insira o 4° a subtrair: '))
    resultado = a-b-c-d
    print(f'O resultado da subtração de {a} menos {b} menos {c} menos {d} é {resultado}')

sub()