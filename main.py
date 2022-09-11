import requests

#método do módulo requests
resposta = requests.get('https://api.exchangerate-api.com/v6/latest')

print(resposta)

dados = resposta.json()
# print(dados.keys()) #retornar uma lista de chaves do dicionario
# print(dados.values()) #retorna uma lista de todos os valores do dicionario
# print(dados.items()) #retorna uma lista de tuplas (chave, valor) do dicionario
valoresdemoedas = dados['rates'] #dicionário das cotações criado
real = valoresdemoedas.get('BRL')
dolar = valoresdemoedas.get('USD')
print('Olá!\n Seja bem vindo ao contador de moedas!\n')
print('R${:.2f} pra dolar U$${:.2f}'.format(real, dolar))

#manipulaçao de dicionário e conversor simples de Real para dolar criado
#side project LestCode e Santander
valorDeConversao = float(input('informe o valor a ser convertido:\nR$ '))
cotaçãoDoValor = valoresdemoedas['BRL']
print(f'R${valorDeConversao} pra dolar US${valorDeConversao/cotaçãoDoValor:.2f}')