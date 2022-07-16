
# View - informação que o usuário irá solicitar.
def view():
    usuario_digitado = input("Informa o seu usuário: ")
    senha_digitado = input("informa a sua senha: ")
    controller(usuario_digitado, senha_digitado)

# Model - Infomação que virá da meu Banco de dados(BD) através de uma request do tipo GET(requisição).
def model_usuario():
    usuario_BD = 'joao'
    return usuario_BD

def model_senha():
    senha_BD = '123'
    return senha_BD

# Controller - irá relalizar a validação a informação solicitada pelo usuário e oretorno do Banco de dados.
def controller(usuario_digitado, senha_digitado):
    usuario_BD = model_usuario
    senha_BD = model_senha
    if usuario_digitado == usuario_BD and senha_digitado == senha_BD:
        print('pode entrar')
    else:
        print('usuário ou senha inválidos')

view()