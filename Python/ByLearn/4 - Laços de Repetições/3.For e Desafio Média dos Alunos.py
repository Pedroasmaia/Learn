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
