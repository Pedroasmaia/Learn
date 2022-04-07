import numbers


def numeros():
    num1 = 10
    num2 = 11
    num3 = 12
    num4 = 13
    num5 = 14
    soma = num1 + num2 + num3 + num4 + num5
    print(soma)
numeros()

# Motivação das listas: Trabalhar com um varios valores, relacionados a uma só variavel
primeira__lista = ['Felipe','Alisson' , 'Haynes', 'ByLearner']
#-------Posição---[---1°-------2°==========3°----------4°]
#-------Indice---[---0°-------1°==========2°----------3°]
print(primeira__lista[0]) #Vai exibir o Felipe

#Para alterar objeto na lista

primeira__lista[0] = 'Guilherme'

print(primeira__lista)

#Para inserir novo objeto na lista

primeira__lista.append('Novo Aluno')
print(primeira__lista)
