# API de conversão de valores de moedas.
## Dados são necessarios pra completar funcionalidades
## Interface online de comunicação de dados: recuperar, pedir, alterar, ciar ou remover
## Consumindo a API
	- Primeiro passo foi olhar a documentação
	- Dados serão recuperados como JSON>>javascript, xml e outros
	
	Utilizando biblioteca REQUESTS
		- pip install requests

# web scraping com python
## protoclo HTTP
### protocolos de interconexão de Redes de Computadores.
### protocolo: padronização do envio e recebimento de informações.
## HTTP: HyperText Transfer Protocol.
	- Define o modo como sites são acessados na internet.
	- Requisição -> resposta.
	- Strigns padronizadas: código de status; cabeçalho; conteúdo.

	Métodos HTTP
		GET: Solicita um recurso para o servidor(uma página web por exemplo).
		POST: Enviamos uma informação para o servidor.
		Outros: Pesquisar.
	
	códigos de Status:
		Informativo(1xx)
			-informação sobre a comunicação
		Sucesso(2xx)
			-Mensagem chegou e era Válida.
		Redirecionamento(3xx)
			-Recurso buscado mudou permanentemente de endereço
		Erro do cliente(4xx)
			-O recurso buscado não existe. Not Found (404).
		Erro do Servidor(5xx)
			-Serviço indisponível devido a algo como: sobrecarga ou em manutenção.