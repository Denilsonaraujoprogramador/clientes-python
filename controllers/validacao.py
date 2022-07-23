import models.banco as banco
import views.formulario as view


# Controller - irá relalizar a validação a informação solicitada pelo usuário e oretorno do Banco de dados.
def validar_login(usuario_digitado, senha_digitado):
    usuario_BD = banco.model_usuario()
    senha_BD = banco.model_senha()
    if usuario_digitado == usuario_BD and senha_digitado == senha_BD:
        print('pode entrar')
    else:
        print('usuário ou senha inválidos')

def iniciar():
    view.formulario_login()