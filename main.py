import requests

#método do módulo requests
resposta = requests.get('https://api.exchangerate-api.com/v6/latest')

print(resposta)

dados = resposta.json()
print(dados)