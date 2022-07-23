import models.banco as banco
import views.formulario as view


# Controller - irá relalizar a validação a informação solicitada pelo usuário e oretorno do Banco de dados.
def validar_login(usuario_completo):
    usuario_BD = banco.model_usuario()
    senha_BD = banco.model_senha()
    if usuario_completo[0] == usuario_BD and usuario_completo[1] == senha_BD:
        view.exibir_mensagem('Pode entrar')
    else:
        view.exibir_mensagem('Usuário ou senha inválidos')
        iniciar()

def iniciar():
    validar_login(view.formulario_login())
    # essa seria uma forma mais didatica porem o mesmo cenario referente a linha acima.
    #usuario_completo = view.formulario_login()
    #validar_login(usuario_completo)

    