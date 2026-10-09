import requests

response = requests.get('https://pokeapi.co/api/v2/pokemon/4/')

print(response.json())