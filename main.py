import requests

#método do módulo requests
resposta = requests.get('https://api.exchangerate-api.com/v6/latest')

print(resposta)

dados = resposta.json()
# print(dados.keys()) #retornar uma lista de chaves do dicionario
# print(dados.values()) #retorna uma lista de todos os valores do dicionario
# print(dados.items()) #retorna uma lista de tuplas (chave, valor) do dicionario
valoresdemoedas = dados['rates'] #dicionário das cotações criado
print(valoresdemoedas)