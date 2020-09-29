import requests
import json
import pandas as pd

def getTxt(nombre):
    with open(nombre, "r") as archivo:
        lineas = archivo.readlines()
    return lineas

def getApi(url):
    response = requests.get(url)
    return response.json()

def getJson(nombre):
    with open(nombre, "r") as archivo:
        contenido = archivo.read()
        dicc=json.loads(contenido)
    return dicc

def getCsv(nombre):
    df = pd.read_csv(nombre)
    return df

# lineas = getTxt('receta.txt')
# for linea in lineas:
#     print(linea)

# usuarios = getApi('https://reqres.in/api/users?page=1')
# for usuario in usuarios['data']:
#     print('{}'.format(usuario['first_name']))

albums = getJson('albums.json')
for album in albums:
    print('{}'.format(album['title']))

# df = getCsv('verduras.csv')
# for index, row in df.iterrows():
#     print(row['nombre'])
