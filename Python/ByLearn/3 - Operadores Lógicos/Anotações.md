# Operadores Lógicos:

## Tipo Booleano de dado:
"Na computação tudo é um ou zero" - Qualquer um sobre computação.
O tipo de dado mais simples é o booleano => tipo logico.
Booleano aceitam apenas dois valores (*True*/*False*),(*1*/*0*). Em eletronica usamos Lâmpada => Acessa = (*Verdadeiro*/*1*/*Sim*) Apagada = (*Falso*/*0*/*Não*/)

### No python:
~~~ Python
boolean = True
print(type(boolean))

#Saída:
<class 'bool'>
~~~

No python, por ser uma linguagem de *tipagem fraca* o booleano é somente *true* ou *false*, porque 0 é inteiro

## Lógica Booleana:

Se verdadeiro então:
    excecução 1
Se não:
    excecução 2

## IF e Else:
O If é uma estrutura de condição, ele verifica se a condição é verdadeira e se for ele executa a excecução desejada, caso não for ele faz a do *else* se ele existir
~~~python
bilhete = True

if bilhete:
    print('É verdade esse bilhete')
#Saida:
# É verdade esse bilhete
bilhete = False

if bilhete:
    print('É verdade esse bilhete')

#Saida:
~~~
Agora com else:
~~~python
bilhete = True

if bilhete:
    print('É verdade esse bilhete')
else:
    print('É falso esse bilhete')
#Saida:
# É verdade esse bilhete
bilhete = False

if bilhete:
    print('É verdade esse bilhete')
else:
    print('É falso esse bilhete')
#Saida:
# É falso esse bilhete
~~~
## Trabalhando IF e Else, sem Booleanos
~~~python:
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
~~~
### Desafio Número Mágico:

- Um mágico pede alguem da plateia pensar num número de um a cinco.
- O usuario escolhe o número:
    - Se o valor do mágico for menor que o seu número, você ira dizer que o mágico deve aumentar o valor.
    - Se o valor do mágico for menor que o seu número, você ira dizer que o mágico deve diminuir o valor.
    - Se o valor do mágico for menor que o seu número, você ira dizer que o mágico acertou.
~~~python
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
~~~

## Simbolos de operadores lógicos
- **>** : Maior que
- **<** : Menor que
- **>=** : Maior ou igual que
- **<=** : Menor ou igual que
- **==** : Igual a (Comparação de igualdade)
- **!=** : Diferente de (Comparação de igualdade)

~~~python

def main():
    numero1 = 2
    numero2 = 3

    if numero1 != numero2:
        print('Os numeros são diferentes')
    else:
        print('Os numeros são iguais')
    
main()

#Saida:
#Os números são diferentes
~~~

## Múltiplas Condições (And e Or)

### **And**: para ter mais de uma condição em que todas sejam verdade
~~~python
def mais():
    char1 = 'f'
    char2 = 'b'

    if char1 == 'f' and char2 == 'b':
        print('Felipe & ByLearn')
    elif char1 == 'f':
        print('felipe')
    elif char2 == 'b':
        print('ByLearn')
    else:
        print('Python')
mais()
~~~

### **Or** para ter mais de uma condição que pelo menos uma seja verdade

~~~python
def outro():
    num1 = 2
    num2 = 4
    num3 = 7
    num__escolhido = 4

    if num1 == num__escolhido or num2 == num__escolhido or num3 == num__escolhido:
        print('Você acertou em um dos chutes')
    else:
        print('Você errou todos os chutes')

outro()
~~~