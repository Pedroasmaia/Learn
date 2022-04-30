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