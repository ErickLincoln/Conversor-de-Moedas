import json
import requests

#método do módulo requests
resposta = requests.get('https://api.exchangerate-api.com/v6/latest')

#print(resposta) ##status

dados = resposta.json()
# print(dados.keys()) #retornar uma lista de chaves do dicionario
# print(dados.values()) #retorna uma lista de todos os valores do dicionario
# print(dados.items()) #retorna uma lista de tuplas (chave, valor) do dicionario
valoresdemoedas = dados['rates'] #dicionário das cotações criado


#criando Json com valores bases
#with open('dicionario_de_moedas.JSON', 'w', encoding = 'utf-8') as arquivo:
#		arquivo.write(str(valoresdemoedas))

# print(valoresdemoedas.get(input('Digite a moeda'))) ##Teste de localização de valor por chave

real = valoresdemoedas.get('BRL')
dolar = valoresdemoedas.get('USD')
print('Olá!\n Seja bem vindo ao contador de moedas!\n')
print('R${:.2f} pra dolar U$${:.2f}'.format(real, dolar))

#manipulaçao de dicionário e conversor simples de Real para dolar criado
#side project LestCode e Santander
valorDeConversao = float(input('informe o valor a ser convertido:\nR$ '))
cotaçãoDoValor = valoresdemoedas['BRL']
print(f'R${valorDeConversao} pra dolar US${valorDeConversao/cotaçãoDoValor:.2f}')