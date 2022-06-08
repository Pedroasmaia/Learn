from copyreg import pickle
import string
from pip import main
import requests as r
import json
from dotenv import load_dotenv
import os
load_dotenv()

api_token = os.environ['key']

year = input('Qual ano você quer?')
uri = 'https://api.football-data.org/v4/matches/'
headers = { 'X-Auth-Token': api_token}
SerieA_Scores = (f'https://api.football-data.org/v4/competitions/SA/scorers?season={year}')

Scores = r.get(SerieA_Scores,headers=headers)
retorno = Scores.json() #Json Todo

#Informações da Competição
competition = retorno['competition']  #Pega 'competition' dentro do Json todo
competition_name = competition['name'] #Pega 'name' dentro de 'competition'
print(f'O Nome da liga é {competition_name}')

#Listar os 10 Jogadores
OrderList = 1
top_scores = retorno['scorers'] #Pega 'scores' no json todo
print('Posição | Jogador | Gols')
for players_block in top_scores: #Separa Bloco de Informações dos Jogadores de 'Scores'
    players = players_block['player'] #Do bloco de informações individualiza os jogadores
    player_name = players['name'] #Informa todo os nomes do que foi individualizado
    player_goals = players_block['goals'] #Pega os gols de cada jogador
    print(f'{OrderList}° | {player_name} | {player_goals} Gols')
    OrderList = OrderList + 1


