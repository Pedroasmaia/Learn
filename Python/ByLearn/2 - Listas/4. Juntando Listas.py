# Juntando listas [ Join ] 
# Serve pra somar duas ou mais listas

Id_professores = [1,2,3]
Id_aluno_py = [10,9]

id_todos = Id_aluno_py + Id_professores 

print(f'Essa é a lista de todos{id_todos}')


Id_aluno_csharp = [4,5,6]

#Podemos juntar a lista de forma mais simples assim:
id_todos += Id_aluno_csharp

print(f'Essa é a  nova lista de todos{id_todos}')
