# Laços de Repetições
## Necessidade de uso
Precisamos interagir com vários elementos de uma lista ou grupo de dados com tamanho dinamico

### Exemplo: Para não fazermos como abaixo, um caso para cada quantidade de dados:
~~~python
def sem__iteracao():
    alunos = ['Felipe','Haynes','Alisson']
    alunos.append('Pedro')

    if len(alunos) == 0:
        print('Sem alunos')
    elif len(alunos) == 1:
        print(alunos[0])
    elif len(alunos) == 2:
        print(alunos[0])
        print(alunos[1])
    elif len(alunos) == 3:
        print(alunos[0])
        print(alunos[1])
        print(alunos[2])
    elif len(alunos) == 4:
        print(alunos[0])
        print(alunos[1])
        print(alunos[2])
        print(alunos[3])
sem__iteracao()
~~~
## Para laços de repetição podemos utilizar o comando FOR

### Ele é utilizado da seguinte forma 'FOR *iterando* in *Lista*'. Exemplo:

~~~python
def com__iteracao():
    #Para todos  os alunos => Vou printar o nome
    for aluno in alunos:
        print(aluno)
com__iteracao()
~~~
## Desafio: Criar uma lista de notas e adicionar entre 5 e 10 notas a seu criterio, por fim printar todas as notas desta lista atraves de um laço for

## Range() = > Utiliza um intervalo no FOR (ou seja de *x* até *y*)

~~~python
def main():
    #Todos os possiveis alunos
    alunos = ['Felipe','Eduardo','Jorge','Pedro','Jose']
    # Todas respectivas dos alunos
    notas = [[8,2],[10,7],[8,9],[7,7],[10,10]]

    if len(alunos) == len(notas):
    # Se a contagem de (alunos) é igual a contagem de (notas)
        for aluno in range(len(alunos)):
        # Para aluno dentro do intervalo(da contagem de (alunos))
            soma = 0
            for nota in notas[aluno]:
                soma += nota
            media = soma / len(notas[aluno])
            print(f'O aluno {alunos[aluno]} tem a média {media}')
            if(media >= 6):
                print(f'- Portanto, ele foi aprovado')
            else:
                print(f'- Portanto, ele foi reprovado')
main()
~~~
## Laços de repetição for também funcionam com strings, mostranfo caracter por caracterer
~~~python
string = 'Curso de python'
for char in string:
    print(char)
~~~
## Podemos usar o enumerate() => para além do valor, também termos o índice
## Não precisamos necessariamente usar for aninhada, podemos usar a virgula para definir os elementos que queremos recuperar
~~~python
lista = ['p','e','d','r','o']
for chave, valor in enumerate(lista):
    print('O valor',valor,'fica no indice',chave)
~~~