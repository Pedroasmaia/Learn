#Fazendo requisições na API django https://github.com/Pedroasmaia/api_django
#

import re
import requests as r
import json

def buscar_dados():
    terra = {
    "title": "Storytelling com dados: Um guia sobre visualização de dados para profissionais de negócios",
    "author": "Cole Nussbaumer Knaflic",
    "release_year": 2019,
    "state": "novo",
    "pages": 256,
    "publishing_company": "Alta Book"
}
    busca = r.post('http://127.0.0.1:8000/books/',data=terra)
    http_respost = int(busca.status_code)

    if http_respost == 200 or 201:
        print(f'Aqui esta o seu Json: {busca.content}')
    elif http_respost == 404:
        print('Tu errou na solicitação meu camarada')
        print(busca.content)
    else:
        print(f'Pesquisa no Google o que esse Erro: {busca.status_code} significa')

def mostrar_dados():
    book = r.get('http://127.0.0.1:8000/books/')
    book_list= book.json() #Transformando Json em List
    book_obj = book_list[3] # Escolhendo chave do dicionario que eu irei trabalhar
    
    #Setando variaveis com retornos dos Json
    titulo = 'title'
    autor = 'author'
    ano = 'release_year'
    estado = 'state'
    page = 'pages'
    editora = 'publishing_company'
    #Usando Json em uma String
    print(f'O nome do livro é {book_obj[titulo]},foi escrito pelo(a) {book_obj[autor]} no ano de {book_obj[ano]}, seu estado de conservação é {book_obj[estado]}, contem {book_obj[page]} paginas e foi publicado pela {book_obj[editora]}')

if __name__ == '__main__':
    mostrar_dados()