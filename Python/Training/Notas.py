
from secrets import choice


amount__students =  10
#Definindo a lista:
students = ['Pedro','Marques','Fabio','Manuel','Leo','Jorge','Raphael','Oito','Bruna','Lilian']
Chosen = students[0]
first__exame = 10
second__exame = 5
third__exame = 7
fourth__exame = 3

sum__grade__exame = first__exame + second__exame + third__exame + fourth__exame
avg__grade__exame = sum__grade__exame / 4

print(f'As notas somadas do(a) {Chosen} tem o resultado de {sum__grade__exame} pontos, mas a média é de {avg__grade__exame} pontos')


random_students_aprove_one = [1,2,3,4]
random_students_aprove_two = [5,6,7,8]



random_aprove1 = choice(random_students_aprove_one)
random_aprove2 = choice(random_students_aprove_two)


#Clonando a lista
students__aprove = students[random_aprove1 : random_aprove2]
students__aprove.append(Chosen)
print(f'Esses são os alunos aprovados:{students__aprove}')