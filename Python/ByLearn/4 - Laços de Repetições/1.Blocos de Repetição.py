alunos = ['Felipe','Haynes','Alisson']
alunos.append('Pedro')

def sem__iteracao():
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


def com__iteracao():
    #Para todos  os alunos => Vou printar o nome
    for aluno in alunos:
        print(aluno)
com__iteracao()