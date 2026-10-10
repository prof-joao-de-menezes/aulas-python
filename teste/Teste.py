import requests

response = requests.delete('https://viacep.com.br/ws/01001000/json/')

print(response)