#crazy-dictionary-v1.0
#developer : ZeroCoder000

import requests
import json

word = input('Enter Word to Search :')
url = "https://mashape-community-urban-dictionary.p.rapidapi.com/define"
querystring = {"term":word}
headers = {
    'x-rapidapi-host': "mashape-community-urban-dictionary.p.rapidapi.com",
    'x-rapidapi-key': "df712ca9cdmshfa95e98cd61e2c3p1a78e0jsn77fb10c09bd0"
    }
response = requests.get( url, headers=headers, params=querystring)
data = response.json()
for _ in range(0,1):
    for item in data['list']:
        print(('Meaning:').upper() + item['definition'] + '\n' +  ('Example:').upper() + item['example'])
        print('\n')
