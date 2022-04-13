pokemons = ['Pikachu','Caterpile','Aron','Pidgey','Mew']
first = input('Qual será seu primeiro pokemon?' )
pokemons.append(first)

indice_pokemon = pokemons.index(first)

print(f'O seu pokemon esta na posição {indice_pokemon+1}°:')
print(pokemons)

pokemons.pop(5)
position = int(input('Agora que removemos, seu pokemon desta posição, em qual você gostaria de usar? '))

print('Sua lista de pokemons é: ')
pokemons.insert(position-1,first)
print(pokemons)

pokemons.sort()
print('Organizamos a lista pra você em ordem alfabetica: ')
print(pokemons)