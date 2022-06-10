from copyreg import pickle
import string
from tracemalloc import stop
from pip import main
import requests as r
import json
from dotenv import load_dotenv
import os
load_dotenv()
api_token = os.environ['key']
uri = 'https://api.football-data.org/v4/matches/'
headers = { 'X-Auth-Token': api_token}
SerieA_Scores = (f'https://api.football-data.org/v4/competitions/SA/scorers?limit=30')
Scores = r.get(SerieA_Scores,headers=headers)
Scores_status = Scores.status_code
# print(f'HTTPS CODE : {Scores_status}')
retorno = Scores.json() #Json Todo
def GoldenShoes():
    search_player = input('Qual jogador quer ver?')
    top_scores = retorno['scorers'] #Pega 'scores' no json todo
    player_names = []
    player_goals = []
    for players_block in top_scores: #Separa Bloco de Informações dos Jogadores de 'Scores'
        players = players_block['player'] #Do bloco de informações individualiza os jogadores
        player_names.append(players['name']) #Informa todo os nomes do que foi individualizado
        player_goals.append(players_block['goals']) #Pega os gols de cada jogador
    while search_player in player_names:
        indice_player = player_names.index(search_player)
        print(f'Esse jogador fez {player_goals[indice_player]} gols')
        break
    else:
        print('Esse jogador não esta entre os 30 maiores marcadores da liga')
GoldenShoes()

