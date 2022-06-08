from copyreg import pickle
import string
from pip import main
import requests as r
import json
from dotenv import load_dotenv
import os
load_dotenv()

api_token = os.environ['key']

year = 2021
uri = 'https://api.football-data.org/v4/matches/'
headers = { 'X-Auth-Token': api_token}
SerieA_Scores = (f'https://api.football-data.org/v4/competitions/SA/scorers?season{year}')

# response = r.get(uri, headers=headers)
# for match in response.json()['matches']:
# print(match)
def main():
    Scores = r.get(SerieA_Scores,headers=headers)
    Scores_List = Scores.json()
    print(Scores_List)
main()