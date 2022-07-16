
# View - informação que o usuário irá solicitar.
usuario_digitado = input("Informa o seu usuário: ")
senha_digitado = input("informa a sua senha: ")

# Model - Infomação que virá da meu Banco de dados(BD) uma request do tipo GET(requisição).
usuario_BD = 'joao'
senha_BD = '123'

# Controller - irá relalizar a validação a informação solicitada pelo usuário e oretorno do Banco de dados.
if usuario_digitado == usuario_BD and senha_digitado == senha_BD:
    print('pode entrar')
else:
    print('usuário ou senha inválidos')