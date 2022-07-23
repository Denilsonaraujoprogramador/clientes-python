import models.banco as banco
#from banco import*

# Controller - irá relalizar a validação a informação solicitada pelo usuário e oretorno do Banco de dados.
def validar_login(usuario_digitado, senha_digitado):
    usuario_BD = banco.model_usuario
    #usuario_BD = model_usuario

    senha_BD = banco.model_senha
    #senha_BD = model_senha

    if usuario_digitado == usuario_BD and senha_digitado == senha_BD:
        print('pode entrar')
    else:
        print('usuário ou senha inválidos')